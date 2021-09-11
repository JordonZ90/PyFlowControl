def discount():
    price = int(input("Enter the price: "))
    qty = int(input("Enter the quantity "))
    amt = price * qty
    print(amt)

    if amt < 1000:
        print("Sorry discount isn't applicable")

    if amt > 1000:
        print("10% discount is applicable")
        discount = amt * 10 / 100
        amt -= discount
    print(f"Amount payable: {amt}")


def main():
    again = "y"
    while again.lower() == "y":
        discount()
        again = input("Would you like to calculate again? (y|n) ")
        print()
    print("Bye!")


if __name__ == "__main__":
    main()
