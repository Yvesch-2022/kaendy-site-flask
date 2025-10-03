
# Kaendy — Site Web (Flask)

Un site artiste minimal et élégant, fait en Python (Flask).

## 🚀 Lancer en local
```bash
cd kaendy_site_flask
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Ouvre ensuite http://127.0.0.1:5000/ dans ton navigateur.

## ✏️ Éditer le contenu
Modifie le fichier `data/content.json` :
- Textes (bio courte/longue, tagline, emails)
- Liens (Spotify, YouTube, réseaux)
- Embeds Spotify : colle l'URL **embed** (exemple fourni)
- Embeds YouTube : colle l'URL normale, on la convertit en `/embed/` automatiquement
- Images : ajoute tes images dans `static/` et mets le nom de fichier dans `content.json`

## 📦 Déploiement facile (options)
- **Railway/Render/Heroku** : crée un projet Python, ajoute ce repo, et définis la commande de démarrage :
  ```bash
  gunicorn -b 0.0.0.0:5000 app:app
  ```
  (Ajoute `gunicorn` dans `requirements.txt` si tu choisis cette option.)
- **Docker** (optionnel) : ajoute un `Dockerfile` simple :
  ```dockerfile
  FROM python:3.11-slim
  WORKDIR /app
  COPY . .
  RUN pip install -r requirements.txt
  EXPOSE 5000
  CMD ["python", "app.py"]
  ```

## 🖼 Identité visuelle
Couleurs, polices et styles sont configurés dans `static/style.css`.

---
© 2025 Kaendy. Tous droits réservés.
