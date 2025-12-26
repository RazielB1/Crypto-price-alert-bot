import time
from bot.price_service import get_price
from bot.alert_manager import should_trigger
from bot.notifier import send_alert
from bot.config import PRICE_CHECK_INTERVAL
from bot.logger import logger

# Example alert (can be expanded later)
ALERT = {
    "coin": "bitcoin",
    "target_price": 70000,
    "condition": "above"
}

def run():
    logger.info("🚀 Crypto Price Alert Bot started")

    while True:
        try:
            price = get_price(ALERT["coin"])
            logger.info(
                f"{ALERT['coin'].upper()} price: ${price}"
            )

            if should_trigger(
                price,
                ALERT["target_price"],
                ALERT["condition"]
            ):
                message = (
                    "🚨 CRYPTO ALERT 🚨\n\n"
                    f"Coin: {ALERT['coin'].upper()}\n"
                    f"Condition: {ALERT['condition']} ${ALERT['target_price']}\n"
                    f"Current Price: ${price}"
                )

                send_alert(message)
                logger.info("Alert sent successfully")
                break

        except Exception as error:
            logger.error(f"Error occurred: {error}")

        time.sleep(PRICE_CHECK_INTERVAL)

if __name__ == "__main__":
    run()
