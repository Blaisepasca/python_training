#error and Exceptions
# person =['name', 'age']


# try:
#     a = 5/0  # This will raise a ZeroDivisionError
# except:
#     print("An error happened.")

    #or
try:
    a = 5/1  # 0r 5/0
    b = a + '25'  # This will raise a ZeroDivisionError
except ZeroDivisionError as e :
    print(e)

except TypeError as e:
    print("Type Error:", e)
else:
    print("everything is fine.")
finally:
    print("Cleaning up.")