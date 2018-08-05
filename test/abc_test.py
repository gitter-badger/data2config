import pytest


def test_notarr():
    arr = []
    assert not arr

# @pytest.mark.xfail(raises=IndexError)
def test_empty_list():
    arr = []
    with pytest.raises(IndexError):
        arr[0]

def test_empty_str_in():
    s = ''
    assert s in 'aaa'
