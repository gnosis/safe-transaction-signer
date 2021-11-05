from django.db import models

# Create your models here.
class TransactionSignature(models.Model):
    id: models.BigAutoField(primary_key=True)
    safe_address: models.TextField(max_length=42)
    signature: models.TextField(max_length=255)
