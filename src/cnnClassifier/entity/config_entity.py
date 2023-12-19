from dataclasses import dataclass, field
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path = field(default=Path)
    source_url: str = field(default="")
    local_data_file: Path = field(default=Path)
    unzip_dir: Path = field(default=Path)
