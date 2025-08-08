import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

class ThreatDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.encoders = {}

    def preprocess(self, df):
        df = df.copy()

        # Convert timestamp to numeric features
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        df['dayofweek'] = df['timestamp'].dt.dayofweek

        # Encode categorical columns
        for col in ['user', 'source', 'action', 'region', 'ip', 'userAgent']:
            if col not in self.encoders:
                self.encoders[col] = LabelEncoder()
                df[col] = self.encoders[col].fit_transform(df[col].astype(str))
            else:
                df[col] = self.encoders[col].transform(df[col].astype(str))

        # Select features
        features = df[['user', 'source', 'action', 'region', 'ip', 'userAgent', 'hour', 'dayofweek']]
        return features

    def fit(self, df):
        features = self.preprocess(df)
        self.model.fit(features)

    def predict(self, df):
        features = self.preprocess(df)
        df['anomaly_score'] = self.model.decision_function(features)
        df['is_anomaly'] = self.model.predict(features)  # -1 = anomaly
        df['is_anomaly'] = df['is_anomaly'].map({1: 0, -1: 1})  # Flip to 1 = anomaly
        return df
