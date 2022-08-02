from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers_objs = []
        pos_line = 0
        for line in mat:
            soldiers_objs.append({'line': pos_line, 'count': line.count(1)})
            pos_line += 1

        soldiers_objs = sorted(soldiers_objs, key=lambda obj: obj['count'])
        soldiers_objs = soldiers_objs[0:k]

        soldiers = [obj['line'] for obj in soldiers_objs]

        return soldiers

if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]

    k = 3
    solution = Solution()
    weakest = solution.kWeakestRows(mat, k)
    print(weakest)