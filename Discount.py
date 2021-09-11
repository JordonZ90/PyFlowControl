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
    playing = True
    discount()
    while playing:
        again = input("Would you like to calculate again? (y|n) ").lower()
        if again == "y":
            discount()
        if again == "n":
            print("Goodbye!")
            playing = False


if __name__ == "__main__":
    main()
