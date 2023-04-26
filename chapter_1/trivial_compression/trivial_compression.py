class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.__compress(gene)

    def __compress(self, gene: str) -> None:
        self.bit_string: int = 1  # start with sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left two bits
            match nucleotide:  # Change the last two bits
                case "A":
                    self.bit_string |= 0b00
                case "C":
                    self.bit_string |= 0b01
                case "G":
                    self.bit_string |= 0b10
                case "T":
                    self.bit_string |= 0b11
                case _:
                    raise ValueError(f"Invalid Nucleotide: {nucleotide}")

    def decompress(self) -> str:
        gene: str = ""
        for i in range(
            0, self.bit_string.bit_length() - 1, 2
        ):  # -1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11  # get just 2 relevant bits
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalid bits: {bits}")
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = (
        "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA"
        * 100
    )
    print(f"original is {getsizeof(original)} bytes\n")
    compressed: CompressedGene = CompressedGene(original)
    print(f"compressed is {getsizeof(compressed)} bytes")
    print(compressed)
    print(
        f"original and decompressed are the same {original == compressed.decompress()}"
    )
