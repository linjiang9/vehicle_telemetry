"""Dataset helpers for the vehicle maintenance telemetry repository."""

from __future__ import annotations

import csv
from gettext import install
from pathlib import Path

import pip

DATASET_SOURCE_URL = "https://www.kaggle.com/datasets/tejalaveti2306/vehicle-maintenance-telemetry-data"
REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = REPO_ROOT / "data" / "raw"


def find_raw_dataset(raw_data_dir: Path = RAW_DATA_DIR) -> Path:
    """Return the single raw CSV dataset path."""
    csv_files = sorted(raw_data_dir.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(
            f"No CSV dataset found in {raw_data_dir}. Download the dataset from "
            f"{DATASET_SOURCE_URL} and place the CSV file in this directory."
        )
    if len(csv_files) > 1:
        raise FileExistsError(
            f"Expected one CSV dataset in {raw_data_dir}, found {len(csv_files)}: "
            f"{', '.join(path.name for path in csv_files)}"
        )
    return csv_files[0]


def load_dataset(csv_path: Path | None = None) -> list[dict[str, str]]:
    """Load the raw CSV dataset into a list of row dictionaries."""
    path = csv_path or find_raw_dataset()
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

