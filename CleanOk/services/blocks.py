from wagtail.core import blocks
from wagtail.core.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamField
from django.db import models

class TitleAndTextBlock(blocks.StreamBlock):
    """Блок для описания сотрудника. Картина Текст """
    custom_title = models.CharField(
        max_length=100,
        blank=True,
        null=False,
        help_text="Заголовок слева",
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    # ("title_and_text", blocks.TitleAndTextBlock()),
    # ("simple_richtext", blocks.SimpleRichtextBlock()),
    # ("cards", blocks.CardBlock()),
    # ("cta", blocks.CTABlock()),
    # content = StreamField(
    #     [
    #         ("full_richtext", RichTextField()),
    #     ],
    #     null=True,
    #     blank=True,
    # )

    # content_panels = Page.content_panels + [
    #     FieldPanel("custom_title"),
    #     ImageChooserPanel("blog_image"),
    #     StreamFieldPanel("content"),
    # ]

    block_content = blocks.RichTextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "services/tabel.html"
        icon = "edit"
        label = "Блок сервисов"