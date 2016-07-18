from django.contrib import admin
from .models import Question
from .models import Choice
from .forms import ChoiceForm
#we need to tell the admin that Question objects have an admin interface.

# Register your models here.
class ChoiceAdmin(admin.ModelAdmin):
    form = ChoiceForm

admin.site.register(Question)
admin.site.register(Choice)
