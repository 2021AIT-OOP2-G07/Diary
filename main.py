from diaries.DiarySample import DiarySample
from diaries.FujisawaDiary import FujisawaDiary
from diaries.YokoboriDiary import YokoboriDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(), 
    FujisawaDiary(),
    YokoboriDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()