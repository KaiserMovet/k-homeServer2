from django.http import HttpResponse
from django.template import loader


def indexx(request):
    template = loader.get_template('khS/base.html')

    return HttpResponse(template.render())
