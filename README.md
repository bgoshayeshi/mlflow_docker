# mlflow_docker

If you are using mlflow to track and log your machine learning project and want to have it all in a "black box" aka docker container, here this repository will help you do that. 
First, assume that you have already done all the training and have all the model data stored in a directory. 
tip: the directory that has all the model data and rest of the required file necessary to do run mlflow upon contain a file named:
```MLmodel``` and  ```conda.yaml``` 

Now, you like to use the model to do predictions and use the answer in your workflow/pipeline. A docker container can take care of all of the model dependencies and environment variables ( and all other advantages of Docker). 
You can use the code here to make a wrap the mlflow model in a docker container with "input" to invoke the prediction. 
In order to make a container use the following function in "mlflow_in_container.py"

```
model_to_docker_container(modelpath = str,  dockerpath=str) -> str

    Prepare the required file and make a docker container
    :param modelpath:   model path (it should contain MLmodel and conda.yaml files)
    :param dockerpath:  where you like to save the docker container files. 
    :return:            produced docker image id

```

## test.py

At the ```test.py``` an example is illustrated. After downloading the example from ```https://github.com/mlflow/mlflow-example``` 
 and training the model, the model data (saved by pickle) is stored at ```example/wine_quality``` folder. ```test.py``` use these data and containerize the model. After finishing  successfully, it should print 
```
Successfully built IMAGE_ID 
```
and then you can run the container using: 
```
docker run IMAGE_ID input '{"columns":["alcohol","chlorides","citric acid","density","fixed acidity","free sulfur dioxide","pH","residual sugar","sulphates","total sulfur dioxide","volatile acidity"],"index":[0],"data":[[12.8,0.029,0.48,0.98,6.2,29,3.33,1.2,0.39,75,0.66]]}'

```
and the docker response should be: 

```
[5.62578167]
```

### Contact

Babak Goshayeshi
email:      bgoshayeshi@gmail.com
website:    bgoshayeshi.com/babak
linkedin:   https://www.linkedin.com/in/bgoshayeshi/
