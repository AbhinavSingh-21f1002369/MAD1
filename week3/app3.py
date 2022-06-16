from jinja2 import Template

TEMPLATE = """Hello {{ name }}, how are you doing today ?"""

def main():
	template = Template(TEMPLATE)
	print(template.render(name="Abhinav"))

if __name__ == "__main__":
	main()
