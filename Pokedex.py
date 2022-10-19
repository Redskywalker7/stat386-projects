import pandas as pd
import requests
import streamlit as st

image_1 = 'https://github.com/Redskywalker7/stat386-projects/blob/main/assets/header.png?raw=true'

def PokeInfo(entry):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(entry)
    res = requests.get(url)
    return res

def pokedex(entry):
    res = PokeInfo(str.lower(entry))
    Name = res.json()['name']
    Primary_Type = res.json()['types'][0]['type']['name']
    Weight = res.json()['weight']
    Height = res.json()['height']
    HP = res.json()['stats'][0]['base_stat']
    Experience = res.json()['base_experience']
    Pokemon_DF = pd.DataFrame([[Name,Primary_Type,Weight, Height, HP, Experience]],columns = ['Pokemon','Type','Weight','Height','HP','Experience'])
    return Pokemon_DF

def image(entry):
    res = PokeInfo(str.lower(entry))
    image = res.json()['sprites']['front_default']
    return image

def main():
    st.title('Luke\'s Pokedex')
    st.image(image_1,caption = 'Gotta Catch \'em All!')
    text_input = st.text_input(
        "Welcome to my Pokedex",
        placeholder='Search Pokemon by number or name',
    )

    if text_input:
        DF = pokedex(text_input)
        container1 = st.container()
        col1,col2,col3 = st.columns([3,2,2])
        with container1:
            with col1:
                st.image(image(text_input),width = 200)
            with col2:
                st.metric(label = 'Pokemon',value = DF.Pokemon[0])
            with col3:
                st.write('Type: ' + DF.Type[0])
                st.write('Weight: ' + str(DF.Weight[0]))
                st.write('Height: ' + str(DF.Height[0]))
                st.write('HP: ' + str(DF.HP[0]))
                st.write('Experience: ' + str(DF.Experience[0]))          
    
if __name__ == "__main__":
    main()
