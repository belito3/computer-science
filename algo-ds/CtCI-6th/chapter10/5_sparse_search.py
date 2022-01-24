from typing import List

def search(words: List[str], target=""):
    tail = len(words) - 1
    left, right = 0, tail

    while left <= right:
        mid = (left + right) // 2
        if words[mid] == "":
            low, high = mid - 1, mid + 1
            while low >= 0 or high <= tail:
                if low >=0 and words[low] != "":
                    mid = low
                    break

                if high <= tail and words[high] != "":
                    mid = high
                    break
                low -= 1
                high += 1

        if words[mid] == target:
            return mid
        elif words[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":

    inputs = [[], ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]]
    targets = ["a", "ball"]

    for i in range(len(inputs)):
        rs = search(inputs[i], targets[i])
        print(f"input={inputs[i]}, target = {targets[i]}, rs = {rs}")
