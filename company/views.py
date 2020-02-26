from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .serializers import *
# from .permissions import IsOwnerOrReadOnly
# Create your views here.


# @api_view(['GET'])
# def apt_root(request, format=None):
#     return Response({
#         'department': reverse('department-list', request=request, format=format),
#         'staff': reverse('staff-list', request=request, format=format),
#         'project': reverse('project-list', request=request, format=format),
#     })

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        id_depart = request.data.get('depart')
        depart_name = get_object_or_404(Department, id=id_depart)
        print(depart_name)
        depart = get_object_or_404(Department, depart_name=depart_name)
        if depart:
            depart.number_staff += 1
            depart.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     department = self.get_object()
    #     return Response(department.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
#generics
# class StaffList(generics.ListCreateAPIView):
#     queryset = Staff.objects.all()
#     serializer_class = StaffSerializer
#
#
# class StaffDetail(generics.RetrieveUpdateAPIView):
#     queryset = Staff.objects.all()
#     serializer_class = StaffSerializer
#
#
# class ProjectList(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class ProjectDetail(generics.RetrieveUpdateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class DepartmentList(generics.ListCreateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
#
#
# class DepartmentDetail(generics.ListCreateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
