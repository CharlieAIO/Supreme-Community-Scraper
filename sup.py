import requests
from bs4 import BeautifulSoup
from dhooks import Webhook,Embed
import random

webhook = ' '

Hook = Webhook(webhook)

droplist_link = 'https://www.supremecommunity.com/season/fall-winter2019/droplist/2019-11-07/'

def main():
    r = requests.get(droplist_link)
    soup = BeautifulSoup(r.text,"html.parser")
    cards = soup.find_all('div',{'class':'card card-2'})
    for card in cards:
        item = card.find("div",{"class":"card-details"})["data-itemname"]
        img = card.find("img",{"class":"prefill-img"})["src"]
        image = f'https://supremecommunity.com{img}'
        price = card.find("span",{"class":"label-price"}).text
        price = price.replace(" ","")
        price = price.replace("\n","")
        upvotes = card.find("p",{"class":"upvotes hidden"}).text
        downvotes = card.find("p",{"class":"downvotes hidden"}).text

        webhook_name = f'embed_{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
        webhook_name = Embed()
        webhook_name.set_title(title='Supreme Droplist',url=droplist_link)
        webhook_name.color = 0x99e8de
        webhook_name.set_image(url=image)
        webhook_name.add_field(name='Item',value=f'**{item}**',inline=False)
        webhook_name.add_field(name='Price',value=f'**{price}**',inline=False)
        webhook_name.add_field(name='Upvotes',value=f'**{upvotes}**',inline=True)
        webhook_name.add_field(name='Downvotes',value=f'**{downvotes}**',inline=True)
        webhook_name.set_footer(text='CharlieAIO | Supreme Droplist')
        Hook.send(embed=webhook_name)
        print("| WEBHOOK SENT |")

        
if __name__ == "__main__":
    main()
