from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


class ReplyUser:
    
    async def start_kb():
        builder = ReplyKeyboardBuilder([
            [
                KeyboardButton(text='Договорились 🫶🏻'),    
            ],
        ])
        builder.adjust(1)

        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    
class AdminReply:

    async def admin_panel():
        builder = ReplyKeyboardBuilder([
            [
                KeyboardButton(text='😎 Пользователи'),
                KeyboardButton(text='📝 Сделать рассылку')
            ]
        ])

        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    
    async def result_distribution():
        builder = ReplyKeyboardBuilder([
            [
                KeyboardButton(text='✅ Отправить'),
                KeyboardButton(text='❌ Отмена')
            ]
        ])

        return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)