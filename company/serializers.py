from rest_framework import serializers
from company.models import Department, Staff, Project


class ProjectSerializer(serializers.ModelSerializer):
    staffs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        # exclude = ('staffs',)
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = ('id', 'staff_name', 'depart', 'projects')

    def get_projects(self, obj):
        projects = ProjectSerializer(obj.project_set, many=True)
        return projects.data


class StaffNumberSerializer(serializers.ModelSerializer):
    # staffs = StaffSerializer(many=True)
    staffs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Department
        fields = ('id', 'depart_name', 'number_staff', 'staffs')
