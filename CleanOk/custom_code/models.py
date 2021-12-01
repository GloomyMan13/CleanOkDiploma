from django_extensions.db.fields import AutoSlugField


from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)

from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel
from django.db import models

@register_snippet
class CustomCode(ClusterableModel):
    """Класс для добавления кастомного кода"""

    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="title", editable=True)
    js_name_file = models.CharField(max_length=50, default="customer.js")
    js_file = models.FileField(upload_to="js/", default="customer.js")
    css_name_file = models.CharField(max_length=50, default="customer.css")
    css_file = models.FileField(upload_to="css/", default="customer.css")


    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
            FieldPanel("js_name_file"),
            FieldPanel("js_file"),
            FieldPanel("css_name_file"),
            FieldPanel("css_file"),
        ], heading="Code"),
    ]

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "Добавить Дополнительный код"
        verbose_name_plural = "Добавить Дополнительный код"