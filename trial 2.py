print('hellow world')
print('this amazing pycharm programmining formy project')

# Basic fundamentals of python
#First Program
print("This is Agumase!!")
print("Hello, World!\nWhat should I do?")#\n, or newline in printing makes the strings after the \n in a new line,\n\n(double)

#Data-Type(integer, float, string, boolean and complex
#int
a=10
type(a)
a=10.5#float
type(a)
#str
a="agumase"#str
type(a)
#bool
a=True
type(a)
# complex
a=3+4j
type(a)
##Arithmetic Operators +,-,*,/
a=10
b=20
# add
a+b
a-b # sub
a*b#multip
a/b#div
14//3#Integer Division 14 // 3 == 4
14 % 3 #Remainder (modulo) 14 % 3 ==2
# This is not quite true outside of USA
# and is based on my dim memories of my younger years
print("Firstish Grade")

print("2 + 4 =", 2 + 4)#2 + 4 = 6
print("243 - 23 =", 243 - 23)#243 - 23 = 220
print("12 * 4 =", 12 * 4)#12 * 4 = 48
print("12 / 3 =", 12 / 3)#12 / 3 = 4.0
print("13 / 3 =", 13 // 3, "R", 13 % 3)#13 / 3 = 4 R 1
print("123.56 - 62.12 =", 123.56 - 62.12)#123.56 - 62.12 = 61.440000000000005
print("(4 + 3) * 2 =", (4 + 3) * 2)#(4 + 3) * 2 = 14
print("4 + 3 * 2 =", 4 + 3 * 2)#4 + 3 * 2 = 10
print("3 ** 2 =", 3 ** 2) #3 ** 2 = 9
#########################################

integer = int(input("Type in an integer: "))#Type in an integer:
text = input("Type in a string: ")#Type in a string:
print("number =", number)#number = 5
print("number is a", type(number))
print("number * 2 =", number * 2)
print("integer =", integer)
print("integer is a", type(integer))
print("integer * 2 =", integer * 2)
print("text =", text)
print("text is a", type(text))
print("text * 2 =", text * 2)
#####################################
## Relational Operators  ==, <,>,!=
a<b
a>b
a!=b
a==b
#Logical Operators and(&),or(|)
a=True
b=False
a&b
b&a
a&a
b&b
a|b
b|a
a|a
b|b
#Strings
my_string="My name is agumase"
my_string[0] # first index
my_string[-1]# last index
my_string[3-7]# index -4
my_string[3:7]# index 3 to 7 excluding 7 i.e 'name'
len(my_string)# to see the length of all
my_string.lower()# to change all to lower case
my_string.upper()# to change all to upper case
my_string.replace('y','a')# change y to a i.e My=Ma
new_string = "hello hello world"
new_string.count("hello")# to see repeated strings

# Rate_times.py
# This program calculates rate and distance problems
print("Input a rate and a distance")
rate = float(input("Rate: "))#5
distance = float(input("Distance: "))#10
time=(distance/ rate)
print("Time:", time)#2.0
#####

#Area.py
# This program calculates the perimeter and area of a rectangle
print("Calculate information about a rectangle")
length = float(input("Length: "))#4
width = float(input("Width: "))#let's take width 3
Perimeter=(2 * length + 2 * width)
print("Area:", length * width)#12.0
print("Perimeter:",Perimeter)#14.0
#Temperature.py

# This program converts Fahrenheit to Celsius
fahr_temp = float(input("Fahrenheit temperature: "))# 40
celc_temp = (fahr_temp - 32.0) *( 5.0 / 9.0)
print("Celsius temperature:", celc_temp)# the result will be 4.44444
##########################################
##While loops
a = 0  # FIRST, set the initial value of the variable a to 0(zero).
while a < 10:  # While the value of the variable a is less than 10 do the following:
    a = a + 1  # Increase the value of the variable a by 1, as in: a = a + 1!
    print(a)  # Print to screen what the present value of the variable a is.
              # REPEAT! until the value of the variable a is equal to 9!? See note.
    # NOTE:
    # The value of the variable a will increase by 1
    # with each repeat, or loop of the 'while statement BLOCK'.
    # e.g. a = 1 then a = 2 then a = 3 etc. until a = 9 then...
    # the code will finish adding 1 to a (now a = 10), printing the
    # result, and then exiting the 'while statement BLOCK'.
    #              --
    # While a < 10: |
    #     a = a + 1 |<--[ The while statement BLOCK ]
    #     print (a) |
    #              --
#conditional statment im python
x=1

if x>2:
    print ('case1!')
if x<=2:
    print ('case2')

i = 100
while(i<=200):
    print(i)
i+=20:



s1={1,2,3,4}
s2={4,5,6}
print(s1&s2)