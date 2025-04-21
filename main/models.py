from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from froala_editor.fields import FroalaField,FroalaEditor
  


class CourseSeries(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=True)
    slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
    published = models.DateTimeField('Date published', default=timezone.now)

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']



class Faculty(models.Model):
    name = models.CharField(max_length=200,default="",null=True,blank=True,unique=True)
    edu = models.CharField(max_length=200, default='', blank=True)
    field_of_expertise = models.CharField(max_length=200)
    desg = models.CharField(max_length=200)
    yoe = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    Course_slug = models.SlugField("Course slug", null=False, blank=False, unique=True)
    content = models.TextField()
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    content = FroalaField(options={
        'codeMirror': False, 
      
    })
    notes = FroalaField(options={
      'codeMirror': False, 
      
    })
    series = models.ForeignKey(CourseSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    course_faculty=models.ForeignKey(Faculty,null=True,blank=True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.Course_slug

    class Meta:
        verbose_name_plural = "Course"
        ordering = ['-published']


class Event(models.Model):
    title = models.CharField(max_length=200, null=False, default="Announcement")
    # desc = HTMLField(blank=True, default="")
    desc = FroalaField()
    event_date = models.DateTimeField("Date of the event")

    def __str__(self):
        return self.title

