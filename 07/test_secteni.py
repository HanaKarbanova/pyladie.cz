def secti(a, b):
    return a+b

def test_secti():
    assert secti(1,2)==3
    assert secti(0,0)==0
    assert secti(-1,2)==1
