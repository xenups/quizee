from quiz_factory import views
from django.urls import path, include
from django.views.decorators.cache import cache_page


urlpatterns = [
    # path('profile/<int:pk>/', views.UserProfileDetail.as_view()),
    path('questions/', cache_page(60 * 60)(views.QuestionCreateList.as_view())),
]
