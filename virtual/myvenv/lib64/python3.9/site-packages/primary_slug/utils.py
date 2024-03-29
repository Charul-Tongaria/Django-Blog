# -*- coding: utf-8 -*-
#
#  This file is part of django-primary-slug.
#
#  django-primary-slug provides a custom SlugField for Django projects.
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-primary-slug
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-primary-slug
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

def get_prepopulated_value(field, instance):
    """
    Returns preliminary value based on `populate_from`.
    
    Taken from django-autoslug.
    
    """
    if hasattr(field.populate_from, '__call__'):
        # AutoSlugField(populate_from=lambda instance: ...)
        return field.populate_from(instance)
    else:
        # AutoSlugField(populate_from='foo')
        attr = getattr(instance, field.populate_from)
        return callable(attr) and attr() or attr


def simple_slugify(data):
    return data.replace(' ', '-')

def simple_slugify_lower(data):
    return data.lower().replace(' ', '-')

