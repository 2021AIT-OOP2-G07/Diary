from diaries.AbstractDiary import AbstractDiary


class YokoboriDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "今日はオブジェクト指向プログラミング演習２のグループワークだった。"

    def get_author(self):
        return "Yokobori"
