# Generated by Django 3.2.9 on 2021-11-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_menus', '0023_auto_20211127_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menufooter',
            name='footer_phone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menufooter',
            name='footer_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
