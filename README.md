This generates a sql query from provided text in natural language using
gpt3.5 and runs the same on a provided database

this works with any database, i have tried
imdb-movie.sqlite from kaggle (https://www.kaggle.com/code/priy998/imdb-sqlite/)
as i am a movie buff
uri is
sqlite:////imdb-movie.sqlite

I also got the omdb movies database imported into a postgres db
on vercel via psql and the current version uses the same as a reference
uri is
postgres://default:GT4dg3OemzlA@ep-curly-violet-36509009.us-east-1.postgres.vercel-storage.com:5432/verceldb

I tried implementing the same using ctransformers based local quantized llama and nsql llms, but the results proved to be inaccurate and in some situations irrelevant.

gpt3.5 isn't the best, but the sanest option at this point.

Setup:
pip install -r requirements.txt --user
streamlit is optional, but it seemed good enough for getting an interface going and hosting the solution, plus i like the way i works with github actions

:P Amar

you can access a live version at
https://text-to-sql-langchain-amar.streamlit.app/
