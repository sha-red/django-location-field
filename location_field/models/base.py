class BaseLocationField(object):
    def __init__(self, *args, **kwargs):
        self._based_fields = kwargs.pop('based_fields', [])
        self._zoom = kwargs.pop('zoom', 2)
        self._suffix = kwargs.pop('suffix', None)
        self._initial = kwargs.pop('initial', '')
        super(BaseLocationField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super(BaseLocationField, self).formfield(
            form_class=self.formfield_class,
            based_fields=self._based_fields,
            zoom=self._zoom,
            initial=self._initial,
            **kwargs)
