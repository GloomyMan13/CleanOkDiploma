# Generated by Django 3.2.9 on 2021-11-25 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('custom_code', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomStyle',
        ),
    ]
