from rest_framework import serializers
from .models import tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tags
        fields = '__all__'