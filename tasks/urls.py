from django.urls import include, path
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TasksView, 'tasks')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
