from django.db import models
from django.conf import settings


class Questionnaire(models.Model):
    """
    Questionnaire model
    """
    name = models.CharField(max_length=255)
    questions = models.ManyToManyField("Question")

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    Question model
    """
    prompt = models.CharField(max_length=255)
    response_options = models.ManyToManyField("ResponseOption")

    def __str__(self):
        return self.prompt


class ResponseOption(models.Model):
    """
    ResponseOption model
    """
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class UserQuestionnaire(models.Model):
    """
    UserQuestionnaire model
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_questionnaires",
    )
    questionnaire = models.ForeignKey(
        to=Questionnaire,
        on_delete=models.CASCADE,
        related_name="user_questionnaires",
    )


class UserResponse(models.Model):
    """
    UserResponse model
    """
    questionnaire = models.ForeignKey(
        to=UserQuestionnaire,
        on_delete=models.CASCADE,
        related_name="user_responses",
    )
    question = models.ForeignKey(
        to=Question,
        on_delete=models.CASCADE,
        related_name="user_responses",
    )
    response_option = models.ForeignKey(
        to=ResponseOption,
        on_delete=models.CASCADE,
        related_name="user_responses",
    )
