from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from src.errors import register_all_errors
from src.middlewarre import register_middleware

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
)


register_all_errors(app)

register_middleware(app)


app.include_router(book_router, prefix=f"/api/{version}/books", tags=['book'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=['auth'])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=['reviews'])
app.include_router(tags_router, prefix=f"/api/{version}/tags", tags=['tags'])
