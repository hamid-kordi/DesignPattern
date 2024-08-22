
import xmltodict

class Apliction:
    def send_request(self):
        return 'adapter.xml'
    
class Analytic:
    def receiv_request(self,json):
        return json
    

class Adapter:
    def convert_xml_json(self,file):
        with open(file,'r') as myfile:
            obj = xmltodict.parse(myfile.read())
            return obj 
        

def client_adapter():
    sender = Apliction().send_request()
    convert_data = Adapter().convert_xml_json(sender)
    receiver =  Analytic().receiv_request(convert_data)
    print(receiver)


client_adapter()

    
