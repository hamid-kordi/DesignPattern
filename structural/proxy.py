"""

Proxy
- a structural design pattern that lets you provide 
a substitute or placeholder for another object. 
A proxy controls access to the original object, 
allowing you to perform something either before or 
after the request gets through to the original object.

"""

import abc
import time
import datetime


class AbstractServer(abc.ABC):
    @abc.abstractmethod
    def recieve(self):
        pass


class Server(AbstractServer):
    def recieve(self):
        print("on working...")
        time.sleep(1)
        print("done")


class LogProxy(AbstractServer):
    def __init__(self,server):
        self._server = server

    def recieve(self):
        self.logging()
        #.... any methods
        self._server.recieve()

    def logging(self):
        with open('logproxy.log','a') as log:
            log.write(f'Request {datetime.datetime.now()} \n')


def client_server(server,proxy):
    s = server()
    p = proxy(s)
    p.recieve()


client_server(Server, LogProxy)