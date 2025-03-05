# Authentification React FastAPI

## Setup

### DB
Create a `.env` as follows
```
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=superPassword!
POSTGRES_DB=authentification_react_fastapi
VITE_API_URL=http://backend:8000
```

### Configuration

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
