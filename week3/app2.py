TEMPLATE = """
Hello {name}. How are you doing today ?
"""

TEMPLATE2 = """
This is {p:+}, and this is {n:+}
"""

TEMPLATE3 = """
Decimal = {value:d}, HexaDecimal = {value:x}
"""

def main():
	#print(TEMPLATE.format(name="Abhinav"))
	#print(TEMPLATE2.format(p=5,n=-9))
	print(TEMPLATE3.format(value=10))


if __name__=="__main__":
	main()
