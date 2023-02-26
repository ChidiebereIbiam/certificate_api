from rest_framework.serializers import ModelSerializer
from .models import Certificate

class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"
