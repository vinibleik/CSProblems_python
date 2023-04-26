from string import printable

import pytest
import unbreakable_encryption as ue


@pytest.mark.parametrize(
    "data",
    ["", "a", "test", printable],
)
def test_decryption(data: str) -> None:
    key1, key2 = ue.encrypt(data)
    assert data == ue.decrypt(key1, key2)
