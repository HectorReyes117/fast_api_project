import database.generate_tables as generate
from fastapi import FastAPI, HTTPException, Depends
import include_routers as routers

generate.generate_tables()

app = FastAPI()

routers.include_routers(app)
