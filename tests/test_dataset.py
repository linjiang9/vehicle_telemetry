from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.vehicle_telemetry.dataset import DATASET_SOURCE_URL, find_raw_dataset, load_dataset


class DatasetHelpersTest(unittest.TestCase):
    def test_find_raw_dataset_returns_single_csv(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir = Path(temp_dir)
            dataset_path = raw_dir / "vehicle_maintenance.csv"
            dataset_path.write_text("vehicle_id,status\n1,ok\n", encoding="utf-8")

            self.assertEqual(find_raw_dataset(raw_dir), dataset_path)

    def test_find_raw_dataset_requires_csv(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaisesRegex(FileNotFoundError, DATASET_SOURCE_URL):
                find_raw_dataset(Path(temp_dir))

    def test_find_raw_dataset_rejects_multiple_csv_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir = Path(temp_dir)
            (raw_dir / "a.csv").write_text("a\n1\n", encoding="utf-8")
            (raw_dir / "b.csv").write_text("b\n2\n", encoding="utf-8")

            with self.assertRaises(FileExistsError):
                find_raw_dataset(raw_dir)

    def test_load_dataset_returns_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            dataset_path = Path(temp_dir) / "vehicle_maintenance.csv"
            dataset_path.write_text(
                "vehicle_id,need_maintenance\n1,Yes\n2,No\n",
                encoding="utf-8",
            )

            rows = load_dataset(dataset_path)

        self.assertEqual(
            rows,
            [
                {"vehicle_id": "1", "need_maintenance": "Yes"},
                {"vehicle_id": "2", "need_maintenance": "No"},
            ],
        )


if __name__ == "__main__":
    unittest.main()
