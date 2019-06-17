import json
import math
from pathlib import Path
from timeit import timeit


def sign_filter(function):
    def wrapper(x):
        if x > 0:
            function(x)
    return wrapper


@sign_filter
def is_repdigit_guerziz(x):
    """Test if the number given is only
    composed by the sames characters,
    (mathematical method)."""

    # x = number given

    answer = 9 * x / (math.pow(10, int(math.log10(x) + 1)) - 1)
    
    if answer.is_integer():
        return x 
    
@sign_filter 
def is_repdigit_string(x):
    string = str(x)
    if string == string[0] * len(string):

        return x


def serialize(data, path="Results"):
    """Create a json file with file data."""

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    final_dict = {
        "start": number_start,
        "range": number_range + 1,
        "step": number_step,
        "exec time": runtime,
        "number of rep digit": number_of_rep_digit,
        "data": data,
    }

    with path.open("w") as f:
        json.dump(final_dict, f, indent=4)


def run_range(function, start=0, stop=10000, step=1):

    repdigits_stream = (function(i) for i in range(start, stop, step))
    return list(filter(None, repdigits_stream))


if __name__ == "__main__":
    equals = (run_range(is_repdigit_guerziz) == run_range(is_repdigit_string))
    print("equals:", equals)
    
    print(run_range(is_repdigit_guerziz))
    print(run_range(is_repdigit_string))
    
    runtime = timeit("run_range(is_repdigit_guerziz)", globals=globals(), number=1)
    runtime2 = timeit("run_range(is_repdigit_string)", globals=globals(), number=1)
    
    print("is_repdigit_guerziz", runtime)
    print("is_repdigit_string", runtime2)


