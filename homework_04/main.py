"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

# Хотел задать вопрос. Что означает ошибка "Event loop is closed", которую игнорирует PyCharm? И почему данная ошибка не всплывала в уроках?

import asyncio
from models import engine, Base, Session, User, Post
from jsonplaceholder_requests import fetch_json_data, USERS_DATA_URL, POSTS_DATA_URL


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_all(session, users_data, posts_data):
    for el in users_data:
        json_id = el.get('id')  # Правильным решением было создавать отдельный атрибут? Без него я бы не смог привязать post к user.
        name = el.get('name')   # id я не смог использовать, так как он появляется только при добавлении в таблицу
        username = el.get('username')
        email = el.get('email')
        new_user = User(json_id=json_id, name=name, username=username, email=email)
        session.add(new_user)
        for el2 in posts_data:
            if new_user.json_id == el2.get('userId'):
                title = el2.get('title')
                body = el2.get('body')
                new_post = Post(body=body, title=title, user=new_user)
                session.add(new_post)
    await session.commit()


async def async_main():
    await create_tables()
    users_data, posts_data = await asyncio.gather(fetch_json_data(USERS_DATA_URL), fetch_json_data(POSTS_DATA_URL))
    async with Session() as session:
        await add_all(session, users_data, posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
