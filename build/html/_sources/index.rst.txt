.. Readthedocs documentation master file, created by
   sphinx-quickstart on Sun Mar  2 00:10:43 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=============================
Tic-Tac-Toe - Documentation
=============================

Bienvenue dans la documentation du jeu **Tic-Tac-Toe** développé avec `Pygame` et une intelligence artificielle utilisant l'algorithme `Minimax`.

------------
Installation
------------

Avant d'exécuter le jeu, assurez-vous d'avoir installé les dépendances requises.

1. **Installer Pygame**

```bash
pip install pygame
```

2. **Lancer le jeu**

```bash
python runner.py
```

------------
Comment jouer ?
------------

Lorsque vous lancez le jeu, vous devez choisir votre rôle :

- **"Play as X"** → Vous commencez en premier.
- **"Play as O"** → L'IA commence en premier.

### Interface du jeu
Le jeu affiche un plateau de **3x3** où vous devez cliquer pour placer votre marque (`X` ou `O`). L'IA utilise l'algorithme **Minimax** pour jouer automatiquement.

### Objectif
L'objectif est d'aligner **trois X ou trois O** sur une ligne, une colonne ou une diagonale.

------------
Algorithme Minimax
------------

L'algorithme `Minimax` est utilisé pour permettre à l'IA de jouer de manière optimale.

1. L'IA analyse toutes les actions possibles sur le plateau.
2. Elle évalue chaque action avec une fonction de score :
   - **1** → Victoire de `X`
   - **-1** → Victoire de `O`
   - **0** → Match nul
3. Elle choisit le **meilleur coup** qui minimise les pertes et maximise les gains.

Exemple de code :

```python
def minimax(board):
    """
    Retourne le meilleur mouvement possible pour le joueur courant.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_value = -math.inf if current_player == X else math.inf
    best_move = None

    for action in actions(board):
        value = min_value(result(board, action)) if current_player == X else max_value(result(board, action))
        if (current_player == X and value > best_value) or (current_player == O and value < best_value):
            best_value = value
            best_move = action

    return best_move
```

------------
Structure du Code
------------

Le projet est structuré comme suit :

📂 `tictactoe/`
  ├── `runner.py`  → Interface graphique avec `Pygame`
  ├── `tictactoe.py`  → Logique du jeu et IA Minimax
  ├── `OpenSans-Regular.ttf` → Police utilisée pour l'affichage

### Fonctionnalités principales
- 🎮 **Interface Pygame**
- 🧠 **IA avec Minimax**
- ✅ **Détection de fin de partie**
- 🔄 **Option Rejouer**

------------
Crédits et Remerciements
------------

Ce projet a été réalisé par **Chegdati Chouaib**.

### Bibliothèques utilisées
- `Pygame` → Interface graphique
- `Math` et `Copy` → Calculs pour l'algorithme Minimax

Merci d'avoir joué à **Tic-Tac-Toe** 🎉 !

