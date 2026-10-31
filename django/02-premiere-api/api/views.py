from django.http import JsonResponse


def index(request, *args, **kwargs):
    return JsonResponse({'name': 'rochinel', 'langage': 'python'})
