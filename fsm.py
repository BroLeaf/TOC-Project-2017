from transitions.extensions import GraphMachine

U = 'https://www.youtube.com/results?search_query='
time = 0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_breakfast(self, update):
        text = update.message.text
        return text.lower() == '吃早餐'

    def is_going_to_lunch(self, update):
        text = update.message.text
        return text.lower() == '吃午餐'

    def is_going_to_dinner(self, update):
        text = update.message.text
        return text.lower() == '吃晚餐'

    def is_going_to_satisfied(self, update):
        text = update.message.text
        return (text.lower() == '飽了' or text.lower() == '聽音樂')

    def is_going_to_search(self, update):
  #      U = U + update.message.text
        text = update.message.text
        return (text.lower() != '推薦' and text.lower() != '不要')

    def is_going_to_recommend(self, update):
        text = update.message.text
        return text.lower() == '推薦'

    def is_going_to_choose(self, update):
        text = update.message.text
        return text.lower() == '不要'

#do something
    def on_enter_choose(self, update):
        global time
        if time == 0:
            update.message.reply_text("想吃三餐還是聽音樂？\n")
            time = 1
        else:
            update.message.reply_text("還想要吃或聽音樂嗎？\n")

    def on_enter_breakfast(self, update):
        update.message.reply_text("我推薦你吃黑色香蕉\n")
        update.message.reply_photo(open("photo/banana.jpg","rb"))
 #       self.go_back(update)

    def on_enter_lunch(self, update):
        update.message.reply_text("你可以吃麥當勞\n")
        update.message.reply_photo(open("photo/M.jpg","rb"))
#        self.go_back(update)

    def on_enter_dinner(self, update):
        update.message.reply_text("肯德雞讓你參考看看\n")
        update.message.reply_photo(open("photo/GIGI.jpg","rb"))
 #       self.go_back(update)

    def on_enter_satisfied(self, update):
        update.message.reply_text("那來聽個音樂吧\n直接回覆我 可以幫你找音樂喔\n也可以輸入\"推薦\"讓我推薦給你喔~")
        update.message.text = ""
#        self.go_back(update)

    def on_enter_search(self, update):
        tmp = U + update.message.text
        tmp = tmp.replace(' ','+')
        update.message.reply_text(tmp)
        self.go_back(update)

    def on_enter_recommend(self, update):
        update.message.reply_text("gfriend超讚的給你認識一下")
        update.message.reply_text("https://www.youtube.com/results?search_query=gfriend")
        self.go_back(update)

    def on_exit_satisfied(self, update):
        print('Leaving satisfied')

    def on_exit_search(self, update):
        print('Leavin search')
