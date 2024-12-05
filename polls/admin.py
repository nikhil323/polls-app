from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra= 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Questions", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]})

    ]
    inlines=[ChoiceInline]
    list_display =["question_text", "pub_date","was_published_recently"]
    list_filter = ["pub_date"] #shows filter to the right side by published date
    search_fields = ["question_text"] #creates a search field to the top by question text
    # fields = ["pub_date", "question_text"]

admin.site.register(Question, QuestionAdmin)