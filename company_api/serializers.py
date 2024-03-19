from rest_framework import serializers
from .models import Company, Employee
from rest_framework.permissions import IsAuthenticated

# create your serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Employee
        fields = "__all__"
