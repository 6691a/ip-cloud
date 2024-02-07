from django.views.generic.base import ContextMixin, View

from utility.template.layout import TemplateLayout, TemplateLayoutBlank


class LayoutBlankMixin(ContextMixin, View):
    def get_context_data(self, **kwargs) -> dict:
        context: dict = super().get_context_data(**kwargs)
        return TemplateLayoutBlank(self.request, context)


class LayoutMixin(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        return TemplateLayout(self.request, context)
