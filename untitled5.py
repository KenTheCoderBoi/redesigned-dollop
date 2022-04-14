from tkinter import *
import requests
import json
root=Tk()
root.geometry("500x500")
root.config(bg="red")
title=Label(root,text="City Searcher",font=("Comic Sans MS", 40, "bold"))
title.place(relx=0.5,rely=0.2,anchor=CENTER)
city_name_label=Label(root,text="Capital City Name:",font=("Comic Sans MS", 10, "bold"))
city_name_label.place(relx=0.1,rely=0.3)
city_entry=Entry(root)
city_entry.place(relx=0.35,rely=0.306)

country=Label(root,text="Country:")
country.place(relx=0.2,rely=0.4,anchor=CENTER)
region=Label(root,text="region:")
region.place(relx=0.2,rely=0.45,anchor=CENTER)
language=Label(root,text="language:")
language.place(relx=0.2,rely=0.5,anchor=CENTER)
population=Label(root,text="population:")
population.place(relx=0.2,rely=0.55,anchor=CENTER)
area=Label(root,text="area:")
area.place(relx=0.2,rely=0.60,anchor=CENTER)

def city_details():
    api_request=requests.get("https://restcountries.eu/rest/v2/capital/"+city_entry.get())
    api_output_json=json.loads(api_request.content)
    country=api_output_json[0]['name']
city_details()
root.mainloop()