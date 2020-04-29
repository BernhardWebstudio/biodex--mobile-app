# REST API for Lepi App
The REST API is built with Django REST Framework. 

It is used for user management as well as storing data about prediction cases. This data could be used to retrieve all previous
cases, analysis etc. 

The data is stored in a Postgres database.

> In following explanation, https://api.lepi.propulsion-home.ch is used as domain name. If you deploy your app to another domain, you will of course have to update this address.
> Each url is also accessible with http://yourLocalDomain:PORT, if you run a local development server

## Endpoints

Detailed documentation about the API endpoints can be found at https://api.lepi.propulsion-home.ch/backend/api/docs/

For convenience, you can import the Lepi.postman_collection.json into postman and test the endpoints there. https://www.postman.com/

## Admin

With a staff or superuser account, you are able to login to https://api.lepi.propulsion-home.ch/backend/lepi-admin/ to
manage users and cases.

The site .../admin/ is the default location for the admin site in Django. For security measures, we have renamed it as 
mentioned above. All login requests to /admin/ will land in a honeypot and be visible in /lepi-admin/.

## Users

Users can be created via the admin panel or via App. As logged in user, you can invite other users. They will receive an
email with a registration code and they can sign up with it.

There is currently no way to register without knowing an admin or getting invited by an existing user.

## Cases and Predictions

Cases hold the information about which user uploaded an image, if and which image he confirmed as well as information about
the model, other prediction choices etc.

## Emails

Emails are automatically sent when a user is invited or a reset password code has been requested. This is handled in the 
background / asynchronously with redis and celery.

### Email Models

- Email: Is the effective data bout an email content and if it has been sent. It also includes the base html template.
- EmailType: Defines the dynamic content based on what email type it is and the html extension. For example registration or password reset.
- DevEmail: Email addresses need to be registered as dev emails if you want to receive emails in development mode.

## Models
![](models.png)

## Run the project locally

- You will need to have Docker installed on your machine. https://docs.docker.com/get-docker/

- After having cloned the repo, through the terminal, navigate inside the folder where the Dockerfile is located
- Run `docker build -t lepi .` to create the Docker image on your machine. You can replace 'lepi' with any name you want
- Replace the image name of the backend container in 'docker-compose.yml', with the name you used to build the image in previous step

- Run `docker-compose up -d` in your terminal, to start up all containers. This will also pull the Docker images if you don't already have them on your machine.
- Run `docker exec -ti lepi_backend_1 bash` in your terminal. This is to log into the container, which is running the REST API. Make sure 'lepi_backend_1' is the name of the running container. Else replace it with the correct name or with the container ID.
- Run `python manage.py runserver 0:8000` and visit http://0.0.0.0:8000/ - you should get a 404 served by Django
- Run `python manage.py createsuperuser` to create a superuser. Visit http://0.0.0.0:8000/backend/lepi-admin and use the credentials to log in