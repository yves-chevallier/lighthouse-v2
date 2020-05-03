from lfsr import LFSR
from constants import polys
import itertools

def nth(iterable, nth):
    return next(itertools.islice(iterable, nth, nth+1))

def search(poly, cipher):
    i = 0
    lfsr = LFSR(poly)
    while (next(lfsr) != cipher): i += 1
    return i

p = 7
x = 8421
delta = -376
u = nth(LFSR(polys[p]), x)
v = nth(LFSR(polys[p]), x + delta)
print(u, v)

candidates = sorted(
    [
        (
            k,
            abs(search(poly, u) - search(poly, v))
        )
        for k, poly in enumerate(polys)
    ],
    key=lambda x: x[0]
)


