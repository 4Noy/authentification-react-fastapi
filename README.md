# Authentification React FastAPI

## Setup
### Create .env file as follows
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
De l'IA generative a ete utilise sur ces points precis:
- URL dynamique liee au reseau Docker (Non 100% fonctionnel)
- Certaines lignes du frontend React specifiee dans le code source
