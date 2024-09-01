from rest_framework import viewsets
from .serializer import TagSerializer
from .models import tags

# Create your views here.
class TagsView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = tags.objects.all()