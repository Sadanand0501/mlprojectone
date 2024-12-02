# End to End Data Science Project
import dagshub
dagshub.init(repo_owner='Sadanand0501', repo_name='mlprojectone', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)