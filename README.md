# Binance Futures Testnet Trading Bot

## Overview
This is a Python CLI-based trading bot that places **MARKET** and **LIMIT** orders on Binance Futures Testnet (USDT-M).

The application is structured with separation of concerns:
- API client layer
- Order execution logic
- Input validation
- CLI interface
- Logging system
---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Shriya-Guptaa/Trading-Bot-Binance.git
cd Trading-Bot-Binance
````

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory. It should look like  [.env.example file](https://github.com/Shriya-Guptaa/Trading-Bot-Binance/blob/5ebd7cbfa308a5a5de0234696c6b88a51c2827aa/.env.example)

---

## How to Run

### MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000
```

---

## Output

The application prints:

* Order request summary
* Order response details:

  * Order ID
  * Status
  * Executed Quantity
  * Average Price
* Success or failure message

---

## Assumptions

* Binance Futures Testnet is used (no real money involved)
* Minimum notional value (≥ 100 USDT) must be satisfied
* LIMIT orders may remain in `NEW` state if price is not reached
* Testnet may not always fully simulate order execution (e.g., MARKET orders may show `NEW`)

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py                     # Binance client wrapper
│   ├── orders.py                     # order placement logic
│   ├── validators.py                 #  input validation
│   └── logging_config.py
│
├── cli.py                            # CLI entry point
├── bot.log                           # Log Files
├── .env
├── requirements.txt
└── README.md
```
---

## Logging

* Logs are stored in:
```
bot.log
```

* Includes:

  * Order requests
  * API responses
  * Errors

---

##  Notes

* This project uses `python-binance` for API interaction
* CLI is implemented using `Typer`
---

