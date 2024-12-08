from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from .models import *
from .models import Administrator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(self.user)
        superstatus=False
        user_type=None
        flag=True
        if hasattr(self.user, 'administrator'):
            Administrator = self.user.administrator
            user_type = "administrator"
            UserGroup = Administrator.group_in
            superstatus=Administrator.is_superuser
        elif hasattr(self.user, 'patient'):
            patient = self.user.patient
            user_type = "patient"
            UserGroup = patient.group_in
            superstatus = patient.is_superuser
        else:
            raise AuthenticationFailed("Unauthorized access")
        if superstatus ==True:
           group_permissions=Permission.objects.all()
        else:
         group_permissions = UserGroup.permissions.all()
        list=[]
        for group in group_permissions:
            list.append(group.codename)
        list.append(user_type)
        data['username'] = self.user.username
        data['Permission'] = list
        return data
class AddAdminSerial(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ["username","profile_img","bio","email","name"]

class AdminShowDetails(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ['name', 'profile_img', 'bio', 'SpecialInformation', 'GraduationFrom', 'GraduationDate', 'IsDoctor', 'DoctorSpecializations']