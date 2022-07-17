from django.shortcuts import get_object_or_404, render
from requests import get
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets, status
from .models import Job
from .serializers import JobSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Min, Max, Count
from .filters import JobsFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.


@api_view(['GET'])
def getAllJobs(request):
    jobs = Job.objects.all()

    filterSet = JobsFilter(request.GET, queryset = Job.objects.all().order_by('id'))

    count = filterSet.qs.count()

    # Pagination
    results_per_page = 3
    paginator = PageNumberPagination()
    paginator.page_size = results_per_page
    queryset = paginator.paginate_queryset(filterSet.qs, request)
    serializer = JobSerializer(queryset, many=True)

    context = {
        'count':count,
        'results_per_page':results_per_page,
        'jobs': serializer.data,
    }
    return Response(context)

@api_view(['GET'])
def getJob(request, pk):
    jobs = get_object_or_404(Job, id=pk)
    serializer = JobSerializer(jobs)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newJob(request):
    request.data['user'] = request.user
    data = request.data
    # **data is essentially the spread operator that spreads all the data in the create function for the Job fields. 

    job = Job.objects.create(**data)

    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])

def updateJob(request, pk):

    job = get_object_or_404(Job, id=pk)

    if job.user != request.user:
        return Response({
            'message':'Forbidden Access, you are not the owner of this posting'
        }, status= status.HTTP_403_FORBIDDEN)

    job.title = request.data['title']
    job.section_one = request.data['section_one']
    job.section_two = request.data['section_two']
    job.section_three = request.data['section_three']
    job.section_four = request.data['section_four']
    job.section_five = request.data['section_five']
    job.email = request.data['email']
    job.address = request.data['address']
    job.jobType = request.data['jobType']
    job.education = request.data['education']
    job.education_detail = request.data['education_detail']
    job.industry = request.data['industry']
    job.industry_detail = request.data['industry_detail']
    job.experience = request.data['experience']
    job.salary = request.data['salary']
    job.positions = request.data['positions']
    job.company = request.data['company']

    job.save()

    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    if job.user != request.user:
        return Response({
            'message':'Forbidden Access, you are not the owner of this posting'
        }, status= status.HTTP_403_FORBIDDEN)

    job.delete()

    return Response({ 'message': 'Job is Deleted.' }, status=status.HTTP_200_OK)


@api_view(['GET'])
def getTopicStats(request, topic):
    # Matches the title that contains the topic.
    args = { 'title__icontains': topic }
    jobs = Job.objects.filter(**args)

    if len(jobs) == 0:
        return Response({ 'message': 'Not stats found for {topic}'.format(topic=topic) })

    
    stats = jobs.aggregate(
        total_jobs = Count('title'),
        avg_positions = Avg('positions'),
        avg_salary = Avg('salary'),
        min_salary = Min('salary'),
        max_salary = Max('salary')
    )

    return Response(stats)