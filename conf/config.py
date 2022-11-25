
BOT_TOKEN = 'TOKEN'

NEWS_LINK = 'link'
SALES_LINK = 'link'
SPARE_PARTS_LINK = 'link'
EVENTS_LINK = 'link'
ADDRESS_LINK = 'link'
TECH_LINK = 'link'

WEBHOOK_HOST = 'IP-address of your sever'
WEBHOOK_PORT = 443  # 443, 80, 88 or 8443
WEBHOOK_LISTEN = 'IP-address of your sever'  # or 0.0.0.0

WEBHOOK_SSL_CERT = 'path/to/webhook_cert.pem'  # it's recommended to place it in the 'data' folder
WEBHOOK_SSL_PRIVATE = 'path/to/webhook_pkey.pem'  # it's recommended to place it in the 'data' folder

WEBHOOK_URL_BASE = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}'
WEBHOOK_URL_PATH = f'/webhook/{BOT_TOKEN}'
