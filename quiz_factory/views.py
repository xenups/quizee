from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from quiz_factory.models import Question
from quiz_factory.serializers import QuestionSerializer


class QuestionCreateList(generics.ListCreateAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
