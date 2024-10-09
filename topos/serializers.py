from rest_framework import serializers
from .models import Topo

class TopoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topo
        fields = '__all__'


