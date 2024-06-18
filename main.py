from fastapi import FastAPI #FastAPI로 사이트 만들기
from fastapi.responses import FileResponse #FastAPI에 Html파일 가져오기
from pydantic import BaseModel #유저에게 데이터를 받을떄 사용


app = FastAPI()

@app.get("/")
def holy():
    return FileResponse('index.html')

@app.get("/data")
def dataset():
    return 'dataset NO.1'
from pydantic import BaseModel #유저에게 데이터를 받을떄 사용

class Model(BaseModel):
    name : str
    phone : int

@app.post("/send")
def user_send_file(data : Model):
    print(data)
    return '전송완료'

# 실행 명령어 : uvicorn main:app --reload
# HTML 파일을 가져오기 위해서 사용 : from fastapi.responses import FileResponse

"""
일종의 템플릿 느낌으로 사용하면 되는 부분 [ ]으로 되어있는 부분을 수정하여 사용하면 된다.
@app.[get](["주소"])
def [작명]():
    return '[내용]'
"""