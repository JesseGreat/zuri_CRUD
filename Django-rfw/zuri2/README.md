# HNG-STAGE ONE

Full documentation available at [https://www.django-rest-framework.org/][docs].

---

# Requirements

* Python 3.6+
* Django 4.2, 4.1, 4.0, 3.2, 3.1, 3.0

# Installation

Clone the repo
   ```sh
   git clone https://github.com/JesseGreat/zuri_CRUD.git
   ```

Install using `pip`...

    pip install requirement

Add `'rest_framework'` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```


    ./manage.py runserver to access on your local host in your browser at `http://127.0.0.1:8000/`, and view your new 'users' API.  you'll  be able to create, read, update and delete users from the system. Examples below

# Hosted Api link

Link: https://jessegreat.pythonanywhere.com/

## APIs

### Create Person

- Route: /api
- Method: POST
- Body:

```

 {
    "name":"Mark Essien"
}

```

- Responses

Success

```
{
    "id": 3,
    "name": "Mark Essien"
}

```

---

### Get user Details

- Route: /api/_id
- Method: GET
- Params: _id

```
URL: /api/3


```

- Responses

Success

```
{
    "id": 3,
    "name": "Mark Essien"
}
```

---

### Update User details

- Route: /api/_id
- Method: PUT
- Params: _id
- Body: name

```
URL: /api/3


```

-Body:

```
{
    "name":"JesseGreat"
}


```

- Responses

Success

```
{
    "id": 3,
    "name": "JesseGreat"
}
```

### Delete User details

- Route: /api/_id
- Method: DELETE
- Params: _id

```

 URL:/api/3

```

- Responses

Success
{
    "message": "Person deleted successfully."
}

# Screenshots 

![api/](https://i.imgur.com/8aAMD9S.png)
![api/name](https://i.imgur.com/jSQA6Iy.png)
![api/id](https://i.imgur.com/rHgPUbq.png)

# Documentation 

Full documentation for the project is available at [https://www.django-rest-framework.org/][docs].
