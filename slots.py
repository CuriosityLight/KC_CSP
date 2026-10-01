import random
from random import SystemRandom


slot_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
rand = SystemRandom()
slot1 = ""
slot2 = ""
slot3 = ""
slot4 = ""
slot5 = ""
slot6 = ""
slot7 = ""
slot8 = ""
slot9 = ""
coins = 50



def slots(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9):
        while True:
            slot1 = rand.choice(slot_choices)
            slot2 = rand.choice(slot_choices)
            slot3 = rand.choice(slot_choices)
            slot4 = rand.choice(slot_choices)
            slot5 = rand.choice(slot_choices)
            slot6 = rand.choice(slot_choices)
            slot7 = rand.choice(slot_choices)
            slot8 = rand.choice(slot_choices)
            slot9 = rand.choice(slot_choices)
            print(f"""
                
                {slot1}    {slot2}    {slot3}
                {slot4}    {slot5}    {slot6}
                {slot7}    {slot8}    {slot9}

            """)
            if slot4 == slot5 and slot5 == slot6:
                print("you win!")
                return
            else:
                print("you lost")
                return
            
slots(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9)