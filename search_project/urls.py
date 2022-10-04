from django.urls import path
from . import views
app_name = 'projects'


urlpatterns = [
    path('new/', views.project_new, name='new')
]
 