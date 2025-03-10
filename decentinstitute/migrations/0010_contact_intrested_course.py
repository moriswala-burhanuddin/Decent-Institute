# Generated by Django 5.1.4 on 2025-02-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decentinstitute', '0009_remove_contact_email_addr_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='intrested_course',
            field=models.CharField(blank=True, choices=[('web_dev', 'Web Development'), ('app_dev', 'App Development'), ('data_science', 'Data Science'), ('cyber_security', 'Cyber Security'), ('ai_ml', 'AI & Machine Learning'), ('graphic_design', 'Graphic Design'), ('digital_marketing', 'Digital Marketing')], max_length=50, null=True),
        ),
    ]
