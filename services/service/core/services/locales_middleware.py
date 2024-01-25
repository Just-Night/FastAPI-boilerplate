from babel import Locale, negotiate_locale
from core import Config
from fastapi import Request


async def set_locale_middleware(request: Request, call_next):
    accept_language = request.headers.get("accept-language", "uk")
    parsed_languages = [lang.partition(";")[0] for lang in accept_language.split(",")]

    chosen_locale = negotiate_locale(parsed_languages, Config.SUPPORTED_LANGUAGES, sep="-")
    if not chosen_locale:  # Fallback to a default locale if none is chosen
        chosen_locale = 'en'  # Replace 'en' with your default locale

    request.state.language = Locale.parse(chosen_locale, sep="-")
    response = await call_next(request)
    return response
