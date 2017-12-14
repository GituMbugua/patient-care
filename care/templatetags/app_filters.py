from django import template
from care.models import Patient

register = template.Library()

@register.filter(name='filter_injuries')
def filter_injuries(value):
    status = Patient.status

    if status == 'green':
        return '#00CC00'
    elif status == 'yellow':
        return '#ffff1a'
    elif status == 'red':
        return '#ff0000'
    elif status == 'black':
        return '#000000'