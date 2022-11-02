from cipher_qy2245 import cipher_qy2245

import pytest
def test_cipher():
    expected = 'bqqmf'
    actual = cipher_qy2245.cipher('apple',1,True)
    assert actual == expected, 'cipher not working'
test_cipher()
