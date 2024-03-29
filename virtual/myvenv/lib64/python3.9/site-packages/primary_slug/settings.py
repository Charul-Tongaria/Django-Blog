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

from django.conf import settings


#DEFAULT_SLUGIFY = 'django.template.defaultfilters.slugify'
#DEFAULT_SLUGIFY = 'primary_slug.translit.greek.simple_slugify'
#DEFAULT_SLUGIFY = 'primary_slug.translit.greek.simple_slugify_lower'
#DEFAULT_SLUGIFY = 'primary_slug.utils.simple_slugify_lower'
DEFAULT_SLUGIFY = 'primary_slug.utils.simple_slugify'
PRIMARY_SLUG_SLUGIFY_FUNC = getattr(settings, 'PRIMARY_SLUG_SLUGIFY_FUNC', DEFAULT_SLUGIFY)

# '-_0-9a-zA-ZαβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩςάέήίϊΐόύϋΰώΆΈΉΊΪΌΎΫΏ'
# Set:  # -*- coding: utf-8 -*-   in the first line of settings.py if unicode chars are used.
# and supply a properly decided string. Eg:
# 
PRIMARY_SLUG_VALID_CHARS = getattr(settings, 'PRIMARY_SLUG_VALID_CHARS', u'-_0-9a-zA-Z')

