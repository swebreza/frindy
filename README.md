# frindy

first of all we create a virtual environment for our project so that our current project would not affect pre install packagers or libraries.
open windows shell or cmd and enter

` pip install pipenv `


after that we need to go top project file and open terminal. Now we need to create/run the virtual environment. To do that type following command into the terminal

` pipenv shell `


A virtual environment starts running

In-order to handel Images file into our virtual environment we meed to have package named as pillow.
to install that package type

` pipenv install Pillow `


Into our virtual environment we meed to have install Django

` pipenv install django `


To run the application. Type the following command. make sure that ' pipenv shell ' is up and running

` py manage.py runserver `
