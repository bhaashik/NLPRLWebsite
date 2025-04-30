from cgitb import enable
from enum import unique

from django.db import models
from django.utils import timezone
from django.utils.translation.template import blankout
# from tinymce.models import HTMLField
from froala_editor.fields import FroalaField,FroalaEditor


class CourseSeries(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, unique=True)
    subtitle = models.CharField(max_length=200, default='', blank=True, unique=True)
    slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
    published = models.DateTimeField('Date published', default=timezone.now, null=False, blank=False, unique=True)
    degree = models.TextChoices(choices=[], possible_choices = ['B.Tech.', 'IDD', 'M.Tech.', 'PhD'], enabled=True, null=False, unique=True)
    parent_discipline = models.TextChoices(choices=[], possible_choices = [], enabled=True, null=False, blank=False, unique=True)
    major_discipline = models.TextChoices(choices=[], possible_choices = [], enabled=False, null=True, blank=True, unique=False)
    minor_discipline = models.TextChoices(choices=[], possible_choices = [], enabled=False, null=True, blank=True, unique=False)
    semester = models.TextChoices(choices=[], possible_choices = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'], enabled=True, blank=False, null=False, unique=False)
    even_odd = models.TextChoices(choices=[], possible_choices = ['EVEN', 'ODD'], enabled=True, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published', 'title', 'degree', 'parent_discipline', 'minor_discipline', 'semester', 'even_odd']


class Faculty(models.Model):
    name = models.CharField(max_length=100,default="",null=False,blank=False,unique=False)
    designation = models.TextChoicesCharField(choices = [], default='Assistant Professor', blank=False, null=False, unique=False)
    field_of_expertise1 = models.CharField(max_length=200)
    field_of_expertise2 = models.CharField(max_length=200)
    field_of_expertise3 = models.CharField(max_length=200)

    description = models.CharField(max_length=200, null=False, blank=False, unique=False)
    institue_email_id = models.EmailField(null=False, blank=False, unique=True)
    personal_email_id = models.EmailField( null=True, blank=True, unique=True)
    employee_id = models.BigIntegerField(max_digits=6, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_code = models.TextChoices(choices=[], possible_choices = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'], enabled=True, null=False, unique=False)
    course_name = models.CharField(max_length=100, enabled=True, null=False, unique=False)
    subtitle = models.CharField(max_length=200, default='', null=False, blank=True, unique=False)
    slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
    published = models.DateTimeField('Date published', default=timezone.now, null=True, enabled=False, blank=False, unique=True)
    degree = models.TextChoices(choices=[], possible_choices = ['B.Tech.', 'IDD', 'M.Tech.', 'PhD'], enabled=True, null=False, blank=False, unique=False)
    parent_discipline = models.TextChoices(choices=[], possible_choices = [], enabled=False, null=False, blank=False, unique=True)
    major_discipline = models.TextChoices(choices=[], possible_choices = [], enabled=False, null=False, blank=False, unique=True)
    minor_discipline = models.TextChoices(choices=[], possible_choices = [], enabled=False, null=False, blank=False, unique=True)
    semester = models.TextChoices(choices=[], possible_choices = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'], enabled=False, null=False, blank=False, unique=True)
    even_odd = models.TextChoices(choices=[], possible_choices = ['EVEN', 'ODD'])
    course_series = models.TextChoices(choices=[], possible_choices = [], enabled=False, null=True, blank=True, unique=True)


    # title = models.CharField(max_length=200)
    # subtitle = models.CharField(max_length=200, default="", blank=True)
    # Course_slug = models.SlugField("Course slug", default=timezone.now, null=False, blank=False, unique=True)
    # Course_code = models.TextField()
    # Course_name = models.TextField()
    brief_content = models.TextField(enabled=False, null=True, blank=True, unique=True)
    # published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now, null=False, enabled=False, blank=False, unique=True)
    content = FroalaField(options={
        'codeMirror': False
    }, null=False, enabled=False, blank=False, unique=True)

    notes = FroalaField(options={
      'codeMirror': False
    }, null=True, blank=True, enabled=False, unique=False)
    series = models.ForeignKey(CourseSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    course_faculty=models.ForeignKey(Faculty,null=True,blank=True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.Course_slug

    # class Meta:
    #     verbose_name_plural = "Course"
    #     ordering = ['course_code', 'course_name', 'degree', 'series' 'parent_discipline', 'minor_discipline', 'semester', 'even_odd']

    class Meta:
        verbose_name_plural = "Course"
        ordering = ['course_code', 'course_name', 'degree', 'parent_discipline', 'minor_discipline', 'semester', 'even_odd', 'course_series', '-published', '-modified']


class Event(models.Model):
    title = models.CharField(max_length=200, null=False, enabled=True, blank=False, unique=False)
    event_code = models.IntegerField(max_digit=12, null=False, enabled=True, blank=False, unique=True)
    subtitle = models.CharField(max_length=200, default="", blank=True, unique=False, enabled=True)
    venue = models.CharField(max_length=100, null=False, blank=False, unique=False)
    start_date = models.DateTimeField("Start Date", default=timezone.now, null=False, enabled=True, blank=False, unique=True)
    end_date = models.DateTimeField("End Date", default=timezone.now, null=False, enabled=True, blank=False, unique=True)

    # def save(self, *args, **kwargs):
    #     if not self.Event_slug:
    #         self.Event_slug = slugify(self)
    #
    #     # Check for uniqueness
    #     original_slug = self.Event_slug
    #     queryset = Event.objects.all()
    #     counter = 1
    #
    #     while queryset.filter(Event_slug=self.Event_slug).exists():
    #         self.Event_slug = f"{original_slug}-{counter}"
    #         counter += 1
    #
    #     super().save(*args, **kwargs)


    Event_slug = models.SlugField("Event slug", default=timezone.now(), null=False, blank=False, unique=True)
    content = models.TextField()
    published = models.DateTimeField("Date published", default=timezone.now, unique=True)
    modified = models.DateTimeField("Date modified", default=timezone.now, unique=True)
    content = FroalaField(options={
        'codeMirror': False,

    }, null=False, enabled=False, blank=False, unique=False)

    notes = FroalaField(options={
        'codeMirror': False,

    }, enabled=False, null=True, blank=True, unique=False)
    series = models.ForeignKey(CourseSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    event_faculty = models.ForeignKey(Faculty, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.Event_slug

    class Meta:
        verbose_name_plural = "Event"
        ordering = ['-published']

    def __str__(self):
        return self.title


#class EventDetail(models.Model):
#    title = models.CharField(max_length=200, null=False, default="Announcement")
#    desc = HTMLField(blank=True, default="")
#    desc = FroalaField()
#    event_date = models.DateTimeField("Date of the event")

#    def __str__(self):
#        return self.title
