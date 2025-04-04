import django_filters
from .models import Medico

class MedicoFilter(django_filters.FilterSet):
    especialidade = django_filters.CharFilter(lookup_expr='icontains')
 

    class Meta:
        model = Medico
        fields = ['especialidade']