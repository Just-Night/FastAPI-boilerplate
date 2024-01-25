from .auth_messages import (AuthSerializerMessage, PasswordValidator,
                            RegistrationSerializerMessage)
from .user_messages import UsernameValidation


class Messages(
    AuthSerializerMessage,
    RegistrationSerializerMessage,
    PasswordValidator,
    UsernameValidation
):
    ...


__all__ = [
    'Messages'
]
