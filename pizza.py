art_friends={"rolf", "anne"}
science_friends={"jen","charlie"}
art_friends.add("jen")
art_but_not_science = art_friends.difference(science_friends)
art_and_science = art_friends.intersection(science_friends)
print (art_friends)