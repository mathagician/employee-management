from rest_framework import serializers

from .models import Employee
from .models import Designation


class EmployeeSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(read_only=True)
  designation = serializers.PrimaryKeyRelatedField(
      queryset=Designation.objects.all())

  def create(self, validated_data):
    """
    Create and return a new `Employee` instance, given the validated data.
    """
    return Employee.objects.create(**validated_data)

  class Meta:
    model = Employee
    fields = ('id', 'name', 'email', 'phone', 'designation')
