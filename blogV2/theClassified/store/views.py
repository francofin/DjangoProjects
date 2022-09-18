from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
# Create your views here.


def get_payment_key(request):

    stripe_payment_key = settings.STRIPE_SECRET_KEY

    return Response(stripe_payment_key)