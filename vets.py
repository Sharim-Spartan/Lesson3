
class vets():
    def __init__(self, name, phone, email, location, speciality):
        self.name=name
        self.phone=phone
        self.email=email
        self.location=location
        self.speciality=speciality

    def see_patient(self, status):
        if status=='cured':
            return ('This patient is cured, off you go')
        elif status=='not cured':
            return ('This boi got rekted')
        else:
            return ('Do you even have a dog?')

