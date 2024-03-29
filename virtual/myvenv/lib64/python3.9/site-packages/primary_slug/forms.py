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

import re

from django.forms import SlugField
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from primary_slug import settings



slug_re = re.compile(r'^[%s]+$' % settings.PRIMARY_SLUG_VALID_CHARS)
validate_slug = RegexValidator(slug_re, _(u"Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens."), 'invalid')
    
class PrimarySlugFormField(SlugField):
    default_validators = [validate_slug]

