import rest_framework
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from company import views

router = DefaultRouter()
# router.register(r'department', views.DepartmentViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'staff_number', views.StaffNumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

# urlpatterns =[
#     path('staff/', views.StaffList.as_view()),
#     path('staff/<int:pk>/', views.StaffDetail.as_view()),
#     path('project/', views.ProjectList.as_view()),
#     path('project/<int:pk>/', views.ProjectDetail.as_view()),
#     path('depart/', views.DepartmentList.as_view()),
#     path('depart/', views.DepartmentDetail.as_view()),
#     path('api-auth/', include('rest_framework.urls')),
# ]
#
# format_suffix_patterns(urlpatterns)
