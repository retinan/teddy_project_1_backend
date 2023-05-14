from django.urls import path, include
from rest_framework import routers
from api.views import CustomRegisterView, CustomLoginView, FindUserID

urlpatterns = [
    # 회원가입, 로그인 커스텀 오버라이딩
    # 순서가 중요 커스텀 url을 기본 제공 url 보다 먼저 위치해야 함.
    path('accounts/login/', CustomLoginView.as_view()),
    path('accounts/signup/', CustomRegisterView.as_view()),
    path('accounts/forgot_id/', FindUserID.as_view()),
    # dj_rest_auth 회원가입, 로그인 기본 제공 URL
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]
