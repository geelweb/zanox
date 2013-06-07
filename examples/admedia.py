from zanox.client import Client
import config

c = Client(config.CONNECTID);
response = c.getAdmedia()
print response
