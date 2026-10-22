class PrintMixin:
    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}({self.name}, {self.description},"  # type: ignore[attr-defined]
                f"{self.price},"  # type: ignore[attr-defined]
                f" {self.quantity})")  # type: ignore[attr-defined]
