import base64
import zlib

tstr = open("favicon.png","rb").read();
#tstr = zlib.compress(tstr);
tstr = base64.b64encode(tstr);
print(tstr);
