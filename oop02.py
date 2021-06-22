class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property # This decorator allows this method to be treated as an attribute/property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @fullname.setter # equivalent to an override of the original fullname() method and changes the access to a property access and NOT a method; and sets instance variables.
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    # Usage: del emp1.fullname