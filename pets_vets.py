from Pets import*
from vets import*

dog1=dog('Jamie','Oliver','23')
dog2=dog('Sammy', 'Dean', '10')
dog3=dog('Deku','Tusinori', '12')

vet1=vets('Drogo','234','Drogo@.com','Dog street','Dogtor')

vet2=vets('Arky', '777','Arky@epic', 'Fight Street','Arkygeon')

print (vet1.see_patient('cured'), dog1.name)
print(vet2.see_patient('not cured'),',', dog2.owner)


