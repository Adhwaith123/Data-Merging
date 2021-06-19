from selenium import webdriver
from bs4 import BeautifulSoup
import csv
starturl="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser=webdriver.chrome("/Users/LENOVO/Downloads/chromedriver_win32/chromedriver")
browser.get(starturl)

def scrape():
    headers=["Star","Constellation","Right_ascenion","Declination","App.mag.","Distance(ly)","Sectral_type","Brown_dwarf","Mass(M)","Radius(Rj)","Orbital_period(d)","Semimajor_axis(AU)","Ecc.","Discovery_year"]
    
        for trtag in soup.find_all("ul",attrs={"class"," brighteststars"}):
        thtags=trtag.find_all("li")
        templist=[]
        for index,thtags in enumerate(thtags):
            if index==0:
                templist.append(thtags.find_all("a")[0].contents[0])

            else:
                try:
                    templist.append(thtags.contents[0])

                except:
                    templist.append("")

         starsData.append(templist)   
         

   with open("scrper.csv","w")as f:
        csvWriter=csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(starsData)                  

scrape()



