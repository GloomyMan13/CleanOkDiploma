"""Flexible page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks as streamfield_blocks

from streams import blocks


class FlexPage(Page):
    """Кастомная страница"""

    template = "flex/flex_page.html"
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("employer", blocks.EmployerBlock()),
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
        verbose_name = "Кастомная Страница"
        verbose_name_plural = "Кастомная Страница"
