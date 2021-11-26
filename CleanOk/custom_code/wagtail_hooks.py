# # from django.contrib.staticfiles.templatetags.staticfiles import static
# # from django.contrib.staticfiles.templatetags.staticfiles import static
# from django.templatetags.static import static
# from django.utils.html import format_html
# from  .models import CustomStyle
#
# from wagtail.core import hooks
#
# # @hooks.register("insert_global_site_css", order=100)
# def global_admin_css(code):
#     """Add /static/css/custom.css to the admin."""
#     # '<link rel="stylesheet" href="{}">'
#     return format_html(
#         code,
#         static("css/custom.css")
#     )
#
#
# # @hooks.register("insert_global_site_js", order=100)
# def custom_js(code):
#     """Add /static/css/custom.js to the admin."""
#     # '<script src="{}"></script>'
#     # print(code)
#     return format_html(
#         code,
#         static("/js/custom.js")
#     )
#
# data = CustomStyle.objects.all()[0].save()
# custom_js(data)

# CustomStyle.custom_js('code')