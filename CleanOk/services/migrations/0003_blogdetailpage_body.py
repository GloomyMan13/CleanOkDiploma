# Generated by Django 3.2.9 on 2021-11-19 04:24

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20211119_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetailpage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]