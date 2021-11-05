from django.db.models import fields
from rest_framework import serializers
from .models import TransactionSignature


class TransactionSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSignature
        fields = ["id", "safe_address", "signature"]
