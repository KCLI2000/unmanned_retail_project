#This py file is used to create customer object
class Customer(object):
	"""Customer Class"""
	def __init__(self, Id, Purchase_history,Cart):
		super(Customer, self).__init__()
		self.Id=Id
		self.Purchase_history=Purchase_history
		self.Cart=Cart

	def myprint(self):
		print("Id is",self.Id)
		print("Purchase history is",self.Purchase_history)
		print("Cart is",self.Cart)
	
	def Reset(self):
		self.Id=-1
		self.Purchase_history={}
		self.Cart={}
		print("This Infromation is Resetted")    

	def Add_to_history(self,New_record):    
		for new_item in New_record:
			if new_item in self.Purchase_history:
				self.Purchase_history[new_item]+=New_record[new_item]
			else:
				self.Purchase_history[new_item]=1

	def Del_from_history(self,Del_Record):
		for del_item in Del_Record:
			if del_item in self.Purchase_history:
				self.Purchase_history.pop(del_item)


