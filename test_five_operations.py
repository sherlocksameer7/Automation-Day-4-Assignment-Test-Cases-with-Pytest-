import pytest

import five_operations

@pytest.mark.xfail
@pytest.mark.parametrize("a, b", [(150, True), (370, True), (371, False), (407, True), (1, True), (137, True)])
def test_armstrong_or_not(a, b):
    Res = five_operations.Armstrong_Num_or_Not(a)
    assert Res == b



@pytest.mark.parametrize("a, b", [(16, True), (42, True), (56, True), (66, True), (72, True), (43, True)])
def test_divisible_by_8(a, b):
    Res = five_operations.Divisible_by_8_Not(a)
    assert Res == b



@pytest.mark.parametrize("a, b, c, res",[(2, 3, 4, 2), (4, 3, 5, 3), (15, 16, 14, 14), (12, 32, 34, 14), (13, 8, 7, 17)])
def test_Smallest(a, b, c, res):
    Result = five_operations.Smallest_among_3(a, b, c)
    assert Result == res



@pytest.mark.skip(reason="No Need")
@pytest.mark.parametrize("a, b",[(2,True),(5,False),(14,True)])
def test_Evenorodd(a, b):
    Res = five_operations.Even_or_Odd(a)
    assert Res == b



@pytest.mark.xfail
@pytest.mark.parametrize("Str, Eq", [("mom", True), ("fizz", True), ("madam", True), ("sameer", True), ("sherlock", True)])
def test_String_Pslindrome(Str, Eq):
    Res = five_operations.String_is_Palindrome_or_Not(Str)
    assert Res == Eq