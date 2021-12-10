from typing import List

def paint_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    old_color = image[sr][sc]
    fill(image, sr, sc, len(image)-1, len(image[0])-1, new_color, old_color)
    return image

def fill(image: List[List[int]], sr: int, sc: int, r: int, c: int, new_color: int, old_color: int):
    if sr >= 0 and sr <= r and sc >=0 and sc <= c:
        if image[sr][sc] != old_color:
            return

        image[sr][sc] = new_color
        fill(image, sr+1, sc, r, c, new_color, old_color)
        fill(image, sr-1, sc, r, c, new_color, old_color)
        fill(image, sr, sc+1, r, c, new_color, old_color)
        fill(image, sr, sc-1, r, c, new_color, old_color)


if __name__ == "__main__":
    tests = [([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
          ([[0,0,0],[0,0,0]], 0, 0, 2),
          ([[1,1,1],[1,1,2],[1,2,1]], 1, 1, 2)]

    for test in tests:
        image = test[0]
        sr = test[1]
        sc = test[2]
        new_color = test[3]
        print(f"image = {image}, sr = {sr}, sc = {sc}, new_color = {new_color}")
        paint_fill(image, sr, sc, new_color)
        print(f"rs = {image}")
        print("=" * 10)
