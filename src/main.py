
def main():
    num_of_loans = int(input("Number of loans: "))
    years_to_pay_off = int(input("Pay off in ___ years: "))
    auto_payment_amount = float(input("Next auto payment amount: $"))
    final_amount = 0
    most_interest_accrued = 0
    most_interest_accrued_loan_number = -1
    
    for i in range(num_of_loans):
        print("------Student loan #{}------".format(i + 1))
        current_balance = float(input("Current balance: $"))
        interest_rate = float(input(("Interest rate: ")))

        total_amount = calculate_total_amount(current_balance, interest_rate, years_to_pay_off)
        interest_accrued = calculate_interest_accrued(total_amount, current_balance)
        
        final_amount += total_amount

        if interest_accrued > most_interest_accrued:
            most_interest_accrued = interest_accrued
            most_interest_accrued_loan_number = i + 1

        print("Interest accrued: {:.2f}".format(interest_accrued))
        print("Total amount for loan {}: ${:.2f}".format(i + 1, total_amount))
    
    payment_amount = calculate_payment_amount(final_amount, years_to_pay_off, auto_payment_amount)

    print("------Final Numbers------")
    print("Final amount: ${:.2f}".format(final_amount))
    print("Pay ${:.2f} this month to loan {}.".format(payment_amount, most_interest_accrued_loan_number))

    return {
        final_amount: final_amount,
        payment_amount: payment_amount,
        most_interest_accrued: most_interest_accrued,
        most_interest_accrued_loan_number: most_interest_accrued_loan_number
    }

def calculate_total_amount(current_balance, interest_rate, years_to_pay_off):
    return current_balance * (interest_rate / 100 + 1) ** years_to_pay_off

def calculate_interest_accrued(total_amount, current_balance):
    return total_amount - current_balance

def calculate_payment_amount(final_amount, years_to_pay_off, auto_payment_amount):
    return (final_amount / years_to_pay_off / 12) - auto_payment_amount

if __name__ == "__main__":
    main()