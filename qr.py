import pyqrcode
import png
from pyqrcode import QRCode
s="www.google.org"
url=pyqrcode.create(s)
url.svg("qrcode.svg",scale=8)
url.png("qrcode.png",scale=8)