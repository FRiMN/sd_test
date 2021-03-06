# Generated by Django 2.1.1 on 2018-09-26 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sibdev', '0002_urlqueue_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executed_at', models.DateTimeField(auto_now=True, verbose_name='Дата получения данных страницы')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок страницы')),
                ('header', models.CharField(max_length=256, null=True, verbose_name='Заголовок H1 на странице')),
                ('charset', models.CharField(max_length=256, verbose_name='Кодировка страницы')),
            ],
        ),
        migrations.AlterField(
            model_name='urlqueue',
            name='url',
            field=models.CharField(max_length=256, verbose_name='URL для парсинга'),
        ),
        migrations.AddField(
            model_name='results',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sibdev.UrlQueue'),
        ),
    ]
