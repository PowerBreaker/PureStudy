from django.contrib import admin

# Register your models here.
from .models import Course, Chapter, Maker, Img

admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Maker)
admin.site.register(Img)