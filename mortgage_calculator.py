#FINE 3300 ASSIGNMENT 1
#mortgage calculator

def mortgage_payments(principal, rate, amortization):
    """
    This function calculates different mortgage payment options.

    :param principal: Loan amount (float)
    :param rate: Annual quoted interest rate as a percentage (float, e.g., 5.5 for 5.5%)
    :param amortization: Loan term in years (int)
    :return: Tuple of six different payment amounts
    """

    # Convert annual rate to decimal
    rate = rate / 100  

    # Number of total payments
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52

    # Convert the quoted interest rate to the periodic rate for each schedule
    r_monthly = (1 + rate / 2) ** (2 / 12) - 1
    r_semi_monthly = (1 + rate / 2) ** (2 / 24) - 1
    r_bi_weekly = (1 + rate / 2) ** (2 / 26) - 1
    r_weekly = (1 + rate / 2) ** (2 / 52) - 1

    # Present Value of Annuity formula: PVA = (1 - (1 + r)^-n) / r
    def calculate_payment(principal, rate, n):
        return (principal * rate) / (1 - (1 + rate) ** -n)

    # Calculate payments
    monthly = calculate_payment(principal, r_monthly, n_monthly)
    semi_monthly = calculate_payment(principal, r_semi_monthly, n_semi_monthly)
    bi_weekly = calculate_payment(principal, r_bi_weekly, n_bi_weekly)
    weekly = calculate_payment(principal, r_weekly, n_weekly)

    # Accelerated payments
    rapid_bi_weekly = monthly / 2
    rapid_weekly = monthly / 4

    return round(monthly, 2), round(semi_monthly, 2), round(bi_weekly, 2), round(weekly, 2), round(rapid_bi_weekly, 2), round(rapid_weekly, 2)

# Prompt user input
principal = float(input("Enter the mortgage principal amount: "))
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
