# python-fastapi-app

## Command

- install package

```shell
pip install -r requirements.txt
```

- start server

```shell
uvicorn server.main:app --reload
```

- docker build

```shell
docker build -t server .
```

- docker start

```shell
docker run -dp 80:80 server
```
