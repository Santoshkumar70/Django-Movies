from rest_framework import viewsets
from .import models
from .import serarilizers

class MovieViewset(viewsets.ModelViewSet):
    queryset = models.Movies.objects.all()
    serializer_class = serarilizers.MoviesSerializer