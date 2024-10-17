class Article:
    def showall(self):
        '''Shows df of all items'''
        pass

    def purchase(self):
        '''Reduce in_stock by1 when purchase'''
        pass


class Receipt:
    def generate(self):
        '''Generates a pdf receipt of what user bought'''
        pass


print(showall())
user_choice = input("Choose an Article ID to buy: ")
if df.loc[df['id']==user_choice, 'id']:
    if df