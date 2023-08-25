''' =====================================================================
===========  LOOPING THROUGH A SLICE ===========================
==========================================================='''

# now, we will use loops to print the name of first three players

players = ['Rishabh', 'priyanshu', 'Manish', 'Vikash', 'Rishu']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
