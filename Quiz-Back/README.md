# QuizBack ESIEE

## Description
QuizBack ESIEE est une API de quiz développée en Python. Ce projet permet de gérer des quiz en offrant des fonctionnalités d'authentification et de gestion de quiz.

## Prérequis
Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 
- Requirement

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

Avant de lancer le serveur, configurez les variables d'environnement nécessaires pour l'authentification. 
Un fichier `generate_hash.py` est inclus dans le projet pour générer un mot de passe hashé à configurer dans votre environnement.

Utilisez ce fichier pour générer un mot de passe hashé et configurez les variables d'environnement suivantes :

```sh
export APP_ADMIN_PASSWORD=<votre_mot_de_passe_hashé>
export JWT_SECRET='Faut pas chercher trop loin on est le meilleure G'
