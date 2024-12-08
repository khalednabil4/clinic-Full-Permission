from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

class CustomPermissionDenied(APIException):
    status_code = 550
    default_detail = 'Not Have Permission'
    default_code = 'permission_denied'
def get_permission_adminChoice(request, permission_codename):
    try:
        user = request.user.administrator
        if user.has_perm(permission_codename):
            return True,user.Organization
        return False,"Wrong"
    except  Exception as e:
        return False,e
def CompareBetweenPermisson(request,ListPermsion):
    try:
        user=request.user.administrator
        ListPermsionHave=[]
        for per in ListPermsion:
            permission_codename = per.get("code")
            if user.has_perm(permission_codename):
                ListPermsionHave.append(per)
        highest_level = min(ListPermsionHave, key=lambda x: x['Level'])
        print(highest_level)
        return True,highest_level
    except  Exception as e:
        raise CustomPermissionDenied()