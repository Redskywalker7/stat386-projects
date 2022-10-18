---
layout: post
title:  "How to Create a Simple Pokedex with PokeAPI"
date:   2022-10-18
author: "Luke McDowell"
description: Using one of the easiest APIs around to catch 'em all.
image: blob/main/assets/images/Pokedex.png
---


So you wanna be a Pokemon Master? Well, you won't get very far without a Pokedex - every respected trainer's favourite [Pokemon indexing tool](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9dex). Unfortunately, Professor Oak isn't around to gift us with one, so our only option is to build one ourselves. Luckily, we have access to one of the easiest-to-use APIs (Application Programming Interface) available to help us do just that. 

![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/Jigglypuff.png?raw=true)


# PokeAPI
PokeAPI is a RESTful API that utilizes code from Pokemon videogame ROMs as well as other sources to provide us with an easy means of accessing detailed information on the many cute and fearsome creatures across the Pokemon Universe. As a consumption-only API, No tokens are necessary for interaction, and pulling data is as easy as running a get request, with which we receive data in json format. 

  <br> 
  
## Creating a Pokemon Pandas DataFrame

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
  
# Using Streamlit



While Streamlit is most powerful when deployed as an online app hosted in a repository like github, for the purpose of this tutorial lets create a simple app that runs locally and determines whether an entered word is a palindrome or not.  We'll start by installing and importing the streamlit library, configuring our app, then integrating our function with Streamlit's framework.

 <br> 

### Installing Streamlit:


Opening your terminal of choice and entering a simple 'pip install' should do the trick, though a more detailed installation guide can be found [on Streamlit's web page].(https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-windows)
  
```
pip install streamlit
```
  <br> 
  
  
### Configuring the App:

To start, we'll import the library:
```
import streamlit as st  
```


Streamlit has a respectable array of options when it comes to styling and configuring your app. In this case, we'll create a title for our app, then set it to a wide layout with the side bar expanded using the following syntax: 
```
st.set_page_config(
    page_title="Sample Streamlit App",
    layout="wide",
    initial_sidebar_state="expanded",
)
```
  <br> 
  
  
### Integrating our Work:

Now let's add our palindrome function before the main streamlit function for initialization purposes. 
```
def palindrome(word):
    word = word.replace(" ","")
    x = 0
    result = "Is Not Palindrome"
    if len(word)%2 != 0:
        result = "Is Palindrome"
        while x != (len(word)-1-x):
            if word[x] != word[(len(word)-1-x)]:
                result = "Is not palindrome"
                break
            x += 1          
    return(result)
```
 <br> 
 
### Utilizing the Widgets:

Lets add functionality to our app by referencing Streamlits helpful widget documentation. Within our main(): function, lets add and configure a title, [text input box](https://docs.streamlit.io/library/api-reference/widgets/st.text_input), and hang a pretty [image](https://docs.streamlit.io/library/api-reference/media/st.image). 

The app will beckon us to enter some text with which our palindrome app with return it's result in the style of a Streamlit metric. All our code should be encased within Streamlits framework as set out below:


```
image = 'https://media.istockphoto.com/photos/beautiful-sunrise-over-the-sea-picture-id610041376?k=20&m=610041376&s=612x612&w=0&h=JoEPWYoq1-FN5ANIQHNNdI2XrRDYnPCUWuLOHMrgLnE='

def main():
    st.title('The Palindrome Test')
    st.image(image,caption = 'Where will you find YOUR next palindrome?')
    print(palindrome('Hi there'))
    text_input = st.text_input(
        "Welcome to the Palindrome Test",
        placeholder='Enter word here',
    )

    if text_input:
        st.metric(label="Result of Palindrome Test: ", value=palindrome(text_input))   
    
if __name__ == "__main__":
    main()
```

 <br> 

### Running the App:

Once our .py is finalized, we'll save the file as 'streamlit_app.py' and save it to our local directory of choice. We'll then open up a new terminal window, navigate to the directory our file is found in and enter the following:
```
streamlit run streamlit_app.py
```    

This should produce the following:

![image:](https://i.ibb.co/c8zy0d1/Palindrome-Result.png)

<br> 

Horray!

Once you feel comfortable creating an app locally, deploying your app online is the next natural step. Thankfully, [Streamlit's webpage](https://docs.streamlit.io/) is awash with many helpful tips, cheatsheets and guides. 

There is no going back now, so happing app-baking!

