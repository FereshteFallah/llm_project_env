

### What is LLM?
LLM, or Large Language Model, refers to large language models like __GPT-3__, __GPT-4__, which can generate text, answer questions, and even engage in conversation. These models are trained on a massive amount of textual data.
### The project we want to build:
We want to create an API with Flask that, when given a piece of text, generates the continuation of the text using a language model like GPT-2. For example, if we say:

- Hello, today the weather is very...
The model could continue:

- Sunny and pleasant, and I decided to go to the park.

### Project Steps:
- 1️⃣ __Create a Virtual Environment__
  *  The virtual environment helps us install Python libraries only for this project without affecting other projects.

Open CMD or Terminal and run the following commands:
```bach
# Create a virtual environment
python -m venv llm_project_env
```
 Activate the virtual environment
```bach
# For Windows:
llm_project_env\Scripts\activate    
```
```bach
# For macOS or Linux:
source llm_project_env/bin/activate
```
- 2️⃣ __Install Flask and Transformers__

  * In the same virtual environment, install the required libraries:
```bach
pip install flask transformers torch
```
- 3️⃣ __Create the app.py file for Flask code__

  
  * Now, create a Python file named app.py   in the main project folder.
- 4️⃣ __Write the code to receive text and generate its continuation__  
  * for test LLM you can use postman,url, and python.here we write the python test_request.py file.
- 5️⃣ __Run the application and test the API__
 ```bach
python app.py
  ```
If everything is set up correctly, you should see:
-  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

then run :
 ```bach
python test_request.py
  ```

