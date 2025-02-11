# This sample tests the special-case handling of the __self__
# attribute for a function when it is bound to a class or object.

# pyright: reportFunctionMemberAccess=error


from typing import Literal


def func1(a: int) -> str:
    ...


# This should generate an error because func1 isn't
# bound to a "self".
s1 = func1.__self__


class A:
    def method1(self) -> None:
        ...

    @classmethod
    def method2(cls) -> None:
        ...

    @staticmethod
    def method3() -> None:
        ...


s2 = A().method1.__self__
t_s2: Literal["A"] = reveal_type(s2)

s3 = A.method2.__self__
t_s3: Literal["Type[A]"] = reveal_type(s3)

s3 = A.method2.__self__
t_s3: Literal["Type[A]"] = reveal_type(s3)

s4 = A().method2.__self__
t_s4: Literal["Type[A]"] = reveal_type(s4)

# This should generate an error because method3 is static.
s5 = A().method3.__self__

# This should generate an error because method3 is static.
s6 = A.method3.__self__
