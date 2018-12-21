names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append( name.lower().replace(" ","_") )

print(usernames)

'''
['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']
'''