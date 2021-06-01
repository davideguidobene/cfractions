from numbers import Complex

from hypothesis import given

from cfractions import Fraction
from . import strategies


@given(strategies.finite_non_fraction_numbers, strategies.fractions)
def test_alternatives(first: Complex, second: Fraction) -> None:
    result = first - second

    assert result == first + (-second)
