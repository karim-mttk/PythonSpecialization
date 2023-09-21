friends = {"Bob", "Rolf", "Ann"}
abroad = {"Bob", "Ann"}

local_friends = abroad.intersection(friends)
diff = abroad.difference(friends)
total = friends.union(abroad)

print(diff)
print(local_friends)
print(total)