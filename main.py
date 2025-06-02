# main.py
import os
from dotenv import load_dotenv


from fastapi import FastAPI
from api.main import api_router 
from db.session import engine, Base

load_dotenv()


Base.metadata.create_all(bind=engine)




def create_application() -> FastAPI:
    

    app = FastAPI(
        title="Farmers Market API",
        version="1.0.0",
        # debug=settings.DEBUG,
        openapi_url=f"/api/docs/openapi.json"

    )

    app.include_router(api_router, prefix=os.environ["API_PREFIX"])
    
    return app

app = create_application()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
