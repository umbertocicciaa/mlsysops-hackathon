import joblib
import pickle
import pandas as pd
import numpy as np

# Load the saved model
loaded_model = joblib.load('rf_model_predictive.joblib')

# Load the important features list
with open('important_features.pkl', 'rb') as f:
    important_features = pickle.load(f)
    
print(f"Model loaded successfully from 'rf_model_predictive.joblib'")
print(f"Loaded {len(important_features)} important features:")
print(important_features)

# Demonstrate how to use the model for prediction
predictions = []
def prepare_data_for_prediction(loaded_model, df_sample_path = "data_cleaned_to_test.pkl"):
    """
    Prepare data for prediction, ensuring it has all required features.
    
    Parameters:
    -----------
    df_sample_path : str
        Path to the sample dataframe (CSV file) with system metrics
    loaded_model : sklearn.ensemble.RandomForestClassifier
        The loaded Random Forest model for making predictions

    Returns:
    --------
    pandas.DataFrame
        Processed dataframe ready for prediction
    """
    # Load the sample dataframe
    df_sample = pd.read_pickle(df_sample_path)

    # Ensure all required columns are present
    missing_cols = set(important_features) - set(df_sample.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    predictions.extend(loaded_model.predict(df_sample[important_features]))
    print(f"Predictions made on {len(df_sample)} samples.")
    print(f"Predictions: {predictions}")
    # Return only the important features in the correct order
    return pd.DataFrame(predictions)

prepare_data_for_prediction(loaded_model, df_sample_path = "data_cleaned_to_test.pkl")