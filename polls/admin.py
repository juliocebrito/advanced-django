from django.contrib import admin
from django.utils import timezone

from advanced_django.utils import BaseModelAdmin
from .models import ExampleModel, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(BaseModelAdmin):
    # fields = ['pub_date', 'question_text']
    # exclude = ['count_choices']
    list_display = (
        'pub_date', 
        'question_text',
        'count_choices',
        'days',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
        'state',
        'substate'
    )
    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text']
    list_editable = ['question_text']

    inlines = [ChoiceInline]

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None,             {'fields': ['count_choices']}),
    ]

    def days(self, obj):
        diff = timezone.now() - obj.created_at
        return diff.days


@admin.register(Choice)
class ChoiceAdmin(BaseModelAdmin):
    # fields = ['question', 'choice_text', 'votes']
    list_display = (
        'question', 
        'choice_text',
        'votes',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
        'state',
        'substate'
    )
    list_filter = ['question', 'choice_text']
    search_fields = ['question']
    raw_id_fields = ['question']

admin.site.register(ExampleModel)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
