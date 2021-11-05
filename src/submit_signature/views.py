from django.shortcuts import render
from rest_framework.generics import ListAPIView
from submit_signature.models import TransactionSignature
from submit_signature.serializers import TransactionSignatureSerializer

# Create your views here.
class ListTransactionSignatures(ListAPIView):
    queryset = TransactionSignature.objects.all()
    serializer_class = TransactionSignatureSerializer
