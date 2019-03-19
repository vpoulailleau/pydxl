"""Descriptor for a register."""


class Register:
    """Descriptor for a register."""

    def __init__(self, address=0, read=True, write=False, size=1):
        """Initializer."""
        self.address = address
        self.read = read
        self.write = write
        self.size = size

    def __repr__(self):
        """Represent a string."""
        if self.write:
            if self.read:
                rw = "R/W"
            else:
                rw = "W"
        else:
            rw = "R"
        return f"Reg(@{self.address}, {rw}, size: {self.size})"

    def __get__(self, instance, owner):
        """Getter."""
        # instance.attr
        if instance:
            return instance.read(self.address, self.size)
        # class.attr
        else:
            return self

    def __set__(self, instance, value):
        """Setter."""
        if self.write:
            instance.write(self.address, value, self.size)

    def __delete__(self, instance):
        """Deleter. Does nothing."""
        pass
