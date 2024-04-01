import unittest

from src.DataBuffer import DataBuffer
from src.dataclass import Transaction


class TestDataBuffer(unittest.TestCase):
    def test_add_and_get_transaction(self):
        buffer = DataBuffer(max_size=2)
        transaction1 = Transaction(id="1", product="apple", amount=5, timestamp=100.0)
        transaction2 = Transaction(id="2", product="banana", amount=3, timestamp=101.0)

        buffer.add(transaction1)
        buffer.add(transaction2)

        # Test FIFO behavior
        self.assertEqual(buffer.get(), transaction1)
        self.assertEqual(buffer.get(), transaction2)
        # Test buffer is empty now
        self.assertIsNone(buffer.get())

    def test_buffer_over_capacity(self):
        buffer = DataBuffer(max_size=1)
        transaction1 = Transaction(id="1", product="apple", amount=5, timestamp=100.0)
        transaction2 = Transaction(id="2", product="banana", amount=3, timestamp=101.0)

        buffer.add(transaction1)
        buffer.add(transaction2)

        # Transaction1 should be dropped
        self.assertEqual(buffer.get(), transaction2)
        self.assertIsNone(buffer.get())


if __name__ == '__main__':
    unittest.main()
