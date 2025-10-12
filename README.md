# Design Patterns Repository

Welcome to the **Design Patterns** repository! This project serves as a comprehensive guide and practice resource for common design patterns in software engineering. Design patterns provide reusable solutions to common problems in software design, categorized into Creational, Structural, and Behavioral patterns.

This repository is intended for learning, practicing, and contributing. Whether you're a beginner looking to understand these patterns or an experienced developer wanting to refresh your knowledge, you'll find explanations, real-world analogies, and code examples here.

## Table of Contents

- [Creational Patterns](#creational-patterns)
  - [Singleton](#singleton)
  - [Factory Method](#factory-method)
  - [Abstract Factory](#abstract-factory)
  - [Builder](#builder)
  - [Prototype](#prototype)
- [Structural Patterns](#structural-patterns)
  - [Adapter](#adapter)
  - [Composite](#composite)
  - [Decorator](#decorator)
  - [Facade](#facade)
  - [Flyweight](#flyweight)
  - [Proxy](#proxy)
- [Behavioral Patterns](#behavioral-patterns)
  - [Observer](#observer)
  - [Strategy](#strategy)
  - [Command](#command)
  - [Chain of Responsibility](#chain-of-responsibility)
  - [Mediator](#mediator)
  - [State](#state)
  - [Visitor](#visitor)
  - [Template Method](#template-method)
  - [Interpreter](#interpreter)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contributing](#contributing)
- [License](#license)

## Creational Patterns

These patterns focus on object creation mechanisms, making your code more flexible and reusable by controlling how objects are instantiated.

### Singleton

**Purpose:** Ensures a class has only one instance and provides a global point of access to it. Useful for resources like database connections or configuration managers.

**Real-World Analogy:** A single government in a country – only one official instance exists.

**Python Example:**

```python
# Impliment
class Singleton(type):
    _instance = None

    def __call__(self,*args,**kwargs):
        if self._instance is None:
            self._instance = super().__call__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1.value) 
print(s1 is s2)  
```

### Factory Method

**Purpose:** Defines an interface for creating an object but lets subclasses alter the type of objects created. Promotes loose coupling.

**Real-World Analogy:** A hiring manager (factory) who decides what type of employee to hire based on the job role.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Result of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self):
        return "Result of ConcreteProductB"

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        return f"Creator: {product.operation()}"

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Usage
creator_a = ConcreteCreatorA()
print(creator_a.some_operation())  # Output: Creator: Result of ConcreteProductA
```

### Abstract Factory

**Purpose:** Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

**Real-World Analogy:** A furniture factory that produces matching sets of chairs, tables, and sofas in different styles (modern, Victorian).

**Python Example:**

```python
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A1."

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A2."

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self):
        pass

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B1."

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B2."

# Usage
factory = ConcreteFactory1()
product_a = factory.create_product_a()
product_b = factory.create_product_b()
print(product_a.useful_function_a())  # Output: The result of the product A1.
print(product_b.useful_function_b())  # Output: The result of the product B1.
```

### Builder

**Purpose:** Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

**Real-World Analogy:** Building a house – a director oversees the process, while builders handle the steps for different types (e.g., wooden vs. brick).

**Python Example:**

```python
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.build_part_a()
        self._builder.build_part_b()

class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self._product = Product()

    def build_part_a(self):
        self._product.add("Part A")

    def build_part_b(self):
        self._product.add("Part B")

    def get_result(self):
        return self._product

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Product parts: {', '.join(self.parts)}"

# Usage
builder = ConcreteBuilder()
director = Director(builder)
director.construct()
product = builder.get_result()
print(product.list_parts())  # Output: Product parts: Part A, Part B
```

### Prototype

**Purpose:** Creates new objects by copying an existing instance (prototype), avoiding the cost of creating objects from scratch.

**Real-World Analogy:** Cloning sheep like Dolly – create duplicates from a prototype.

**Python Example:**

```python
import copy

class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)

# Usage
original = Prototype("Original Value")
clone = original.clone()
clone.value = "Cloned Value"
print(original.value)  # Output: Original Value
print(clone.value)     # Output: Cloned Value
```

## Structural Patterns

These patterns explain how to assemble objects and classes into larger structures while keeping them flexible and efficient.

### Adapter

**Purpose:** Allows incompatible interfaces to work together by wrapping an object with a new interface.

**Real-World Analogy:** A power adapter that converts a US plug to a EU socket.

**Python Example:**

```python
class Target:
    def request(self):
        return "Target: The default target's behavior."

class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()[::-1]}"

# Usage
adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Output: Adapter: (TRANSLATED) Special behavior of the Adaptee.
```

### Composite

**Purpose:** Composes objects into tree structures to represent part-whole hierarchies, treating individual objects and compositions uniformly.

**Real-World Analogy:** A file system with files and folders – folders can contain files or other folders.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def operation(self):
        results = [child.operation() for child in self._children]
        return f"Branch({'+'.join(results)})"

# Usage
tree = Composite()
branch1 = Composite()
branch1.add(Leaf())
branch1.add(Leaf())
tree.add(branch1)
tree.add(Leaf())
print(tree.operation())  # Output: Branch(Branch(Leaf+Leaf)+Leaf)
```

### Decorator

**Purpose:** Adds new behaviors to objects dynamically by wrapping them in decorators.

**Real-World Analogy:** Adding toppings to a pizza – each topping decorates the base pizza.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(ABC):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def operation(self):
        pass

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

# Usage
simple = ConcreteComponent()
decorated = ConcreteDecoratorA(ConcreteDecoratorB(simple))
print(decorated.operation())  # Output: ConcreteDecoratorA(ConcreteDecoratorB(ConcreteComponent))
```

### Facade

**Purpose:** Provides a simplified interface to a complex subsystem, hiding its complexities.

**Real-World Analogy:** A hotel front desk that handles check-ins, room service, etc., without exposing internal operations.

**Python Example:**

```python
class Subsystem1:
    def operation1(self):
        return "Subsystem1: Ready!"

    def operation_n(self):
        return "Subsystem1: Go!"

class Subsystem2:
    def operation1(self):
        return "Subsystem2: Get ready!"

    def operation_z(self):
        return "Subsystem2: Fire!"

class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        results = []
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation1())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)

# Usage
facade = Facade()
print(facade.operation())
# Output:
# Subsystem1: Ready!
# Subsystem1: Go!
# Subsystem2: Get ready!
# Subsystem2: Fire!
```

### Flyweight

**Purpose:** Reduces memory usage by sharing as much data as possible with similar objects.

**Real-World Analogy:** Sharing common parts of game characters (e.g., textures) across instances.

**Python Example:**

```python
class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        return f"Flyweight: Displaying shared ({self._shared_state}) and unique ({unique_state}) state."

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]

# Usage
factory = FlyweightFactory()
fw1 = factory.get_flyweight("Shared1")
print(fw1.operation("Unique1"))  # Output: Flyweight: Displaying shared (Shared1) and unique (Unique1) state.
fw2 = factory.get_flyweight("Shared1")
print(fw2.operation("Unique2"))  # Same shared state
```

### Proxy

**Purpose:** Provides a surrogate or placeholder for another object to control access to it.

**Real-World Analogy:** A credit card as a proxy for cash in your bank account.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject: Handling request."

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self._check_access():
            result = self._real_subject.request()
            self._log_access()
            return result
        return "Proxy: Access denied."

    def _check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def _log_access(self):
        print("Proxy: Logging the time of request.")

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())
# Output:
# Proxy: Checking access prior to firing a real request.
# RealSubject: Handling request.
# Proxy: Logging the time of request.
```

## Behavioral Patterns

These patterns manage object collaboration and delegation of responsibilities.

### Observer

**Purpose:** Defines a one-to-many dependency between objects so that when one changes state, all dependents are notified.

**Real-World Analogy:** Subscribers to a YouTube channel get notified of new videos.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        self._state = "New State"
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class ConcreteObserverA(Observer):
    def update(self, subject):
        if subject._state == "New State":
            print("ConcreteObserverA: Reacted to the event.")

# Usage
subject = ConcreteSubject()
observer_a = ConcreteObserverA()
subject.attach(observer_a)
subject.some_business_logic()  # Output: ConcreteObserverA: Reacted to the event.
```

### Strategy

**Purpose:** Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

**Real-World Analogy:** Different payment methods (credit card, PayPal) in an e-commerce checkout.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def do_some_business_logic(self, data):
        result = self._strategy.do_algorithm(data)
        return result

# Usage
context = Context(ConcreteStrategyA())
print(context.do_some_business_logic([3, 1, 2]))  # Output: [1, 2, 3]
context = Context(ConcreteStrategyB())
print(context.do_some_business_logic([3, 1, 2]))  # Output: [3, 2, 1]
```

### Command

**Purpose:** Encapsulates a request as an object, allowing parameterization of clients with queues, requests, and operations.

**Real-World Analogy:** A remote control where each button is a command to the TV.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class SimpleCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        print(f"SimpleCommand: {self._payload}")

class ComplexCommand(Command):
    def __init__(self, receiver, a, b):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:
    def do_something(self, a):
        print(f"Receiver: Working on ({a}.)")

    def do_something_else(self, b):
        print(f"Receiver: Also working on ({b}.)")

class Invoker:
    def __init__(self):
        self._on_start = None
        self._on_finish = None

    def set_on_start(self, command):
        self._on_start = command

    def set_on_finish(self, command):
        self._on_finish = command

    def do_something_important(self):
        if self._on_start:
            self._on_start.execute()
        # Business logic...
        if self._on_finish:
            self._on_finish.execute()

# Usage
invoker = Invoker()
invoker.set_on_start(SimpleCommand("Say Hi!"))
receiver = Receiver()
invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))
invoker.do_something_important()
# Output:
# SimpleCommand: Say Hi!
# Receiver: Working on (Send email.)
# Receiver: Also working on (Save report.)
```

### Chain of Responsibility

**Purpose:** Passes a request along a chain of handlers, where each handler decides to process or pass it on.

**Real-World Analogy:** Customer support tiers – level 1 handles simple issues, escalates complex ones to level 2.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if request == "Banana":
            return f"Monkey: I'll eat the {request}."
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request):
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}."
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request):
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}."
        else:
            return super().handle(request)

# Usage
monkey = MonkeyHandler()
squirrel = SquirrelHandler()
dog = DogHandler()
monkey.set_next(squirrel).set_next(dog)

print(monkey.handle("Banana"))  # Output: Monkey: I'll eat the Banana.
print(monkey.handle("Nut"))     # Output: Squirrel: I'll eat the Nut.
print(monkey.handle("Coffee"))  # Output: None
```

### Mediator

**Purpose:** Reduces chaotic dependencies between objects by restricting direct communications through a mediator.

**Real-World Analogy:** Air traffic control mediating between planes.

**Python Example:**

```python
from abc import ABC

class Mediator(ABC):
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()

class BaseComponent:
    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")

class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")

    def do_d(self):
        print("Component 2 does D.")
        self.mediator.notify(self, "D")

# Usage
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)
c1.do_a()
# Output:
# Component 1 does A.
# Mediator reacts on A and triggers following operations:
# Component 2 does C.
```

### State

**Purpose:** Allows an object to alter its behavior when its internal state changes, as if changing its class.

**Real-World Analogy:** A vending machine that behaves differently based on states (e.g., has money, out of stock).

**Python Example:**

```python
from abc import ABC, abstractmethod

class Context:
    def __init__(self, state):
        self._state = state
        self._state.context = self

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self._state.context = self

    def request(self):
        self._state.handle()

class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA handles request.")
        self.context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB handles request.")
        self.context.state = ConcreteStateA()

# Usage
context = Context(ConcreteStateA())
context.request()  # Output: ConcreteStateA handles request.
context.request()  # Output: ConcreteStateB handles request.
```

### Visitor

**Purpose:** Separates an algorithm from an object structure by moving the hierarchy of methods into one object.

**Real-World Analogy:** A tax auditor (visitor) who visits different businesses to calculate taxes without changing business classes.

**Python Example:**

```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteComponentA(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self):
        return "A"

class ConcreteComponentB(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self):
        return "B"

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element):
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element):
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element):
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")

# Usage
components = [ConcreteComponentA(), ConcreteComponentB()]
visitor = ConcreteVisitor1()
for component in components:
    component.accept(visitor)
# Output:
# A + ConcreteVisitor1
# B + ConcreteVisitor1
```

### Template Method

**Purpose:** Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.

**Real-World Analogy:** A recipe template where steps like "bake" are fixed, but ingredients vary.

**Python Example:**

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self):
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self):
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self):
        pass

    @abstractmethod
    def required_operations2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self):
        print("ConcreteClass1 says: Implemented Operation2")

# Usage
concrete = ConcreteClass1()
concrete.template_method()
# Output:
# AbstractClass says: I am doing the bulk of the work
# ConcreteClass1 says: Implemented Operation1
# AbstractClass says: But I let subclasses override some operations
# ConcreteClass1 says: Implemented Operation2
# AbstractClass says: But I am doing the bulk of the work anyway
```

### Interpreter

**Purpose:** Defines a grammar for a simple language and an interpreter that uses the representation to interpret sentences.

**Real-World Analogy:** Interpreting regular expressions to match patterns in text.

**Python Example:**

```python
from abc import ABC, abstractmethod

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def __init__(self, data):
        self._data = data

    def interpret(self, context):
        return self._data in context

class OrExpression(AbstractExpression):
    def __init__(self, expr1, expr2):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context):
        return self._expr1.interpret(context) or self._expr2.interpret(context)

class AndExpression(AbstractExpression):
    def __init__(self, expr1, expr2):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context):
        return self._expr1.interpret(context) and self._expr2.interpret(context)

# Usage
john = TerminalExpression("John")
henry = TerminalExpression("Henry")
male = OrExpression(john, henry)

print(male.interpret("John"))  # Output: True
print(male.interpret("Jane"))  # Output: False
```

## How to Use This Repository

1. **Clone the Repo:** `git clone https://github.com/yourusername/design-patterns.git`
2. **Run Examples:** Each pattern has a Python code snippet. Copy and run them in your Python environment.
3. **Practice:** Implement these patterns in your own projects or modify the examples.
4. **Explore Further:** Read books like "Design Patterns: Elements of Reusable Object-Oriented Software" by the Gang of Four.

## Contributing

This repository is open for contributions! We welcome improvements, additional examples in other languages (e.g., Java, C++), bug fixes, or new patterns.

1. Fork the repo.
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request.

Please follow the code style in the examples and add clear documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.