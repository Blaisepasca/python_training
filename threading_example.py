# from threading import Thread
# import time

# # database_value = 0

# # def increase():
# #     global database_value
# #     # copier la valeur actuelle dans une variable locale
# #     local_copy = database_value
# #     local_copy += 1
# #     time.sleep(0.1)
# #     database_value = local_copy

# # if __name__ == "__main__":

# #     print('start value:', database_value)

# #     Thread1 = Thread(target=increase)
# #     Thread2 = Thread(target=increase)

# #     Thread1.start()
# #     Thread2.start()

# #     Thread1.join()
# #     Thread2.join()

# #     print('end value:', database_value)

# def add_100(number):
#     print('start add 100')
#     time.sleep(0.01)
#     number.value += 1
# if __name__ == "__main__":
#     shared_number = value('i', 0)
#     print('number at beginning:', shared_number.value)

# p1 = process(target=add_100, args=(shared_number,))
# p2 = process(target=add_100, args=(shared_number,))

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# print('number at end:', shared_number.value)

