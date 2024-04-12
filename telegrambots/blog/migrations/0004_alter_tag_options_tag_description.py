# Generated by Django 5.0.2 on 2024-04-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.CharField(default='Описание', max_length=255, verbose_name='Описание'),
        ),
    ]
