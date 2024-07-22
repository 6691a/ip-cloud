from django.shortcuts import render
from django.views import View


class MinecraftView(View):
    def get(self, request):
        return render(request, "minecraft.html")
