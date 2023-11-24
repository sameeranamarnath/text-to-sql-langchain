This generates a sql query from provided text in natural language using
gpt3.5/4 and runs the same on a provided database uri 
powered by python, langchain, gpt3.5/4

[![Sample of the working app:](https://github.com/sameeranamarnath/text-to-sql-langchain/assets/85400557/f1c7ecfe-07ae-4598-8773-6ec2847ff6af)](
https://clipchamp.com/watch/RuGd8O4BnmA)


this works with any database, i have tried
imdb-movie.sqlite from kaggle (https://www.kaggle.com/code/priy998/imdb-sqlite/)
uri is
sqlite:///imdb-movie.sqlite

I also got the omdb movies database imported into a hosted postgres db
on Neon service [neon.tech] , the current version uses the same reference as the default uri.  (https://github.com/df7cb/omdb-postgresql was used for getting the required sql files and then imported into the db with psql command).

uri from the neon service has the following format,note the use of pooling, sslmode and endpoint same as the domain name as mentioned in neon's doc. 
postgresql+psycopg2://username:password@ep-floral-frog-97311990-pooler.ap-southeast-1.aws.neon.tech/omdb?sslmode=require&options=endpoint%3Dep%2Dfloral%2Dfrog%2D97311990%2Dpooler
"

 tried implementing the same using ctransformers based local quantized llama and nsql llms, but the results proved to be inaccurate and in some situations irrelevant.

pip install -r requirements.txt --user

streamlit is optional, seemed good enough for getting an interface going and hosting the solution

in case you want to skip using openapi paid access, u can :P
you can just use the g4f version, it will be a bit slow
Shoutout to @xtekky for  gpt4free and @Midoribin for
langchain-gpt4free


you can access a live version by running it from
codespaces 


Setup:
pip install -r requirements.txt --user

Run it:
streamlit run text-to-sql.py --server.enableCORS false --server.enableXsrfProtection false
