import copy

class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)

# Usage
original = Prototype("Original Value")
clone = original.clone()
print(clone.value)
clone.value = "Cloned Value"
print(original.value)  # Output: Original Value
print(clone.value) 