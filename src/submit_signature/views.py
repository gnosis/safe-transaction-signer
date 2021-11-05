from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import TransactionSignature
from .serializers import TransactionSignatureSerializer

# Create your views here.
class ListTransactionSignatures(ListAPIView):
    queryset = TransactionSignature.objects.all()
    serializer_class = TransactionSignatureSerializer
