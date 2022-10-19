---
layout: post
title:  "How to Create a Simple Pokedex with PokeAPI"
date:   2022-10-18
author: "Luke McDowell"
description: Using one of the easiest APIs around to catch 'em all.
#image: /assets/images/Pokedex.png
---
![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/Jigglypuff.png?raw=true)

So you wanna be a Pokemon Master? Well, you won't get very far without a Pokedex - every respected trainer's favourite [Pokemon indexing tool](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9dex). Unfortunately, Professor Oak isn't around to hand them out, so our only option is to build one ourselves. Luckily, we have access to one of the easiest-to-use APIs (Application Programming Interface) available to help us do just that. 




# PokeAPI
PokeAPI is a RESTful API that utilizes code from Pokemon videogame ROMs as well as other sources to provide us with an easy means of accessing detailed information on the many cute and fearsome creatures across the Pokemon Universe. As a consumption-only API, No tokens are necessary for interaction, and pulling data is as easy as running a get request, with which we receive data in json format. 

  <br> 
  
## Creating a Pokemon Dataframe with Pandas and PokeAPI

For purposes of our Pokedex creation, lets gather data from the first two generations of Pokemon from the late 90's. This equates to the first 252 Pokemon. We'll pull data on each Pokemon's HP (Hit Points), Weight, Height, Type and Experience, and organize it into a neat pandas dataframe. Then, we'll intergrate our dataframe within the [Streamlit Framework](https://streamlit.io/) to create a basic Pokedex.

Let's start by importing the libraries we will. If any of the libraries below aren't installed on your system, a quick google search for the relevant installation guide will come in handy.

```
import pandas as pd
import requests
import streamlit as st
```

  <br> 
  
Let's use lists to store each data item, before creating a dictionary that we will feed into a pandas dataframe. We'll start by initializing the lists, then we'll use a for loop to request data on Pokemons 1-252 through the PokeAPI. Each request returns json-formatted data that we can traverse to pull the data items we want.    

```
# Initialize the lists we will use to place our variables in
Name = []
Primary_Type = []
Weight = []
Height = []
HP = []
Experience = []

# Loop through Pokemons 1 - 252 to request and append the gathered data to our lists
for x in range(1,252):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(x)
    res = requests.get(url)
    Name.append(res.json()['name'])
    Primary_Type.append(res.json()['types'][0]['type']['name'])
    Weight.append(res.json()['weight'])
    Height.append(res.json()['height'])
    HP.append(res.json()['stats'][0]['base_stat'])
    Experience.append(res.json()['base_experience'])
```

  <br> 
  
  
Now that our lists are full of data, let's create a dictionary and feed it into a pandas dataframe. We'll also increase each index number by one to match the id number for each Pokemon.

```
    
Poke_Dict = {
    'Pokemon': Name,
    'Type': Primary_Type,
    'Weight': Weight,
    'Height': Height,
    'HP': HP,
    'Experience':Experience
}
Pokemon_DF = pd.DataFrame(Poke_Dict)
Pokemon_DF.index += 1 
```

  <br> 

## Using Streamlit to Create a Pokedex!
Now that we are able to pull Pokemon data from the PokeAPI into a pandas dataframe, our next step is to turn that data into a Pokedex! I've decided to use the Streamlit app framework to build mine in, but there are endless app frameworks available online with which incredible Pokedexes can be made. If you'd also like to use Streamlit to build your Pokedex app, then instructions on how to get started can be found [here](https://redskywalker7.github.io/stat386-projects/2022/09/22/How_to_Use_Streamlit.html).

  <br> 
  
# [Click Here to See My Pokedex App!](https://redskywalker7-stat386-projects-pokedex-q0yt5b.streamlitapp.com/)
