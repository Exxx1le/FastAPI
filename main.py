from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    }
]


# @app.get('/', summary='main_page', tags=['main'])
# def root():
#     return 'hello world'

@app.get('/books', summary='get_all_books', tags=['books'])
def get_all_books():
    return books


@app.get('/books/{book_id}', summary='get_book_by_id', tags=['books'])
def get_book_by_id(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail='Book not found')


class NewBook(BaseModel):
    title: str
    author: str


@app.post('/books', summary='create_book', tags=['books'])
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"success": True, "message": "Book created successfully"}


if __name__=="__main__":
	uvicorn.run("main:app", reload=True)