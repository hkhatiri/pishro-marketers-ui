import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_CONFIG = {
    'host': os.environ.get("MONGO_HOST", "127.0.0.1"),
    'port': int(os.environ.get("MONGO_PROT", 27017)),
}

SETTINGS = {
    'market_development': {
        'bot_name': 'market_development',
        'BOT_TOKEN': os.environ.get("MD_BOT_TOKEN", "6993959087:AAEqBVz4_VnRDtBTwgDqH11F76UHVfkNMSg"),
        'CHANNEL_ID': int(os.environ.get("MD_CHANNEL_ID", -1002225661089)),
        'LOG_CHANNEL_ID': int(os.environ.get("MD_LOG_CHANNEL_ID", -1002225661089)),
        'INVITE_LINK': os.environ.get("MD_INVITE_LINK", "https://t.me/+thgWUCS7gyE5NTBk"),

        'PISHRO_GATEWAY_CONFIG': {
            'username': os.environ.get("MD_PISHRO_GATEWAY_USERNAME"),
            'password': os.environ.get("MD_PISHRO_GATEWAY_PASSWORD"),
        },

        'MONGO_DB': os.environ.get("MD_MONGO_DB", "pishrobot"),
    },
    'marketers': {
        'bot_name': 'marketers',
        'BOT_TOKEN': os.environ.get("MR_BOT_TOKEN", "6993959087:AAEqBVz4_VnRDtBTwgDqH11F76UHVfkNMSg"),
        'LOG_CHANNEL_ID': int(os.environ.get("MR_LOG_CHANNEL_ID", -1002225661089)),

        'PISHRO_GATEWAY_CONFIG': {
            'username': os.environ.get("MR_PISHRO_GATEWAY_USERNAME"),
            'password': os.environ.get("MR_PISHRO_GATEWAY_PASSWORD"),
        },

        'MONGO_DB': os.environ.get("MR_MONGO_DB", "marketersbot"),
    }
}
