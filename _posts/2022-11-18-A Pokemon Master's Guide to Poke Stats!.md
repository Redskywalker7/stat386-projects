---
layout: post
title:  "A Pokemon Master's Guide to Poke Stats!"
date:   2022-11-18
author: "Luke McDowell"
description: Exploratory Analysis within the world of Pokemon
image: /assets/images/Pikachu.png
---


Let's go on a journey together - a journey to be a Pokemon Master. We may not know too much about these awesome creatures, but armed with the data that helped us recently build a Pokedex, we have just what we need to learn more about the kind of Pokemon that will help us claim that grand title. 


## Are you my Type?
A basic thing to know about Pokemon is that they are usually of a certain type. These types range from water and fire, to dragon and fairy types. Each type has vulnerabilities, or 'weakness' to certain other types, and is inversely 'super affective' against a few other types.Let's start by exploring which Pokemon types  have more of a comparitive advantage over others by looking at the top types by mean attacking and defensive stats from our Pokemon data. This would best be displayed as a bar chart:

![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/plots.png?raw=true)

Interesting, we see Ground and Steel appearing in the top five for both stats. Before we just settle on be-lining for Ground and Steel Pokemon, let's remind ourselves that these bar charts represent the means for each respective stat, so we are taking a lot of Pokemon into consideration. There may be more of a mix of weak and powerful pokemon amongst other types. In fact, we haven't even explored how each type type is represented within the Pokemon population as a whole
![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/Types.png?raw=true)

Well this changes things... we thought Steel Pokemon were the type to go for, but now we know there are only a few of them to even choose from. We now also know that water-type Pokemon are very common in comparison to other types. One would naturally consider collecting Pokemon that are strong against water types -  electric type Pokemon like Pikachu for instance.

While a greater understanding of Pokemon's types is important, we also need to learn how to develop all of our Pokemon's stats. To gain some insights into this, lets create a correlation matrix with the stats that we do have, to see if we can learn how to better improve them.
![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/Matrix.png?raw=true)

Notice the strong correlation between experience and HP. This may have already been intuitive, but this shows that our HP, or Hit-points (the amount of damage a Pokemon can withstand before fainting) is affected by the amount of experience it has in battle. In short, the more we train our Pokemon, the strong they will become. This is further illustrated by this scatter plot:
![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/Scatter.png?raw=true)


## Ok, But show me the Strongest Pokemon!
Well, let's go ahead to try and find the top five Attacking Pokemon. With this information we should be able to single out some of the best potential attackers in our team, and give us an idea of which Pokemon to seak out. We'll do this by simply sorting our dataframe by the Attack statistic:

![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/Top5.png?raw=true)![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/tyranitar.png?raw=true)![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/dragonite.png?raw=true)![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/flareon.png?raw=true)![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/hooh.png?raw=true)![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/machamp.png?raw=true)

We've also been told that speed is one of the most important attributes in the Pokemon world. Let's create a new stat that measures a Pokemon's speed + a Pokemon's attacking stat. This way we can find the Pokemon that can deal devasting damage at the quickest rate. We'll do that with the following code:
```
Pokemon_DF['SpeedAttack'] = Pokemon_DF['Attack']+ Pokemon_DF['Speed']
Pokemon_DF.sort_values(by = 'SpeedAttack',ascending = False)[0:5]
```

Here are our results:

![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/FinalTable.png?raw=true)

![image:](https://github.com/Redskywalker7/stat386-projects/blob/main/assets/images/mewtwo.png?raw=true)

Well, there we have it. The Pokemon 'Mewtwo' has come out on top of the list for our final metric. As a highly ambitious Pokemon trainer, there is no way we can't set out to try and obtain Mewtwo for our team now. 

Despite the invaluable insights we've gained here, there is still a world of data to pull more from. The power of data can truly be a deciding factor in many competitive environments, and the processing of surfacing previously hidden insights can be incredibly fulfilling. What analysis would you carry out on this data set?


