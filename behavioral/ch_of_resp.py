"""
chain of reponsibility
- a behavioral design pattern that lets you pass 
requests along a chain of handlers.
Upon receiving a request, each handler 
decides either to process the request 
or to pass it to the next handler in the chain.

"""

from abc import ABC , abstractmethod

class AbstractHandler(ABC):
    @abstractmethod
    def set_next(self,handler):
        pass
    @abstractmethod
    def handle(self,handler):
        pass

class BaseHandler(AbstractHandler):
    _next_handler = None

    def set_next(self,handler):
        self._self_next = handler
        return handler
    
    @abstractmethod
    def handle(self,reqeust):
        if self._next_handler:
            return self._next_handler.handle(reqeust)
        return None
    
class HnadlerOne(BaseHandler):
    def handle(self, reqeust):
        if 0 <= reqeust <= 10 : 
            print(f'handlerone is processing this request{reqeust}')
        else:
            return super().handle(reqeust)
        
class HandleTwo(BaseHandler):
    def handle(self, reqeust):
        if 10 < reqeust <= 30 : 
            print(f'handlertwo is processing this request{reqeust}')
        else:
            return super().handle(reqeust)
        


class HandleDefault(BaseHandler):
    def handle(self, reqeust):
        print(f'default handler is processing this request{reqeust}')



def client(handler,request):
    for num in request:
        handler.handle(num)



nums = [3,14,31,9]
h_one = HnadlerOne()
h_two = HandleTwo()
h_default = HandleDefault()

h_one.set_next(h_two).set_next(h_default)

client(h_one,nums)

        



