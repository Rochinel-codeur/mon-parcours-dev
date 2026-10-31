# Django

Mes premiers projets Django, réalisés en août 2025.

| Projet | Description |
|--------|-------------|
| [`01-generateur-qrcode/`](01-generateur-qrcode/) | On saisit un texte ou un lien et l'application génère son QR code (`qrcode` + Pillow, image enregistrée dans un `ImageField`) |
| [`02-premiere-api/`](02-premiere-api/) | Une première API qui renvoie du JSON avec `JsonResponse`, plus un petit client `requests` dans `client/` |

## Lancer un projet

```bash
cd django
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd 01-generateur-qrcode
cp .env.example .env        # puis mettre une vraie SECRET_KEY
python manage.py migrate
python manage.py runserver
```

Pour l'API, lance le serveur sur le port 9000 (`python manage.py runserver 9000`), puis, dans un autre terminal, `python client/basic.py`.
