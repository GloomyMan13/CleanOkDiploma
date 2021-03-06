# Generated by Django 3.2.9 on 2021-11-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_addresses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'подвал левый', 'verbose_name_plural': 'подвал левый'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='map_file',
            field=models.FileField(default='map.html', upload_to='map/'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='map_name_file',
            field=models.CharField(default='map.html', max_length=50),
        ),
    ]
