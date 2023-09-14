from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return {'msg': 'hello fast api'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "run:main",
        host='localhost',
        port=8000,
        log_level='info',
        reload=True
    )
