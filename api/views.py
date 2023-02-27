from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Certificate
from .serializers import CertificateSerializer
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def endpoints(request):
    """Returns all the endpoints available for the api"""
    data = ['/certificate', 'certificate/:certificate_number', '/verify/:certificate_number']
    return Response(data)

class Certificate_List(APIView):
    """Returns the List of Certificates and Generates New Certificate"""
    
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        certificates = Certificate.objects.all()
        serializer = CertificateSerializer(certificates, many = True)
        return Response(serializer.data)
    
    def post(self, request):

       
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            certificate = Certificate.objects.create(
            profile_pic = request.data['profile_pic'],
            certificate_number = request.data['certificate_number'],
            fullname = request.data['fullname'],
            role=request.data['role'],
            organization = request.data['organization'],
            internship_organizer = request.data['internship_organizer'],
            start_date = request.data['start_date'],
            end_date = request.data['end_date'],
            issue_date = request.data['issue_date'],
            verification_link = f"http://127.0.0.1:3000/verify/{request.data['certificate_number']}"

        )
            return Response (serializer.data,  status=status.HTTP_201_CREATED)
        else:
            print(request.data['start_date'])
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)