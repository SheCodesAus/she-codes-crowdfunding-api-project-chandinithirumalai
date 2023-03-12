from django.urls import path, include 
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project-detail"), 
    path('pledges/', views.PledgeList.as_view(), name="pledge-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)