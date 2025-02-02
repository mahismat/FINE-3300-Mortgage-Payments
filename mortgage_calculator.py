#FINE 3300 ASSIGNMENT 1
#mortgage calculator

def mortgage_payments(principal, rate, amortization):
    """
    Calculates different mortgage payment options.
    The parameters are as follows:
     Principal: Loan amount (float)
     Rate: Annual interest rate as percentage (float, e.g., 5.5 for 5.5%)
     Amortization: Loan term in years (int)
    The formula will return: 
     Tuple of six different payment amounts
    """

    # Converting annual rate to decimal
    rate = rate / 100  

    # Number of total payments
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52 

    # Converting the quoted interest rates to the periodic rates 
    r_monthly = (1 + rate / 2) ** (2 / 12) - 1
    r_semi_monthly = (1 + rate / 2) ** (2 / 24) - 1
    r_bi_weekly = (1 + rate / 2) ** (2 / 26) - 1
    r_weekly = (1 + rate / 2) ** (2 / 52) - 1

    # Present Value of Annuity factor: PVA = (1 - (1 + r)^-n) / r
    def calculate_payment(principal, rate, n):
        return (principal * rate) / (1 - (1 + rate) ** -n)

    # Calculating payments
    monthly = calculate_payment(principal, r_monthly, n_monthly)
    semi_monthly = calculate_payment(principal, r_semi_monthly, n_semi_monthly)
    bi_weekly = calculate_payment(principal, r_bi_weekly, n_bi_weekly)
    weekly = calculate_payment(principal, r_weekly, n_weekly)

    # Accelerated payments
    rapid_bi_weekly = monthly / 2
    rapid_weekly = monthly / 4

    return round(monthly, 2), round(semi_monthly, 2), round(bi_weekly, 2), round(weekly, 2), round(rapid_bi_weekly, 2), round(rapid_weekly, 2)

# Prompting user for input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the quoted annual interest rate (e.g., 5.5 for 5.5%): "))
amortization = int(input("Enter the amortization period (in years): "))

# Call the function
payments = mortgage_payments(principal, rate, amortization)

# Print formatted output
print("\n--- Mortgage Payment Schedule ---")
print(f"Monthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")
