from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from users_app.models import User
from users_app.serializers import UserSerializer


def chat(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("user-login")

    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    context = {}
    # context = {"users": serializer.data}
    return render(request, "chats/chat.html", context)
    # return render(request, "users/users.html", )


class ChatBotView(TemplateView):
    template_name: str = "chats/chat_bot.html"
