# NewsApp
A Simple Flask News Application for Code Lou

### Features
- Connect to an external/3rd party API and read data into your app 
  - I use the NewsAPI and OpenWeather API, the latter still needs some work but is returing JSON.
- Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code 
  - You can see the use of several  functions in views.py where I use them to retrieve data via an API and return them to my templates.
- Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
  -  I do that with NewsAPI and retrieve the data in my templates through the use of empty lists. 

### Quick Start for Running App

1. Open the terminal, clone the repo, and enter project directory
  ```
  $ git clone https://github.com/terrafirmatrekker/NewsApp
  $ cd NewsApp
  ```

2. Initialize and activate a virtualenv:
Mac OS

  ```
  $ python3 -m venv venv
  $ source venv/bin/activate
  ```
Windows

  ```
  $ python -m venv env
  $ env\Scripts\activate.bat
  ```
3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
Mac OS
  ```
  $ python3 run.py
  ```
Windows
```
  $ python run.py
  ```
6. Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or whatever is mentioned in the terminal as the dev server

TODOS
- Organize views better to have seperate "components" via Blueprints. 
- Connect Read More button to the text of the full stories. 
- Create a user search that will search by topic or location. 
