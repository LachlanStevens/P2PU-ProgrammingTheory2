class Property:

    property_id = 0
    name = ""
    description = ""
    address = ""
    owner_name = ""
    owner_telephone = ""
    owner_email = ""
    selling_price = ""
    surface_area = ""
    status = ""

    def __init__(self):
        self.property_id = 1

    def print_advert(self):
        if self.status == "Available":
            print "Property: P-%d - %s for $%d" % (self.property_id, self.name, self.selling_price)
            print self.description
            print "Surface Area: %s" % (self.surface_area)
            print "Owner: %s (%s)" % (self.owner_name, self.owner_telephone)
            print "Contact the owner at %s" % (self.owner_email)
        else:
            print "Sold!"

    def mark_sold(self):
        self.status = "Sold"

    def mark_available(self):
        self.status = "Available"

class Farm(Property):

    plot_number = ""
    land_area = 0
    farm_type = ""
    num_employees = 0
    num_buildings = 0
    has_dam = False
    has_stables = False
    has_greenhouse = False
    has_orchard = False