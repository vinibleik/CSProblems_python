import pytest
import trivial_compression as tc


@pytest.fixture
def noGene() -> tc.CompressedGene:
    return tc.CompressedGene("")


@pytest.fixture
def oneGene() -> tc.CompressedGene:
    return tc.CompressedGene("G")


@pytest.fixture
def someGenes() -> tc.CompressedGene:
    return tc.CompressedGene("ATTGGCCA")
