"""Exercise 03: one clear basic inheritance example."""


class Animal:
    """A basic animal with a name."""

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    """A dog is an animal and can make a dog sound."""

    def speak(self) -> str:
        return f"{self.name}: woof"


if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
    # Dog is an Animal because Dog inherits Animal's shared name behavior.
