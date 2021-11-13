from wagtail.core import blocks
from wagtail.core.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from django import forms


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.RichTextBlock(required=True, help_text="Add additional text")
    body = RichTextField(blank=True, help_text="Add additional text")
    img = ImageChooserBlock(required=True)

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


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
