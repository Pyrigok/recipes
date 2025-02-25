from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models import Count, Sum, Avg, Value

from rest_framework import generics, viewsets, status, response

from recipes_app.models import Recipe, Meat
from recipes_app.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk, **kwargs):
        try:
            recipe = Recipe.objects.get(id=pk)
        except ObjectDoesNotExist as ex:
            return response.Response({"details": str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = RecipeSerializer(recipe)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class InfoView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        meat_type = request.query_params.get("type", None)
        info = Recipe.objects.select_related("meat").filter(meat__type=meat_type).values("title").aggregate(
            count=Count('meat__id'),
            weight_sum=Sum("meat__weight"),
            weight_avg=Avg("meat__weight"),
            prices_sum=Avg("price"),
            prices_avg=Avg("price")
        )

        # info={}
        # data = Recipe.objects.all()
        # data= data.filter(meat__type=meat_type).values("title")
        # info["count"] = data.count()
        # info["weight_sum"] = Sum(data.)


        return response.Response({"info": info})


class MeatInfoView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        meat_type = request.query_params.get("type", None)
        info = Meat.objects.filter(title=meat_type).values("title").annotate(
        # info = Meat.objects.values("title").annotate(
            count=Count('title'),
            weight_sum=Sum("weight"),
            weight_avg=Avg("weight")
        )
        # if meat_type:
        #     info = info.filter(title=meat_type)
        return response.Response({"meat_info": info})
