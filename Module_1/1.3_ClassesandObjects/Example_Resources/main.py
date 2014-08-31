from page import Page
from page import SomeClassName

def main():

	first = Page(1)
	
	first.title = "The first Page"
	first.add_content("Welcome to the first page. Here is a bunch of content")
	
	print first.get_page_number()
	print first.get_content()

	SomeClassName.my_static_function("Test")

if __name__ == '__main__':
	main()