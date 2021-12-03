# Generated by Django 3.2.9 on 2021-12-02 14:30

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0010_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Добавьте заголовок', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Добавьте текст', required=True)), ('img', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('employer', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Введите ФИО сотрудника', required=True)), ('position', wagtail.core.blocks.CharBlock(help_text='Введите должность сотрудника', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Введите дополнительный текст', required=False)), ('img', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('full_richtext', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(help_text='Добавьте текст', required=True))]))], blank=True, null=True),
        ),
    ]
