from datetime import datetime
from babel.support import Translations

from passlib.context import CryptContext
from core.config import Config


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def gettext(message: str) -> str:
    return message


def unixify_timestamp(date: datetime) -> int:
    return int(datetime.timestamp(date))


def hash(password: str) -> str:
    return pwd_context.hash(password)


def verify(plain_password: str, hashed_password: str) -> str:
    return pwd_context.verify(plain_password, hashed_password)


class TranslationClass:
    def __init__(self, language='en'):
        self.language = language
        self.translations = self.load_translations()

    def load_translations(self):
        translations = Translations.load(Config.LOCALES_PATH, locales=[self.language])
        return translations

    def gettext(self, message):
        return self.translations.gettext(message)
