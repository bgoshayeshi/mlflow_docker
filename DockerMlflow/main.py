from  mlflow.pyfunc import load_model
import pandas as pd
import click

import json
@click.command()
@click.argument('input', nargs=-1, type=click.STRING)
@click.option('--output_format', default = 'json')
def model_prediction( input, output_format):
    model = load_model('mlflow_model')
   
    input_json = pd.read_json(input[1], orient='split')
    print(model.predict(input_json))
    
model_prediction()