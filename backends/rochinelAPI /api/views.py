
import json
from django.shortcuts import render
from django.http import JsonResponse

def index(request, *args, **kwargs):
     print(request.body)
     data = json.loads()
     
     return JsonResponse({'name':'rochinel', 'langage':'puthon'})