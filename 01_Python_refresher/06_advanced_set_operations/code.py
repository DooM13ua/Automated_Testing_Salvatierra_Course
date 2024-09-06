friend = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friend = friend.difference(abroad) # .difference - use to find difference in sets
print(local_friend)

print("---------------------------------------------")
local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad) # .union - use to unite 2 sets
print(friends)

print("---------------------------------------------")

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science) # .intersection helps to find common(shared) elements
print(both)