"""
This is an entry and Bootstrap class for the theme level.
"""
import json

from django.conf import settings

from utility.template.theme import TemplateHelper

menu_file_path = (
    settings.BASE_DIR
    / "templates"
    / "layout"
    / "partials"
    / "menu"
    / "horizontal"
    / "json"
    / "horizontal_menu.json"
)


class TemplateBootstrapLayoutHorizontal:
    @staticmethod
    def init(context: dict) -> dict:
        context.update(
            {
                "layout": "horizontal",
                "is_navbar": True,
                "navbar_full": True,
                "is_menu": True,
                "menu_horizontal": True,
                "is_footer": True,
                "navbar_detached": False,
            }
        )
        # map_context according to updated context values
        TemplateHelper.map_context(context)

        # Init menu data and update context
        TemplateBootstrapLayoutHorizontal.init_menu_data(context)

        return context

    @staticmethod
    def init_menu_data(context: dict):
        # Load the menu data from the JSON file
        menu_data = json.load(menu_file_path.open()) if menu_file_path.exists() else []

        # Updated context with menu_data
        context.update({"menu_data": menu_data})
