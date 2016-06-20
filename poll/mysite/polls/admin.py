from django.contrib import admin
from .models import Question
from .models import Choice
#we need to tell the admin that Question objects have an admin interface.
admin.site.register(Question)
admin.site.register(Choice)
# Register your models here.
