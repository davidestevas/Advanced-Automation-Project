import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, Input
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

def create_lstm_model(input_shape, units_1=100, units_2=50, dropout_rate=0.2):
    """
    Creates and compiles the LSTM Neural Network architecture used in the project.
    
    Args:
        input_shape (tuple): Input shape (timesteps, features).
        units_1 (int): Neurons in the first LSTM layer.
        units_2 (int): Neurons in the second LSTM layer.
        dropout_rate (float): Dropout rate to prevent overfitting.
        
    Returns:
        model: Compiled Keras model.
    """
    model = Sequential()
    
    # Explicit Input Layer
    model.add(Input(shape=input_shape))
    
    # Layer 1: LSTM with return sequences
    model.add(LSTM(units=units_1, return_sequences=True))
    model.add(Dropout(dropout_rate))
    
    # Layer 2: Standard LSTM
    model.add(LSTM(units=units_2, return_sequences=False))
    model.add(Dropout(dropout_rate))
    
    # Output Layer
    model.add(Dense(units=1, activation='linear'))
    
    model.compile(loss='mean_squared_error', optimizer='adam')
    
    return model

def create_random_forest():
    """
    Returns the Random Forest model configured with the best parameters found.
    """
    return RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)

def create_svr_model():
    """
    Returns the configured SVR (Support Vector Regression) model.
    """
    return SVR(kernel='rbf', C=10, epsilon=5)
