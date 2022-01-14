from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # bucket counting
    # Time: O(m*n)
    # Space: O(m)
    mapList = dict()
    for word in strs:
        k = buildKey(word)
        if k in mapList:
            mapList[k].append(word)
        else:
            mapList[k] = [word]

    return [mapList[k] for k in mapList]


def buildKey(word: str) -> str:
    frequencyChar = [0] * 26

    for c in word:
        frequencyChar[ord(c) - ord('a')] += 1

    key = ""
    for i in range(len(frequencyChar)):
        key += str(frequencyChar[i]) + chr(i+ord('a'))

    return key



def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    # S1: Sort array m*nlog(n)
    # Time: O(m)
    mapList = dict()

    for s in strs:
        s2 = sortString(s)
        if s2 in mapList:
            mapList[s2].append(s)
        else:
            mapList[s2] = [s]

    return [mapList[k] for k in mapList]


def sortString(s: str) -> str:
    return "".join(sorted(s))


if __name__ == "__main__":
    strs = [["eat","tea","tan","ate","nat","bat"], [""], ["a"], ["aab", "abb"], ["bdddddddddd","bbbbbbbbbbc"]]

    for s in strs:
        rs = groupAnagrams(s)
        print(f"{s}")
        print(f"{rs}")
        print("=" * 10)

