import time
from collections import deque, defaultdict


class DataConsumer:
    def __init__(self, buffer, process_interval):
        self.buffer = buffer
        self.process_interval = process_interval
        self.total_sales = 0
        self.sales_per_product = {}  # key: product type, value: amount
        self.transaction_count = 0

        # this is for processing time-based metrics
        self.transactions = deque()

        print(f"init consumer successfully, the process_interval is {self.process_interval}")

    def start_consuming(self):
        print("consumer starts consuming")
        while True:
            transaction = self.buffer.get()
            if not transaction:
                continue
            self.process_transaction(transaction)

            # the following are for processing time-based metrics
            self.transactions.append(transaction)
            self.clean_old_transactions()  # drop the outdated transactions
            self.calculate_metrics()  # calculate the metrics

            time.sleep(self.process_interval)

    def process_transaction(self, transaction):
        self.transaction_count += 1
        self.sales_per_product[transaction.product] = self.sales_per_product.get(transaction.product, 0) + 1
        self.total_sales += 1
        print(f"{transaction} is processed, transaction_count: {self.transaction_count}",
              f"total_sales: {self.total_sales}",
              f"sales_per_product: {self.sales_per_product}"
              )

    def clean_old_transactions(self):
        current_time = time.time()
        while self.transactions and self.transactions[0].timestamp < current_time - 1800:  # Older than 30 minutes
            self.transactions.popleft()

    def calculate_metrics(self):
        current_time = time.time()
        intervals = [300, 600, 900]  # 5, 10, 15 minutes in seconds
        metrics = {
            interval: {
                'total_sales': 0,
                'transaction_count': 0,
                'sales_per_product': defaultdict(int)
            } for interval in intervals
        }

        for transaction in self.transactions:
            for interval in intervals:
                if transaction.timestamp >= current_time - interval:
                    metrics[interval]['total_sales'] += transaction.amount
                    metrics[interval]['transaction_count'] += 1
                    metrics[interval]['sales_per_product'][transaction.product] += transaction.amount

        for interval, metric in metrics.items():
            print(f"In the last {interval // 60} minutes:")
            print(f"  Transactions: {metric['transaction_count']}")
            print(f"  Total Sales: {metric['total_sales']}")
            for product, sales in metric['sales_per_product'].items():
                print(f"  {product.capitalize()}: {sales} sales")
