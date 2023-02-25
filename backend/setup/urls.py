"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dj_rest_auth.registration.views import (
    ConfirmEmailView,
    RegisterView,
    VerifyEmailView,
)
from dj_rest_auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from document.views import DocumentViewSet
from folder.views import FolderViewSet
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'folders', FolderViewSet)

urlpatterns = (
    [
        path('', include(router.urls)),
        path('admin/', admin.site.urls),
        path('register/', RegisterView.as_view()),
        path('login/', LoginView.as_view()),
        path('logout/', LogoutView.as_view()),
        path(
            'verify-email/',
            VerifyEmailView.as_view(),
            name='rest_verify_email',
        ),
        path(
            'account-confirm-email/',
            VerifyEmailView.as_view(),
            name='account_email_verification_sent',
        ),
        path(
            'account-confirm-email/<str:key>/',
            ConfirmEmailView.as_view(),
            name='account_confirm_email',
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
