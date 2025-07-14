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



class ValueTooHighError(Exception):
    pass

class valueTooSmallError(Exception):
    def _init_(self,message,value):
        self.message = message
        self.value = value
    


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high!")
    if x < 5:
        raise valueTooSmallError("Value is too small!", x)
  

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except valueTooSmallError as e:
    print(e.message ,e.value)