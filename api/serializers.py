from rest_framework import serializers

from api.models import APITestModel


class APITestModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APITestModel
        fields = ["url", "year"]
