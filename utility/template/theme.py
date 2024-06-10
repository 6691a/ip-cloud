import os
from importlib import import_module, util
from pprint import pprint
from typing import Any

from django.conf import settings
from django.template import Library
from django.utils.safestring import mark_safe

from config import template

register = Library()


@register.simple_tag
def get_theme_variables(scope: str) -> str:
    return mark_safe(TemplateHelper.get_theme_variables(scope))


@register.simple_tag
def get_theme_config(scope: str) -> str:
    return mark_safe(TemplateHelper.get_theme_config(scope))


# Core TemplateHelper class
class TemplateHelper:
    # Init the Template Context using TEMPLATE_CONFIG
    @staticmethod
    def init_context(context: dict) -> dict:
        context.update(
            {
                "layout": template.TEMPLATE_CONFIG.get("layout"),
                "theme": template.TEMPLATE_CONFIG.get("theme"),
                "style": template.TEMPLATE_CONFIG.get("style"),
                "rtl_support": template.TEMPLATE_CONFIG.get("rtl_support"),
                "rtl_mode": template.TEMPLATE_CONFIG.get("rtl_mode"),
                "has_customizer": template.TEMPLATE_CONFIG.get("has_customizer"),
                "display_customizer": template.TEMPLATE_CONFIG.get("display_customizer"),
                "content_layout": template.TEMPLATE_CONFIG.get("content_layout"),
                "navbar_type": template.TEMPLATE_CONFIG.get("navbar_type"),
                "header_type": template.TEMPLATE_CONFIG.get("header_type"),
                "menu_fixed": template.TEMPLATE_CONFIG.get("menu_fixed"),
                "menu_collapsed": template.TEMPLATE_CONFIG.get("menu_collapsed"),
                "footer_fixed": template.TEMPLATE_CONFIG.get("footer_fixed"),
                "show_dropdown_onhover": template.TEMPLATE_CONFIG.get("show_dropdown_onhover"),
                "customizer_controls": template.TEMPLATE_CONFIG.get("customizer_controls"),
            }
        )
        return context

    # ? Map context variables to template class/value/variables names
    @staticmethod
    def map_context(context) -> dict:
        # ! Header Type (horizontal support only)
        if context.get("layout") == "horizontal":
            if context.get("header_type") == "fixed":
                context["header_type_class"] = "layout-menu-fixed"
            elif context.get("header_type") == "static":
                context["header_type_class"] = ""
            else:
                context["header_type_class"] = ""
        else:
            context["header_type_class"] = ""

        # ! Navbar Type (vertical/front support only)
        if context.get("layout") != "horizontal":
            if context.get("navbar_type") == "fixed":
                context["navbar_type_class"] = "layout-navbar-fixed"
            elif context.get("navbar_type") == "static":
                context["navbar_type_class"] = ""
            else:
                context["navbar_type_class"] = "layout-navbar-hidden"
        else:
            context["navbar_type_class"] = ""

        # Menu collapsed
        context["menu_collapsed_class"] = (
            "layout-menu-collapsed" if context.get("menu_collapsed") else ""
        )

        # ! Menu Fixed (vertical support only)
        if context.get("layout") == "vertical":
            if context.get("menu_fixed") is True:
                context["menu_fixed_class"] = "layout-menu-fixed"
            else:
                context["menu_fixed_class"] = ""

        # Footer Fixed
        context["footer_fixed_class"] = "layout-footer-fixed" if context.get("footer_fixed") else ""

        # RTL Supported template
        context["rtl_support_value"] = "/rtl" if context.get("rtl_support") else ""

        # RTL Mode/Layout
        context["rtl_mode_value"], context["text_direction_value"] = (
            ("rtl", "rtl") if context.get("rtl_mode") else ("ltr", "ltr")
        )

        # ! Show dropdown on hover (Horizontal menu)
        context["show_dropdown_onhover_value"] = (
            "true" if context.get("show_dropdown_onhover") else "false"
        )

        # Display Customizer
        context["display_customizer_class"] = (
            "" if context.get("display_customizer") else "customizer-hide"
        )

        # Content Layout
        if context.get("content_layout") == "wide":
            context["container_class"] = "container-fluid"
            context["content_layout_class"] = "layout-wide"
        else:
            context["container_class"] = "container-xxl"
            context["content_layout_class"] = "layout-compact"

        # Detached Navbar
        if context.get("navbar_detached"):
            context["navbar_detached_class"] = "navbar-detached"
        else:
            context["navbar_detached_class"] = ""

        return context

    # Get theme variables by scope
    @staticmethod
    def get_theme_variables(scope: str) -> Any:
        return template.THEME_VARIABLES[scope]

    # Get theme config by scope
    @staticmethod
    def get_theme_config(scope: str) -> Any:
        return template.TEMPLATE_CONFIG[scope]

    # Set the current page layout and init the layout bootstrap file
    @staticmethod
    def set_layout(view, context=None):
        # Extract layout from the view path
        if context is None:
            context = {}

        layout = os.path.splitext(view)[0].split("/")[0]

        # Get module path
        module = f"templates.{template.THEME_LAYOUT_DIR.replace('/', '.')}.bootstrap.{layout}"

        # Check if the bootstrap file is exist
        if util.find_spec(module) is not None:
            # Auto import and init the default bootstrap.py file from the theme
            TemplateBootstrap = TemplateHelper.import_class(
                module, f"TemplateBootstrap{layout.title().replace('_', '')}"
            )
            TemplateBootstrap.init(context)
        else:
            module = f"templates.{template.THEME_LAYOUT_DIR.replace('/', '.')}.bootstrap.default"

            TemplateBootstrap = TemplateHelper.import_class(module, "TemplateBootstrapDefault")
            TemplateBootstrap.init(context)

        return f"{template.THEME_LAYOUT_DIR}/{view}"

    # Import a module by string
    @staticmethod
    def import_class(fromModule, import_className: str):
        if settings.DEBUG:
            pprint(f"Loading {import_className} from {fromModule}")
        module = import_module(fromModule)
        return getattr(module, import_className)
