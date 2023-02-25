buffer = str(input("Ввидите последовательность скобок:\n"))
def buffer_controller(buffer):
    counter = 0
    for item in buffer:
        if buffer == "(":
            counter +=1
            if buffer == ")":
                counter -=1
                if counter < 0:
                    return False
                if counter > 0:
                    return False
                if counter == 0:
                    return True
