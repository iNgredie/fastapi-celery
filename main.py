from fastapi import FastAPI

from celery_worker import create_order
from schemas import Order

app = FastAPI()


@app.post('/order')
def add_order(order: Order):
    # user delay() method to call the celery task
    create_order.delay(order.customer_name, order.order_quantity)
    return {'message': 'Order Received! Thank you for your patience'}
