# StudyVault

StudyVault is a Django-based study resource platform built to provide a simple, authenticated space for organizing and accessing academic resources.

The project was built as a portfolio project to practice Django fundamentals, user authentication, protected views, templates, static-file handling, and production deployment.

## Live Demo

**[StudyVault](https://studyvault-production-a728.up.railway.app/)**

## Features

- User registration with email validation
- User login and logout using Django authentication
- Protected pages for authenticated users
- Study resources section
- Personal library section
- User profile page
- Django messages for authentication feedback
- Responsive frontend with HTML, CSS, and JavaScript
- Production static-file serving with WhiteNoise
- Production deployment with Gunicorn and Railway

## Tech Stack

| Category | Technology |
| --- | --- |
| Backend | Python, Django 6.1 |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Authentication | Django Authentication System |
| Static Files | WhiteNoise |
| Web Server | Gunicorn |
| Deployment | Railway |
| Version Control | Git, GitHub |

## Project Structure

```text
StudyVault/
├── home/
│   ├── static/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── myApp/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── staticfiles/
├── manage.py
├── requirements.txt
└── README.md
```

## Authentication

StudyVault uses Django's built-in authentication system for registration and login.

The application includes:

- `UserCreationForm` for registration
- Password validation through Django
- Session-based authentication
- `@login_required` protection for authenticated pages
- Login, logout, and registration flows

## Local Development

### 1. Clone the repository

```bash
git clone https://github.com/OmDhakal/StudyVault.git
cd StudyVault
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Django secret key

For local development, set the `SECRET_KEY` environment variable rather than committing a secret to the repository.

Linux/macOS:

```bash
export SECRET_KEY="your-secret-key"
```

Windows PowerShell:

```powershell
$env:SECRET_KEY="your-secret-key"
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Collect static files

```bash
python manage.py collectstatic
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Production Deployment

StudyVault is deployed on Railway using:

- Gunicorn as the WSGI server
- WhiteNoise for static files
- Railway for hosting
- Environment variables for deployment configuration

The production server runs:

```bash
gunicorn myApp.wsgi:application
```

## What I Practiced

This project helped me build hands-on experience with:

- Django project and app structure
- URL routing and views
- Django templates
- Forms and validation
- User authentication and sessions
- Database migrations and SQLite
- Static-file collection and production serving
- CSRF and allowed-host configuration
- Git and GitHub workflow
- Deploying a Django application to Railway

## Author

**Om Dhakal**

- GitHub: [@OmDhakal](https://github.com/OmDhakal)
- LinkedIn: [Om Dhakal](https://www.linkedin.com/in/om-dhakal-82226230a/)

## License

This project is intended as a personal portfolio and learning project.
