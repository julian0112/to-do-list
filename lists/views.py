from rest_framework import viewsets
from .serializer import ListSerializer
from .models import Lists

# Create your views here.
class ListView(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = Lists.objects.all()