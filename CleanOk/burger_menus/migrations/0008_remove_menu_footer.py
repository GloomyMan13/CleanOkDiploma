# Generated by Django 3.2.9 on 2021-11-27 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burger_menus', '0007_alter_menu_footer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='footer',
        ),
    ]
