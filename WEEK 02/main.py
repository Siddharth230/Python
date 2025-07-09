ram_bank_balance = 100000
# Ram's bank balance, note that it is positive

ram_loan = 500000
# Ram's loan, this is to be returned by him and hence will count as negative

lakshman_bank_balance = 2000000
# Lakshman's bank balance, note that it is positive

lakshman_loan = 1000000
# Lakshman's loan, this is to be returned by him and hence will count as negative


net_income = ram_bank_balance + lakshman_bank_balance
# It is the total bank balance of the two brother's

net_liability = ram_loan + lakshman_loan
# It is the total loan of the brother's

final_value = net_income - net_liability
# Family's final money

print(f"SO the family has {final_value}")
