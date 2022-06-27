from django.contrib import admin
from django import forms

from apps.questionare.models import (
    Questionnaire,
    Question,
    ResponseOption
)


class QuestionnaireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionnaireForm, self).__init__(*args, **kwargs)
        self.fields['questions'].help_text = "Questions"
        self.fields['questions'].required = False

    class Meta:
        model = Questionnaire
        fields = '__all__'


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    form = QuestionnaireForm
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)
    ordering = ('id', 'name',)
    filter_horizontal = ('questions',)
    readonly_fields = ('id',)


class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['response_options'].help_text = "Response Options"
        self.fields['response_options'].required = False

    class Meta:
        model = Question
        fields = '__all__'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    list_display = ('id', 'prompt',)
    list_display_links = ('id', 'prompt',)
    search_fields = ('id', 'prompt',)
    ordering = ('id', 'prompt',)
    filter_horizontal = ('response_options',)
    readonly_fields = ('id',)


class ResponseOptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResponseOptionForm, self).__init__(*args, **kwargs)
        self.fields['text'].help_text = "Text"
        self.fields['text'].required = False

    class Meta:
        model = ResponseOption
        fields = '__all__'


@admin.register(ResponseOption)
class ResponseOptionAdmin(admin.ModelAdmin):
    form = ResponseOptionForm
    list_display = ('id', 'text',)
    list_display_links = ('id', 'text',)
    search_fields = ('id', 'text',)
    ordering = ('id', 'text',)
    readonly_fields = ('id',)
