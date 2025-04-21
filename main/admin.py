from django.contrib import admin
from .models import Course, CourseSeries,Faculty,Event
# from tinymce.widgets import TinyMCE
from django.db import models
from froala_editor.widgets import FroalaEditor


class CourseSeriesAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "subtitle",
        "slug",
        # "published"
    ]

class CourseAdmin(admin.ModelAdmin):
     fieldsets = [
        ("Header", {'fields': ["title", "subtitle", "article_slug", "series"]}),
        ("Content", {"fields": ["content", "notes"]}),
        ("Date", {"fields": ["modified"]})
    ]
     

class EventAdmin(admin.ModelAdmin):
     formfield_overrides = {
         models.TextField: {'widget':  FroalaEditor()},
     }
     fieldsets = [
        ("Header", {'fields': ["title"]}),
        ("Content", {"fields": ["desc"]}),
        ("Date", {"fields": ["event_date"]})
    ]













# Register your models here.
admin.site.register(CourseSeries)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Event, EventAdmin)