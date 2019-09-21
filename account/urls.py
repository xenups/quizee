from account import views
from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)

urlpatterns = [
    path('registration/', cache_page(1 * 1)(views.UserProfileViewSet.as_view())),
    path('profile/<int:pk>/', views.UserProfileDetail.as_view()),
    path('profileImage/', cache_page(60 * 60)(views.ProfileImageViewSet.as_view())),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

]
