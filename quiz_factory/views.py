from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from quiz_factory.models import Question, QuestionChoices, Category
from quiz_factory.serializers import QuestionSerializer, QuestionChoicesSerializer, CategorySerializer


class QuestionCreateList(generics.ListCreateAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ChoiceCreateList(generics.ListCreateAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    serializer_class = QuestionChoicesSerializer
    queryset = QuestionChoices.objects.all()


class ChoiceDetails(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    serializer_class = QuestionChoicesSerializer
    queryset = QuestionChoices.objects.all()


class CategoryCreateList(generics.ListCreateAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
