#1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

def myfunction(fn):
    print(fn(10))

#2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
myfunction(lambda data: data * 2)

#3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.
def my_infinite_function(fn, *args):
    for arg in args:
        print(fn(arg))


my_infinite_function(lambda data: data * 2,1,2,3,4,5)
#4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def my_infinite_function_fmt(fn, *args):
    for arg in args:
        print('{:20.2f}'.format(fn(arg)))

my_infinite_function_fmt(lambda data: data * 2,1,2,3,4,5)
