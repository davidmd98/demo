from pathlib import Path

WORKSPACE = Path(__file__).parent.parent.parent
ASSETS_DIR = WORKSPACE / "assets"
MODEL_FILE = ASSETS_DIR / "knn_model.pkl"
DATA_FILE = ASSETS_DIR / "data.pkl"
PRED_FILE = ASSETS_DIR / "pred.pkl"