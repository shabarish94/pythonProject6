# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def decoratormethod(func):
    def innerf(num1,num2):
        func(num1,num2)
        func(num1,num2)
    return innerf
@decoratormethod
def multiply(num1,num2):
    print(num1*num2)

multiply(5,6)