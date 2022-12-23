from tkinter import *
import json
import requests

root = Tk()
root.geometry("350x350")
root.config(background="lime")

city_name_label=Label(root, text="Capital City Name",font=("Helvetica", 18,'bold'),bg="light slate blue", fg="white")
city_name_label.place(relx=0.35,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.24,rely=0.25,anchor=CENTER)

country_name = Label(root,text="Country:", bg="light slate blue",fg="White", font=("Helvetica",10,"bold"))
country_name.place(relx=0.06,rely=0.45,anchor=W)

region = Label(root,text="Region:", bg="light slate blue", fg="white", font=("Helvetica",10,"bold"))
region.place(relx=0.06,rely=0.55,anchor=W)

language = Label(root,text="Language:", bg="light slate blue", fg="white", font=("Helvetica",10,"bold"))
language.place(relx=0.06,rely=0.65,anchor=W)

population= Label(root,text="Population:", bg="light slate blue", fg="white", font=("Helvetica",10,"bold"))
population.place(relx=0.06,rely=0.75,anchor=W)

area = Label(root,text="Area:",bg="light slate blue", fg="white", font=("Helvetica",10,"bold"))
area.place(relx=0.06,rely=0.85,anchor=W)

def city_details():
    api_request = requests.get("https://restcountries.eu/rest/v2/capital/" + city_entry.get())
    
    api_output_json = json.loads(api_request.content)
    country = api_output_json[0]['name']
    print(country)
    region = api_output_json[0]['region']
    print(region)
    language = api_output_json[0]['languages'][0]["name"]
    print(language)
    population = api_output_json[0]['population']
    print(population)
    area = api_output_json[0]['area']
    print(area)
    
    country_name['text'] = "Country: " + country 
    region['text'] = "Region: " + region
    language['text'] = 'Language: ' + language
    population['text'] = "Population: " + str(population)
    area['text'] = "Area: " + str(area)
    
search_btn = Button(root,text = "City Details", command = city_details)
search_btn.place(relx = 0.16,rely = 0.35,anchor = CENTER)

root.mainloop()
    