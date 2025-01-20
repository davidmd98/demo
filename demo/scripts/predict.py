import click
import joblib
import multiprocessing
import time

from .path import DATA_FILE, MODEL_FILE, PRED_FILE

@click.command("predict")
def predict():
    """
    This functions predicts the values for the test data and stores it in a pkl inside the assets folder
    """
    try:
        _, X_test, _, _ = joblib.load(DATA_FILE)
    except Exception as ex:
        raise Exception(f"Data not found. Run 'train' first.") from ex
    try:
        model = joblib.load(MODEL_FILE)
    except Exception as ex:
        raise Exception(f"Model not found. Run 'train' first.") from ex

    y_pred = model.predict(X_test)
    joblib.dump(y_pred, PRED_FILE)