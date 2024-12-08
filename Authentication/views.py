from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .querys import *
from Authentication.Serializer import MyTokenObtainPairSerializer
from .PermissionMix import *
from .models import *
from  .Serializer import *
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class AdministratorSetoldVersion(ViewSet):
    permission_classes = [IsAuthenticated]
    def get (self, request):

        seliz = None
        flag, organization = get_permission_adminChoice(request=request, permission_codename="Authentication.DoctorSpecializations")
        if flag==True:
            doctor_specializations = request.user.administrator.DoctorSpecializations.all()
            query = Administrator.objects.filter(
                Organization=organization,
                DoctorSpecializations__in=doctor_specializations
            ).distinct()
            flag, organization = get_permission_adminChoice(request=request, permission_codename="Authentication.ShowAdmin")
        if flag == True:
                query = Administrator.objects.filter(Organization=organization)
                seliz = AdminShowDetails(query, many=True)
        if seliz==None:
            return Response("Not Have Permsaion", status=status.HTTP_9090_Permsaion)
        seliz = AdminShowDetails(query, many=True)
        return Response(seliz.data, status=status.HTTP_200_OK)

class AdministratorSetNewVersion(ViewSet):
            permission_classes = [IsAuthenticated]
            def get(self, request):
                user=request.user
                listPermsion=[]
                FirstPermsion={"code": "Authentication.ShowAdmin", "Level": 1,"query": QueryShowAllAdmin}
                secondPermsion={"code": "Authentication.DoctorSpecializations", "Level":2,"query": QueryShowDoctorSamespecializations}
                listPermsion.extend([FirstPermsion, secondPermsion])
                flag,query=CompareBetweenPermisson(request,listPermsion)
                query=query["query"]
                seliz = AdminShowDetails(query(user), many=True)
                return Response(seliz.data, status=status.HTTP_200_OK)