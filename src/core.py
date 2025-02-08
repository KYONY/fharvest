import os
import shutil
from typing import List, Optional

class FileHarvester:
    def __init__(
        self,
        source_dirs: List[str],
        destination_dir: str,
        excluded_files: Optional[List[str]] = None,
        file_extensions: Optional[List[str]] = None
    ):
        self.source_dirs = source_dirs
        self.destination_dir = destination_dir
        self.excluded_files = excluded_files or ['__init__.py']
        self.file_extensions = file_extensions or ['.py', '.js', '.css', '.json']

    def copy_files(self, additional_files: Optional[List[str]] = None) -> None:
        """
        Copy specified files from source directories to a destination directory.

        Args:
            additional_files: Optional list of additional files to copy.
        """
        if not os.path.exists(self.destination_dir):
            os.makedirs(self.destination_dir)

        self._copy_from_sources()
        if additional_files:
            self._copy_additional_files(additional_files)

    def _copy_from_sources(self) -> None:
        for source_dir in self.source_dirs:
            for root, _, files in os.walk(source_dir):
                for file in files:
                    if self._should_copy_file(file):
                        source_file = os.path.join(root, file)
                        shutil.copy(source_file, self.destination_dir)
                        print(f'Copied: {source_file} to {self.destination_dir}')

    def _should_copy_file(self, filename: str) -> bool:
        return (
            any(filename.endswith(ext) for ext in self.file_extensions)
            and filename not in self.excluded_files
        )

    def _copy_additional_files(self, additional_files: List[str]) -> None:
        for file in additional_files:
            if os.path.exists(file):
                shutil.copy(file, self.destination_dir)
                print(f'Copied: {file} to {self.destination_dir}')
            else:
                print(f'File not found: {file}')