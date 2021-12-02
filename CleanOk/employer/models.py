"""Страница сотрудников"""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from streams import blocks


class EmployerPage(Page):
    """Класс страницы сотрудников."""

    template = "employer/employer_page.html"
    content = StreamField(
        [
            ("employer", blocks.EmployerBlock()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудники"

