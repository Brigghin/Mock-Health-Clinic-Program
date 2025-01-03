from clinic.patient_record import PatientRecord

class Patient:
	def __init__(self, phn, name, birth_date, phone, email, address, autosave=False):
		self.phn = phn
		self.name = name
		self.birth_date = birth_date
		self.phone = phone
		self.email = email
		self.address = address
		self.autosave = autosave
		
		self.record = PatientRecord(phn, autosave) # Give each patient their own PatientRecord()

	def __str__(self) -> str:
		return "Patient(%i, %s, %s, %s, %s, %s)" % (self.phn, self.name, self.birth_date, self.phone, self.email, self.address)

	def __eq__ (self, other):
		return isinstance(other, Patient) and self.phn == other.phn \
			and self.name == other.name and self.birth_date == other.birth_date \
			and self.phone == other.phone and self.email == other.email \
			and self.address == other.address