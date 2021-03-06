# Generated by Django 3.2.9 on 2021-11-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_code', '0010_auto_20211126_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customcode',
            name='file',
        ),
        migrations.RemoveField(
            model_name='customcode',
            name='name_file',
        ),
        migrations.AddField(
            model_name='customcode',
            name='css_file',
            field=models.FileField(default='customer.css', upload_to='js/'),
        ),
        migrations.AddField(
            model_name='customcode',
            name='css_name_file',
            field=models.CharField(default='customer.css', max_length=50),
        ),
        migrations.AddField(
            model_name='customcode',
            name='js_file',
            field=models.FileField(default='customer.js', upload_to='js/'),
        ),
        migrations.AddField(
            model_name='customcode',
            name='js_name_file',
            field=models.CharField(default='customer.js', max_length=50),
        ),
    ]
