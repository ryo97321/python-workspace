from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer

def nowtime():
    return datetime.now().isoformat()

server = SimpleXMLRPCServer(('localhost', 6789))
server.register_function(nowtime, 'nowtime')
server.serve_forever()