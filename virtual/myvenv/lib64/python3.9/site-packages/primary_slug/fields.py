# -*- coding: utf-8 -*-
#
#  This file is part of django-primary-cms.
#
#  django-primary-slug provides a custom SlugField for Django projects.
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-primary-cms
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-primary-cms
#
#  Copyright 2011 George Notaras <gnot [at] g-loaded.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from django.db.models.fields import SlugField
from django.core.urlresolvers import get_callable
from django.utils.translation import ugettext_lazy as _
from primary_slug import settings
from primary_slug import utils
from primary_slug.forms import PrimarySlugFormField



default_slugify = get_callable(settings.PRIMARY_SLUG_SLUGIFY_FUNC)

class PrimarySlugField(SlugField):
    """This model field is an enhanced version of Django's ``SlugField``.
    
    *django-primary-slug* provides an enhanced version of the default Django's
    ``SlugField``, which supports:
    
    - Custom slugify function.
    - Custom list of valid characters.
    
    The ``PrimarySlugField`` derives from the default ``SlugField`` and thus
    all attributes and methods of the default ``SlugField`` are inherited.
    
    In addition to the default arguments, the ``PrimarySlugField`` also
    supports the following:
    
    ``populate_from``
        A string or callable that returns the initial value to be slugified.
        If this is not set, then the slug field is not populated automatically.
        Also, if the slug field is set by the user, then it is not auto-
        populated.
    ``slugify``
        A callable python object which slugifies the value retrieved from the 
        ``populate_from`` field. If this is not set, then the function defined
        in the ``PRIMARY_SLUG_SLUGIFY_FUNC`` setting is used.

    The following code snippet illustrates how to use the ``PrimarySlugField``::

        from django.db import models
        from primary_slug.fields import PrimarySlugField
        
        class MyModel(models.Model):
            title = models.CharField(max_length=160)
            slug = PrimarySlugField(populate_from='title', max_length=160)
    
    
    """
    
    def __init__(self, *args, **kwargs):
        
        self.populate_from = kwargs.pop('populate_from', None)
        if self.populate_from:
            # Here we force blank=True or else the form validation will fail.
            kwargs['blank'] = True
            
        self.slugify = kwargs.pop('slugify', default_slugify)
        assert hasattr(self.slugify, '__call__')
        
        super(PrimarySlugField, self).__init__(*args, **kwargs)
        
    
    def pre_save(self, instance, add):
        """Returns field's value just before saving."""

        # get currently entered slug
        slug = self.value_from_object(instance)

        # If no slug has been set and a ``populate_from`` field has been set,
        # generate a slug from the value of the ``populate_from`` field.
        if self.populate_from and not slug:
            populate_from_field_value = utils.get_prepopulated_value(self, instance)

            # Slugify value
            slug = self.slugify(populate_from_field_value)
    
            if slug:
                # Hard reset slug length
                if self.max_length < len(slug):
                    slug = slug[:self.max_length]
                
                assert slug, 'slug is not set'
                
                # Make the slug available as instance attribute as if the user had set it
                setattr(instance, self.name, slug)
        
        return slug
    
    def formfield(self, **kwargs):
        defaults = {'form_class': PrimarySlugFormField}
        defaults.update(kwargs)
        return super(PrimarySlugField, self).formfield(**defaults)


