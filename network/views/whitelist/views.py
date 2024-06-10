from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from network.models.models import WhiteList
from utility.form.mixin import LoginRequiredLayoutMixin


class WhiteListBaseView(LoginRequiredLayoutMixin, View):
    model = WhiteList
    success_url = reverse_lazy("network:whitelist_list")


class WhiteListListView(WhiteListBaseView, ListView):
    model = WhiteList
    template_name = "whitelist/list.html"


#
# class WhiteListCreateView(LoginRequiredLayoutMixin, CreateView):
#     form_class = WhiteListCreateForm
#     template_name = "whitelist/create.html"
#     success_url = reverse_lazy("network:whitelist-list")
#
#     def form_valid(self, form):
#         # TODO Kafka producer create taks
#         return super().form_valid(form)
