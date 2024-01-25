from core.utils import TranslationClass


class PasswordValidator(TranslationClass):
    @property
    def UPPERCASE_LETTERS(self):
        return self.gettext('The password must contain at least one uppercase letter.')
