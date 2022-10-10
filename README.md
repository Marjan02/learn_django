# Django

### Clone this repo and cd to it

### Create a virtual environment :

```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname
```

### Activate the virtual environment

```bash
envname\scripts\activate
```

### Deactivate the virtual environment

```bash
deactivate
```

### Install the requirements

```bash
pip install -r requirements.txt
```

### Run Server

```bash
python manage.py runserver
```

### Migration

```bash
# migrate
python manage.py migrate

# Make migrate
python manage.py makemigrations
```

### Admin

- URL Admin panel `http://127.0.0.1:8000/admin/`
- Make admin
  ```bash
  python manage.py createsuperuser
  ```
