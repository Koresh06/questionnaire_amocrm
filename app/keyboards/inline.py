from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.requests.requests import AdminRequest


group_women = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👱🏻‍♀️ Женский клуб', url='https://t.me/+U0skcyzwzG8wYWEy')]
    ]
)

class AdminInline():

    async def users():
        builder = InlineKeyboardBuilder()

        id_users = await AdminRequest.get_users()
        for item in id_users:
            builder.add(InlineKeyboardButton(text=item.username_tg, url=f'tg://user?id={item.tg_id}'))
        builder.adjust(1)

        return builder.as_markup()