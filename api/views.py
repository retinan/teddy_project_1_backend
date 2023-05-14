
from rest_framework import status
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView
from rest_framework.views import APIView

from api.serializers.accountSerializer import CustomLoginSerializer, CustomRegisterSerializer
from dj_rest_auth.views import LoginView

import re
from django.core.mail import send_mail
from django.contrib.auth.models import User


class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    # def create(self, request, *args, **kwargs):
    #
    #     # 약관 동의 체크 여부 확인
    #     if not request.data.get('isCheck'):
    #         return Response({'non_field_errors': '약관에 동의해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
    #     return super().create(request, *args, **kwargs)


class FindUserID(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        if not email:
            return Response({'message': '이메일을 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return Response({'message': '유효한 이메일 주소를 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': '해당 이메일 주소를 가진 사용자가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        send_mail(
            'ID 찾기',
            f'귀하의 ID는 {user.username}입니다.',
            'noreply@example.com',
            [email],
            fail_silently=False,
        )

        return Response({'message': '입력하신 이메일 주소로 ID가 전송되었습니다.'}, status=status.HTTP_200_OK)
