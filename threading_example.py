from threading import Thread
import time

database_value = 0

def increase():
    global database_value
    # copier la valeur actuelle dans une variable locale
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy

if __name__ == "__main__":

    print('start value:', database_value)

    Thread1 = Thread(target=increase)
    Thread2 = Thread(target=increase)

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print('end value:', database_value)
