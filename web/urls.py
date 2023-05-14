from django.urls import path, include
from .views import HomeView
from django.shortcuts import render


urlpatterns = [
    # path('', lambda request: render(request, 'main.html')),
    path('', HomeView.as_view(), name="home"),
    path('accounts/', include('web.accounts.urls')),
]