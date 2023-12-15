from moviesapp.viewsets import MovieViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movie',MovieViewset)