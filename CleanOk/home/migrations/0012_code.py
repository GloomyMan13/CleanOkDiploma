# Generated by Django 3.2.9 on 2021-11-26 05:12

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_delete_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('js_code', wagtail.core.fields.RichTextField()),
                ('css_code', wagtail.core.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Добавить кастомный код',
                'verbose_name_plural': 'Добавить кастомный код',
            },
        ),
    ]
