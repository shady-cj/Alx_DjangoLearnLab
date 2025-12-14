# Social Media API (Django + DRF)

This project is a simple starter backend for a social media–style API built with **Django** and **Django REST Framework (DRF)**. It focuses on user authentication, profiles, and token-based access.

---

## 1. Environment Setup

### Requirements

* Python 3.8+
* pip

### Install Dependencies

```bash
pip install django djangorestframework
```

### Create Project and App

```bash
django-admin startproject social_media_api
cd social_media_api
python manage.py startapp accounts
```

### Update `settings.py`

Add the following to `INSTALLED_APPS`:

* `rest_framework`
* `rest_framework.authtoken`
* `accounts`

---

## 2. User Authentication Setup

### Custom User Model

* Extend Django’s `AbstractUser`
* Add extra fields such as:

  * `bio`
  * `profile_picture`
  * `followers` (self-referencing `ManyToManyField` with `symmetrical=False`)

> Using `symmetrical=False` allows one-way following (e.g., User A follows User B without B following back).

### Token Authentication

* Enable DRF token authentication
* Run migrations to create the token table:

```bash
python manage.py migrate
```

### API Features

* User registration
* User login
* Token generation and retrieval

---

## 3. URL Configuration

Create routes in `accounts/urls.py` for:

* `POST /register` – user registration
* `POST /login` – user login
* `GET /profile` – user profile management

Both registration and login endpoints return an authentication token on success.

Include the `accounts` URLs in the main project `urls.py`.

---

## 4. Testing & Running the Server

### Start Development Server

```bash
python manage.py runserver
```

---


---


