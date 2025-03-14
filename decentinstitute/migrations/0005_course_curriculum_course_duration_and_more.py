# Generated by Django 5.1.4 on 2025-02-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decentinstitute', '0004_remove_course_description_course_full_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='curriculum',
            field=models.TextField(blank=True, help_text='Topics covered in the course.', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default='Not Specified', help_text='Duration of the course', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor_name',
            field=models.CharField(default='Not Assigned', help_text="Instructor's name", max_length=255),
        ),
        migrations.AddField(
            model_name='course',
            name='mode_of_learning',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline'), ('Hybrid', 'Hybrid')], default='Online', max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='full_description',
            field=models.TextField(help_text='Detailed course description.'),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.TextField(help_text='Brief introduction of the course.'),
        ),
    ]
