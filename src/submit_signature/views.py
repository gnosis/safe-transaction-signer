from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import TransactionSignature
from .serializers import TransactionSignatureSerializer


class ListTransactionSignatures(ListAPIView):
    serializer_class = TransactionSignatureSerializer
    queryset = TransactionSignature.objects.all()
