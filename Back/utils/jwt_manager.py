'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the JWT manager.
  It is used to create and validate JWT tokens.
'''
# Importing libraries
from jwt import decode, encode
# Adding the secret key
pwd = 'backendcourse2023'

# Create the token functions
def create_token(data, secret=pwd):
  return encode(payload=data, key=secret, algorithm="HS256")

# Validate the token functions
def validate_token(token):
  return decode(token, pwd, algorithms=["HS256"])