from django.urls import path, include
from .views import OrganizationViewSet, OrganizationUserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('organizations/', TokenObtainPairView.as_view()),

]