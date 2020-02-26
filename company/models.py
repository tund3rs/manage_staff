from django.db import models

DEPARTMENTS = (('HR', 'HR'),
               ('DEV', 'DEV'),
               ('SALE', 'SALE'),
               ('MARKETING', 'MARKETING'),
               ('TESTER', 'TESTER'),
               ('AI', 'AI'))


class Department(models.Model):
    depart_name = models.CharField(choices=DEPARTMENTS, default='DEV', max_length=100)
    number_staff = models.IntegerField(default=1)

    def __str__(self):
        return self.depart_name


# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    depart = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    staffs = models.ManyToManyField(Staff)
    # number_staff = models.IntegerField(default=1)

    def __str__(self):
        return self.project_name
