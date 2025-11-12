import psycopg2
import logging

from sshtunnel import SSHTunnelForwarder
from pathlib import Path
from xml_api import record_xml
from info_bot import send_message, send_message_to_channel
from xlsx_api import record_xlsx, parse_xlsx
from collect_cards import get_rims_cards_from_feed, get_tyres_cards_from_feed
from config import SSH_HOST, SSH_USERNAME, SSH_PASSWORD, LOCAL_HOST, LOCAL_PORT, REMOTE_PORT,\
DB_NAME, DB_USER, DB_PASSWORD, XLSX_PATH, INPUT_FILE, LOG_PATH, URL_DICT, SILENT

def main() -> None:
    """Collects data from the database and creates xml files for avito.

    :return: None.
    """
    Path(LOG_PATH).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, filename=LOG_PATH + 'log.txt', filemode='a',\
                        format="%(asctime)s %(levelname)s %(message)s")
    
    if not SILENT:
        send_message_to_channel(f'Старт')

    result = 0
    try:
        # with SSHTunnelForwarder(
        #     ssh_address_or_host = SSH_HOST,  
        #     ssh_username = SSH_USERNAME,
        #     ssh_password = SSH_PASSWORD,
        #     local_bind_address  = (LOCAL_HOST, LOCAL_PORT),
        #     remote_bind_address = (LOCAL_HOST, REMOTE_PORT)
        # ) as server:
        #     logging.info('\n\n<main> Start')
        #     server.start()

        #     params = {
        #         'database': DB_NAME,
        #         'user': DB_USER,
        #         'password': DB_PASSWORD,
        #         'host': LOCAL_HOST,
        #         'port': LOCAL_PORT
        #         }

        #     conn = psycopg2.connect(**params)

        #     cards_dict = get_cards_from_db(conn=conn, url_dict=URL_DICT,\
        #                                 input_file_path=XLSX_PATH, input_filename=INPUT_FILE)
        rims = get_rims_cards_from_feed(url=URL_DICT["rims_url"], url_moscow=URL_DICT["rims_moscow_url"],\
                            headers=URL_DICT["headers"], root_url=URL_DICT["root_url"], url_portfolio=URL_DICT["url_portfolio"])
        # tyres = get_tyres_cards_from_feed(url=URL_DICT["tyres_url"], avito_url=URL_DICT["url_avito_tyres_brands"],\
        #                     headers=URL_DICT["headers"], root_url=URL_DICT["root_url"])
        cards_dict = {**rims}
        if cards_dict:
            record = record_xlsx(input_file_path=XLSX_PATH, db_cards=cards_dict,\
                                input_filename=INPUT_FILE, url_dict=URL_DICT)
            if record == 1:
                cards_to_xml = parse_xlsx(input_file_path=XLSX_PATH, input_filename=INPUT_FILE)
                if cards_to_xml != 0:
                    result = record_xml(cards=cards_to_xml)
                    if result == 1:
                        send_message('Success')
                        if not SILENT:
                            send_message_to_channel(f'Конец, xml-файлы созданы успешно')
                        logging.info('<main> Success')
                    else:
                        send_message('Error, xml not created')
                        if not SILENT:
                            send_message_to_channel(f'Возникла ошибка, xml-файлы не созданы')
                        logging.error('<main> xml not created, result != 1')
                else:
                    send_message('Error in parse_xlsx, cards_to_xml is 0')
                    if not SILENT:
                        send_message_to_channel(f'Возникла ошибка, не удалось прочитать файл input.xlsx')
                    logging.error('<main> error in parse_xlsx, cards_to_xml is 0')
            else:
                send_message('Error in record_xlsx')
                if not SILENT:
                    send_message_to_channel(f'Возникла ошибка, не удалось записать файл input.xlsx, выгрузки для авито не созданы')
                logging.error('<main> error in record_xlsx')
        else:
            send_message('Error when getting data from db, cards_dict is 0')
            if not SILENT:
                send_message_to_channel(f'Возникла ошибка, не удалось получить данные из выгрузок XML')
            logging.error('<main> cards_dict is 0')

    except Exception as ex:
        logging.error(f"{ex}\n\n")
        print(f"{ex}\n\n")
        send_message(f"<<ERROR>>\n{ex}")
        if not SILENT:
            send_message_to_channel(f'Процесс прерван, возникла ошибка: {ex}')



    logging.info('========================================\n\n')
        


if __name__ == '__main__':
    main()

