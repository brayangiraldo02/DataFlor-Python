from jwt import decode, encode
pwd = 'backendcourse2023'

def create_token(data, secret=pwd):
  return encode(payload=data, key=secret, algorithm="HS256")

def validate_token(token):
  return decode(token, pwd, algorithms=["HS256"])