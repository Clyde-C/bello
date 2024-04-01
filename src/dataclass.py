from typing import NamedTuple


class Transaction(NamedTuple):
    id: str
    product: str
    amount: int
    timestamp: float  # Epoch time
