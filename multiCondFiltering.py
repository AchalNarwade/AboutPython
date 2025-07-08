users = {
    'Hans': 'active',
    'Raveena': 'inactive',
    'Sonam': 'inactive',
    'Harshita': 'active',
    'Heena': 'inactive',
    'Ishan': 'active'
}

# Words to search for
keywords = ['an', 'sh', 'on']

# Filtered result
filtered_users = {}

for user, status in users.items():
    if status == 'active' and any(word in user for word in keywords):
        filtered_users[user] = status

print(filtered_users)



