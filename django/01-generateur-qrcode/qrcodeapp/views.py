from django.shortcuts import render
from .models import QR_code

# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if data:  # Vérifier que les données ne sont pas vides
            obj = QR_code.objects.create(data=data)
            qr_code = obj.qr_code
            context = {
                'qr_code': qr_code,
                'data': data  # Ajouter les données pour les afficher dans le formulaire
            }
        else:
            context = {
                'error': 'Veuillez entrer des données valides.'
            }
    else:
        context = {}
    
    return render(request, 'index.html', context)