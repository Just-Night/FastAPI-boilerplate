from fastapi import HTTPException, status


def has_permission(perm):
    """
    Return `raise` if permission is granted not found.
    """
    if not perm:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        )


def IsStaffUser(user):
    """
    Allows access only to staff users.
    """

    return has_permission(bool(user.is_staff or user.is_superuser))


def IsSyperUser(user):
    """
    Allows access only to syper users.
    """

    return has_permission(bool(user.is_superuser))
