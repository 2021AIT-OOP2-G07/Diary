from diaries.DiarySample import DiarySample
from diaries.takagiDiary import takagiDiary
from diaries.KamiyaDiary import KamiyaDiary
from diaries.FujisawaDiary import FujisawaDiary
from diaries.YokoboriDiary import YokoboriDiary
from diaries.a_imaiDiary import a_imaiDiary
from diaries.UkyoDiary import UkyoDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    FujisawaDiary(),
    YokoboriDiary(),
    KamiyaDiary(),
     a_imaiDiary(),
     UkyoDiary(),
    takagiDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()