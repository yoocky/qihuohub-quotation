import sys
import easyquotation
stock_list = sys.argv
del stock_list[0]
quotation = easyquotation.use("ctp")
data = quotation.real(stock_list)
print(data)

