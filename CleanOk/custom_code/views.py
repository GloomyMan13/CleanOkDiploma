from django.shortcuts import render
from  models import CustomStyle

def html_loader(request):

    data = CustomStyle.objects.all()
    print(data)
    Html_file = open("./CleanOk/templates/custom_code/style_page.html", "w")
    Html_file.write(data)
    Html_file.close()
    # render(request, "./CleanOk/templates/custom_code/style_page.html", {
    #     'data': data,
    # })
    return data

# html_loader()
#
# data = CustomStyle.objects.all()
# print(data)

