import cards


def mayshiy_brend():
    m_brend = input("""
                    1. eSavdo
                    2. All good
                    3. ASaxiy
                    4. Goodwell
                    5. Good_zone
                    6. Media park
                    0. Back
                        >>>>""")

    if m_brend == "1":
        return cards.all_cards_pay()
    elif m_brend == "2":
        return cards.all_cards_pay()
    elif m_brend == "3":
        return cards.all_cards_pay()
    elif m_brend == "4":
        return cards.all_cards_pay()
    elif m_brend == "5":
        return cards.all_cards_pay()
    elif m_brend == "6":
        return cards.all_cards_pay()
    elif m_brend == "0":
        return m_brend

    else:
        print("Kechirasiz xatolik yuz berdi")
        return m_brend
