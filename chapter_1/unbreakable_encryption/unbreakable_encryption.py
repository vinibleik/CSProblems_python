from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    """random_key

    Generate a new length pseudo-random bytes and return its int representation

    Args:
        length (int): The length of the pseudo-random bytes

    Returns:
        int: The int representation of the length pseudo-random bytes
    """
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    """encrypt Encrypt the original string

    Encrypts the original string using the XOR operation with an dummy data

    Args:
        original (str): The string to be encrypted

    Returns:
        Tuple[int, int]: dummy_data, encrypted_original
    """
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes)
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    """decrypt decrypt an data encrypted by the encrypt function

    Args:
        key1 (int): dummy_data | encrypted_data
        key2 (int): encrypted_data | dummy_data

    Returns:
        str: The decrypted str
    """
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    original = "vini"
    print(f"{original=}")
    key1, key2 = encrypt(original)
    print(f"{key1=}, {key2=}")
    decrypted = decrypt(key1, key2)
    print(f"{decrypted=}")
    decrypted = decrypt(key2, key1)
    print(f"{decrypted=}")
    assert original == decrypted
