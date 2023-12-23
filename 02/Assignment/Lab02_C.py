# Lab02_C.py
class Array:
    """A Array is a self-defined sequential data type which contains a name."""

    def __init__(self, name, contents=None):
        """Initialize the contents.
        name: string
        contents: initial contents.
        """
        self.name = name
        if contents == None:
            contents = []
        self.contents = contents

    def __str__(self):
        """Return a string representaion of this Array."""
        t = [self.name + " has contents:"]
        for obj in self.contents:
            s = "    " + object.__str__(obj)
            t.append(s)
        return "\n".join(t)

    def __getitem__(self, key):
        return self.contents[key]

    def __setitem__(self, key, value):
        self.contents[key] = value

    # TODO_C1
    # Hint: two special functions here

    def add_item(self, item):
        """Adds a new item to the contents.
        item: any object to be added
        """
        self.contents.append(item)

    def __repr__(self):
        return f"Array('{self.name}', {self.contents})"


def main():
    arr1 = Array("MyFirstArray")

    arr1.add_item("wallet")
    arr1.add_item("car keys")

    print(arr1)
    # you shouldsee the output:
    # MyFirstArray has contents:
    #   'wallet'
    #   'car keys'

    # The following 3 statements should work
    # after you finish TODO_C1
    print(arr1[0])  # 'wallet'
    arr1[0] = "toys"
    print(arr1[0])  # 'toys'

    arr2 = Array("MySecondArray")
    arr1.add_item(arr2)
    print(arr2)
    # If you run this program as is, it seems to work.
    # To see the problem, trying printing arr2.


if __name__ == "__main__":
    main()

