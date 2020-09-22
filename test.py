
from mlflow_in_container import model_to_docker_container

if __name__ == "__main__":
    model_path = 'example/wine_quality'
    
    model_to_docker_container(modelpath='example/wine_quality/', dockerpath='example/wine_quality_docker/')
    
    pass