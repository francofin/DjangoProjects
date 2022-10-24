from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from pytz import timezone
from requests import get
from django.conf import settings
import urllib.parse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Journal
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import JournalSerializer
from rest_framework.pagination import PageNumberPagination



@api_view(['GET'])
def get_all_journals(request):
    filterSet =Journal.objects.all().order_by('-created_at')

    count = filterSet.count()

    results_per_page = 10
    paginator = PageNumberPagination()
    paginator.page_size = results_per_page
    myPages = paginator.paginate_queryset(filterSet, request)
    serializer = JournalSerializer(myPages, many=True)

    context = {
        'count':count,
        'results_per_page':results_per_page,
        'indexes': serializer.data,
    }
    return Response(context)