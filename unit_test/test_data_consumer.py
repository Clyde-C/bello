import unittest
from unittest.mock import MagicMock

from src.DataConsumer import DataConsumer
from src.dataclass import Transaction


class TestDataConsumer(unittest.TestCase):
    def test_process_transaction(self):
        consumer = DataConsumer(buffer=MagicMock(), process_interval=1)
        transaction = Transaction(id="1", product="apple", amount=5, timestamp=100.0)

        consumer.process_transaction(transaction)  # Assuming this method is added for testing

        # feel free to modify the number to others, then the test would be failed
        self.assertEqual(consumer.total_sales, 1)
        self.assertEqual(consumer.sales_per_product['apple'], 1)


if __name__ == '__main__':
    unittest.main()
