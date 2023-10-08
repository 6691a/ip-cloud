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
    / "vertical"
    / "json"
    / "vertical_menu.json"
)


class TemplateBootstrapLayoutVertical:
    @staticmethod
    def init(context: dict) -> dict:
        context.update(
            {
                "layout": "vertical",
                "content_navbar": True,
                "is_navbar": True,
                "is_menu": True,
                "is_footer": True,
                "navbar_detached": True,
            }
        )

        # map_context according to updated context values
        TemplateHelper.map_context(context)

        TemplateBootstrapLayoutVertical.init_menu_data(context)

        return context

    @staticmethod
    def init_menu_data(context: dict):
        # Load the menu data from the JSON file
        menu_data = json.load(menu_file_path.open()) if menu_file_path.exists() else []

        # Updated context with menu_data
        context.update({"menu_data": menu_data})
