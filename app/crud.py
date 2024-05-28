from sqlalchemy.orm import Session


from app import models
from app import schemas


def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_all_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books_by_author(db: Session, author_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Book).filter(models.Book.author_id == author_id).offset(skip).limit(limit).all()
