from django.db import models


class Category(models.Model):
    category = models.CharField(
        verbose_name="Category",
        max_length=250, blank=True,
        unique=True, null=True)

    def __str__(self):
        return self.category


class Question(models.Model):
    question_context = models.CharField(max_length=400, blank=False)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, null=True, blank=True,
        verbose_name="Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.question_context


class QuestionChoices(models.Model):
    question_id = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    is_right_choice = models.BooleanField(default=False)
    choice = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.choice
