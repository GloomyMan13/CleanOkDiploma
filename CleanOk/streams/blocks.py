from wagtail.core import blocks
from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from services import blocks as custom_block
from django import forms
from django.db import models


class TitleAndTextBlock(blocks.StructBlock):
    """Блок для Текст и заголовка h1"""

    title = blocks.CharBlock(required=True, help_text="Добавьте заголовок")
    text = blocks.RichTextBlock(required=True, help_text="Добавьте текст")
    img = ImageChooserBlock(required=False)

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Заголовок и текст"


class PictureBlock(blocks.StructBlock):
    """Блок для описания сотрудника. Картина Текст """
    text = blocks.RichTextBlock(required=False, help_text="Добавьте текст")
    img = ImageChooserBlock(required=True)


    class Meta:
        template = "streams/image_block.html"
        icon = "image"
        label = "Картинка"



class Requisites(blocks.StructBlock):
    """Блок для реквизитов """

    name_company = blocks.CharBlock(required=True, help_text="Наименование организации")
    inn_company = blocks.CharBlock(required=True, help_text="ИНН")
    name_bank = blocks.CharBlock(required=True, help_text="Наименование банка")
    bic_bank = blocks.CharBlock(required=True, help_text="БИК банка")
    pc_company = blocks.CharBlock(required=True, help_text="р/с")


    class Meta:
        template = "streams/requisites.html"
        icon = "form"
        label = "Реквизиты"

class EmployerBlock(blocks.StructBlock):
    """Блок для описания сотрудника. Картина Текст """

    name = blocks.CharBlock(required=True, help_text="Введите ФИО сотрудника")
    position =  blocks.CharBlock(required=True, help_text="Введите должность сотрудника")
    text = blocks.RichTextBlock(required=False, help_text="Введите дополнительный текст")
    img = ImageChooserBlock(required=False)

    class Meta:
        template = "streams/employer_block.html"
        icon = "edit"
        label = "Крточка Сотрудники"


class ServicesBlock(blocks.StructBlock):
    """Тестовый блок сервисов"""
    custom_title = models.CharField(
        max_length=100,
        blank=True,
        null=False,
        help_text="Заголовок слева",
    ) # required=True,
    number = models.CharField(help_text="Номер слева")
    block = custom_block.TitleAndTextBlock()

    class Meta:
        template = "services/tabel.html"
        icon = "edit"
        label = "Сервисы"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        return context


class CardBlock(blocks.StructBlock):
    """Блок для описания карточек сертификатов. Картинка Текст """

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
                        help_text="If the button page above is selected, that will be used first.",
                    ),
                ),
            ]
        )
    )

    class Meta:
        template = "streams/pdf_block.html"
        icon = "placeholder"
        label = "Карточки Сертификаты"

class SimpleRichtextBlock(blocks.RichTextBlock):
    pass

class RichtextBlock(blocks.StructBlock):
    """Блок с Richtext. Текст с заголовком h2 для textpage"""

    text = blocks.RichTextBlock(required=True, help_text="Добавьте текст")

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Блок Текста"



class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:
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

    class Meta:
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue