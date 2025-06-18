from fastapi import Path, Query, Depends, APIRouter
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.book import Book
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import JWTBearer
from services.book import BookService
from schema.book import Book

book_router = APIRouter()

@book_router.get('/', tags=['Home'])
def message():
    return 'Hello World'

@book_router.get('/books', tags=['Books'], response_model = List[Book], status_code = 200, dependencies = [Depends(JWTBearer())])
def get_books() -> List[Book]:
    db = Session()
    result = BookService(db).get_books()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@book_router.get('/books/{id}', tags=['Books'], response_model = Book, status_code = 200, dependencies = [Depends(JWTBearer())])
def get_book(id:int = Path(ge=1, le=2000)) -> Book:
    db = Session()
    result = BookService(db).get_book(id)
    if not result:
        return JSONResponse(status_code = 404, content = {"message": "libro no encontrado"})
    #for item in books:
     #   if item["id"] == id:
      #      return JSONResponse(content = item)
    return JSONResponse(status_code = 404, content = jsonable_encoder(result))

@book_router.get('/book/', tags=['Books'], response_model = List[Book], dependencies = [Depends(JWTBearer())])
def get_book_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Book]:
    db = Session()
    result = BookService(db).get_book_by_category(category)
    if not result:
        return JSONResponse(status_code = 404, content = {"message": "No se encontraron libros en esta categoria"})
    return JSONResponse(content = jsonable_encoder(result))

@book_router.post('/books', tags=['Books'], response_model = dict, status_code = 201, dependencies = [Depends(JWTBearer())])
def create_book(book: Book) -> dict:
    db = Session()
    BookService(db).create_book(book)
    return JSONResponse(content = {"message": "Se ha registrado el libro"})

@book_router.put('/books/{id}', tags=['Books'], response_model = dict, dependencies = [Depends(JWTBearer())])
def update_book(id:int, book: Book) -> dict:
    db = Session()
    result = BookService(db).get_book(id)
    if not result:
        return JSONResponse(status_code = 404, content = {"message": "No se encontraron libros en esta categoria"})
    BookService(db).update_book(id, book)
    return JSONResponse(status_code=200, content= {"message": "Se ha actualizado el libro"})

@book_router.delete('/books/{id}', tags=['Books'], response_model = dict, dependencies = [Depends(JWTBearer())])
def delete_book(id:int) -> dict:
    db = Session()
    result = BookService(db).get_book(id)
    if not result:
        return JSONResponse(status_code = 404, content = {"message": "No se encontraron libros en esta categoria"})
    BookService(db).delete_book(id)
    return JSONResponse(status_code=200, content= {"message": "Se ha eliminado el libro"})

#1 38