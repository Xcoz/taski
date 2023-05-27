from django.contrib import admin
from rest_framework import routers
from django.urls import include, path

from api import views


router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
