# Light

This is an simple API with a few basic operations concerning people and its salaries.

# Instructions

Make sure to have the port `8000` free since these instructions consider this is the port where the project will run, or use another port, adjusting the suggested commands.

## Requirements

The project's requirements are present in the `requirements.txt` file and also Python3, which is not present in the requirements file. So, what you will need for this project is Python3, `Django`, `Djangorestframework` and `psycopg`.

**Attention: this project was idealized to be ran through Docker, so it is recommended to install make sure you have docker and docker-compose in your machine before proceding. With docker installed, just jump this section and go directly to [Using Docker](#using-docker) below.**

Alternatively, using a package manager such as `pip` is enough to install the dependencies through the `pip3 install -r requirements.txt` command from the project's root directory. After installing the dependencies, make sure to add your local postgres configuration such as host, port, password and etc. in `settings.py` file. With that configured, you need to run the database migrations by running `python3 manage.py migrate`, and after that the project is ready to run. So, run the command

```
python3 manage.py runserver 0.0.0.0:8000
```

and it should be enough.

## Using Docker

Docker makes it easier to run this project. From the project's root directory simply run

```
docker-compose up --build
```

and you should be ready to go in `localhost:8000`.

# The API

## Endpoints

Acessing the project's root URL will display a Django 404 page, since there is no endpoint for that. The project has 2 main domain paths, them being the API itself and the Django's admin interface. They are present in `/api/v1/` and `/admin` paths respectively.

Acessing `/api/v1/` will display the necessary endpoints for this challenge. There is three, the requested `/users` and `/salaries`, and also a `/statistics` that display statistics about the salaries present in the database. This last one is a optional extra.

### /users

The `/users` endpoint has the full CRUD operations implemented, displaying a list and allowing the creation in its root path. Acessing an specific user through `/users/:id` makes it possible to retrieve the user with the specified ID and also update/delete it via DRF's native interface.

The retrieved users will display its native fields, such as `id`, `name`, `cpf` and `date_of_birth` and also the list of its registered salaries, along with some requested statistics about the salaries of this specific user, such as its average salary, average discounts, max and min salaries.

### /salaries

The `/salaries` endpoint is similar to the `/users` endpoint in the form of having all CRUD operations available. The difference is it shows no additional informations other than its own fields. The retrieved informations about salaries are `id`, `date`, `value`, `discounts` and the `user` it belongs to.

### /statistics

This endpoint is optional and it is a way to implement the same statistics shown in the `/users` endpoint, but in a global way, meaning it will calculate averages, max and min for every salary present in the database. This endpoint does not have all CRUD operations since it doesn't represent a database entity, and it is dynamically calculated. The only operations implemented for this endpoint is `list` and `retrieve`, where `list` returns a single information: the statistics about every salary present in the database.

Calling the `retrieve` action will require an ID, and it is the ID of an user. So, accessing `/statistics/:user_id` will retrieve the same statistics present in the `/users` endpoint, calculating averages, max and min for this specific user.

# Tests

This project has a few model and viewsets tests implemented, just as an form to guarantee the minimal features are working. They are not very deep and were implemented as a form of understanding how Django API tests work.

To run the tests using docker, simply run the command `docker-compose run web python manage.py test` in the project's root directory.
