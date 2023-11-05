from fastapi import FastAPI
import schemas

app= FastAPI()



@app.post('/blog')
def create(request:schemas.Blog):
  # print(type(request))
  return request