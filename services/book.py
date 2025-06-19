from models.book import Book as BookModel


class BookService():
  def __init__(self, db) -> None:
    self.db = db

  def get_books(self):
    result = self.db.query(BookModel).all()
    return result
  
  def get_book(self, id):
    result = self.db.query(BookModel).filter(BookModel.id == id).first()
    return result
  
  def get_book_by_category(self, category):
    result = self.db.query(BookModel).filter(BookModel.category == category).all()
    return result
  
  def create_book(self, book):
    new_book = BookModel(**book.model_dump())
    self.db.add(new_book)
    self.db.commit()
    return
  
  def update_book(self, id, book):
    result = self.db.query(BookModel).filter(BookModel.id == id).first()
    if not result:
      return None
    result.title = book.title
    result.autor = book.autor
    result.year = book.year
    result.category = book.category
    result.pages = book.pages
    self.db.commit()
    return result
  
  def delete_book(self, id):
    self.db.query(BookModel).filter(BookModel.id == id).delete()
    self.db.commit()
    return