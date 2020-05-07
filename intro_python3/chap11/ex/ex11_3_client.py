import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
result = proxy.nowtime()
print(result)