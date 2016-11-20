import piskvorky_kouc
import pytest


def test_tah():
    pole = piskvorky_kouc.tah('-------', 1,'x')
    assert len(pole) == 7
    assert pole[1] == 'x'

def test_chybny_tah():
    with pytest.raises(ValueError):
        piskvorky_kouc.tah('xxxxxxx',2,'o')
