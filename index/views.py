from django.views.generic import TemplateView

from utility.form.mixin import LayoutMixin


class IndexView(LayoutMixin, TemplateView):
    template_name = "index.html"
