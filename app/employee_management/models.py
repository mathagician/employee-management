from django.db import models


class Base(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Designation(Base):
  name = models.CharField(max_length=256)
  code = models.CharField(max_length=6)

  def __repr__(self):
    return self.name

  def __str__(self):
    return self.__repr__()


class Employee(Base):
  name = models.CharField(max_length=256)
  email = models.CharField(
      max_length=1024,
      unique=True)
  phone = models.CharField(max_length=10)
  designation = models.ForeignKey(
      Designation,
      on_delete=models.CASCADE)

  def __repr__(self):
    return self.name + " : " + self.designation.code

  def __str__(self):
    return self.__repr__()
