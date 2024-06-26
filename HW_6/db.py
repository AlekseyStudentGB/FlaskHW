import sqlalchemy
from datetime import datetime
from sqlalchemy import create_engine
import databases
from settings import settings

DATABASE_URL = settings.DATABASE_URL
db = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

products = sqlalchemy.Table('products', metadata,
                            sqlalchemy.Column('product_id', sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column('product_name', sqlalchemy.String(40), nullable=False, unique=True),
                            sqlalchemy.Column('description', sqlalchemy.String),
                            sqlalchemy.Column('price', sqlalchemy.Float, )
                            )

orders = sqlalchemy.Table('orders', metadata,
                         sqlalchemy.Column('order_id', sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('product_id', sqlalchemy.Integer,
                                           sqlalchemy.ForeignKey('products.product_id'), nullable=False),
                         sqlalchemy.Column('user_id', sqlalchemy.Integer,
                                           sqlalchemy.ForeignKey('users.user_id'), nullable=False)
                         )
users = sqlalchemy.Table('users', metadata,
                         sqlalchemy.Column('user_id', sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('username', sqlalchemy.String(20), nullable=False, unique=True),
                         sqlalchemy.Column('surname', sqlalchemy.String(20), nullable=False, unique=True),
                         sqlalchemy.Column('email', sqlalchemy.String(80), nullable=False, unique=True),
                         sqlalchemy.Column('password', sqlalchemy.String(), nullable=False)
                         )


engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)