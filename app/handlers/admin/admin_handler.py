from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.methods.send_video_note import SendVideoNote
from aiogram.types.input_media_video import InputMediaVideo

from app.middlewares.middleware import Is_Admin
from app.keyboards.reply import AdminReply
from app.keyboards.inline import AdminInline
from app.requests.requests import AdminRequest
from app.FSM.state import NewLetter, CirlcleVideo


admin = Router()

admin.message.middleware(Is_Admin())


@admin.message(Command('admin'), StateFilter(default_state))
async def cmd_admin(message: Message):
    await message.answer('Панель администартора', reply_markup=await AdminReply.admin_panel())


@admin.message(F.text.endswith('Пользователи'))
async def cmd_get_users(message: Message):
    await message.answer(text='Пользователи', reply_markup=await AdminInline.users())

@admin.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Отмена рассылки!', reply_markup=await AdminReply.admin_panel())
    await state.clear()

@admin.message(F.text.endswith('Сделать рассылку'), StateFilter(default_state))
async def cmd_distribution(message: Message, state: FSMContext):
    await state.set_state(NewLetter.text)
    await message.answer('Отправьте сообщение для рассылки!\n\n❌ Отмена - /cancel')

@admin.message(NewLetter.text)
async def cmd_message(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer(f'<b><u>Проверьте текст РАССЫЛКИ</u></b>\n\n\n{message.text}\n\n\n❌ Отмена - /cancel', reply_markup=await AdminReply.result_distribution())
    await state.set_state(NewLetter.result)

@admin.message(F.text.endswith('Отправить'), NewLetter.result)
async def cmd_send(message: Message, state: FSMContext):
    users = await AdminRequest.get_users()
    data = await state.get_data()
    for item in users:
        try:
            await message.bot.send_message(chat_id=item.tg_id, text=data['text'])
        except Exception as exxit:
            print(exxit)
    await message.answer('🔰 Рассылка завершена', reply_markup=await AdminReply.admin_panel())
    await state.clear()

@admin.message(F.text.endswith('Отмена'), NewLetter.result)
async def cmd_cancle_distribution(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Отмена рассылки!', reply_markup=await AdminReply.admin_panel())

@admin.message(Command('circle_video'), StateFilter(default_state))
async def cirlce_cmd(message: Message, state: FSMContext):
    await state.set_state(CirlcleVideo.video)
    await message.answer('Отправьте video для рассылки')

@admin.message(StateFilter(CirlcleVideo.video))
async def cirlce_cmd(message: Message, state: FSMContext):
    await state.update_data(video=message.video_note.file_id)
    users = await AdminRequest.get_users()
    data = await state.get_data()
    for item in users:
        try:
            await message.bot.send_video_note(chat_id=item.tg_id, video_note=data['video'])
        except Exception as exxit:
            print(exxit)
    await message.answer('🔰 Рассылка завершена', reply_markup=await AdminReply.admin_panel())
    await state.clear()
