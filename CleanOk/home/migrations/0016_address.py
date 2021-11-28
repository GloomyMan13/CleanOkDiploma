# Generated by Django 3.2.9 on 2021-11-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_footerr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(help_text='Напишите имя города', max_length=100)),
                ('address', models.CharField(help_text='Напишите адрес', max_length=100)),
                ('phone_number', models.CharField(help_text='Напишите номер телефона', max_length=100)),
            ],
            options={
                'verbose_name': 'адреса карты',
                'verbose_name_plural': 'адреса карты',
            },
        ),
    ]
