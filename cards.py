import pay


def all_cards_pay():
    cards_pay = input("""Iltimos kartani tanlang !!!
                        1. Humo
                        2. Uzcard
                        3. VISA
                        4.Mastercard
                        5. Orqaga
                            >>>>""")
    if cards_pay == "1":
        return cards_pay
    elif cards_pay == "2":
        return pay.humo_uz()
    elif cards_pay == "3":
        return pay.uz_card()
    elif cards_pay == "4":
        return pay.master_card()
    elif cards_pay == "5":
        return pay.visa_card()
