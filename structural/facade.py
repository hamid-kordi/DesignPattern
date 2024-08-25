"""

Facade
    - a structural design pattern that provides 
    a simplified interface to a library,
    a framework, or any other complex set of classes.

"""

class CPU:
    def execute(self):
        print("execute cpu config...")

    
class SSD:
    def write(self):
        print("save to ssd...")


class Memory:
    def calculate(self):
        print("calculate in memory...")



class Computer(): #Facade
    def __init__(self) -> None:
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SSD()

    def start(self):
        self.cpu.execute()
        self.memory.calculate()
        self.ssd.write()



class client_facade():
    computer_facade = Computer()
    computer_facade.start()


client_facade()