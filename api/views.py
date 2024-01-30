from django.shortcuts import render
from api.handlers.file_handler import FileHandler
from api.handlers.document_signer import DocumentSigner
from api.handlers.signature_verifier import SignatureVerifier
from django.http import HttpRequest, HttpResponse
import uuid
# Create your views here.

def index(request):
	return render(request, 'index.html')

def signer(request):
	return render(request, 'signer.html')

def verifier(request):
	return render(request, 'verifier.html')
	
	
def get_signed_signature(request: HttpRequest):
    document = request.FILES.get('document')
    hash = FileHandler(document).get_hash()
    private_key_text = request.POST.get('private_key')
    private_key_bytes = private_key_text.encode('utf-8')
    encoded_signature = DocumentSigner.sign_document(hash, private_key_bytes)
    filename = f"{uuid.uuid4()}.cms"
    response = HttpResponse(encoded_signature, content_type='application/cms')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


def verify_signature(request: HttpRequest):
    document = request.FILES.get('document')
    cms_file = request.FILES.get('cms')
    hash = FileHandler(document).get_hash()
    encoded_signature = FileHandler(cms_file).get_data()
    public_key_text = request.POST.get('public_key')
    public_key_bytes = public_key_text.encode('utf-8')
    is_valid = SignatureVerifier.verify_signature(hash, encoded_signature, public_key_bytes)
    context = {"success": is_valid}
    return render(request, 'verifier.html', {"context": context})