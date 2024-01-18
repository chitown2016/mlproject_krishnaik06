## End to End Machine Learning Project

This is a toy ML project that works in AWS Elastic BeanStalk as of January 2024. The code is mainly from @krishnaik06. The main issue I've faced in deployment was remembering to use OS agnostic directory naming in src\pipeline\predict_pipeline.py like this:

```python
model_path = os.path.join("artifacts", "model.pkl")
preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
```

As opposed to using 

```python
model_path = "artifacts\model.pkl"
preprocessor_path = "artifacts\preprocessor.pkl"
```
To catch this error I also added more complete logging that uses gunicorn_logger and works in Elastic Beanstalk. Using this form of logging, the error was easy to spot in /var/log/web.stdout.log. 
For details about the logging see application.py


