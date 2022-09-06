FROM ubuntu

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update && apt-get install -y \  
    python3.9 \
    python3-pip 
RUN pip install poetry

WORKDIR /backend_projects
COPY pyproject.toml /backend_projects/

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev
 
EXPOSE 8000