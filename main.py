from threading import Thread

from src.DataProducer import DataProducer
from src.DataBuffer import DataBuffer
from src.DataConsumer import DataConsumer


def main():
    buffer = DataBuffer(max_size=50)
    consumer = DataConsumer(buffer, process_interval=1)  # process each txn every 2 seconds

    consumer_thread = Thread(target=consumer.start_consuming)
    consumer_thread.start()

    producer = DataProducer(buffer.add)
    producer.start_producing()


if __name__ == "__main__":
    main()
