from datetime import datetime, timezone

from fastapi import Depends, HTTPException, Request, status
from jose import jwt, JWTError

from app.config import get_auth_data
from app.exceptions import NoJwtException, NoUserIdException, TokenExpiredException, TokenNoFoundException
from app.users.dao import UsersDAO


def get_token(request: Request):
    """Извлекает токен из куков"""
    token = request.cookies.get('users_access_token')
    if not token:
        raise TokenNoFoundException
    return token


async def get_current_user(token: str = Depends(get_token)):
    """
    Декодирует токен с помощью ключа и алгоритма шифрования.
    Проверяет срок действия токена, наличие уже существующего пользователя.
    Возвращает найденного пользователя.
    """
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(token, auth_data['secret_key'], algorithms=auth_data['algorithm'])
    except JWTError:
        raise NoJwtException

    expire: str = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
    if (not expire) or (expire_time < datetime.now(timezone.utc)):
        raise TokenExpiredException

    user_id: str = payload.get('sub')
    if not user_id:
        raise NoUserIdException

    user = await UsersDAO.find_one_or_none_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    return user
