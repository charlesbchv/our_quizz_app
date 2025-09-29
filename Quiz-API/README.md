# QuizBack ESIEE

## Description
QuizBack ESIEE est une API de quiz développée en Python, permettant de gérer des quiz avec des fonctionnalités d'authentification et de gestion des quiz.

## Prérequis
Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python
- Les dépendances spécifiées dans `requirements.txt`

## Installation

1. Créez un environnement virtuel :
    ```sh
    python -m venv env
    ```

2. Activez l'environnement virtuel :
    - Sur Windows :
      ```sh
      .\env\Scripts\activate
      ```
    - Sur macOS et Linux :
      ```sh
      source env/bin/activate
      ```

3. Installez les dépendances requises :
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

### Génération du mot de passe hashé

Ajoutez le code suivant dans un fichier `generate_hash.py` pour générer un mot de passe hashé :

```python
import hashlib

password = "YourPassword"
password_hash = hashlib.md5(password.encode("UTF-8")).hexdigest()
print(f"The MD5 hash for 'YourPassword' is: {password_hash}")
```
Exécutez ce script pour obtenir le mot de passe hashé, puis configurez les variables d'environnement :

```sh
export APP_ADMIN_PASSWORD=<votre_mot_de_passe_hashé>
export JWT_SECRET='Faut pas chercher trop loin on est le meilleur'
```
## Utilisation
Pour démarrer le serveur, exécutez la commande suivante :

```sh
python app.py
```