from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class CustomStyle(Page, models.Model):
    """Класс для добавления кастомного кода"""
    template = "custom_code/style_page.html"
    css_code = models.CharField(max_length=50)

    content_panels = Page.content_panels + [
        FieldPanel('css_code')
    ]

    def __str__(self):
        return self.css_code

    class Meta:

        verbose_name = "Добавить Стиль css"
        verbose_name_plural = "Добавить Стили css"