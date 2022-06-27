from rest_framework import routers

from apps.questionare.views import QuestionnaireViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(
    prefix='questionnaires',
    viewset=QuestionnaireViewSet,
    basename='questionnaires'
)

urlpatterns = [
    *router.urls,
]
