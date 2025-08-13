# from .models import RegistrationForm
from django.shortcuts import render
from django.http import HttpResponse
from  rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from .models import *

# Create your views here.


def Home(request):
    return HttpResponse('Hello Django')


def Page(request):
    return render(request, 'Login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Save user
        RegistrationForm.objects.create(username=username, email=email, password=password)
        return render(request, 'index.html', {'success': 'User registered successfully!'})
    return render(request, 'index.html')


class RegisterApiView(APIView):
    def get(self,request):
        data=RegistrationForm.objects.all()
        serialized_data =RegisterSerializers(data,many=True)
        return Response(serialized_data.data)
