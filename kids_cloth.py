import cards


def brend():
    cloth = input("""
                    1. Polo
                    2. Lora Piano
                    3. Nike
                    4. Adidas
                    5. Guchchi
                    6. Chanel
                    0. Back
                        >>>>""")
    if cloth == "1":
        return cards.all_cards_pay()
    elif cloth == "2":
        return cards.all_cards_pay()
    elif cloth == "3":
        return cards.all_cards_pay()
    elif cloth == "4":
        return cards.all_cards_pay()
    elif cloth == "5":
        return cards.all_cards_pay()
    elif cloth == "6":
        return cards.all_cards_pay()
    elif cloth == "0":
        return brend()