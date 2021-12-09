from diaries.DiarySample import DiarySample
from diaries.KamiyaDiary import KamiyaDiary
from diaries.FujisawaDiary import FujisawaDiary
from diaries.YokoboriDiary import YokoboriDiary
from diaries.a_imaiDiary import a_imaiDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    FujisawaDiary(),
    YokoboriDiary(),
    KamiyaDiary(),
     a_imaiDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
