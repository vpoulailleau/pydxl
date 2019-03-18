class Register:
    def __init__(self, address=0, read=True, write=False, size=1):
        self.address = address
        self.read = read
        self.write = write
        self.size = size

    def __repr__(self):
        if self.write:
            if self.read:
                rw = "R/W"
            else:
                rw = "W"
        else:
            rw = "R"
        return f"Reg(@{self.address}, {rw}, size: {self.size})"

    def __get__(self, instance, owner):
        # instance.attr
        if instance:
            return instance.read(self.address, self.size)
        # class.attr
        else:
            return self

    def __set__(self, instance, value):
        if self.write:
            instance.write(self.address, value, self.size)

    def __delete__(self, instance):
        pass
