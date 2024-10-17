import pandas as pd
from pdf_code import pdf_generate

df = pd.read_csv('articles.csv', dtype={'id':str})

class Article:
    def showall(self):
        '''Shows df of all items'''
        return df

    def purchase(self,user_choice):
        '''Reduce in_stock by1 when purchase'''
        df.loc[df['id']== user_choice, 'in stock'] -=1
        df.to_csv('articles.csv', index=False)


class Receipt:
    def generate(self):
        '''Generates a pdf receipt of what user bought'''
        name = df.loc[df['id']==user_choice,'name'].squeeze()
        price = df.loc[df['id']==user_choice,'price'].squeeze()
        pdf_generate(name,price)
        

article = Article()
print(article.showall())
user_choice = input("Choose an Article ID to buy: ")
if not df.loc[df['id']==user_choice].empty:
    if df.loc[df['id']==user_choice,'in stock'].values[0]>0:
        receipt = Receipt()
        receipt.generate()
        
        article.purchase(user_choice)
    else:
        print('Article not in stock')
else:
    print("ID not in range")