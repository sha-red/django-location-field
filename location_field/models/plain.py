from django.db.models import CharField

from location_field.forms import plain as forms
from location_field.models.base import BaseLocationField


class PlainLocationField(BaseLocationField, CharField):
    formfield_class = forms.PlainLocationField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 63)
        super(PlainLocationField, self).__init__(*args, **kwargs)
