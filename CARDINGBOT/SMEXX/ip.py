# IP CHEKER PY

from telethon import events
import telethon.utils
from telethon.tl import functions

from CARDINGBOT.CONDOM import http
from CARDINGBOT import SUDO_USERS, smx

@smx.on(events.NewMessage(pattern="^/ip"))
async def ip_fruad(event):
    IP = event.message.message[len('/ip '):]
    try:
      res = await http.get(f'https://fraudchkip.herokuapp.com/{IP}')
      result = res.json()
      msg = f'''
      IP: {IP}
      FRAUD SCORE: {result['score']}
      RISK LEVEL: {result['risk']}
      ASN: {result['asn']}
      HOST: {result['host']}
      Connection Type: {result['ctype']}
      Web Proxy: {result['wproxy']}
      Robot: {result['robot']}
      ISP: {result['isp']}
      Orgnization: {result['org']}
      City: {result['city']}
      Region: {result['region']}
      Zip: {result['zip']}
      Country: {result['country']}
      VPN: {result['vpn']}
      Tor: {result['tor']}
      '''
      await event.edit(msg)
    except Exception as e:
      err = f'Error: {e}'
      await event.edit(err)
