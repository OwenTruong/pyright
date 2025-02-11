# This sample tests the case where a ParamSpec is used within a generic
# type alias with a Callable.

from typing import Any, Callable, Generic, Protocol
from typing_extensions import Concatenate, ParamSpec

P = ParamSpec("P")

# Example 1: Callable generic type alias

CommandHandler1 = Callable[Concatenate[int, P], dict[str, Any]]


class Command1(Generic[P]):
    def __init__(self, handler: CommandHandler1[P]) -> None:
        ...


class Application1:
    def func1(self, handler: CommandHandler1[P]) -> Command1[P]:
        return Command1(handler)

    def func2(
        self,
        handler: CommandHandler1[P],
    ) -> Callable[[CommandHandler1[P]], Command1[P]]:
        def decorator(handler: CommandHandler1[P]) -> Command1[P]:
            return self.func1(handler)

        return decorator


# Example 2: Callback Protocol


class CommandHandler2(Protocol[P]):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> dict[str, Any]:
        ...


class Command2(Generic[P]):
    def __init__(self, handler: CommandHandler2[P]) -> None:
        ...


class Application2:
    def func1(self, handler: CommandHandler2[P]) -> Command2[P]:
        return Command2(handler)

    def func2(
        self,
        handler: CommandHandler2[P],
    ) -> Callable[[CommandHandler2[P]], Command2[P]]:
        def decorator(handler: CommandHandler2[P]) -> Command2[P]:
            return self.func1(handler)

        return decorator


def handler(arg1: int, arg2: str) -> dict[str, Any]:
    ...


v1: CommandHandler2 = handler
