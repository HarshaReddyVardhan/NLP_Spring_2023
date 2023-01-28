import tags
import currency
import date
import phone_numbers

input_data = open('input.txt','r',encoding='utf-8')
for x in input_data:
    print(x)
    if not tags.isTagPresent(x):
        phone_numbers.mobileNumber(x)
        currency.isValidCurrency(x)
        date.isValidDate(x)
    