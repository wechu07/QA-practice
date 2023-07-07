from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# create a model admin class, 

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]

# # forms with dozens of fields, you might want to split the form up into fieldsets:
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]

# then pass it as the second argument to admin.site.register()

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

# adding choices together with questions

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)


