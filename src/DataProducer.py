
import time
import random
import uuid

from src.dataclass import Transaction


class DataProducer:
    def __init__(self, callback):
        self.products = ['apple','banana','strawberry','grape','pineapple']
        self.callback = callback
        print("init producer successfully")

    def start_producing(self):
        while True:
            current_time = time.time()
            thirty_minutes_ago = current_time - 1800  # 30 minutes in seconds
            random_timestamp = random.uniform(thirty_minutes_ago, current_time)

            transaction = Transaction(
                id=str(uuid.uuid4()),
                product=random.choice(self.products),
                amount=random.randint(1, 10),
                timestamp=random_timestamp
            )
            self.callback(transaction)

            # for testing
            # time.sleep(1)
