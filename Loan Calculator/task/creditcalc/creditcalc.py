import math
import argparse


def number_of_payment(x_loan, x_monthly, x_interest):
    i = x_interest / (12 * 100)  # 12 month in a year and 100%
    n = math.log((x_monthly / (x_monthly - i * x_loan)), (1 + i))
    n = math.ceil(n)  # number of periods
    total = x_monthly * n
    over = total - x_loan
    # converting to years and month
    year = n // 12
    months = n % 12
    if year == 0:
        if months > 1:
            print(f"It will take {months} months to repay this loan!")
            print(f"Overpayment = {int(over)}")
        else:
            print(f"It will take 1 month to repay this loan!")
            print(f"Overpayment = {int(over)}")
    else:
        if year != 1:
            if months > 1:
                print(f"It will take {year} years and {months} months to repay this loan!")
                print(f"Overpayment = {int(over)}")
            elif months == 0:
                print(f"It will take {year} years to repay this loan!")
                print(f"Overpayment = {int(over)}")
            else:
                print(f"It will take {year} years and 1 month to repay this loan!")
                print(f"Overpayment = {int(over)}")
        else:
            print(f"It will take 1 year and {months} month to repay this loan!")
            print(f"Overpayment = {int(over)}")


def annuity(x_loan, x_periods, x_interest):
    i = x_interest / (12 * 100)  # 12 month in a year and 100%
    # calculation of annuity payment
    A = x_loan * i * pow(1 + i, x_periods) / (pow(1 + i, x_periods) - 1)
    total = math.ceil(A) * x_periods
    over = total - x_loan
    print(f"Your monthly payment = {math.ceil(A)}!")
    print(f"Overpayment = {int(over)}")


def loan_principal(x_annuity, x_periods, x_interest):
    total = x_annuity * x_periods
    i = x_interest / (12 * 100)  # 12 month in a year and 100%
    # calculation of loan principal P
    P = x_annuity / (i * pow((1 + i), x_periods) / (pow((1 + i), x_periods) - 1))
    over = total - P
    print(f"Your loan principal = {int(P)}!")
    print(f"Overpayment = {int(over)}")


def diff(p, n, interest):
    i = interest / (12 * 100)  # 12 month in a year and 100%
    total = 0
    for m in range(1, n + 1):
        D = math.ceil(p / n + i * (p - p * (m - 1) / n))
        print(f"Month {m}: payment is {D}")
        total += D
    over = total - p
    print()
    print(f"Overpayment = {int(over)}")


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=float)  # "P" in formula
parser.add_argument('--periods', type=int)  # "n" in formula, periods in months
parser.add_argument('--interest', type=float)  # "i" in formula, but first you need to divide by 100% and by 12 months
parser.add_argument('--payment', type=float)  # "A" in formula
args = parser.parse_args()

list_of_argument = []
for arg in vars(args):
    if getattr(args, arg):
        list_of_argument.append(getattr(args, arg))

# Checking the "type" input
if (args.type not in ["annuity", "diff"] or args.type is None) \
        or (args.type == "diff" and args.payment) \
        or len(list_of_argument) != 4:
    print("Incorrect parameters")
else:
    # differentiated payments
    if args.type == "diff":
        diff(args.principal, args.periods, args.interest)
        # annuity payments
    elif args.type == "annuity":
        #  calculation of loan principal
        if args.principal is None:
            loan_principal(args.payment, args.periods, args.interest)
        # calculation of periods
        elif args.periods is None:
            number_of_payment(args.principal, args.payment, args.interest)
            # calculation of payment
        elif args.payment is None:
            annuity(args.principal, args.periods, args.interest)
