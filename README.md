# Software-Engineering-Project
Our group is creating a one stop spot for all Florida Poly students

To Run:
Clone this repository
Download CanvasAPI https://github.com/ucfopen/canvasapi
Install Flask: pip install flask
Run 'canvas_to_web.py'
Go to http://0.0.0.0:5000/


All code was hosted on Github for version control and to make collaboration easy. The application was stored under /Application/Android/. The code is organized by pages of the app. Everything is in one directory with data separated from the code. The website is split into a few sections. Initially there is the python file ‘canvas_to_web’ that runs the website. The python reaches into the templates folder for the html files. The static folder hosts the CSS and JS files. 
The code we did was our HTML and our CSS. The component 1 CSS file is the CSS of our button and the other CSS file was the rest of our sites CSS. the libraries we used were modernizr and polyfills, these just make it so we do not need to worry about differences between web browsers and different devices like mobile. We developed the canvas_to_web python file. Dependencies for the it to go live are listed below:
Flask: A python library for python web servers.
CanvasAPI: An API wrapper that gets information from Canvas.
Datetime: Outputs current date
Nginx: Popular open source web host for UNIX
