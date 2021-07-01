import django
from django.core.management.commands import startproject
import venv

print(django.get_version())

print(startproject.TemplateCommand.help)
