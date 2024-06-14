from fastapi import FastAPI, status, HTTPException, Depends
import database
from sqlalchemy.orm import Session
import auth 
from auth import current_user
from typing import Annotated

app = FastAPI()
app.include_router(auth.router)


user_dep = Annotated[dict, Depends(current_user)]
database.Base.metadata.create_all(bind = database.Engine)

@app.get("/", status_code=status.HTTP_200_OK)
def user (user : user_dep, db: Session = Depends(database.get_db)):
    if user is None: 
        raise HTTPException(status_code=401, detail= "Authendication failed")
    else:
        return{"user": user}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port= 5000)