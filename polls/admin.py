from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):

    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        ("Question text section", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
