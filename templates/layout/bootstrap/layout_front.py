"""
This is an entry and Bootstrap class for the theme level.
"""
from utility.template.theme import TemplateHelper


class TemplateBootstrapLayoutFront:
    @staticmethod
    def init(context: dict) -> dict:
        context.update(
            {
                "layout": "front",
                "is_front": True,
                "display_customizer": True,
                "content_layout": "wide",
                "navbar_type": "fixed",
            }
        )
        # map_context according to updated context values
        TemplateHelper.map_context(context)

        return context
