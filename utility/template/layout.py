from utility.template.theme import TemplateHelper


class BaseTemplateLayout(dict):
    def __new__(cls, request, context, **kwargs):
        instance = TemplateHelper.init_context(context)
        instance = TemplateHelper.map_context(instance)
        return instance


class TemplateLayout(BaseTemplateLayout):
    def __new__(cls, request, context, **kwargs):
        instance = super().__new__(cls, request, context, **kwargs)
        instance.update(
            {
                "layout_path": TemplateHelper.set_layout(
                    f"layout_{instance['layout']}.html", context
                ),
            }
        )
        return instance


class TemplateLayoutBlank(BaseTemplateLayout):
    def __new__(cls, request, context, **kwargs):
        instance = super().__new__(cls, request, context, **kwargs)
        instance.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )
        return instance
