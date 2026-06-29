from fastapi import FastAPI

app = FastAPI(title="Library API - Lesson 2")

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False
    }
]

@app.get("/health")
def check_health():
    return {"message": "Library API is running"}


@app.get ("/books")
def get_available_books():
    return [book for book in books if book["is_available"]== True]

@app.get ("/books/borrowed")
def get_borrowed_books ():
    return [book for book in books if book ["is_available"] == False]