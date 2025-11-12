import requests
import time
import logging

from config import BOT_TOKEN, SSH_PASSWORD, DB_PASSWORD, CHAT_ID, TG_HEADER, CHAN_CHAT_ID, CHAN_TOKEN

def send_message(message:str) -> None:
    """Send message to telegram dispatcher.

    :param message: a string with the message.
    :return: None.
    """
    message = f"{TG_HEADER}\n{message}".replace(BOT_TOKEN, '<token>')\
        .replace(SSH_PASSWORD, '<pass>').replace(DB_PASSWORD, '<pass>')
    count = 0
    while True:
        count += 1
        if count >= 15:
            logging.error(f"<send_message> count >= 15")
            break
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
            logging.info(requests.get(url, timeout=60).json())
            break
        except requests.exceptions.ConnectionError as connecterr:
            logging.error(f"<send_message> {connecterr}")
            time.sleep(15)
        except Exception as ex:
            logging.error(f"<send_message> {ex}")
            time.sleep(15)
        

def send_message_to_channel(message:str) -> None:
    """Send message to telegram dispatcher channel.

    :param message: a string with the message.
    :return: None.
    """
    message = f"{TG_HEADER}\n{message}".replace(CHAN_TOKEN, '<token>')\
        .replace(SSH_PASSWORD, '<pass>').replace(DB_PASSWORD, '<pass>')
    count = 0
    while True:
        count += 1
        if count >= 15:
            logging.error(f"<send_message> count >= 15")
            break
        try:
            url = f"https://api.telegram.org/bot{CHAN_TOKEN}/sendMessage?chat_id={CHAN_CHAT_ID}&text={message}"
            logging.info(requests.get(url, timeout=60).json())
            break
        except requests.exceptions.ConnectionError as connecterr:
            logging.error(f"<send_message> {connecterr}")
            time.sleep(15)
        except Exception as ex:
            logging.error(f"<send_message> {ex}")
            time.sleep(15)