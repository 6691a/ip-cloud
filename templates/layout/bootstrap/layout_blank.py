"""
This is an entry and Bootstrap class for the theme level.
"""

from utility.template.theme import TemplateHelper


class TemplateBootstrapLayoutBlank:
    @staticmethod
    def init(context: dict) -> dict:
        context.update(
            {
                "layout": "blank",
                "content_layout": "wide",
                "display_customizer": False,
            }
        )
        # map_context according to updated context values
        TemplateHelper.map_context(context)

        return context
