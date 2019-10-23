ua_generator.py is meant to play the role of the flask server. This program repeatedly takes a user-agent string from an array containing 
five user-agent strings. This ua is then sent to an AWS FIFO queue.

parsing_engine.py grabs the ua from the AWS queue, parses it (assuming the ua hash is not in the hash database), and sends the resulting JSON 
to a Mongo database, also hosted on an AWS server. This code is now replaced by the aws_lambda/lambda_function.py