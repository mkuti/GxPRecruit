"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `development`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from os import environ

from split_settings.tools import include, optional

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'common.py',  # standard django settings
    # 'database.py',  # postgres

    # You can even use glob:
    # '*.py'

    # Select the right env:
    '{0}.py'.format(ENV),
    # Optionally override some settings:
    optional('local.py'),
]

# Include settings:
include(*base_settings)
