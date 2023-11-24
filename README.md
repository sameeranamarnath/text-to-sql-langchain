This generates a sql query from provided text in natural language using
gpt3.5 and runs the same on a provided database

this works with any database, i have used
imdb-movie.sqlite from kaggle (https://www.kaggle.com/code/priy998/imdb-sqlite/) as i am a movie buff

I tried implementing the same using ctransformers based local quantized llama and nsql llms, but the results proved to be inaccurate and in some situations irrelevant.

gpt3.5 isn't the best, but the sanest option at this point.

Setup:
pip install -r requirements.txt --user
streamlit is optional, but it seemed good enough for getting an interface going and hosting the solution, plus i like the way i works with github actions

:P Amar
