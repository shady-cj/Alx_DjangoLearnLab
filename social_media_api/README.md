# Social Media API (Django + DRF)

This project is a simple starter backend for a social media–style API built with **Django** and **Django REST Framework (DRF)**. It focuses on user authentication, profiles, posts, comments, following, feeds, likes, notifications, and token-based access.

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
python manage.py startapp notifications
```

### Update `settings.py`

Add the following to `INSTALLED_APPS`:

* `rest_framework`
* `rest_framework.authtoken`
* `accounts`
* `posts`
* `notifications`

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

## 3. Posts, Comments, Likes, and Notifications

### Step 1: Models

* **Post**: `author` (ForeignKey to User), `title`, `content`, `created_at`, `updated_at`
* **Comment**: `post` (ForeignKey), `author` (ForeignKey to User), `content`, `created_at`, `updated_at`
* **Like**: `user` (ForeignKey), `post` (ForeignKey to Post) in `posts` app
* **Notification**: `recipient` (ForeignKey to User), `actor` (ForeignKey to User), `verb`, `target` (GenericForeignKey), `timestamp` in `notifications` app

Run migrations for the new models:

```bash
python manage.py makemigrations posts notifications
python manage.py migrate
```

### Step 2: Serializers

* Create serializers for `Post`, `Comment`, `Like`, and `Notification`
* Handle user relationships, data validation, and notification formatting

### Step 3: Views

* **Posts & Comments**: CRUD with DRF viewsets
* **Likes**: Views for liking/unliking posts

  * Prevent multiple likes from the same user on the same post
  * Trigger notifications when posts are liked
* **Notifications**: Views to fetch user notifications, prioritizing unread ones

### Step 4: URL Routing

* **Posts/Comments**: `posts/urls.py` with CRUD routes
* **Likes**: `posts/<int:pk>/like/` and `posts/<int:pk>/unlike/`
* **Notifications**: `notifications/urls.py` with `/notifications/` endpoint

### Step 5: Pagination and Filtering

* Apply pagination to posts, comments, and notifications lists
* Filter posts by `title` or `content` for search functionality

### Step 6: Feed

* Endpoint to return posts from users that the current user follows, ordered by `created_at` descending

---

## 4. Follow Management

### Views

* `follow_user(user_id)`
* `unfollow_user(user_id)`
* Permissions enforce that users can only modify their own following list

### URL Routing

* `accounts/urls.py`: `/follow/<int:user_id>/`, `/unfollow/<int:user_id>/`
* Feed endpoint in `posts/urls.py`: `/feed/`

---

## 5. URL Configuration for Accounts

* `POST /register` – user registration
* `POST /login` – user login
* `GET /profile` – user profile management
* Follow/unfollow endpoints
* Feed endpoint
* Likes endpoints
* Notifications endpoint
* Registration and login endpoints return an authentication token

Include `accounts`, `posts`, and `notifications` URLs in the main project `urls.py`.

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
* Like/unlike posts
* Fetch notifications and test feed
* Validate filtering, pagination, and permission enforcement using Postman or similar tools

---
