from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_status(request):
    return Response({'status': 'ok', 'application': 'CSC325 CI/CD Pipeline'})
