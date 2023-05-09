from django.contrib import admin

from .models import Designation
from .models import Employee


admin.site.register(Designation)
admin.site.register(Employee)
