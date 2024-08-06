### Baixar os requisitos
```cmd
pip install -r requirements.txt
```

### Criar o usuário do admin (super user)

```
python3 manage.py createsuperuser
```

### Quando realizar alguma mudança em models, rodar:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Para rodar a aplicação: 
```
python3 manage.py runserver
```