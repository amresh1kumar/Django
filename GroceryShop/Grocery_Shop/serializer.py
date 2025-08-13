from rest_framework import serializers
from .models import *


class RegisterSerializers(serializers.ModelSerializer):
   class Meta:
      model = RegistrationForm
      fields = '__all__'
