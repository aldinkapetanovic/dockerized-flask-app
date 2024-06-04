# Docker Compose Configuration

## Description
This Docker Compose configuration defines two services, Flask and Nginx, and a custom network named `mynetwork`. The Flask service is built from the local Dockerfile, exposing (random) port on the host and connecting to the `mynetwork` network. The Nginx service uses the official Nginx image from Docker Hub, exposing (random) port on the host, and mounting a local `nginx.conf` file. It also connects to the `mynetwork` network and depends on the Flask service.

## Configuration

### Services

#### Flask
- **Build**: Builds the Docker image from the local directory.
- **Ports**: Maps port 8000 (or random) on the host to port 8000 in the container.
- **Networks**: Connects to the `mynetwork` network.

#### Nginx
- **Image**: Uses the latest Nginx image from Docker Hub.
- **Ports**: Maps port 80 (or random) on the host to port 80 in the container.
- **Volumes**: Mounts the local `nginx.conf` file to `/etc/nginx/nginx.conf` in the container.
- **Networks**: Connects to the `mynetwork` network.
- **Depends_on**: Specifies that the Nginx service depends on the Flask service.

### Networks

#### mynetwork
- **Driver**: Specifies the bridge driver for the network.

## Usage
To run these services using Docker Compose, execute `docker compose up` in the directory containing the `docker-compose.yml` file.

```bash
docker compose up -d
```

```bash
docker compose port flask 8000
docker compose port nginx 80
```

```bash

docker network create mynetwork

docker build -t myflaskimage .

docker run -d \
    --name flask \
    -p 8000:8000 \
    --network mynetwork \
    myflaskimage:latest

docker run -d \
    --name nginx \
    -p 80 \
    --network mynetwork \
    -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
    nginx:latest
```

```bash
docker port flask
docker port nginx
```

## Run Flask app locally

```bash
python3 -m venv venv

source ./venv/bin/activate

pip install -r requirements.txt

python app.py
```
