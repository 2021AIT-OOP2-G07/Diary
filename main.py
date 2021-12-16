from diaries.DiarySample import DiarySample
<<<<<<< Updated upstream
=======
from diaries.TakagiDiary import TakagiDiary
from diaries.KamiyaDiary import KamiyaDiary
>>>>>>> Stashed changes
from diaries.FujisawaDiary import FujisawaDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(), 
    FujisawaDiary(),
<<<<<<< Updated upstream
    ]
=======
    YokoboriDiary(),
    KamiyaDiary(),
     a_imaiDiary(),
     UkyoDiary(),
    TakagiDiary(),
]

>>>>>>> Stashed changes
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()