"""
11. Inheritance

    11.1. Implement the following class hierarchy using Python: A publication
          can be either a book or a magazine. Each publication has a name. Each
          book also has an author and a page count, whereas each magazine has a
          chief editor. Also write the required initializers to both classes.
          Create a print_information method to both subclasses for printing out
          all information of the publication in question. In the main program,
          create publications Donald Duck (chief editor Aki Hyyppä) and
          Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all
          information of both publications using the methods you implemented.
"""


class Publication:

    def __init__(self, name):
        self.name = name

    def get(self, prop):
        return getattr(self, prop, '')

    def info(self):
        return ['name']

    def print_information(self):
        lines = [f'{self.__class__.__name__}: ']
        for item in self.info():
            lines.append(f"    {item.replace('_', ' ').title()}:  {self.get(item)}")
        print('\n'.join(lines))


class Book(Publication):

    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def info(self):
        return ['name', 'author', 'pages']


class Magazine(Publication):

    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def info(self):
        return ['name', 'chief_editor']


if __name__ == '__main__':
    magazine = Magazine('Donald Duck', 'Aki Hyyppä')
    book = Book('Compartment No. 6', 'Rosa Liksom', 192)
    magazine.print_information()
    print()
    book.print_information()
