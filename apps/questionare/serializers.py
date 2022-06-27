from rest_framework import serializers

from apps.questionare.models import (
    Questionnaire,
    Question,
    ResponseOption
)


class ResponseOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseOption
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    response_options = ResponseOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Questionnaire
        fields = '__all__'
