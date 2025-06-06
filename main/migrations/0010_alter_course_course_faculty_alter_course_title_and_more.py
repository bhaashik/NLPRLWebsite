# Generated by Django 4.1.1 on 2023-12-04 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_course_course_faculty_alter_faculty_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.faculty'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(default='unnamed', max_length=200),
            preserve_default=False,
        ),
    ]
