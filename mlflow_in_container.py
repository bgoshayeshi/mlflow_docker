from io import BytesIO
from docker import Client
import os 
import shutil
from typing import TYPE_CHECKING, List, Dict, Optional, Tuple
from exceptions import * 
from ast import literal_eval

def prepare_the_files(modelpath: str, dockerpath: str) -> str:
    
    ## name of the model is assigned in the main.py
    mlflow_model = 'mlflow_model'
    
    if not os.path.exists(dockerpath):
        os.makedirs(dockerpath)
    else: 
        shutil.rmtree(dockerpath)
    
    shutil.copytree(src=modelpath, dst= os.path.join(dockerpath, mlflow_model))
    shutil.copy('DockerMlflow/main.py', dockerpath)
    shutil.copy('DockerMlflow/Dockerfile', dockerpath)
    return os.path.join(dockerpath, 'DockerMlflow')
 
def model_to_docker_container(modelpath = str,  dockerpath=str) -> str:
    """
    Prepare the required file and make a docker container
    :param modelpath:   model path (it should contain MLmodel and conda.yaml files)
    :param dockerpath:  where you like to save the docker container files. 
    :return:            produced docker image id
    """
    dockermlflow_path = prepare_the_files(modelpath= modelpath, dockerpath=dockerpath)
   
    cli = Client()
    try: 
        working_path = os.getcwd()
        path = os.path.dirname(dockermlflow_path)
        response = cli.build(dockerfile='Dockerfile', rm=True, tag='docker_test_api', path=path)
        for line in response:
           
            if b'Successfully built' in line:
                d = literal_eval(line.decode('ascii'))
                print(d['stream'])
                image_id  = d['stream'].replace('Successfully built ', '')
            if b'errorDetail' in line:
                d = literal_eval(line.decode('ascii'))
                raise DockerBuildError(d['errorDetail']['message'])
    except DockerBuildError as e:
        print("Error: " + e.args[0])
        raise
    
    return image_id