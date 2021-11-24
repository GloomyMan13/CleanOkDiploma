from django.db import models
from django.http import HttpResponseNotFound

from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class MenuItem(Orderable):
    link_title = models.CharField(
        blank=False,
        null=False,
        default=None,
        max_length=50
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=False,
        blank=False,
        default=None,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(
        default=False,
        blank=True
    )

    page = ParentalKey("Menu", related_name="menu_items")

    panel = [
        FieldPanel("link_title"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]
    @property
    def link(self):
        if self.link_page is not None:
            return self.link_page.url
        # TODO: logging
        return HttpResponseNotFound("Something going wrong\nPage under maintaince")

    @property
    def title(self):
        if self.link_title is not None:
            return self.link_title
        else:
            return "Blank title"

@register_snippet
class Menu(ClusterableModel):
    """Main clusterable menu"""

    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="title", editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")
    ]

    def __str__(self):
        return self.title