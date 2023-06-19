
def main():
    num_of_loans = int(input("Number of loans: "))
    years_to_pay_off = int(input("Pay off in ___ years: "))
    final_amount = 0
    
    for i in range(num_of_loans):
        print("------Student loan #{}------".format(i + 1))
        current_balance = float(input("Current balance: "))
        interest_rate = float(input(("Interest rate: ")))

        total_amount = current_balance * ((interest_rate / 100 + 1) ** years_to_pay_off)
        final_amount += total_amount

        print("Total amount for loan {}: {}".format(i, total_amount))
    
    print("Final amount: {}".format(final_amount))

if __name__ == "__main__":
    main()