# api id, hash
API_ID = 1488
API_HASH = 'abcde1488'


DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'RELOGIN': [5, 10],  # delay after failed login
    'TASK':  [5, 10],  # delay after complete task
    'PAINT': [5, 7],  # delay after paint pixel
    'RECOVERY_CHARGE': [20, 50],  # additional sleep time before energy charging
    'UPGRADE': [5, 7],  # delay after upgrade booster
    'JOIN_IN_CHAT': [5, 10]  # delay after join in tg chat
}


BOOSTERS = {
    'reChargeSpeed': {  # <- booster name
        'UPGRADE': True,   # True - if need upgrade
        'MAX_LVL': 10,  # max upgrade lvl; max -  11 lvl
        'PRICES': [5, 100, 200, 300, 400, 500, 600, 700, 800, 900]  # do not change!!!
    },
}


# True - if need join chat in tasks
JOIN_CHAT = False


# minimum time before claim after previous claim; min = 60
MIN_MINING_TIME_CLAIM = [60, 70]


PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "http",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "http"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30

SOFT_INFO = f"""{"Not Pixel".center(40)}
Soft for https://t.me/notpixel
{"Functional:".center(40)}
Register accounts in web app; Claim mining farming; paint pixels;
complete tasks; upgrade booster "Recharging Speed"; wait recharge energy

The soft also collects statistics on accounts and uses proxies from {f"the {PROXY['PROXY_PATH']} file" if PROXY['USE_PROXY_FROM_FILE'] else "the accounts.json file"}
To buy this soft with the option to set your referral link write me: https://t.me/Axcent_ape
"""
