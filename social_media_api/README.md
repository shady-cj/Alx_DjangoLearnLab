# Social Media API (Django + DRF)

This project is a simple starter backend for a social media–style API built with **Django** and **Django REST Framework (DRF)**. It focuses on user authentication, profiles, posts, comments, following, feeds, and token-based access.

---

## 1. Environment Setup

### Requirements

* Python 3.8+
* pip

### Install Dependencies

```bash
pip install django djangorestframework
```

### Create Project and Apps

```bash
django-admin startproject social_media_api
cd social_media_api
python manage.py startapp accounts
python manage.py startapp posts
```

### Update `settings.py`

Add the following to `INSTALLED_APPS`:

* `rest_framework`
* `rest_framework.authtoken`
* `accounts`
* `posts`

---

## 2. User Authentication Setup

### Custom User Model

* Extend Django’s `AbstractUser`
* Add extra fields:

  * `bio`
  * `profile_picture`
  * `followers` (self-referencing `ManyToManyField` with `symmetrical=False`)
  * `following` (self-referencing `ManyToManyField` to track users that the user follows)

Run migrations to update the user model:

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

### Token Authentication

* Enable DRF token authentication
* Run migrations to create the token table if not already done:

```bash
python manage.py migrate
```

### API Features

* User registration
* User login
* Token generation and retrieval
* Follow/unfollow other users
* View feed based on followed users' posts

---

## 3. Posts and Comments Functionality

### Step 1: Models

* **Post**: Fields include `author` (ForeignKey to User), `title`, `content`, `created_at`, `updated_at`
* **Comment**: Fields include `post` (ForeignKey), `author` (ForeignKey to User), `content`, `created_at`, `updated_at`

Run migrations for the new models:

```bash
python manage.py makemigrations posts
python manage.py migrate
```

### Step 2: Serializers

* Create serializers for `Post` and `Comment` in `posts/serializers.py`
* Handle user relationships and data validation

### Step 3: Views

* Use DRF viewsets in `posts/views.py` for CRUD operations
* Implement permissions to allow users to edit/delete only their own posts/comments

### Step 4: URL Routing

* Define routes in `posts/urls.py` using DRF routers
* Include endpoints for listing, creating, editing, and deleting posts and comments

### Step 5: Pagination and Filtering

* Add pagination to post and comment lists
* Implement filtering in post views to search by `title` or `content`

### Step 6: Feed

* Create a feed endpoint in `posts/views.py`
* Return posts from users that the current user follows, ordered by `created_at` descending

---

## 4. Follow Management

### Views

* Implement actions in `accounts/views.py`:

  * `follow_user(user_id)`
  * `unfollow_user(user_id)`
* Enforce permissions so users can modify only their own following list

### URL Routing

* Add to `accounts/urls.py`:

  * `/follow/<int:user_id>/`
  * `/unfollow/<int:user_id>/`
* Add feed endpoint to `posts/urls.py`: `/feed/`

---

## 5. URL Configuration for Accounts

* `POST /register` – user registration
* `POST /login` – user login
* `GET /profile` – user profile management
* Follow/unfollow endpoints and feed endpoint
* Registration and login endpoints return an authentication token

Include `accounts` and `posts` URLs in the main project `urls.py`.

---

## 6. Testing & Running the Server

### Start Development Server

```bash
python manage.py runserver
```

### API Testing

* Register and log in users
* Follow/unfollow users
* Create, edit, and delete posts and comments
* Test feed to ensure it shows posts from followed users only
* Test filtering, pagination, and permission enforcement using Postman or similar tools

---
