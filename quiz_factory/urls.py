from quiz_factory import views
from django.urls import path, include
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('questions/<int:pk>/', views.QuestionDetails.as_view()),
    path('questions/', cache_page(60 * 60)(views.QuestionCreateList.as_view())),

    path('choices/<int:pk>/', views.ChoiceDetails.as_view()),
    path('choices/', cache_page(60 * 60)(views.ChoiceCreateList.as_view())),

    path('category/<int:pk>/', views.CategoryDetails.as_view()),
    path('category/', cache_page(60 * 60)(views.CategoryDetails.as_view())),

]
