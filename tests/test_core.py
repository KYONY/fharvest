import tempfile
from pathlib import Path
import pytest
from src.core import FileHarvester

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname

def test_file_harvester(temp_dir):
    # Setup
    source_dir = Path(temp_dir) / "source"
    source_dir.mkdir()

    # Create test files
    (source_dir / "test.py").touch()
    (source_dir / "test.js").touch()
    (source_dir / "__init__.py").touch()

    dest_dir = Path(temp_dir) / "dest"

    # Test
    harvester = FileHarvester(
        source_dirs=[str(source_dir)],
        destination_dir=str(dest_dir)
    )
    harvester.copy_files()

    # Verify
    assert (dest_dir / "test.py").exists()
    assert (dest_dir / "test.js").exists()
    assert not (dest_dir / "__init__.py").exists()