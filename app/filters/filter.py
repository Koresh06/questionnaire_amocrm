from aiogram.filters import BaseFilter
from aiogram.types import Message
import re


class CheckUrlIstargam(BaseFilter): 
    
    async def __call__(self, message: Message) -> bool:  

        instagram_link = message.text
        
        if re.match(r'https://www\.instagram\.com/', instagram_link):
            return True
        else:
            await message.answer("Неправильный формат ссылки. Введите корректную ссылку на Instagram:")
            return False