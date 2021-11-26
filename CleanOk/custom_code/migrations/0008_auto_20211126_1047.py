# Generated by Django 3.2.9 on 2021-11-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_code', '0007_customcode_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customcode',
            name='javascript',
        ),
        migrations.AddField(
            model_name='customcode',
            name='name_file',
            field=models.CharField(default='customeeer.js', max_length=50),
        ),
        migrations.AlterField(
            model_name='customcode',
            name='file',
            field=models.FileField(default='customeeer.js', upload_to='js/'),
        ),
    ]