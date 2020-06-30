# Class
class Book(object):
  def __init__(self, book_id, book_name, book_store_count):
    self.book_id = book_id
    self.book_name = book_name
    self.book_store_count = book_store_count

  def __add__(self, book):
    return self.book_store_count + book.book_store_count

python_intro_book = Book(1, 'python入门', 100)
ml_intro_book = Book(2, '机器学习入门', 200)

sales_count = python_intro_book + ml_intro_book
print(sales_count)