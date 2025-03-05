# Authentification React FastAPI

## Setup
### Create .env file as follows
```
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=superPassword!
POSTGRES_DB=authentification_react_fastapi
VITE_API_URL=http://backend:8000
```

### Add yourself as a user of the docker group
```
sudo usermod -aG docker $USER
newgrp docker
```

### Make sure docker is running
```
sudo systemctl start docker
```

## Run
```
docker-compose up --build
```

## Contribute

#### config login:
```bash
git config --global user.name "xavier.login"
```


#### config email:
```bash
git config --global user.email "xavier.login@mail.fr"
```

#### Install Precommit
```bash
pre-commit install && pre-commit install --hook-type commit-msg
```

## Utilisation IA Generative
De l'IA generative a ete utilise sur ces points precis:
- URL dynamique liee au reseau Docker (VITE_API_URL)
