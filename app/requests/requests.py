from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select


class AdminRequest:

    async def get_users():
        async with async_session() as session:
            users = await session.scalars(select(User))
            return users
        
class UserHandler:

    async def chek_user(tg_id, username):
        async with async_session() as session:
            user_query = await session.scalar(select(User).where(User.tg_id == tg_id, User.username_tg == username))
            if not user_query:
                return False
        
            return True
        
    async def add_user(tg_id, username, data):
        async with async_session() as session:
            try:
                session.add(User(tg_id=tg_id, username_tg=username, name=data['name'], phone=data['telephone'], inst=data['inst'], descriphion=data['descriphion']))
                await session.commit()
                return True
            except Exception as exxit:
                print(exxit)
                return False