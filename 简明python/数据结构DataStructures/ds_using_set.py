bri = set (['brazil', 'russia', 'india'])
if 'india' in bri:
    print('india in bri')

if 'usa' not in bri:
    print('usa not in bri')

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))

bri.remove('russia')
print(bri & bric) #intersection