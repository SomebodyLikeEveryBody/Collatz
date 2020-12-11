import sys

def collatz(p_start, p_level):
    current_nb = int(p_start)
    got_nb = []
    for i in range(0, int(p_level)):
        got_nb.append(current_nb)

        if (current_nb % 2 == 0):
            current_nb //= 2
        else:
            current_nb = 3 * current_nb + 1

        if (current_nb in got_nb):
            got_nb.append(current_nb)
            break

    found = False
    last_nb = got_nb[-1]
    for number in got_nb:
        if (found == False):
            if (number == last_nb):
                found = True
                print("{0}-----|".format(number))
            else:
                print("{0}".format(number))
        else:
            if (number == last_nb):
                print("{0}-----|".format(number))
            else:
                print("{0}     |".format(number))

    print("max value: {0}".format(max(got_nb)))
    
if __name__ == "__main__":
    if (len(sys.argv) == 3):
        collatz(sys.argv[1], sys.argv[2])
