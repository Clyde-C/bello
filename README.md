# Real-Time Data Pipeline Simulation

This project simulates a real-time data pipeline in Python, illustrating the generation, buffering, and consumption of sales transactions. It's designed to demonstrate the interaction between different components in a data processing architecture, including a Data Producer, Data Buffer, and Data Consumer.

## Overview

The simulation consists of three main components:

- **Data Producer**: Generates random sales transactions at a set interval, including a unique ID, product type, and amount.
- **Data Buffer**: Acts as a FIFO queue, temporarily storing incoming transactions from the Data Producer.
- **Data Consumer**: Processes transactions from the Data Buffer, calculating real-time metrics such as total sales and sales per product.

The system also features configurable parameters for the Data Buffer size and the processing intervals, making it a flexible tool for understanding basic concepts in data streaming and processing.

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Running the Simulation

To run the simulation, execute the main script from the command line:
`python main.py`

