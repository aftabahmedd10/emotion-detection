
import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/aftabahmedd10/emotion-detection.mlflow')
dagshub.init(repo_owner='aftabahmedd10', repo_name='emotion-detection', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)