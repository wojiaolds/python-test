import pandas as pd

print ("display.max_rows = ", pd.get_option("display.max_rows"))
print ("display.max_columns = ", pd.get_option("display.max_columns"))

pd.set_option("display.max_rows",80)
print ("after set display.max_rows = ", pd.get_option("display.max_rows"))

pd.set_option("display.max_columns",32)
print ("after set display.max_columns = ", pd.get_option("display.max_columns"))


pd.describe_option("display.max_rows")




