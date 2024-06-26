from fastapi import APIRouter
from db import *
from pydetic_model import *

router = APIRouter()


@router.get('/produts/')
async def get_products():
    query = products.select()
    return await db.fetch_all(query)


@router.get('/produts/{product_id}', response_model=Product)
async def get_product(product_id):
    query = products.select().where(products.c.product_id == product_id)
    return await db.fetch_one(query)


@router.post('/produts/')
async def create_product(new_product: ProductIn):
    query = products.insert().values(**new_product.dict())
    await db.execute(query)
    return {'msg': f'{new_product.product_name} добавлен в ассартимент'}


@router.put('/produts/{product_id}')
async def update_product(product_id: int, new_data_product: ProductIn ):
    query = products.update().where(products.c.product_id == product_id).values(**new_data_product.dict())
    await db.execute(query)
    return {'msg': f'товар успешно изменен'}


@router.delete('/produts/{product_id}')
async def delete_product(product_id: int):
    query = products.delete().where(products.c.product_id == product_id)
    await db.execute(query)


@router.get('/users/')
async def get_users():
    query = users.select()
    return await db.fetch_all(query)


@router.get('/users/{user_id}', response_model=User)
async def get_user(user_id):
    query = users.select().where(users.c.product_id == user_id)
    return await db.fetch_one(query)


@router.post('/users/')
async def create_user(new_user: UserInPassword):
    query = users.insert().values(**new_user.dict())
    await db.execute(query)
    return {'msg': f'{new_user.username} добавлен'}


@router.put('/users/{user_id}')
async def update_user(user_id: int, new_data_user: UserIn ):
    query = users.update().where(users.c.user_id == user_id).values(**new_data_user.dict())
    await db.execute(query)
    return {'msg': f'данные успешно изменены'}


@router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.user_id == user_id)
    await db.execute(query)


@router.get('/orders/')
async def get_orders():
    query = orders.select()
    return await db.fetch_all(query)


@router.get('/orders/{order_id}', response_model=Order)
async def get_order(order_id):
    query = orders.select().where(orders.c.order_id == order_id)
    return await db.fetch_one(query)


@router.post('/orders/')
async def create_order(new_order: OrderIn):
    query = orders.insert().values(**new_order.dict())
    await db.execute(query)
    return {'msg': 'заказ оформлен'}


@router.put('/orders/{order_id}')
async def update_order(order_id: int, new_data_order: UserIn ):
    query = orders.update().where(orders.c.order_id == order_id).values(**new_data_order.dict())
    await db.execute(query)
    return {'msg': f'данные успешно изменены'}


@router.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.order_id == order_id)
    await db.execute(query)
