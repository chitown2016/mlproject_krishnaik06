from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import logging

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

## Route for a home page

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        application.logger.info("HERE IS GET")
        return render_template('home.html')
    else:
        application.logger.info("HERE IS POST")
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df = data.get_data_as_dataframe()
        application.logger.info("HERE IS PREDICTION DATA FRAME")
        application.logger.info(pred_df.iloc[0])
        application.logger.info("NOW CREATING PREDICT PIPELINE")
        predict_pipeline = PredictPipeline()
        application.logger.info("NOW PREDICTING")
        results = predict_pipeline.predict(pred_df)
        application.logger.info("RESULTS ARE HERE:")
        application.logger.info(results)
        return render_template('home.html',results=results[0])
    
if __name__ == "__main__":
    application.run(host="0.0.0.0",debug=True,port=80)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    application.logger.handlers = gunicorn_logger.handlers
    application.logger.setLevel(logging.INFO)
