from flask import Flask, request, send_file
from flask_cors import CORS
import pandas as pd
import requests
import json
import io

app = Flask(__name__)
CORS(app)


@app.route('/get_departments', methods=['GET'])
def get_departments():
    return {'answer': {'departments': sorted(df['Department Title'].unique().tolist())}}


@app.route('/find_jobs_by_department', methods=['POST'])
def find_jobs_by_department():
    department = dict(json.loads(request.data))['department']
    return {'answer': {'jobs': sorted(df[df['Department Title'] == department]['Job Class Title'].unique().tolist())}}


@app.route('/find_job_description/<job>', methods=['GET'])
def find_job_description(job):
    description_link = df[df['Job Class Title'] == job]['Job Class Link'].unique().tolist()[0]
    return send_file(io.BytesIO(requests.get(description_link).content), mimetype='application/pdf')


if __name__ == '__main__':
    df = pd.read_csv('https://drive.google.com/uc?id=1K5E7ONYWNLIEW3sJmfZeBgd6nxSDLzyi')
    app.run()
