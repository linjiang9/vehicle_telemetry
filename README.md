# Vehicle Maintenance Telemetry Data Analysis

Minimal starter structure for working with the Kaggle
[Vehicle Maintenance Telemetry Data](https://www.kaggle.com/datasets/tejalaveti2306/vehicle-maintenance-telemetry-data)
dataset.

## Repository structure

```text
vehicle_telemetry/
├── data/
│   ├── processed/
│   └── raw/
├── notebooks/
│   └── telemetry_exploration.ipynb
├── src/
│   └── vehicle_telemetry/
└── tests/
```

## Getting started

1. Download the dataset from Kaggle.
2. Place the CSV file in `data/raw/`.
3. Use `src/vehicle_telemetry/dataset.py` to locate and load the raw dataset.
4. Open `notebooks/telemetry_exploration.ipynb` for an interactive Jupyter workflow.

The raw dataset is intentionally not committed to the repository.
