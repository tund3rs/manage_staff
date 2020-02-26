from rest_framework import serializers
from company.models import Department, Staff, Project


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'staff_name', 'depart']


class ProjectSerializer(serializers.ModelSerializer):
    staffs = StaffSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'staffs']
