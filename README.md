<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://applifting.cz/img/e7a83d6232e3c1e0ede78075f5ecb078.svg">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
    * [Built With](#built-with)
* [The taks](#the-task)
    * [Requirements](#requirements)
    * [Data model](#data-model)
        *[Products](#products)
        *[Offers](#offers)
    * [Relations](#relations)
* [Specification](#specification)
    * [Must have](#must-have)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
    * [Authentication](#authentication)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

This API service was created as an exercise result made by AppLifting.

### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)

<!-- THE TASK -->
## The task
Create REST API JSON Python microservice, which allows to browse a product catalog and
automatically updates prices from the offer service (provided by AppLifting)

### Requirements:
* Provide API to create, update and delete product
* Periodically query provided microservice for offers/shops with products

### Data model:
* #### Products
    * Each product corresponds to a real world product you can buy
    * id: The type is up to you :-)
    * name : string
    * description: string
* #### Offers
    * Each offer represents a product offer being sold for some price somewhere
    * id: The type is up to you :-)
    * price : integer
    * items_in_stock: integer

### Relations:
* Product has many Offers
* Offer belongs to Product

<!-- SPECIFICATION -->
## Specification

#### Must have:
* Use an SQL database as internal database, library for API layer is up to you :-)
* Request an access token from the offers microservice
    * This should be done only once, all your registered products are tied to this
token. Provide this token for all calls to the offers microservice.
* Create CRUD for Products
    * When a new Product is created, call the offers microservice to register it.
* Create background (job) service which periodically call the offers microservice to
request new/updated offers for your products (price from offer ms is updated every
minute).
* Base URL for the Offers MS should be configurable via an environment variable
* Write basic tests with pytest

<!-- GETTING STARTED -->
## Getting Started
If you want to get a local copy of this service up and running, follow these steps:

### Prerequisites

You need to install these before running 
* [python-3.7.9](https://www.python.org/downloads/)
```shell script
Ubuntu: sudo apt install python3.7
MacOS: brew install python
```

* [PostgreSQL](https://www.postgresql.org/download/)

### Installation
If you want to run this app locally and, for example, test it, you can. 

Good Advise: Use a virtual environment ([pipenv](https://github.com/pypa/pipenv), [anaconda](https://www.anaconda.com/products/individual), ...)

1. Clone the repo
```shell script
git clone https://github.com/johnunar/praggregator.git
```
2. Install requirements from the provided file
```shell script
pip install -r requirements.txt
```
3. Create a local database with these exact commands for quick setup. If you would like to change user's details, do not forget to chnage them in praggregator.local_settings.py too!
```shell script
psql postgres

CREATE DATABASE praggregator;
CREATE USER praggregatoruser WITH PASSWORD 'Z4dtOScE/RFqWhj1o74KSZ/A';
ALTER ROLE praggregatoruser SET client_encoding TO 'utf8';
ALTER ROLE praggregatoruser SET default_transaction_isolation TO 'read committed';
ALTER ROLE praggregatoruser SET timezone TO 'UTC';
ALTER ROLE praggregatoruser CREATEDB; # TESTING DATABASES
GRANT ALL PRIVILEGES ON DATABASE myproject TO praggregatoruser;

\q
```
4. Generate a secret key
```shell script
python
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```
5. Get an AppLifting API Token
```shell script
POST https://applifting-python-excercise-ms.herokuapp.com/api/v1/auth
```
6. Set the environment variables
```shell script
export AL_BASE_URL="https://applifting-python-excercise-ms.herokuapp.com/api/v1"
export AL_TOKEN="<API_token_from_step_5>"
export DJANGO_DEBUG="True"
export DJANGO_SECRET_KEY="<Secret_key_from_step_4 >"
```
7. Migrate
```shell script
./manage.py migrate
```
8. Run tests
```shell script
./manage.py test
```
9. Run the development server
```shell script
./manage.py runserver
```
10. If there is anything wrong, do not hesitate and contact me.



<!-- USAGE -->
## Usage
Full documentation with endpoints and request examples can be found [here](https://praggregator.herokuapp.com/swagger/).

Base URL: http://praggregator.herokuapp.com/api/v1

### Authentication
Before you can access the API, you have to get your AUTH TOKEN. There are two ways to do that:
1. Sign up at http://praggregator.herokuapp.com/signup/ and then use your credentials in a POST request on /auth endpoint
```shell script
curl --request POST \
  --url http://praggregator.herokuapp.com/api/v1/auth/ \
  --header 'content-type: multipart/form-data;' \
  --form username=<your_username> \
  --form password=<your_password>
```

2. OR use the already created Test Token: 
`2dc395b341e2c5bcfdacf597bce76dd3790ca834`
This token is generated for the test user. (username: test, password: test). You can login with these credentials to the [admin console](https://praggregator.herokuapp.com/admin/), too. If you want to test the admin console with a superuser, contact me.

<!-- CONTACT -->
## Contact

Jan Unar
* [@JohnnyUnar](https://twitter.com/JohnnyUnar)
* [johnunar@gmail.com](mailto:johnunar@gmail.com)

Project Link: [https://github.com/johnunar/praggregator](https://github.com/johnunar/praggregator)
