import click
import joblib
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from .path import DATA_FILE, MODEL_FILE, PRED_FILE

_RANDOM_STATE = 0
_N_NEIGHBORS = 3

def _load(dataset=load_iris):
    """
    This function loads a dataset and splits train test data before storing it in a .pkl file inside the assets folder
    """
    try:
        x, y = dataset(return_X_y=True, as_frame=True)
        X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=_RANDOM_STATE)
        joblib.dump((X_train, X_test, y_train, y_test), DATA_FILE)
        return (X_train, X_test, y_train, y_test)
    except Exception as ex:
        raise Exception(f'Error while loading data from sklearn.') from ex

@click.command("train")
def train():
    """
    This functions fits a model with the training data previously stored, and trains a model. Once the model has been trained, it is stored inside the assets folder in a -pkl file.
    """
    X_train, X_test, y_train, y_test = _load()
    model = KNeighborsClassifier(n_neighbors=_N_NEIGHBORS)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_FILE)