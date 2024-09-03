from django.urls import include, path
from rest_framework import routers
from lists import views 

router = routers.DefaultRouter()
router.register(r'lists', views.ListView, 'lists')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
