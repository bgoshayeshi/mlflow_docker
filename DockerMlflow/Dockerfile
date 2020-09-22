# For more information, please refer to https://aka.ms/vscode-docker-python
FROM continuumio/miniconda

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD main.py /app
ADD mlflow_model /app/mlflow_model

# Default library 
RUN conda env update -n base --file /app/mlflow_model/conda.yaml

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# ENTRYPOINT ["mlflow models predict --no-conda -m SmallTest -j 'split' "]
# example: docker run image_id '{"columns":["alcohol","chlorides","citric acid","density","fixed acidity","free sulfur dioxide","pH","residual sugar","sulphates","total sulfur dioxide","volatile acidity"],"index":[0],"data":[[12.8,0.029,0.48,0.98,6.2,29,3.33,1.2,0.39,75,0.66]]}'
ENTRYPOINT ["python", "-W ignore", "main.py"]