from django.shortcuts import render
from api.handlers.file_handler import FileHandler
from api.handlers.document_signer import DocumentSigner
from api.handlers.signature_verifier import SignatureVerifier
from django.http import HttpRequest, HttpResponse
import uuid
from api.handlers.NCANodeClient import nca_node_client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from config.settings import BASE_DIR
# Create your views here.

def index(request):
	return render(request, 'index.html')

def signer(request):
	return render(request, 'signer.html')

def verifier(request):
	return render(request, 'verifier.html')
	
	
def get_signed_signature(request: HttpRequest):
    document_file = request.FILES.get('document')
    key_file = request.FILES.get('key')
    password = request.POST.get('password')
    key = FileHandler(key_file).base64_encode()
    document = FileHandler(document_file).base64_encode()
    encoded_signature = DocumentSigner.sign_document(document, key, password)
    filename = f"{uuid.uuid4()}.cms"
    response = HttpResponse(encoded_signature, content_type='application/cms')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


def verify_signature(request: HttpRequest):
    document = request.FILES.get('document')
    cms_file = request.FILES.get('cms')
    hash = FileHandler(document).get_data()
    encoded_signature = FileHandler(cms_file).get_data()
    is_valid = SignatureVerifier.verify_signature(hash, encoded_signature)
    context = {"success": is_valid}
    return render(request, 'verifier.html', {"context": context})


@api_view(['POST'])
def get_key_info(request: HttpRequest):
    key_file = request.FILES.get('key')
    password = request.POST.get('password')
    key = FileHandler(key_file).base64_encode()
    info = nca_node_client.get_key_info(key, password)
    return Response({"data": info})


@api_view(['POST'])
def sign_doc(request: HttpRequest):
    document_file = request.FILES.get('document')
    key_file = request.FILES.get('key')
    password = request.POST.get('password')
    key = FileHandler(key_file).base64_encode()
    document = FileHandler(document_file).base64_encode()
    data = DocumentSigner.sign_document(document, key, password)
    with open(BASE_DIR / f"zapros.cms", 'w') as cms:
        cms.write(data['cms'])
    return Response({"data": data})


@api_view(['POST'])
def verify_doc(request: HttpRequest):
    cms_file = request.FILES.get('cms')
    cms = FileHandler(cms_file).get_data()
    data = SignatureVerifier.verify_signature(cms)
    return Response({"data": data})


@api_view(['POST'])
def extract_from_cms(request: HttpRequest):
    cms_file = request.FILES.get('cms')
    cms = FileHandler(cms_file).get_data()
    info = nca_node_client.extract_from_cms(cms)
    return Response({"data": info})