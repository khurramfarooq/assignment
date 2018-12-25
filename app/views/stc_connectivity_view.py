
from rest_framework import generics
from rest_framework.decorators import action

from app.models.models import Router
from app.serializer.stc_serializer import ConnectivitySerializer


class STCRouterNeighbour(generics.ListAPIView):
    serializer_class = ConnectivitySerializer

    def get_queryset(self):
        query_params = dict(filter(lambda val: val[1], self.kwargs.items()))
        queryset = Router.objects.filter(**query_params)
        return queryset