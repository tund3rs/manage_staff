from django.db import models

DEPARTMENTS = (('HR', 'HR'),
               ('DEV', 'DEV'),
               ('SALE', 'SALE'),
               ('MARKETING', 'MARKETING'),
               ('TESTER', 'TESTER'),
               ('AI', 'AI'))


class Department(models.Model):
    depart_name = models.CharField(choices=DEPARTMENTS, default='DEV', max_length=100)
    number_staff = models.IntegerField(default=False)

    def __str__(self):
        return self.depart_name


# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    depart = models.ForeignKey(Department, related_name='staffs', on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    staffs = models.ManyToManyField(Staff)
    revenue = models.FloatField(default=None)
    created = models.DateField(blank=True, auto_now_add=True, null=True)
    finished = models.DateField(auto_now_add=False, null=True, blank=True)
    percent = models.FloatField()
    # join_project = models.DateField(auto_now_add=False)

    class Meta:
        default_related_name = 'project_set'

    def __str__(self):
        return self.project_name
