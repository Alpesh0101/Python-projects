#operator overloads
class appu():
    def __init__(self, value):
        self.value = value
    def __and__(self, obj):
        print("and operator overloaded")
        if isinstance(obj, appu):
            self.value % obj.value
        else:
            print("and operator is not an instance of")
    def __or__(self, obj):
        print("or operator overloaded")
        if isinstance(self, appu):
            return self.value | obj.value
        else:
            raise ValueError("or operator is not an instance of")
        
    def __xor__(self, obj):
        print("xor operator overloaded")
        if isinstance(self, appu):
            return self.value ^ obj.value
        else:
            raise ValueError("or operator is not an instance of")
        
            
    def __lshift__(self, obj):
        print("xor operator overloaded")
        if isinstance(self, appu):
            return self.value << obj.value
        else:
            raise ValueError("or operator is not an instance of")

    def __rshift__(self, obj):
        print("xor operator overloaded")
        if isinstance(self, appu):
            return self.value >> obj.value
        else:
            raise ValueError("or operator is not an instance of")
        
    def __invert__(self):
        print("invert operator overloaded")
        return ~self.value
#Drivers code
if __name__ == "__main__":
    a=appu(10)
    b=appu(20)
    print(a&b)
    print(a|b)
    print(a^b)
    print(a>>b)
    print(a<<b)
    print(~a)
