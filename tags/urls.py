from django.urls import include, path
from rest_framework import routers
from tags import views 

# Code generates the routes for the CRUD

router = routers.DefaultRouter()
router.register(r'tags', views.TagsView, 'tags')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
