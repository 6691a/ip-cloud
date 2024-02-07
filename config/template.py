from django.conf import settings

THEME_LAYOUT_DIR = "layout"

TEMPLATE_CONFIG = {  #
    # Options[String]: vertical(default), horizontal
    "layout": "vertical",
    # Options[String]: theme-default(default), theme-bordered, theme-semi-dark
    "theme": "theme-default",
    # Options[String]: light(default), dark, system mode
    "style": "light",
    # options[Boolean]: True(default), Falzzse
    # To provide RTLSupport or not
    "rtl_support": True,
    # options[Boolean]: False(default), True
    # To set layout to RTL layout  (myRTLSupport must be True for rtl mode)
    "rtl_mode": False,
    # options[Boolean]: True(default), False
    # Display customizer or not THIS WILL REMOVE INCLUDED JS FILE. SO LOCAL STORAGE WON'T WORK
    "has_customizer": True,
    # options[Boolean]: True(default), False
    # Display customizer UI or not, THIS WON'T REMOVE INCLUDED JS FILE. SO LOCAL STORAGE WILL WORK
    "display_customizer": True,
    # options[String]: 'compact', 'wide' (compact=container-xxl, wide=container-fluid)
    "content_layout": "compact",
    # options[String]: 'fixed', 'static', 'hidden' (Only for vertical Layout)
    "navbar_type": "fixed",
    # options[String]: 'static', 'fixed' (for horizontal layout only)
    "header_type": "fixed",
    # options[Boolean]: True(default), False # Layout(menu) Fixed (Only for vertical Layout)
    "menu_fixed": True,
    # options[Boolean]: False(default), True # Show menu collapsed, Only for vertical Layout
    "menu_collapsed": False,
    # options[Boolean]: False(default), True # Footer Fixed
    "footer_fixed": False,
    # True, False (for horizontal layout only)
    "show_dropdown_onhover": True,
}

if settings.DEBUG:
    TEMPLATE_CONFIG["customizer_controls"] = [
        "rtl",
        "style",
        "headerType",
        "contentLayout",
        "layoutCollapsed",
        "showDropdownOnHover",
        "layoutNavbarOptions",
        "themes",
    ]  # To show/hide customizer options


THEME_VARIABLES = {
    "creator_name": "PixInvent",
    "creator_url": "https://pixinvent.com/",
    "template_name": "PlayHub",
    "template_suffix": "Django Admin Template",
    "template_version": "1.0.0",
    "template_free": False,
    "template_description": "Vuexy is a modern, clean and fully responsive admin template built with Bootstrap 5, Django, HTML, CSS, jQuery, and JavaScript. It has a huge collection of reusable UI components and integrated with the latest jQuery plugins. It can be used for all types of web applications like custom admin panel, project management system, admin dashboard, Backend application or CRM.",  # noqa
    "template_keyword": "django, django admin, dashboard, bootstrap 5 dashboard, bootstrap 5 design, bootstrap 5",  # noqa
    "facebook_url": "https://www.facebook.com/pixinvents/",  # noqa
    "twitter_url": "https://twitter.com/pixinvents",
    "github_url": "https://github.com/pixinvent",
    "dribbble_url": "https://dribbble.com/pixinvent",
    "instagram_url": "https://www.instagram.com/pixinvents/",
    "license_url": "https://themeforest.net/licenses/standard",
    "live_preview": "https://pixinvent.com/vuexy-bootstrap-django-admin-template/",
    "product_page": "https://1.envato.market/vuexy_admin",
    "support": "https://pixinvent.ticksy.com/",
    "more_themes": "https://1.envato.market/pixinvent_portfolio",
    "documentation": "https://demos.pixinvent.com/vuexy-html-admin-template/documentation/django-introduction.html",  # noqa
    "changelog": "https://demos.pixinvent.com/vuexy/changelog.html",  # noqa
    "git_repository": "vuexy-html-django-admin-template",
    "git_repo_access": "https://tools.pixinvent.com/github/github-access",
}
