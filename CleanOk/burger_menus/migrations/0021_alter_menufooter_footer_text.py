# Generated by Django 3.2.9 on 2021-11-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_menus', '0020_alter_menufooter_footer_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menufooter',
            name='footer_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
