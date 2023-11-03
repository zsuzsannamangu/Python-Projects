#Creating classes that inherit from another class:

#Parent class:

class Content:
    title = ''
    code = '1234567'
    branch = 'Kenton'

#Child classes of Content:
    #the child classes will have the attributes of the Content class
    #but will also have their own attributes

class Book(Content):
    author: ''
    publisher: ''

class DVD(Content):
    director: ''
    producer: ''
