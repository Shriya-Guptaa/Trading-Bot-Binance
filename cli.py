import typer
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_symbol
)
from bot.logging_config import setup_logger

app = typer.Typer()
logger = setup_logger()


@app.command()
def trade(
    symbol: str = typer.Option(...),
    side: str = typer.Option(...),
    order_type: str = typer.Option(..., "--type"),
    quantity: float = typer.Option(...),
    price: float = typer.Option(None)
):
    try:
        # Validation
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        print("\nOrder Request:")
        print(f"Symbol: {symbol}, Side: {side}, Type: {order_type}, Qty: {quantity}, Price: {price}")

        logger.info(f"Request: {symbol}, {side}, {order_type}, {quantity}, {price}")

        # Order execution
        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)
        else:
            response = place_limit_order(symbol, side, quantity, price)

        # Response handling
        if "error" in response:
            print("Order Failed:", response["error"])
            logger.error(response["error"])
        else:

            print("\nOrder Success")
            print("Order ID:", response.get("orderId"))
            print("Status:", response.get("status"))
            print("Executed Qty:", response.get("executedQty"))

            # CHANGED: fallback to price if avgPrice not present
            print("Avg Price:", response.get("avgPrice") or response.get("price"))

            logger.info(f"Response: {response}")

    except Exception as e:
        print("Error:", str(e))
        logger.error(str(e))


if __name__ == "__main__":
    app()