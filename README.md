# time-tracker-api V 1.0
A simple yet efficient time tracker api. (Still to be improved since there is no good frontend yet...)

### A. INSTALLATION AND SETUP ###
# Prerequisites
1. Make sure to download docker/docker-compose
2. (Optional) add Github Actions to make use of the automated checks
    and lints whenever you git [push]. Make sure to have a Github account.
3. (Optional) download Docker Desktop to implement the automated Checks and Lint.

# Quick Setup
1. After forking the repo go to the directory where you cloned the repo on your terminal/bash/WSL.
2. Type in the commands docker-compose build
3. Type in the commands docker-compose up
4. Welcome to the backend api! on your web browser type in 127.0.0.1:8000/api/docs/


# Useful commands:
(On the Terminal or Bash command line on the root folder type)
1. docker-compose run --rm app sh -c "python manage.py test"
- Used for running the backend rest api tests
2. docker-compose run --rm app sh -c "flake8"
- Used for linting and checking out if there are any syntax unconformity

### B. FUNCTIONALITIES AND API ###
- A comprehensive API Docs via Swagger UI at localhost:8000/api/docs
- Complete with Github Actions for Automated Checks and Lint
- Checks completed by the Django package Test (12 backend Rest API tests!)
- Lint completed by the Flake8 package

# To Test the APIs right now since there's no front end (yet)
1. After getting inside 127.0.0.1:8000/api/docs
2. You can create a user, project
3. Visit POST /api/user/create
4. Click on [Try it out]
5. Change the json to your liking
6. Click on Execute
7. Go to POST /api/user/token
8. log in with your previous credentials
9. copy the access token response
10. On the top of page click on authorize -> TokenAuth -> Type in: Token <insert token>
11. explore the api docs fully authenticated

# Features on API
# Models
1. User
2. Time Task
3. Project

User
- logs in via email
- uses token authentication

Time Task
- Logs in the time (hours, up to 2 decimal points), project, date, user
- automatically filtered to the users time task
- can filter the projects
- can filter date, include all the dates after the date on parameters
- can create a new project if no project existed yet with the name

Project
- simple string name

### CHOICES AND FEEDBACK ###
Hello! Thank you so much for the take home exam. I had to prepare a lot
for the choices I would make in this project. Firstly, I wanted to focus on the backend
of the project since this is where my expertise lean. With that in mind, I created lots
of comprehensive backend tests wherever I can and organized the app to where it seems
fit and modular. I also incorporated CI/CD pipelining with Github actions to better
simulate the automation needs. Also I made sure all the relevant API needs were met
namely: Authentication, Tests, Time Tracker, total hours and filter by date.

I really wanted to finish this project with the front end included
but the numerous front end packages ive tried seems to not function as smooth as i would
expect, especially in the docker settings. I would like to revisit this project once
I could fix the frontend design part as fixing it also benefits my skills regardless if this
project was required.

Overall thank you for the coding challenge and test. I enjoyed and learned a lot by this experience.
