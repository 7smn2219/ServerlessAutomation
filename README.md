# ServerlessAutomation

This project demonstrates how to run Selenium for web scraping in a headless environment, suitable for servers and Docker containers.

## Features

- **Headless Browsing:** Uses Chrome in headless mode to perform web scraping without a graphical user interface.
- **Dockerized:** Includes a Dockerfile for easy containerization and deployment.
- **Extensible:** Provides a basic framework that can be extended for various web scraping tasks.

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/7smn2219/ServerlessAutomation.git
   cd ServerlessAutomation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Run the script directly:**
  ```bash
  python main.py
  ```

- **Build and run with Docker:**
  ```bash
  docker build -t serverless-automation .
  docker run serverless-automation
  ```

## Project Structure

```
.
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```
