from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.util import toHexString, toBytes
from smartcard.Exceptions import *
import time

def card():
  while True:  
   try:
      cardtype = AnyCardType()
      cardrequest = CardRequest( timeout=86400,cardType=cardtype )
      cardservice = cardrequest.waitforcard()
      cardservice.connection.connect()
      getuid=[0xFF,0xCA,0x00,0x00,0x00]
      data, sw1, sw2 =cardservice.connection.transmit(getuid)
      idd= toHexString(data)+"%02X%02X" % (sw1, sw2)
      rfid=idd.replace(" ", "")
      print rfid
      time.sleep(1)
   except CardConnectionException:
       print 'exception occurs'
       card()
   except ListReadersException:
       print 'exit'
   except NoReadersException:
       print 'exit'
   except CardRequestTimeoutException:
       card()
   except NoCardException:
       print 'nce'
       card()
card()       
