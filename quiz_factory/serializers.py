from rest_framework import serializers

from quiz_factory.models import Question, Category, QuestionChoices


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category',)


class QuestionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Question
        fields = ('question_context', 'is_active', 'category')

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     category = CategorySerializer.create(CategorySerializer(), validated_data=category_data)
    #     question = Question.objects.create(category=category, question_context=validated_data.pop('question_context')
    #                                        , is_active=validated_data.pop('is_active'))
    #     question.save()
    #     return question


class QuestionChoicesSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = QuestionChoices
        fields = ('question', 'is_right_choice', 'choice')
