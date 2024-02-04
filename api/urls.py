from .views import index, verifier, signer, get_signed_signature, verify_signature, get_key_info, sign_doc, verify_doc, extract_from_cms
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('signer', signer, name="signer"),
    path('signed_signature', get_signed_signature, name="get_signed_signature"),
    path('verify_signature', verify_signature, name="verify_signature"),
    path('verifier', verifier, name="verifier"),
    path('key/info', get_key_info, name="key-info"),
    path('doc/sign', sign_doc, name="sign-doc"),
    path('doc/verify', verify_doc, name="verify-doc"),
    path('doc/cms/extract', extract_from_cms, name="extract-from-cms"),
]
