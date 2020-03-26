alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#dictionaries stores information about an object and as much information needed about that object
#dictionaries use key-value pairs
new_points = alien_0['points']
print(f"You just earned {new_points} points")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = 10
print(alien_1)

favorite_languages = {
    'mason': 'python',
    'sothea': 'javascript'
    }
print(favorite_languages)
user_0 = {
    'username': 'enfermi',
    'f_name': 'mason',
    'l_name': 'eastman'
    }
for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print()
friends = ['sothea', 'mason']
for key in favorite_languages: #loop through keys, deafulted to keys
    print(key.title())
    if key in friends:
         language = favorite_languages[key].title()
         print(f"\t{name.title()}, I see you love {language}")
print()
alien_0 = {'color': "green", 'points': 5}
alien_1 = {'color': "yellow", 'points': 10}
alien_2 = {'color': "red", 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print()

aliens = []
#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print(f"Total number of aliens: {len(aliens)}")

