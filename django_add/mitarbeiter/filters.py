import django_filters

from .models import Mitarbeiter

class MitarbeiterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    einstellungsdatum = django_filters.DateFilter(lookup_expr="gte")
    telefonnummer = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = Mitarbeiter
        fields = ["name", "einstellungsdatum", "telefonnummer" ]