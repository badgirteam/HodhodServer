from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)

from apps.validation.views import Validation


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            data = {
                'success': 'false',
                'message': 'لطفا نام کاربری و رمز عبور خود را وارد کنید',
                'data': ''
            }
            return Response(data, status=HTTP_400_BAD_REQUEST)
        if Validation.is_valid_pass(password) and Validation.is_valid_user_name(username):
            data = {
                'success': 'false',
                'message': 'نام کاربری یا رمز عبور وارد شده صحیح نمی‌باشد',
                'data': ''
            }
            return Response(data, status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            data = {
                'success': 'false',
                'message': 'کاربری با این اطلاعات وجود ندارد',
                'data': ''
            }
            return Response(data, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        data = {
            'success': 'true',
            'message': 'عملیات با موفقیت انجام شد',
            'data': {'token': token.key}
        }
        return Response(data, status=HTTP_200_OK)


class Logout(APIView):
    def get(self, request):
        if request.user.id:
            request.user.auth_token.delete()
            data = {
                'success': 'true',
                'message': 'عملیات با موفقیت انجام شد',
                'data': ''
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'success': 'false',
                'message': 'شما هنوز وارد نشده اید',
                'data': ''
            }
            return Response(data, status=HTTP_401_UNAUTHORIZED)
