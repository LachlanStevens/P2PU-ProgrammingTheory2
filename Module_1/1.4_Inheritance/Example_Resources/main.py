from properties import *

def main():
	# Create Farm
	my_farm = Farm()
	my_farm.property_id = 1
	my_farm.name = "Dairy Queen Farm"
	my_farm.description = "A family-run dairy farm with a friendly staff and well cared for cows"
	my_farm.selling_price = 1200000
	my_farm.surface_area = "20 acres"
	my_farm.owner_name = "Henry Ford"
	my_farm.owner_telephone = "123456789"
	my_farm.owner_email = "henry@ford.com"

	# Set as Available
	my_farm.mark_available()

	# Display Advert
	my_farm.print_advert()

if __name__ == '__main__':
	main()