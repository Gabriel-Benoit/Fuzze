from __future__ import annotations
from typing import Literal


class Cost:
    """A class to represent the cost of a rule expansion in a grammar. It is a wrapper of int extended with the value "inf" to represent an infinite cost.
    This class is used by the cost estimators to estimate the cost of a rule expansion in a grammar. Specific behaviors with the operators +, -, *, /, >, >=, == are implemented to handle the "inf" value.
    """

    def __init__(self, init: int | Literal["inf"] | Cost) -> None:
        if isinstance(init, Cost):
            self._value: int | Literal["inf"] = init.value
        else:
            self._value: int | Literal["inf"] = init

    def __ge__(self, value: int | Cost) -> bool:
        if self == value:
            return True
        return self > value

    def __lt__(self, value: int | Cost) -> bool:
        return not self >= value

    def __le__(self, value: int | Cost) -> bool:
        if self == value:
            return True
        return not self > value

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Cost):
            return self.value == value.value
        return self.value == value

    def __gt__(self, value: int | Cost) -> bool:
        if self.value == "inf":
            return True
        if isinstance(value, Cost):
            if value.value == "inf":
                return False
            return self.value > value.value
        return self.value > value

    def __add__(self, other: int | Cost) -> Cost:
        if isinstance(other, Cost):
            if self.value == "inf" or other.value == "inf":
                return Cost("inf")
            return Cost(self.value + other.value)
        if self.value == "inf":
            return Cost("inf")
        return Cost(self.value + other)

    def __sub__(self, other: int | Cost) -> Cost:
        if isinstance(other, Cost):
            if other.value == "inf":
                # TODO Decide how to handle this case
                raise NotImplementedError(
                    "Subtraction of inf from a finite value is not supported"
                )
            if self.value == "inf":
                return Cost("inf")
            return Cost(self.value - other.value)
        if self.value == "inf":
            return Cost("inf")
        return Cost(self.value - other)

    def __mul__(self, other: int | Cost) -> Cost:
        if isinstance(other, Cost):
            if self.value == "inf" or other.value == "inf":
                return Cost("inf")
            return Cost(self.value * other.value)
        if self.value == "inf":
            return Cost("inf")

        return Cost(self.value * other)

    def __truediv__(self, other: int | Cost) -> Cost:
        if isinstance(other, Cost):
            if self.value == "inf" and other.value == "inf":
                raise NotImplementedError("Division of inf by inf is not supported")
            if self.value == "inf" or other.value == 0:
                return Cost("inf")
            if other.value == "inf":
                return Cost(0)
            return Cost(self.value // other.value)
        if self.value == "inf":
            return Cost("inf")
        if other == 0:
            return Cost("inf")
        return Cost(self.value // other)

    def __radd__(self, other: int | Cost) -> Cost:
        return self.__add__(other)

    def __rsub__(self, other: int | Cost) -> Cost:
        if isinstance(other, Cost):
            return other.__sub__(self)
        return Cost(other).__sub__(self)

    def __rmul__(self, other: int | Cost) -> Cost:
        return self.__mul__(other)

    def __rtruediv__(self, other: int | Cost) -> Cost:
        if isinstance(other, Cost):
            return other.__truediv__(self)
        return Cost(other).__truediv__(self)

    def __repr__(self) -> str:
        return f"Cost({self.value})"

    def __str__(self) -> str:
        return str(self.value)

    @property
    def value(self) -> int | Literal["inf"]:
        return self._value

    def is_infinite(self) -> bool:
        return self.value == "inf"

    @classmethod
    def inf(cls):
        return cls("inf")
