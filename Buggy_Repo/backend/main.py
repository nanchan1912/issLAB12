from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.items import router as items_router
from routes.users import router as users_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(items_router, prefix="/items")
app.include_router(users_router, prefix="/users")
app.include_router(analytics_router, prefix="/analytics")
app.include_router(quiz_router, prefix="/quiz")

@app.get("/home")
async def get_home():
    return {"message": "Welcome to the Multi-Page FastAPI App!"}