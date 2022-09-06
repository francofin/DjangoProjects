from .models import Job
from django_filters import rest_framework as filters



class JobsFilter(filters.FilterSet):
    # gte is greater than ir equal to
    # lte is less than or equal to. 
    keyword = filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = filters.CharFilter(field_name='address', lookup_expr='icontains')
    min_salary = filters.NumberFilter(field_name="salary" or 0, lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name="salary" or 10000000, lookup_expr='lte')
    class Meta:
        model = Job
        fields = ('education', 'jobType', 'experience', 'industry', 'min_salary', 'max_salary', 'keyword', 'location')