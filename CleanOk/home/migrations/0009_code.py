# Generated by Django 3.2.9 on 2021-11-26 04:11

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_add_content'),
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
                'verbose_name': 'Футер',
                'verbose_name_plural': 'Футеры',
            },
        ),
    ]
