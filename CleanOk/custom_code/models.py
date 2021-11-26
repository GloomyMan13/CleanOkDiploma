# from django.db import models
# from wagtail.core.models import Page
# from wagtail.admin.edit_handlers import FieldPanel
# import re
# # from .wagtail_hooks import custom_js
# from django.templatetags.static import static
# from django.utils.html import format_html
# from wagtail.core.fields import RichTextField
#
#
# class CustomStyle(Page, models.Model):
#     """Класс для добавления кастомного кода"""
#     # template = "..static/js/custom.js"
#     template = "base.html"
#     css_code = models.CharField(max_length=50)
#     js_code = RichTextField(blank=True)
#     # intro = RichTextField(blank=True)
#
#
#     content_panels = Page.content_panels + [
#         FieldPanel('css_code'),
#         FieldPanel('js_code'),
#     ]
#
#     def __str__(self):
#         return self.css_code
#
#     # def save(self):
#     #     # self.matchname = re.sub("\W+", "", self.js_code)
#     #     return re.sub("\W+" , "", js_code)
#
#     def custom_js(self):
#         """Add /static/css/custom.js to the admin."""
#         # '<script src="{}"></script>'
#         # print(code)
#         return format_html(
#             self.js_code,
#             static("/js/custom.js")
#         )
#
#     # js = custom_js()
#     class Meta:
#
#         verbose_name = "Добавить Стиль css"
#         verbose_name_plural = "Добавить Стили css"

# from django.apps import AppConfig
#
#
# class CoreConfig(AppConfig):
#     name = 'core'
from wagtail.core.fields import RichTextField

from django.db import models
from django.http import HttpResponseNotFound

from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel
from django.db import models


class CodeItem(Orderable):
    # link_title = models.CharField(
    #     blank=False,
    #     null=False,
    #     default=None,
    #     max_length=50
    # )
    # link_page = models.ForeignKey(
    #     "wagtailcore.Page",
    #     null=False,
    #     blank=False,
    #     default=None,
    #     related_name="+",
    #     on_delete=models.CASCADE,
    # )
    # open_in_new_tab = models.BooleanField(
    #     default=False,
    #     blank=True
    # )

    page = ParentalKey("CustomCode", related_name="code_items")
    css_code = RichTextField()
    js_code = RichTextField()


    panels = [
        FieldPanel('css_code'),
        FieldPanel('js_code'),
    ]

    # panel = [
    #     FieldPanel("link_title"),
    #     PageChooserPanel("link_page"),
    # ]

    # @property
    # def link(self):
    #     if self.link_page is not None:
    #         return self.link_page.url
    #     # TODO: logging
    #     return HttpResponseNotFound("Something going wrong\nPage under maintaince")

    @property
    def code_js(self):
        if self.js_code is not None:
            return self.js_code
        else:
            return "No js"

    @property
    def code_css(self):
        if self.css_code is not None:
            return self.css_code
        else:
            return "No css"

# @register_snippet
# class Menu(ClusterableModel):
#     """Main clusterable menu"""
#
#     title = models.CharField(max_length=50)
#     slug = AutoSlugField(populate_from="title", editable=True)
#
#     panels = [
#         MultiFieldPanel([
#             FieldPanel("title"),
#             FieldPanel("slug"),
#         ], heading="Menu"),
#         InlinePanel("menu_items", label="Menu Item")
#     ]
#
#     def __str__(self):
#         return self.title

@register_snippet
class CustomCode(ClusterableModel):
    """Класс для добавления кастомного кода"""

    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="title", editable=True)
    name_file = models.CharField(max_length=50, default="customeeer.js")
    file = models.FileField(upload_to="js/", default="customer.js")


    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
            FieldPanel("name_file"),
            FieldPanel("file"),
        ], heading="Code"),
        InlinePanel("code_items", label="Code Item")
    ]

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "Добавить Стиль css"
        verbose_name_plural = "Добавить Стили css"