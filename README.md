# Django + Django Ninja + React Project Template

This project template sets up a full-stack web application using Django with Django Ninja for the backend API, and React for the frontend.

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm 6+

## Getting Started

1. Clone the repository:
git clone https://github.com/Aliman00/DjangoReactTemplate.git
cd DjangoReactTemplate

2. Set up the backend:
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.tx

3. Set up the frontend:
cd frontend
npm install
cd ..

4. Run migrations:
python manage.py migrate
python manage.py makemigrations

5. Start the development servers:
./run_dev.sh


This will start the Django server on http://localhost:8000 and the React development server on http://localhost:3000

## Development

- Django admin interface is available at http://localhost:8000/admin/
- API documentation (provided by Django Ninja) is available at http://localhost:8000/api/docs

## Building for Production

1. Build the React app:
cd frontend
npm run build
cd ..

2. Collect static files:
python manage.py collectstatic

3. Run the Django server:
python manage.py runserver


## Docker (Optional)

To build and run the Docker container:
docker build -t django-react-app .
docker run -p 8000:8000 django-react-app


The application will be available at http://localhost:8000

## Project Structure

- `backend/`: Django project settings
- `api/`: Django app and Ninja API
- `frontend/`: React application
- `run_dev.sh`: Script to run both backend and frontend in development mode

