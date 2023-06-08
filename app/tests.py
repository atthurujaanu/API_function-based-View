from django.test import TestCase

# Create your tests here.
from app.models import *
from rest_framework decorators import api_view
from rest_framework import Response
from app.serializers import *
@api_view()
class EmployeeJdata(request):
    EQS=Employee.objets.all()
    ESD=EmployeeJdata(EQS,many=True)
    return Response



    