"""
    - Language:
        Python 3.X
    
    - Creators:
        This program has beeen created by Mr.Guerziz,
        and implemanted in Python 3 by Jim Pavan.

    - Goal:
        Test if a number is only composed by the same characters.
        (Actually it's not supports floating numbers).
        (Moreover, the mathematical function not supports the 0 and
        negative numbers).
"""


import json
import math
from pathlib import Path
from timeit import timeit


def is_repdigit(x):
    """Test if the number given is only
    composed by the sames characters,
    (mathematical method)."""

    # x = number given

    if x <= 0:
        return
        
    answer = 9 * x / (math.pow(10, int(math.log10(x) + 1)) - 1)

    return answer.is_integer()


def serialize(data, path="Results"):
    """Create a json file with file data."""

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    final_dict = {
        "start": number_start,
        "range": number_range + 1,
        "step": number_step,
        "time (s)": runtime,
        "lenght": lenght,
        "data": data,
    }

    with path.open("w") as f:
        json.dump(final_dict, f, indent=4)


def run_range(function, start=0, stop=1000000, step=1):

    repdigits_stream = (function(i) for i in range(start, stop, step))
    return list(filter(None, repdigits_stream))


if __name__ == "__main__":
    runtime = timeit("run_range(is_repdigit)", globals=globals(), number=1)
    print(runtime)

