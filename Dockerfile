# Utiliser l'image officielle Python 3.11 comme image de base
FROM python:3.11

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port (optionnel si vous ne lancez pas de service sur Flask dans ce cas-ci)
EXPOSE 5000

# Définir la commande par défaut (ici rien à exécuter automatiquement)
CMD ["bash"]
