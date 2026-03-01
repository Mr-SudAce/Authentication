# Django Authentication System

A robust user authentication web application built with Django, featuring a modern dark-themed UI and secure session management.

## Features

- **User Registration**: Create new accounts securely.
- **Secure Login**: Authentication using Django's built-in security features.
- **Session Management**: Automatic session expiry after 1 hour of inactivity for enhanced security.
- **Dashboard**: Protected area accessible only to logged-in users.
- **Modern UI**: Custom-styled interface with a responsive Dark Mode design using CSS variables.

## Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3 (Custom Properties/Variables)
- **Database**: SQLite (Default) / Configurable

## Project Structure

- `views.py`: Handles the logic for login, registration, logout, and the dashboard.
- `templates/`: Contains the HTML files (`login.html`, `register.html`, `dashboard.html`).
- `models.py`: Defines the `CustomUser` model.

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Authentication
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```