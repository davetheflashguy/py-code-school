print 5 < 10
print 5 > 10

print 5 == 10

name = 'Pam'

print name == 'Pam'
print name == 'Jim'

print name != 'Dave'

is_raining = True # Boolean values have capitalized first letters

print is_raining

num_players = 4
players_required = 3
weekday = 'Monday'
if num_players > 2:
    print 'We have more then 2 players!'

if num_players > 10:
    print 'We have too many players!'
print 'This happens anyway'

if num_players < players_required:
    print 'Ready to play'
elif weekday == 'Monday':
    print 'Come back on Friday!'
else :
    print 'We need more players'


if num_players >= 4 or weekday == 'Monday':
    print "Game on!"

if num_players >= 4 and weekday == 'Tuesday':
    print "Game on!"