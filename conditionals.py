# KC conditional notes



# boolean -> true or false

# passing = True
# passing = False

time = 1416
day = "tuesday"


if time < 1200 and time > 500:
    print("good morning")
    if day != "saturday" or day != "sunday":
         print("are  you ready for school????")
elif time < 1700:
      print("good afternoon!")
      if day != "saturday" or day != "sunday":
           print("how was school??????")
elif time < 2000:
     print("good evening")
else:
     print("good night")

print("code is done")






# logical operators                                     comparison operators
# and --> both conditionals true                    <   less than
# or ---> one conditonal true                       >   greater than
# not ---> checks if false                          == equal to
#                                                   <= less than or equal to
#                                                   >= greater than or equal to
#                                                   != not equal to