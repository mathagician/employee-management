from django.core.management.base import BaseCommand, CommandError

from employee_management.models import Designation


DESIGNATIONS = [
    {
        "name": "chief executive officer",
        "code": "CEO",
    },
    {
        "name": "chief technology officer",
        "code": "CTO",
    },
    {
        "name": "chief people officer",
        "code": "CPO",
    },
]


class Command(BaseCommand):
  help = "Initialises the designations"

  def handle(self, *args, **options):
    for designation in DESIGNATIONS:
      new_designation, status = Designation.objects.get_or_create(
        name=designation["name"])
      new_designation.code = designation["code"]
      new_designation.save()
