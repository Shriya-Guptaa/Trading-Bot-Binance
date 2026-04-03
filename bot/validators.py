def validate_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_order_type(order_type):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
        return quantity
    except:
        raise ValueError("Quantity must be a positive number")


def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        try:
            price = float(price)
            if price <= 0:
                raise ValueError
            return price
        except:
            raise ValueError("Price must be a positive number")
    return price


def validate_symbol(symbol):
    if not symbol or not symbol.endswith("USDT"):
        raise ValueError("Symbol must be like BTCUSDT")
    return symbol.upper()