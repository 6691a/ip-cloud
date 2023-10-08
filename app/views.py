from django.views.generic import TemplateView

from utility.template.layout import TemplateLayout


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return TemplateLayout(self.request, context)
