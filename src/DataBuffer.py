class DataBuffer:
    def __init__(self, max_size):
        self.buffer = []
        self.max_size = max_size
        print(f"init buffer successfully, the max_size is {self.max_size}")

    def add(self, transaction):
        if len(self.buffer) >= self.max_size:
            dropped_txn = self.buffer.pop(0)  # pop the left most txn
            # todo print the log
            print(f"the buffer is full, dropped {dropped_txn}")
        # lock on
        self.buffer.append(transaction)
        # lock off
        print(f"append {transaction} into the buffer")

    def get(self):
        if len(self.buffer) == 0:
            print(f"the buffer is empty")
            return
        # lock on
        txn = self.buffer.pop(0)
        # lock off
        return txn
