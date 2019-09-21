from account import views
from django.urls import path, include
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('registration/', cache_page(1 * 1)(views.UserProfileViewSet.as_view())),
    path('usersProfile/<int:pk>/', views.UserProfileDetail.as_view()),
    path('uploadProfileImage/', cache_page(60 * 60)(views.ProfileImageViewSet.as_view())),

]
