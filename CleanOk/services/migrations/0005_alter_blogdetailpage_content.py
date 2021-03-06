# Generated by Django 3.2.9 on 2021-12-02 14:06

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_blogdetailpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Добавьте заголовок', required=True)), ('text', wagtail.core.blocks.RichTextBlock(help_text='Добавьте текст', required=True)), ('img', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('full_richtext', streams.blocks.RichtextBlock())], blank=True, null=True),
        ),
    ]
