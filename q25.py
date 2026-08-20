user1_friends = {"Ravi", "Kiran", "Meena", "Anil"}
user2_friends = {"Kiran", "Meena", "Sunil", "Deepa"}
mutual_friends = user1_friends & user2_friends
unique_user1 = user1_friends - user2_friends
unique_user2 = user2_friends - user1_friends
total_unique_friends = user1_friends | user2_friends
print("Mutual friends:", mutual_friends)
print("Unique to User 1:", unique_user1)
print("Unique to User 2:", unique_user2)
print("Total unique friends:", total_unique_friends)
