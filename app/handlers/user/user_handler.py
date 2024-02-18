from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from app.requests.requests import UserHandler
from app.FSM.state import UserInfo
from app.keyboards.reply import ReplyUser
from app.keyboards.inline import group_women
from app.logic_amocrm.amo import save_custom_field
from app.middlewares.middleware import RegisterUser


import tracemalloc
tracemalloc.start()

router = Router()

router.message.middleware(RegisterUser())

@router.message(CommandStart())
async def cmd_start_user(message: Message):
    user = await UserHandler.chek_user(message.from_user.id, message.from_user.first_name)
    if not user:
        photo = FSInputFile("IMG_4863.PNG")
        await message.answer_photo(photo=photo, caption='Добро пожаловать ✨ тебя приветствует помощник Ники Павленко по клубу\n\nДля того чтобы попасть в закрытый чат для бесплатной недели тест-драйва клуба, оставь пожалуйста свои контактные данные, договорились?🤍', reply_markup=await ReplyUser.start_kb())
    else:
        await message.answer('Вы уже прошли регистрацию, посетите наш закрытый чат!', reply_markup=group_women)

@router.message(F.text.startswith('Договорились'), StateFilter(default_state))
async def user_consent(message: Message, state: FSMContext):
    await message.answer(text=' Огонь🔥 тогда начнем с простого, напиши свою Фамилию и Имя')
    await state.set_state(UserInfo.name)

@router.message(StateFilter(UserInfo.name))
async def cmd_save_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Супер, отправь мне пожалуйста свой номер телефона в формате +7…')
    await state.set_state(UserInfo.telephone)

@router.message(StateFilter(UserInfo.telephone))
async def cmd_save_telephone(message: Message, state: FSMContext):
    await state.update_data(telephone=message.text)
    photo = FSInputFile("IMG_4867.PNG")
    await message.answer_photo(photo=photo, caption='Отлично, а теперь напиши СВОЙ ник в соцсетях, как на примере из картинки @…')
    await state.set_state(UserInfo.inst)

@router.message(StateFilter(UserInfo.inst))
async def cmd_save_inst(message: Message, state: FSMContext):
    await state.update_data(inst=message.text)
    await message.answer(text='💬 И последний вопрос перед добавлением в чат, напиши чем ты занимаешься?\n\nФотограф, SMM-щик, блогер, а может ты работаешь в найме или мама в декрете, мне уже не терпится узнать чем занимается такая красотка 😍')
    await state.set_state(UserInfo.descriphion)

@router.message(StateFilter(UserInfo.descriphion))
async def cmd_save_inst(message: Message, state: FSMContext):
    await state.update_data(descriphion=message.text)
    result = await state.get_data()
    if await UserHandler.add_user(message.from_user.id, message.from_user.first_name, result):
        await message.answer(text='Благодарю! нажимай на кнопку и присоединяйся к закрытому чату женского-клуба',  reply_markup=group_women)
        await state.clear()
    else:
        await message.answer(text='Ошибка, обратитесь к администратору!')
        await state.clear()

# await save_custom_field(message.from_user.id, message.from_user.first_name, result) and