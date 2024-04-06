# Generated by Django 5.0.2 on 2024-04-06 07:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
    ]
