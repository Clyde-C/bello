"""
Testing DataProducer directly might be more challenging because it involves randomness and asynchronous behavior.
One approach is to test the DataProducer's ability to generate a transaction with expected properties
(e.g., product in the specified list, amount within the correct range).
We might need to refactor DataProducer to support such a test,
perhaps by isolating the transaction generation logic into a method that can be called synchronously.
"""
