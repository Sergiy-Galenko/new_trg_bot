from telethon import TelegramClient, sync

# Введіть свої api_id і api_hash отримані на my.telegram.org
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# Ініціалізуйте клієнт для роботи з Telegram
client = TelegramClient('anon', api_id, api_hash)

# Список каналів для парсингу
channels = [
    'radarr_top_ua',
    'kpszsu',
    'Tsaplienko',
    'vert_i_call',
    'osirskiy',
    'V_Zelenskiy_official',
    'suspilnesumy',
    'DeepStateUA',
    'kiev_novosti1',
    'thisis_kyiv'
]

def parse_channel(channel_name, limit=100):
    """
    Парсинг певного каналу.

    :param channel_name: назва каналу (або його посилання після 'https://t.me/')
    :param limit: кількість останніх повідомлень для парсингу
    """
    print(f"Парсинг каналу {channel_name}")
    for message in client.iter_messages(channel_name, limit=limit):
        print(message.text)

def main():
    # Починаємо сеанс
    with client:
        client.start()
        for channel in channels:
            parse_channel(channel)

if __name__ == "__main__":
    main()
