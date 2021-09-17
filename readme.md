# Growth Review Async DjangoIOT Project House Project
---
### System Setup:

1. Install docker https://docs.docker.com/
2. Install docker compose https://docs.docker.com/compose/install/
---
### Project Setup:

1. Clone project directory: `git clone `
2. Create environment variables file in main directory typing command: `touch .env`
3. Populate .env according to the *Environment Variables Setup* section.
4. Run `docker-compose build`
5. Run `docker-compose run web python manage.py migrate`
6. Create admin by typing command: `docker-compose run web python manage.py createsuperuser`
7. Start server and app by command: `docker-compose up`
8. Server is active at http://localhost:{WEB_PORT}. WEB_PORT must be set in .env file.
---
### Dev Tools:

1. Run `pytest` to start tests.
2. Run `black .` to auto-reformat code.
3. Run `isort .` to auto-sort all imports
---
### Environment Variables Setup:

User environment variables file (.env) should be created as described below:  

`Postgres`  
POSTGRES_DB=POSTGRES DATABASE NAME  
POSTGRES_USER=POSTGRES DATABASE USER  
POSTGRES_PASSWORD=POSTGRES DATABASE PASSWORD  

`Django`  
SECRET_KEY=DJANGO_SECRET_KEY  
DEBUG=DEBUG MODE (default False) # Optional  
WEB_PORT=WEB APPLICATION PORT NUMBER  

`Django Database`  
HOST=DATABASE SERVICE NAME  
PORT=DATABASE PORT NUMBER  

`Celery`  
CELERY_LOG_LEVEL=LOGGING LEVEL (DEBUG, INFO, WARNING, ERROR, CRITICAL, or FATAL)  

`Sendgrid`  
SENDGRID_API_KEY=API KEY FROM SENDGRID  
SENDGRID_REGISTRATION_TEMPLATE_ID=TEMPLATE ID OF THE EMAIL TEMPLATE FROM SENDGRID  
SENDGRID_SENDER_EMAIL=SENDGRID REGISTERED SENDER EMAIL ADRESS  

`User activation endpoint link expiration`  
ACTIVATION_LINK_EXPIRATION_TIME=ACTIVATION LINK EXPIRATION TIME IN MINUTES (default 60) # Optional  

`JWT access and refresh tokens expiration time`  
ACCESS_TOKEN_LIFETIME=ACCESS TOKEN EXPIRATION TIME IN MINUTES (default 15) # optional  
REFRESH_TOKEN_LIFETIME=ACCESS TOKEN EXPIRATION TIME IN HOURS (default 24) # optional  

`Basket expiration time`  
BASKET_EXPIRATION_TIME=BASKET EXPIRATION TIME IN DAYS (default 30) # optional  
