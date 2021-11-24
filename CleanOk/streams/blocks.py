from wagtail.core import blocks
from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from services import blocks as custom_block
from django import forms
from django.db import models


class TitleAndTextBlock(blocks.StructBlock):
    """Блок для описания сотрудника. Картина Текст """

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.RichTextBlock(required=True, help_text="Add additional text")
    body = RichTextField(blank=True, help_text="Add additional text")
    img = ImageChooserBlock(required=False)
    # img = models.ForeignKey(
    #     "wagtailimages.Image",
    #     blank=True,
    #     null=True,
    #     related_name="+",
    #     on_delete=models.SET_NULL,
    # )

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class EmployerBlock(blocks.StructBlock):
    """Блок для описания сотрудника. Картина Текст """

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.RichTextBlock(required=True, help_text="Add additional text")
    body = RichTextField(blank=True, help_text="Add additional text")
    img = ImageChooserBlock(required=False)
    # img = models.ForeignKey(
    #     "wagtailimages.Image",
    #     blank=True,
    #     null=True,
    #     related_name="+",
    #     on_delete=models.SET_NULL,
    # )

    class Meta:  # noqa
        template = "streams/employer_block.html"
        icon = "edit"
        label = "Крточка Сотрудники"


class ServicesBlock(blocks.StructBlock): #blocks.StructBlock
    """Блок сервисов"""
    custom_title = models.CharField(
        max_length=100,
        blank=True,
        null=False,
        help_text="Заголовок слева",
    ) # required=True,
    number = models.CharField(help_text="Номер слева")
    block = custom_block.TitleAndTextBlock()

    class Meta:  # noqa
        template = "services/tabel.html"
        icon = "edit"
        label = "Сервисы"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        return context


class CardBlock(blocks.StructBlock):
    """Блок для описания карточек сертификатов. Картина Текст """

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("name_company", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/pdf_block.html"
        icon = "placeholder"
        label = "Staff Cards"


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class LinkStructValue(blocks.StructValue):
    """Additional logic for our urls."""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None

    # def latest_posts(self):
    #     return BlogDetailPage.objects.live()[:3]



class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""

    button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page')

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
    #     return context

    class Meta:  # noqa
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue

# class MapBlock(blocks.StructBlock):
#     marker_title = blocks.CharBlock(max_length=120,
#                                     default="Marker Title 'This will be updated after you save changes.'")
#     marker_description = blocks.RichTextBlock()
#     zoom_level = blocks.IntegerBlock(min_value=0, max_value=18, default='2', required=False)
#     location_x = blocks.FloatBlock(default='35.0', required=False)
#     location_y = blocks.FloatBlock(default='0.16', required=False)
#     marker_x = blocks.FloatBlock(default='51.5', required=False)
#     marker_y = blocks.FloatBlock(default='-0.09', required=False)
#
#     @property
#     def media(self):
#         return forms.Media(
#             js=["https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"],
#             css={'all': ["https://unpkg.com/leaflet@1.4.0/dist/leaflet.css"]}
#         )
#
#     class Meta:
#         form_template = 'wagtail_blocks/admin_blocks/map.html'
#         template = 'wagtail_blocks/map.html'
#         icon = "fa-globe"
