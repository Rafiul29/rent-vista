# RentVista Backend

Welcome to **RentVista**, a Django REST API backend for a comprehensive rental advertisement system. This project enables users to post, browse, and manage rental listings. Admins oversee the approval process for ads, while users can submit rental requests, mark favorites, and leave reviews.

## Features

### User Authentication
- **Registration**: New users receive an email verification link.
- **Login and Logout**: Secure authentication and session management.
- **Roles**: Admin and User roles with respective access control.

### Rent Advertisements
- **Post an Advertisement**: Users can create rental listings.
- **Approval by Admin**: Admins approve advertisements before they go public.
- **Visibility**: Only approved ads are visible.

### Rent Requests
- **Send Requests**: Users send rent requests to ad owners.
- **Accept Requests**: Ad owners can accept one request.
- **Request Lock**: No more requests accepted once one is approved.

### Filtering
- Users can filter advertisements based on categories.

### Favorite Advertisements
- Save ads to a personal list for quick access.

### Reviews and Ratings
- Users can review and rate ads.

## Technologies

- **Backend**: Django, Django REST Framework
- **Database**: SQLite

---
## API Endpoints

**Backend API Base URL**: `http://localhost:8000/`

### User Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login/` - User login
- `GET /api/auth/logout/` - User logout
- `GET /users/:id/` - User profile
- `GET /users/role/` - View user roles (admin, users)

### Rent Advertisements
- `POST /ads/create/` - Create a new house rent advertisement (users)
- `GET /ads/list/` - List all approved rent advertisements (public)
- `GET /ads/pending/` - View pending advertisement requests (admin)
- `PATCH /ads/approve/:id/` - Approve an advertisement (admin)
- `GET /ads/list/:id/` - Get details of a specific rent advertisement
- `GET /ads/list/?category=<category>` - Filter advertisements by category

### Rent Requests
- `POST /requests/create/` - Send a rent request to the advertisement owner
- `GET /requests/list/?advertiser_id=<id>` - View all rent requests for a specific advertiser
- `PATCH /requests/accept/:id/` - Accept a rent request (advertiser only)
- `GET /requests/list/?user_id=<user_id>` - List rent requests for a specific user

### Favorites Management
- `GET /favorites/list/` - List all favorite advertisements (for the user)
- `POST /favorites/add/` - Add an advertisement to favorites
- `DELETE /favorites/remove/:id/` - Remove an advertisement from favorites
- `GET /favorites/list/?user_id=<user_id>` - User-specific favorite advertisements

### Reviews and Ratings
- `POST /reviews/add/` - Add a review and rating to a rent advertisement
- `GET /reviews/list/?ad_id=<ad_id>` - List reviews for a specific advertisement
- `GET /reviews/average/?ad_id=<ad_id>` - Get average rating for a specific advertisement

### Menu Category
- `GET /category/list/` - List all menu categories
- `GET /category/list/:id` - Get details of a specific menu category

### Menu Browsing
- `GET /menu/list/` - List all menu items
- `POST /menu/list/` - Add a new menu item
- `GET /menu/list/:id/` - Get details of a specific menu item
- `DELETE /menu/list/:id/` - Delete a specific menu item
- `GET /menu/list/?search=<search_query>` - Filter the menu by category

### Favourite Menu
- `GET /menu/favourite/` - List all favourite menu items
- `POST /menu/favourite/` - Add a menu item to favourites
- `DELETE /menu/favourite/:id/` - Remove a menu item from favourites
- `GET /menu/favourite/?user_id=2` - User-specific favourite menu list


---
## Installation

## Prerequisites
- Python 3.x
- Django
- Django REST framework

## Installation

1. **Clone the repository**
 ```sh
  git clone https://github.com/Rafiul29/rent-vista.git
```
2. **Navigate to the project directory**
```sh
cd rent-vista
```
3. **Create a virtual environment**
```sh
python3 -m venv venv
```
4. **Activate the virtual environment**
```sh
source venv/bin/activate
```
5. **Install dependencies**
```sh
pip install -r requirements.txt
```
6. **Set up environment variables**
- Create a .env file in the root directory and add the following variables:
```sh
EMAIL_HOST=
EMAIL_PASSWORD=
```
7. **Run migrations**
 ```sh
python manage.py migrate
```
8. **Start the server**
```sh
python manage.py runserver
```
The server will be running on http://localhost:8000.

