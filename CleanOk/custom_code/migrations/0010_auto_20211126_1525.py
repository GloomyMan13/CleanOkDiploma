# Generated by Django 3.2.9 on 2021-11-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_code', '0009_auto_20211126_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customcode',
            options={'verbose_name': 'Добавить Стиль css', 'verbose_name_plural': 'Добавить Стили css'},
        ),
        migrations.RemoveField(
            model_name='customcode',
            name='css_file',
        ),
        migrations.RemoveField(
            model_name='customcode',
            name='css_name_file',
        ),
        migrations.RemoveField(
            model_name='customcode',
            name='js_file',
        ),
        migrations.RemoveField(
            model_name='customcode',
            name='js_name_file',
        ),
        migrations.AddField(
            model_name='customcode',
            name='file',
            field=models.FileField(default='customer.js', upload_to='js/'),
        ),
        migrations.AddField(
            model_name='customcode',
            name='name_file',
            field=models.CharField(default='customeeer.js', max_length=50),
        ),
    ]
