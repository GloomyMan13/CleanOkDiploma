from wagtail.core.models import Page


from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from wagtailcaptcha.models import WagtailCaptchaEmailForm

from streams import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.snippets.models import register_snippet
from django.http import JsonResponse
from django.forms.models import model_to_dict

class FormField(AbstractFormField):
    """Модель для формы"""
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='custom_form_fields')

@register_snippet
class Footer(models.Model):

    bodytext = RichTextField()

    panels = [
        FieldPanel('bodytext')
    ]

    class Meta:
        verbose_name = "подвал левый"
        verbose_name_plural = "подвал левый"

    def __str__(self):
        return "подвал левый"

@register_snippet
class Footerr(models.Model):

    bodytext = RichTextField()

    panels = [
        FieldPanel('bodytext')
    ]

    class Meta:
        verbose_name = "подвал правый"
        verbose_name_plural = "подвал правый"

    def __str__(self):
        return "подвал правый"

@register_snippet
class Address(models.Model):

    name_city = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Напишите имя города',
    )
    address = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Напишите адрес',
    )
    phone_number = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Напишите номер телефона',
    )

    panels = [
        FieldPanel("name_city"),
        FieldPanel("address"),
        FieldPanel("phone_number"),
    ]

    class Meta:
        verbose_name = "адреса карты"
        verbose_name_plural = "адреса карты"

    def __str__(self):
        return self.name_city

class Addresses(Page):
    def serve(self, request):
        result = JsonResponse({})
        city = request.GET.get('city')
        if city:
            addresses = Address.objects.filter(name_city__icontains=city)
            result = JsonResponse(model_to_dict(addresses.first()))
        return result


class HomePage(WagtailCaptchaEmailForm, Page):
    """Модель главной страницы"""
    template = "home/home_page.html"
    # template = "home/textpage.html"
    landing_page_template = "form/form_page_landing.html"
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    map_name_file = models.CharField(max_length=50, default="map.html")
    map_file = models.FileField(upload_to="map/", default="map.html")

    content = StreamField(
        [
            ("cards", blocks.CardBlock()),
        ],
        null=True,
        blank=True,
    )
    add_content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )


    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('map_name_file'),
        FieldPanel('map_file'),
        StreamFieldPanel("content"),
        StreamFieldPanel("add_content"),
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('custom_form_fields', label="Контактное поле"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = CityPage.objects.live().public()
        return context

class CityPage(Page):
    """В моделе описывается гиперссылка 60 городов"""
    template = "home/city_page.html"
    body = RichTextField(blank=True)

    name_city = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Напишите имя города',
    )
    address = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Напишите адрес',
    )
    phone_number = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Напишите номер телефона',
    )

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("picture", blocks.PictureBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("name_city"),
        FieldPanel("address"),
        FieldPanel("phone_number"),
        StreamFieldPanel("content"),
    ]

    # def get_context(self, request, *args, **kwargs):
    #     """Adding custom stuff to our context."""
    #     # context = super().get_context(request, *args, **kwargs)
    #     # context["cards"] = BlogDetailPage.objects.live().public()
    #     # print(context["cards"])
    #     #
    #     # return context
    #     context = self.content.all()
    #     return context

# class BlogDetailPage(Page):
#     """Blog detail page."""
#     # template = "blog/blog_detail_page.html"
#     body = RichTextField(blank=True)
#
#     custom_title = models.CharField(
#         max_length=100,
#         blank=False,
#         null=False,
#         help_text='Overwrites the default title',
#     )
#     blog_image = models.ForeignKey(
#         "wagtailimages.Image",
#         blank=True,
#         null=True,
#         related_name="+",
#         on_delete=models.SET_NULL,
#     )
#
#     content = StreamField(
#         [
#             ("title_and_text", blocks.TitleAndTextBlock()),
#             ("full_richtext", blocks.RichtextBlock()),
#             ("simple_richtext", blocks.SimpleRichtextBlock()),
#             ("cards", blocks.CardBlock()),
#             ("cta", blocks.CTABlock()),
#         ],
#         null=True,
#         blank=True,
#     )
#
#     content_panels = Page.content_panels + [
#         FieldPanel("custom_title"),
#         ImageChooserPanel("blog_image"),
#         StreamFieldPanel("content"),
#     ]