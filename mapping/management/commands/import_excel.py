from django.core.management.base import BaseCommand, CommandError
from mapping.models import Country, Department, Task, Subtask, Description
import argparse
import xlrd

class Command(BaseCommand):
    help = 'Imports the data from an Excel 2003 file (xls file)'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs=1, type=argparse.FileType('r'))
        parser.add_argument('department', nargs=1)
        parser.add_argument('shortname', nargs=1)

    def handle(self, *args, **options):
        f = options['file'][0]
        book = xlrd.open_workbook(f.name, formatting_info=True)
        sheet = book.sheet_by_index(0)

        department = Department.objects.get(name=options['department'][0])
        shortname = options['shortname'][0].lower()

        d = {}
        merged_cells = sheet.merged_cells

        PROGRESS = {
            45: 1,
            43: 2,
            42: 3,
            49: 4,
            64: 1,
            27: 3,
            29: 1,
        }

        countries = [
            'Afghanistan',
            'Bangladesh',
            'India',
            'Maldives',
            'Nepal',
            'Pakistan',
            'Sri Lanka'
        ]

        for crange in merged_cells:
            rlo, rhi, clo, chi = crange
            for rowx in range(rlo, rhi):
                for colx in range(clo, chi):
                    task =  sheet.cell(rowx=rowx, colx=colx).value.strip().title()
                    if task and task != 'National Society':
                        self.stdout.write(task)
                        t = Task(department=department, name=task)
                        t.save()
                        d[task] = {
                            'rlo': rlo,
                            'rhi': rhi,
                            'clo': clo,
                            'chi': chi,
                            'subtasks': {},
                        }

        for task in d:
            for i in range(d[task]['clo'], d[task]['chi']):
                subtask = sheet.cell(rowx=2, colx=i).value.strip().title()
                try:
                    t = Task.objects.get(name=task)
                except Task.DoesNotExist:
                    print(task)
                s = Subtask(task=t, name=subtask)
                s.save()
                d[task]['subtasks'][subtask] = []
                for j in range(3, 10):
                    value = str(sheet.cell(rowx=j, colx=i).value).strip()
                    xfx = sheet.cell_xf_index(j, i)
                    xf = book.xf_list[xfx]
                    bgx = xf.background.pattern_colour_index
                    progress = PROGRESS[bgx]
                    country = countries[j - 3]
                    cobj = Country.objects.get(name=country)
                    dobj = Description(subtask=s, country=cobj, description=value, status=progress)
                    dobj.save()
                    # d[task]['subtasks'][subtask].append((value, progress))

        # self.stdout.write(str(d))
