# Authentification React FastAPI

## Setup
### Create ./.env file as follows
```
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=superPassword!
POSTGRES_DB=authentification_react_fastapi

SECRET_KEY=tbXh9MI9lvH8dz99FNKO
VITE_API_URL=http://localhost:8000
POSTGRES_HOST=db
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
Then visit `http://localhost:5173/` with a browser


## Contribute

#### config login && mail:
```bash
git config --global user.name "xavier.login"
git config --global user.email "xavier.login@mail.fr"
```

#### Install Precommit
```bash
pre-commit install && pre-commit install --hook-type commit-msg
```

## Utilisation IA Generative
L'IA générative a été utilisée sur ces points précis :
- URL dynamique liée au réseau Docker (non 100 % fonctionnelle)
- Certaines lignes du frontend React spécifiées dans le code source
