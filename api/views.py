from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def endpoints(request):
    """Returns all the endpoints available for the api"""
    data = ['/certificate', 'certificate/:certificate_number', '/verify/:certificate_number']
    return Response(data)