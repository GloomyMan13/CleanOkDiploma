# Generated by Django 3.2.9 on 2021-11-25 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('custom_code', '0002_delete_customstyle'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomStyle',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('css_code', models.CharField(max_length=50)),
                ('js_code', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Добавить Стиль css',
                'verbose_name_plural': 'Добавить Стили css',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
