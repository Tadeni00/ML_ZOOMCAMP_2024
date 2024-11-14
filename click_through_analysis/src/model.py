# model.py
import joblib
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import logging

from src.utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def train_and_evaluate_model(X, y):
    try:
        # Splitting the data into training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Logistic Regression with GridSearchCV
        param_grid = {
            'C': [1],
            'penalty': ['l2'],
            'solver': ['lbfgs']
        }
        model = LogisticRegression(random_state=42)
        grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1, verbose=2)
        grid_search.fit(x_train, y_train)

        # Get best model
        best_model = grid_search.best_estimator_
        
        # Predictions and evaluation
        y_pred = best_model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, best_model.predict_proba(x_test)[:, 1])

        logger.info(f"Model Evaluation - Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, "
                    f"Recall: {recall:.2f}, F1 Score: {f1:.2f}, ROC-AUC: {roc_auc:.2f}")

        # Save the trained model to disk
        model_path = 'artifacts/model.pkl'
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        joblib.dump(best_model, model_path)
        logger.info(f"Trained model saved to {model_path}")

        return best_model

    except Exception as e:
        logger.error(f"Error during model training: {e}")
        raise e
