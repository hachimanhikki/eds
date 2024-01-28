from .views import index, verifier, signer, get_signed_signature, verify_signature
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('signer', signer, name="signer"),
    path('signed_signature', get_signed_signature, name="get_signed_signature"),
    path('verify_signature', verify_signature, name="verify_signature"),
    path('verifier', verifier, name="verifier"),
]
