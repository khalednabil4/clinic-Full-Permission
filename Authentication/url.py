from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [

#path('StudentsAttendace/<str:Subjectid>', AddStudentsAttendace.as_view({ "post": "create"}))
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('Administratorold/', AdministratorSetoldVersion.as_view({
        'get': 'get',
     })),
    path('Administratornew/', AdministratorSetNewVersion.as_view({
        'get': 'get',
    })),
]