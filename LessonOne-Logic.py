# Here we will learn about basic logic and what theses logical statements can do 
# in a basid sense. But first we will want to start you off as every new programmer
# should learning something new! A hello world program!

# First off make sure you are doing these things in your own files as this will provide
# as a templete.

print("Hellow World")

# Now the first thing we will learn is the if statment this is used when needing to logically
# compare multiple things this is in compination with loops and various other things can be very powerful

i = 0
compare = 1
if(compare == 0):
    print("compare is 0")
elif(i == 0):
    print("i = 0")
else:
    print("nothing = nothing")
    

# If you are fimilar with other programming lang. you will notice the lack of ; that is generally
# present. Python is different it does not care about EOLC (end of line chars) that the ; represents
# another thing is when looking at an if block you will generally look for the code to be enclosed by
# {} however python does this by its indention. so a block of code that you want inside an if statement
# will all be indented to the same level.

# Now we will learn about the different loops particularly about the while and for loop
# These will almost always be uesed the most in when doing any type of itterative process. Something
# to note about python is it is all object oriented (OOP). If you are new to programming you might not know
# what that means which is ok, just know it makes life easy. Another thing to note is that when it comes
# to these types of loops there are some better than others in certain circumstances, for instance,
# while loops are better when you dont know when the loop is going to end ie) reading a file of some var length
# reading a DB that you dont have access to look at. For loops are best used when you know exactly the length
# of the itterative loop. So if you are reading an excel sheet that has exactly 12 cells yo ucould use a for loop
# to itterate to 12 etc... Here will be some examples:

i = 0
print("While loop")
while(i < 10):
    print(i)
    i = i + 1


index = [1,2,3,4,5,6,7]
print("for loop")
for x in index:
    print(x)



# Some things you should take note of in this are what is actually printed to the screen for each loop given the indexes
# also notice the syntax of the for loop the 'in' and understand how that works. This is the OOP side of python which will
# come in handy. Also notice how everything at the same indention level is ran as the same block as talked about above.
# The index var in this case index = [] is called a list.

# Now time for you to try. For this exercise create a list with five words dog, cat, fox, bird, wolf. Then iterate through the
# list and match the word fox. When you match the word fox print out "I found it!"

index = ["dog","cat","fox","bird","wolf"]
for x in index:
    if (x == "fox"):
        print("I found it!")
