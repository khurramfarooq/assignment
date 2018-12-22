from rest_framework import viewsets, generics

from app.models.models import Router
from app.serializer.stc_serializer import RouterSerializer


class STCViewSet(generics.ListAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = RouterSerializer

    def get_queryset(self):
        query_params = dict(filter(lambda val: val[1], self.kwargs.items()))
        queryset = Router.objects.filter(**query_params)
        return queryset
