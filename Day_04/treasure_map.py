map1 = ["⬜", "⬜", "⬜"]
map2 = ["⬜", "⬜", "⬜"]
map3 = ["⬜", "⬜", "⬜"]
map = [map1, map2, map3]
print(f"{map1}\n{map2}\n{map3}")
position = input("Where do you want to put the treasure? ")

row = int(position[0])
column = int(position[1])

map[row-1][column-1] = "X"

print(f"{map1}\n{map2}\n{map3}")