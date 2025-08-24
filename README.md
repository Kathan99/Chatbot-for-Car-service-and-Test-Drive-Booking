# Chatbot-for-Car-service-and-Test-Drive-Booking
 
*********************************************** Installing RASA and SPACY pipeline. ******************************************************************

1)Visual Studio C++ build tool is required to download in Windows for installing the Rasa. Below is the link where you can install the C++ build tools
  
  https://visualstudio.microsoft.com/visual-cpp-build-tools/

2) Create a Virtual environment in Anaconda Command prompt with Python Version >=3.6.0 and write following command

  ->pip install rasa-x --extra-index-url https://pypi.rasa.com/simple

3) After installing Rasa we have to install Spacy pipeline. Run following commands

   -> pip install rasa_nlu[spacy]
   -> python -m spacy download en_core_web_md
   -> python -m spacy link en_core_web_md en

4) Install Flask by running following command
 
   -> pip install Flask


************************************************** Installing Django REST *************************************************************************

1) Open the same virtual environment which you've created for installing RASA. Install Django and Django Rest
   by following command in Virtual environment

  -> pip install Django
  -> pip install djangorestframework

2) Make migrations by writing 'python manage.py makemigrations' and 'python manage.py migrate'

* Installing Duckling Server for extracting Date and Time Information

1) Download the source code of Duckling server from https://github.com/facebook/duckling

2) Install Haskell Stack from https://www.fpcomplete.com/haskell/get-started/

3) Now go the downloaded Source code folder and write following two commands in Anaconda command prompt.

  -> stack build
  -> stack exec duckling-example-exe

**************************************************** Installing Docker Desktop ******************************************************************

1) Prerequisites for installing Docker Toolbox

  -> 64-bit Windows 7 (or higher)
  -> Virtualization enabled

2) Install Docker Desktop from https://www.docker.com/products/docker-desktop

3) After installing open Docker Quickstart Terminal, Click near the $ symbol to activate the terminal. 
   Write 'docker run hello-world' and if you get confirmation message, installation is successful.

4) To run the Duckling server, write 'docker pull rasa/duckling'. It will create an image of Duckling server.

****************************************************** How to run the project? ******************************************************************

1) Open 5 Anaconda Command Prompt and go the virtual environment created for Rasa installation. 

2) Write 'python manage.py runserver' in one the prompt. This will run the Django Rest Server.

3) Open Docker Quickstart Terminal. Wait for it to activate. After activation, write 'docker run -p 8000:8000 rasa/duckling' in Duckling server's 
  source code folder which was downloaded from Github.

4) Now write 'rasa run actions' in one of the Anaconda command prompt. Action server will run after few seconds.

5) write 'rasa run -m models --enable-api --cors "*"' in Anaconda command prompt. Server will be up and running. And go the Chatbot Widget's
   index.html page to use the chatbot.
