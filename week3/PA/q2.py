from string import Template
statement = Template("Today is $today and tomorrow is $tomorrow.")
out = statement.substitute(today = "Monday")
print(out)
