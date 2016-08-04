from django.contrib import admin
from .models import Question, Choice, Roast
from .forms import ChoiceForm
#we need to tell the admin that Question objects have an admin interface.

# Register your models here.
# class ChoiceAdmin(admin.ModelAdmin):
#     form = ChoiceForm

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class RoastAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Question Title',      {'fields':['roast_title']}),
#         ('Author',     {'fields':['author']})
#     ]
    list_display = ('roast_title', 'author')
    list_filter = ['roast_title']
    #search field is not doing good giving errors
    # search_fields = ['author']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
admin.site.register(Roast, RoastAdmin)