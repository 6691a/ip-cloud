from babel import Locale
from django.utils import translation
from phonenumber_field.widgets import REGION_CODE_TO_COUNTRY_CODE


def phone_country_code_choices(language):
    choices = []
    locale_name = translation.to_locale(language)
    locale = Locale(locale_name)

    for region_code, country_code in REGION_CODE_TO_COUNTRY_CODE.items():
        region_name = locale.territories.get(region_code)
        if region_name:
            choices.append((f"{region_code}", f"+{country_code} {region_name}"))
    return choices
