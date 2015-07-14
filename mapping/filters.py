import django_filters
from django.forms import SelectMultiple
from mapping.models import Country, Description, Department, Subtask

class DescriptionFilter(django_filters.FilterSet):
    COUNTRIES = [(c.id, c.name) for c in Country.objects.all()]

    # Get choice fields for subtask
    departments = []
    for department in Department.objects.all():
        subtasks = []
        for task in department.task_set.all():
            for subtask in task.subtask_set.all():
                subtasks.append((subtask.id, subtask.name))

        departments.append((department.name, subtasks))

    country = django_filters.MultipleChoiceFilter(choices=COUNTRIES, widget=SelectMultiple(attrs={'class': 'browser-default', 'size': len(COUNTRIES)}))
    subtask = django_filters.MultipleChoiceFilter(choices=departments, widget=SelectMultiple(attrs={'class': 'browser-default', 'size': 15}))
    status = django_filters.MultipleChoiceFilter(choices=Description.STATUS, widget=SelectMultiple(attrs={'class': 'browser-default'}))

    class Meta:
        model = Description
        fields = ['subtask', 'country', 'status']

    def get_order_by(self):
        return ['country']