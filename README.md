# Realworld Example - UtilMeta

* Powered By: [UtilMeta](https://utilmeta.com/py)

<img src="https://utilmeta.com/img/logo-main.png" href="https://utilmeta.com" alt="drawing" width="50"/> <strong style="font-size: 24px">UtilMeta </strong> | Progressive meta framework for API development in Python

* Implemented [API Specs](https://realworld-docs.netlify.app/docs/specs/backend-specs/endpoints)
* Backend Framwork: [UtilMeta](https://github.com/utilmeta/utilmeta-py)
* Backend Example of [Realworld](https://github.com/gothinkster/realworld)
* Author: [@voidZXL](https://github.com/voidZXL)
* License: MIT

##  Installation

```
pip install -r requirements
```
## Env Vars

file in `conduit/config/env.py` shows the env var required for this project
* `CONDUIT_PRODUCTION`: optional, whether if this project is in production mode
* `CONDUIT_JWT_sECRET_KEY`: **required**, configure the JWT secret key for this project
* `CONDUIT_DJANGO_SECRET_KEY`: optional, configure Django secret key for this project

Before you run the server, please configure these env vars

## Database Migration

Migrate database before run the server
```shell
cd conduit
meta migrate
```

## Run
```shell
cd conduit
meta run
```
or
```shell
cd conduit
python main.py
```

## OpenAPI Docs

When the server is running, view http://127.0.0.1:8000/api/docs to get the OpenAPI json docs of this project auto generated by UtilMeta

## Tutorials
There is a tutorial to build this project step by step, you can find it in

* [Realworld Blog Tutorials](https://docs.utilmeta.com/py/en/tutorials/realworld-blog/)
* [Realworld 博客项目教程](https://docs.utilmeta.com/py/zh/tutorials/realworld-blog/)
