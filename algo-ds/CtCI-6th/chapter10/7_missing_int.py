"""
- Int range: -2^31 - 2 ^31
4 billion number ~ 4 * 10^9 ~ 2^2 * 2^27 = 2 ^ 29
1 G = 2 ^30 byte = 2 ^ 33 bit
Each bit represent a number, bit 1 = number present, bit 0 = missing

"""
def initData(fileName: str):
    arr = [str(i) + "\n" for i in range(0,32)]
    arr[1] = str(8) + "\n"
    f = open(fileName, "w")
    f.writelines(arr)
    f.close()


def findMissingNumber(fileName: str):
    MAX = 2**5 # Example
    range_ = int(MAX/8)
    table = bytearray([0] * range_) # each byte have 8 bit

    # Read number from input File,
    # calculate index number in table, and value table[index]
    # i = number / 8, table[i] | = 1 << (number % 8)
    # Find number index != 8 -> find offset -> missingNumber = 8 * index + offset
    f = open(fileName, "r")

    # Init table
    while True:
        number = f.readline()
        if number == "":
            break
        number = int(number)
        index = number//8
        table[index] |=  1 << (number%8)
    f.close()

    print(table)
    # Find missing number
    for i in range(len(table)):
        print(table[i])
        if table[i] != 255:
            offset = findOffset(table[i])
            number = 8 * i + offset
            print(f"number: {number}")
            print(f"offset: {offset}")
            return number

    return -1

def findOffset(number: int) -> int:
    offset = 0
    while number != 0:
        if number & 1 == 0:
            return offset

        number >>= 1
        offset += 1

    return offset



if __name__ == "__main__":
    filename = "missing_number.txt"
    initData(filename)
    missingNumber = findMissingNumber(filename)
    print(f"{missingNumber}")
