from diaries.DiarySample import DiarySample

diaries = [DiarySample(), ]

for d in diaries:
    print("----------------")
    print(d.get_dare())
    print(d.get_summary())
    print(d.get_author())
    print()