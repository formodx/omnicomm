from rest_framework import serializers

from ..common.models import File
from .models import *


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    files = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), many=True)
    recipients = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all(), many=True)

    class Meta:
        model = Report
        exclude = ['sender']