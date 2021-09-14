from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func


def test_celery_view(request):
    test_func.delay()
    return HttpResponse("done")
