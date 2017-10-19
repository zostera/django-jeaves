# -*- coding: utf-8 -*-

from django.contrib.postgres.fields import JSONField


class JeavesField(JSONField):
    '''
    This model field is used to store the attributes.
    '''
    description = 'Translation storage for a model'

    def __init__(self, *args, **kwargs):

        super(JeavesField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(JeavesField, self).deconstruct()

        return name, path, args, kwargs
