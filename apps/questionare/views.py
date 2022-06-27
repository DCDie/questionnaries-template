from rest_framework import viewsets, permissions

from apps.questionare.models import Questionnaire
from apps.questionare.serializers import QuestionnaireSerializer


class QuestionnaireViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view and create Questionnaires.
    """
    queryset = Questionnaire.objects.prefetch_related(
        'questions',
        'questions__response_options',
    ).all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAuthenticated]
