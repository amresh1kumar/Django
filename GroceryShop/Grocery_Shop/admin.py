from django.contrib import admin

# Register your models here.
from .models import Registration
from .models import RegistrationForm

# Register your models here.
admin.site.register(Registration)
admin.site.register(RegistrationForm)