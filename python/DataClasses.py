import inspect
from pprint import pprint
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str


def main():
    cmt = Comment(2, "This is great!!")
    print(cmt)
    pprint(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == "__main__":
    main()
