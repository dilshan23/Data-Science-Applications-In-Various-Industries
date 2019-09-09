from stockoption  import StockOption

from binomialoption import BinomialEuropeanOption

eu_option = BinomialEuropeanOption(50, 50, 0.05, 0.5, 2,{"pu": 0.2, "pd": 0.2, "is_call": False})

print eu_option.price()
