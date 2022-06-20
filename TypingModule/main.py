from typing import List, Tuple, Dict, Union

e: List[str] = ['a', 'b', 'c']
f: Tuple[int, int, int] = (1, 2, 3)
g: Dict[str, int] = {'a': 1, 'b': 2}

e.append(5)
print(e)


def square(arr: List[float]) -> List[float]:
    return [x ** 2 for x in arr]


print(square([1, 2, 3]))  # 1, 4, 9     It also works for integers, no effect on runtime...


def square(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    return [x ** 2 for x in arr]


print(square([1, 2, 3]))  # 1, 4, 9
print(square([1.1, 2.2, 3.3]))
