from django.urls import path
from .views import ListTransactionSignatures
from .apps import SubmitSignatureConfig

app_name = SubmitSignatureConfig.name

urlpatterns = [
    path("submissions/", ListTransactionSignatures.as_view(), name="list"),
]
