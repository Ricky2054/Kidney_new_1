from dataclasses import dataclass, field
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path = field(default=Path)
    source_url: str = field(default="")
    local_data_file: Path = field(default=Path)
    unzip_dir: Path = field(default=Path)



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: int
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
