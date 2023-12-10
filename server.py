from flask import Flask, request, send_file
from flask_cors import CORS
import pandas as pd
import numpy as np
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
    df = pd.read_csv('https://drive.google.com/uc?id=1YIhPx1nyar7PIniI0KitxEpr5amRJDbf')
    df.drop(['Row ID', 'Payroll Department', 'Record Number', 'MOU', 'MOU Title', 'FMS Department', 'Job Class', 'Pay Grade', 'Benefits Plan'], axis=1, inplace=True)
    df = df[(df['Hourly or Event Rate'].notna()) & (df['Projected Annual Salary'].notna())]
    df = df[df['Employment Type'] == 'Full Time'].reset_index(drop=True)
    df['Year'] = df['Year'].astype(np.int32)

    numeric_cols = [
        'Hourly or Event Rate', 'Projected Annual Salary', 'Q1 Payments',
        'Q2 Payments', 'Q3 Payments', 'Q4 Payments', 'Payments Over Base Pay',
        '% Over Base Pay', 'Total Payments', 'Base Pay', 'Permanent Bonus Pay',
        'Longevity Bonus Pay', 'Temporary Bonus Pay', 'Lump Sum Pay',
        'Overtime Pay', 'Other Pay & Adjustments',
        'Other Pay (Payroll Explorer)', 'Average Health Cost',
        'Average Dental Cost', 'Average Basic Life', 'Average Benefit Cost'
    ]

    for col in numeric_cols:
        df[col] = df[col].apply(
            lambda x: 0 if type(x) != str else round(float(x.replace('$', '').replace('%', '')), 2)).astype(np.float32)

    app.run()
