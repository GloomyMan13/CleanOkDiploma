from wagtail.core.models import Page


from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from wagtailcaptcha.models import WagtailCaptchaEmailForm

from streams import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
# from wagtail.core.fields import RichTextField
# from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

# class HomePage(Page):
#
#     template = "home/home_page.html"

class FormField(AbstractFormField):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='custom_form_fields')

@register_snippet
class Footer(models.Model):

    bodytext = RichTextField()

    panels = [
        FieldPanel('bodytext')
    ]

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футеры"

    def __str__(self):
        return "Футер"

class HomePage(WagtailCaptchaEmailForm, Page):
    template = "home/home_page.html"
    # template = "home/textpage.html"
    landing_page_template = "form/form_page_landing.html"
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    code = RichTextField(blank=True)

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
        StreamFieldPanel("content"),
        StreamFieldPanel("add_content"),
        FieldPanel('code'),
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