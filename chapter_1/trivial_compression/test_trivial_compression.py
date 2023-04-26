import pytest
import trivial_compression as tc


@pytest.fixture
def compressedGene():
    return


class TestTrivialCompression:
    def test_no_CompressedGene(self, noGene: tc.CompressedGene) -> None:
        assert noGene.bit_string == 0b1
        assert not str(noGene)

    def test_one_CompressedGene(self, oneGene: tc.CompressedGene) -> None:
        assert oneGene.bit_string == 0b110
        assert str(oneGene) == "G"

    def test_some_CompressedGene(
        self, someGenes: tc.CompressedGene, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert someGenes.bit_string == 0b10011111010010100
        print(someGenes)
        captured = capsys.readouterr()
        assert captured.out == "ATTGGCCA\n"

    def test_CompressedGene_exceptions(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        with pytest.raises(
            ValueError, match=r"Invalid Nucleotide: V"
        ) as valueError:
            tc.CompressedGene("V")
        with capsys.disabled():
            print(f"\n{valueError}")
            print(valueError.type)
            print(valueError.value)
            print(valueError.traceback)
        assert "Invalid Nucleotide: V" in str(valueError.value)
