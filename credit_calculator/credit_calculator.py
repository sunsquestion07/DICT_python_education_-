import sys
import math
import argparse


def calculate_diff(principal, periods, interest):
    i = interest / (12 * 100)
    total_payment = 0
    for m in range(1, periods + 1):
        payment = principal / periods + i * (principal - principal * (m - 1) / periods)
        payment = math.ceil(payment)
        total_payment += payment
        print(f"Month {m}: payment is {payment}")

    overpayment = total_payment - principal
    print(f"\nOverpayment = {overpayment}")


def calculate_annuity_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    principal = round(principal)
    print(f"Your loan principal = {principal}!")
    return principal


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    payment = principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
    payment = math.ceil(payment)
    print(f"Your annuity payment = {payment}!")
    return payment


def calculate_annuity_periods(principal, payment, interest):
    i = interest / (12 * 100)
    periods = math.log(payment / (payment - i * principal), 1 + i)
    periods = math.ceil(periods)

    years = periods // 12
    months = periods % 12

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        year_word = "year" if years == 1 else "years"
        month_word = "month" if months == 1 else "months"
        print(f"It will take {years} {year_word} and {months} {month_word} to repay this loan!")

    return periods


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["annuity", "diff"])
    parser.add_argument("--principal", type=float)
    parser.add_argument("--payment", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)

    args = parser.parse_args()

    if args.type is None or args.interest is None:
        print("Incorrect parameters")
        return

    if args.type == "diff":
        if args.payment is not None:
            print("Incorrect parameters")
            return
        if args.principal is None or args.periods is None or args.interest is None:
            print("Incorrect parameters")
            return
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect parameters")
            return
        calculate_diff(args.principal, args.periods, args.interest)

    elif args.type == "annuity":
        param_count = sum([1 for x in [args.principal, args.payment, args.periods] if x is not None])

        if param_count != 2:
            print("Incorrect parameters")
            return

        if args.principal is not None and args.principal < 0:
            print("Incorrect parameters")
            return
        if args.payment is not None and args.payment < 0:
            print("Incorrect parameters")
            return
        if args.periods is not None and args.periods < 0:
            print("Incorrect parameters")
            return
        if args.interest < 0:
            print("Incorrect parameters")
            return

        if args.principal is None:
            principal = calculate_annuity_principal(args.payment, args.periods, args.interest)
            overpayment = args.payment * args.periods - principal
            print(f"Overpayment = {round(overpayment)}")
        elif args.payment is None:
            payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            overpayment = payment * args.periods - args.principal
            print(f"Overpayment = {round(overpayment)}")
        elif args.periods is None:
            periods = calculate_annuity_periods(args.principal, args.payment, args.interest)
            overpayment = args.payment * periods - args.principal
            print(f"Overpayment = {round(overpayment)}")


if __name__ == "__main__":
    main()