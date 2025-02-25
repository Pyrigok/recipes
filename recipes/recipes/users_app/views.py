from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets, status, response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from users_app import serializers, models
from users_app.serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    def retrieve(self, request, *args, **kwargs):
    # def get(self, request, pk, **kwargs):
        try:
            # user = models.User.objects.get(id=pk)
            instance = self.get_object()

        except ObjectDoesNotExist as ex:
            return response.Response({
                "details": str(ex)
            }, status=status.HTTP_400_BAD_REQUEST)
        # serializer = UserSerializer(user)

        serializer = self.get_serializer(instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


# class UsersViewSet(viewsets.ViewSet):
#     queryset = models.User.objects.all()
#     serializer = serializers.UserSerializer(queryset, many=True)
#
#     renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
#     template_name = "users/users.html"
#
#     def list(self, request):
#         users = models.User.objects.all()
#         serializer = serializers.UserSerializer(users, many=True)
#
#         # for testing in postman
#         return response.Response(serializer.data, status=status.HTTP_200_OK)
#         # for html template
#         # return render(request, "users/users.html", {"users": serializer.data})
#
#
#     # def get(self, request, *args, **kwargs):
#     #     return render_to_response(template_name, {'data': serializeddata.data})
#
#     def retrieve(self, request, pk, **kwargs):
#         try:
#             user = models.User.objects.get(id=pk)
#         except ObjectDoesNotExist as ex:
#             return response.Response({
#                 "details": str(ex)
#             }, status=status.HTTP_400_BAD_REQUEST)
#         serializer = UserSerializer(user)
#         return response.Response(serializer.data, status=status.HTTP_200_OK)
