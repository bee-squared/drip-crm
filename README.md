# drip-crm

Drip CRM is a customer relationship management tool. Once a user is authenticated and logged in, they can create, read, update, and delete prospect and customer data.

![Intro Image](readme-images/drip-crm.gif "drip-crm.gif")

## Getting Started

#### Setup

1. Create and navigate to the preferred local directory where your project will reside.

```
mkdir drip-crm
cd drip-crm
```

2. Run the latest version of python

```
python3 --version
```

3. Clone the following repository:

```
https://github.com/bee-squared/drip-crm
```

4. Start your DB service (e.g. mysql, downloaded from homebrew):

```
brew services start mysql
```

5. Create the DB and perform migration

```
python3 mydb.py
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Run the django server

```
python3 manage.py runserver
```

7. Navigate to localhost:8000 in your browser

## Built With

- Django
- Python
- MySQL 8.3.0
- HTML
- Bootstrap

## Authors

Brian Bouchard

- [Github Profile](https://github.com/bee-squared)
- [LinkedIn Profile](https://www.linkedin.com/in/brian-bouchard)
- [Project Portfolio](https://www.b-squared.life)
