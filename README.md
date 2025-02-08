# File Harvester (fharvest)

A Python utility for harvesting files from project directories. This tool helps you collect specific files from different project directories into a single destination directory.

## Installation

```bash
pip install fharvest
```
### Quick Start

```python
from fharvest import FileHarvester

# Initialize harvester
harvester = FileHarvester(
    source_dirs=['app'],
    destination_dir='harvested_files'
)

# Copy files with default settings
harvester.copy_files()
```

##### Main Features

* Collect files with specific extensions (.py, .js, .css, .json) from multiple source directories
* Exclude specified files (e.g., init.py)
* Support for additional file copying (.env, docker files, etc.)
* Configurable file extensions and exclusion rules

#### Detailed Usage

##### Basic File Collection

```python
# Default configuration
harvester = FileHarvester(
    source_dirs=['app'],
    destination_dir='harvested_files'
)

# Copy all supported files
harvester.copy_files()
```

##### Custom Configuration

```python
# Custom extensions and exclusions
harvester = FileHarvester(
    source_dirs=['app', 'src'],
    destination_dir='output',
    excluded_files=['__init__.py', 'config.py'],
    file_extensions=['.py', '.yml', '.env']
)

# Include additional files
additional_files = [
    '.env',
    'docker-compose.yml',
    'Dockerfile',
    'requirements.txt',
]

harvester.copy_files(additional_files)
```
### API Reference

**FileHarvester Class**

```python
class FileHarvester:
    def __init__(
        self, 
        source_dirs: List[str], 
        destination_dir: str,
        excluded_files: Optional[List[str]] = None,
        file_extensions: Optional[List[str]] = None
    ):
        """
        Initialize the FileHarvester.

        Args:
            source_dirs: List of directories to search for files
            destination_dir: Directory where files will be copied
            excluded_files: List of files to exclude (default: ['__init__.py'])
            file_extensions: List of file extensions to copy 
                           (default: ['.py', '.js', '.css', '.json'])
        """

    def copy_files(self, additional_files: Optional[List[str]] = None) -> None:
        """
        Copy files from source directories to destination directory.

        Args:
            additional_files: Optional list of additional files to copy
        """
```

###### Examples
**Common Use Cases**

1. Collection of Python files:

```python
harvester = FileHarvester(
    source_dirs=['src'],
    destination_dir='dist',
    file_extensions=['.py']
)
harvester.copy_files()
```

2. Docker project files:

```python
harvester = FileHarvester(
    source_dirs=['app'],
    destination_dir='docker_build'
)
harvester.copy_files([
    'Dockerfile',
    'docker-compose.yml',
    '.dockerignore'
])
```

##### Development

**To contribute to FHarvest:**

1. Clone the repository
2. Install development dependencies:
```python
pip install -e ".[dev]"
```
3. Run tests:
```python
pytest
```
**Links**

GitHub: github.com/kyony/fharvest
Issues: github.com/kyony/fharvest/issues

**License**
This project is licensed under the MIT License.
**Author**
Viktor Pryima (pryima.viktor@gmail.com)

```python
This documentation:
- Provides clear installation instructions
- Shows quick start examples
- Details all main features
- Includes comprehensive API reference
- Demonstrates common use cases
- Includes development setup instructions
- Lists important links and license information

The format is optimized for both PyPI and GitHub display, with proper markdown formatting and code highlighting.
```