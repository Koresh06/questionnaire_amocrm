from aiogram.fsm.state import State, StatesGroup


class UserInfo(StatesGroup):

    name = State()
    telephone = State()
    inst = State()
    descriphion = State()

class NewLetter(StatesGroup):

    text = State()
    result = State()

class CirlcleVideo(StatesGroup):

    video = State()