class Libary:
    books = ['data science','math','os','java','c++','data structure','html']
    count = len(books)

    def addbook(self):
        name = input('enter book name: ')
        self.books.append(name)
        self.showbooks()

    def takebook(self):
        self.showbooks()
        name =input('enter book name: ')
        if name in self.books:
            self.books.remove(name)
            print('remaining books')
            self.showbooks()
     
    def countbooks(self):
        print(f'{self.count} books')  

    def showbooks(self):
        for book in self.books:
            print(book)

rider = Libary()
rider.addbook()
rider.takebook()




                      
