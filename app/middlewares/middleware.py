from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

import config
from app.requests.requests import UserHandler
from app.keyboards.inline import group_women

# Это будет inner-мидлварь на сообщения
class Is_Admin(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if event.from_user.id in config.ADMIN_ID:
            return await handler(event, data)
        await event.answer('Данная команда доступна только для администатора')
        return
    
class RegisterUser(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if not await UserHandler.chek_user(event.from_user.id, event.from_user.first_name):
            return await handler(event, data)
        await event.answer('Вы уже прошли регистрацию, посетите наш закрытый чат!', reply_markup=group_women)