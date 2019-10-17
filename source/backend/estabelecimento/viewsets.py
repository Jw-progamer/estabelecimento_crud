from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Estabelecimento
from .serializers import EstabelecimentoSerializer


class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer

    @action(detail=False, methods=["GET"])
    def location_close(self, request):
        raio_atual = request.GET.get('raio', '')
        raio_atual = int(raio_atual)
        estabelecimentos = Estabelecimento.objects.all()
        if not estabelecimentos:
            return Response(data="estabelecimentos não encotrados", status=status.HTTP_404_NOT_FOUND)
        estabelecimentos = sorted(
            estabelecimentos, key=lambda e: e.distance(raio_atual))
        estabelecimentos_serializados = self.get_serializer(
            estabelecimentos, many=True)
        return Response(data=estabelecimentos_serializados.data, status=status.HTTP_200_OK)
