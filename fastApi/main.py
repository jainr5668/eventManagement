from routes import Routes
from fastapi import FastAPI


routes = Routes()
app = FastAPI()
app.include_router(routes.router)
