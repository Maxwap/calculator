# Utiliser une image de base Python légère
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . /app/

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Démarrer l'application Flask
CMD ["python", "app.py"]
