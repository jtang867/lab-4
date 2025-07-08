import pytest
import math
from geometry.shapes import Square, Circle
from geometry.utils import area_stats

def test_square_area_zero_and_positive():
    s0 = Square(0)
    s5 = Square(5)
    sa0 = s0.area()
    sa5 = s5.area()
    assert sa0 == 0
    assert sa5 == 25
    r0 = Circle(0)
    r5 = Circle(5)
    ca0 = r0.area()
    ca5 = r5.area()
    assert ca0 == 0
    assert ca5 == math.pi * 25

    
    

def test_stats_keys_and_values():
    s = Square(5)
    c = Circle(0)
    As = area_stats(*(s,c))
    assert type(As) is dict

    assert 'n' in As
    assert 'total' in As
    assert 'mean' in As
    assert 'min' in As
    assert 'max' in As

    assert As['n'] == 2
    assert As['total'] == 25
    assert As['mean'] == 12.5
    assert As['min'] == 0
    assert As['max'] == 25
   

def test_stats_raises_without_shapes():
    with pytest.raises(ValueError):
        stats = area_stats()