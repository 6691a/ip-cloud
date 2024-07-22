from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView as DjangoCreateView
from django.views.generic import DeleteView as DjangoDeleteView
from django.views.generic import ListView

from compute.minecraft.models import Minecraft
from utility.form.mixin import LayoutMixin


class HomeView(LayoutMixin, LoginRequiredMixin, ListView):
    model = Minecraft
    template_name = "home.html"


class CreateView(LayoutMixin, LoginRequiredMixin, DjangoCreateView):
    model = Minecraft
    template_name = "create.html"


class DeleteView(LayoutMixin, LoginRequiredMixin, DjangoDeleteView):
    model = Minecraft
    template_name = "delete.html"
    # success_url = "/minecraft/home/"
