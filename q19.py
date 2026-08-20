morning_session = {"Amit", "Priya", "Rahul", "Meena"}
afternoon_session = {"Rahul", "Meena", "Kiran", "Sunil"}
print("Both sessions:", morning_session & afternoon_session)
print("Only morning:", morning_session - afternoon_session)
print("Only afternoon:", afternoon_session - morning_session)
print("At least one session:", morning_session | afternoon_session)
