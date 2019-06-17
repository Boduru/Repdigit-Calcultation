import functools
import json
import math
from pathlib import Path
from pprint import pprint
from timeit import timeit


def sign_filter(f):
    @functools.wraps(f)
    def wrapper(x):
        if x == 0:
            return x
        elif x > 0:
            return f(x)
    return wrapper


@sign_filter
def is_repdigit_gz(x):
    """Test if a number is a repdigit (Guerziz method)"""

    y = 9 * x / (math.pow(10, int(math.log10(x) + 1)) - 1)
    if y.is_integer():
        return x


@sign_filter
def is_repdigit_gz_pow(x):
    """Test if a number is a repdigit (Guerziz method with built-in pow operator)"""

    y = 9 * x / (pow(10, int(math.log10(x) + 1)) - 1)
    if y.is_integer():
        return x


@sign_filter
def is_repdigit_gz_splat(x):
    """Test if a number is a repdigit (Guerziz method with built-in pow operator symbol)"""

    y = 9 * x / (10 ** (int(math.log10(x) + 1)) - 1)
    if y.is_integer():
        return x


@sign_filter
def is_repdigit_wiki_math(x):
    """Test if a number is a repdigit (Wikipedia method, only mathematical operations)
    https://fr.wikipedia.org/wiki/Nombre_uniforme"""

    length = int(math.log10(x) + 1)
    digit = x % 10
    y = digit * (10 ** length - 1) / 9
    if y == x:
        return x


@sign_filter
def is_repdigit_wiki_mix(x):
    """Test if a number is a repdigit (Wikipedia method, mixed type conversions and mathematical operations)
    https://fr.wikipedia.org/wiki/Nombre_uniforme"""

    length = len(str(x))
    digit = x % 10
    y = digit * (10 ** length - 1) / 9
    if y == x:
        return x


@sign_filter
def is_repdigit_wiki_conv(x):
    """Test if a number is a repdigit (Wikipedia method, type conversions)
    https://fr.wikipedia.org/wiki/Nombre_uniforme"""

    string = str(x)
    length = len(string)
    digit = int(string[0])
    y = digit * (10 ** length - 1) / 9
    if y == x:
        return x


@sign_filter
def is_repdigit_str(x):
    """Test if a number is a repdigit (String method)
    https://codegolf.stackexchange.com/a/125156"""

    string = str(x)
    if string == string[0] * len(string):
        return x


@sign_filter
def is_repdigit_set(x):
    """Test if a number is a repdigit (Set method)"""

    if len(set(str(x))) == 1:
        return x


def run_range(function, start=0, stop=100000, step=1):
    """Find repdigits in a range of integer with selective methods"""

    repdigits_stream = (function(i) for i in range(start, stop, step))
    return list(filter(None, repdigits_stream))


def serialize(data, path="Results.json"):
    """Create a json file with file data."""

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    timeit = functools.partial(timeit, globals=globals(), number=1)

    test_methods = [
        is_repdigit_gz,
        is_repdigit_gz_pow,
        is_repdigit_gz_splat,
        is_repdigit_wiki_math,
        is_repdigit_wiki_mix,
        is_repdigit_wiki_conv,
        is_repdigit_str,
        is_repdigit_set,
    ]

    samples = [run_range(m, stop=1000000) for m in test_methods]
    equals = samples.count(samples[0]) == len(samples)
    print("All methodes work the same:", equals, end="\n\n")

    benchmark = ([m.__name__, timeit("run_range({})".format(m.__name__))] for m in test_methods)
    sorted_bench = sorted(benchmark, key=lambda x: x[1])

    name, ref_runtime = sorted_bench[0]
    print("{:<22}: {:.3f}s".format(name, ref_runtime))

    for name, runtime in sorted_bench[1:]:
        overrun = runtime / ref_runtime - 1
        print("{:<22}: {:.3f}s (+{:>6.1%})".format(name, runtime, overrun))
