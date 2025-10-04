class MyClass:
    attr = 5
    def method(self):
        pass

print(lookup(MyClass))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', ..., 'attr', 'method']
