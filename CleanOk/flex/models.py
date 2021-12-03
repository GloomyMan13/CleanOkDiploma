""""Кастомная страница"""
from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from streams import blocks


class FlexPage(Page):
    """Кастомная страница"""

    template = "flex/flex_page.html"
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("picture", blocks.PictureBlock()),
            ("requisites", blocks.Requisites()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Добавить Страницу"
        verbose_name_plural = "Добавить Страницу"
