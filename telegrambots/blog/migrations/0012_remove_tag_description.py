# Generated by Django 5.0.2 on 2024-03-18 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_tag_category_description_category_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
    ]
