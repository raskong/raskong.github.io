---
feature_text: |
  # <span class="white-text black-background">Data overview</span>
  #### <span class="white-text black-background">Basic stats</span>
feature_image: "https://d3iso9mq9tb10q.cloudfront.net/magefan_blog/n/e/new-york-nightlife-things-to-do-at-night-big-bus-tours-jan-2017.jpg"
excerpt: "Where is this written????"
---
<style>
  .white-text {
    color: white;
  }
  .black-background {
    background-color: black;
    padding: 0.2em 0.5em; /* Adjust padding as needed */
    border-radius: 4px; /* Optional: Add rounded corners */
  }
</style>

# A first look on the data

A significant drop can be seen in 2020, which is interesting. BLA...BLA...


<iframe src="/Final_Project/Figures/crashes_per_year.png" width="800" height="500"></iframe>


As a secound step, we can have a brief look if there is any corrlations (Spearman) that pop and are interesting to investigate more furter: 

<img src="/Final_Project/Figures/spearman_corr_matrix.png" width="100%" height="auto">


In the Corrlation matrix there some patterns showing there is a  



### Contributing factors
Below you can find a Bokeh plot showing the 14 most frequent contributing factors (Refered to as focus factors). The label *'unspecified'* has been left out as it is not deemed interesting in this case. The numbers are all based on vehicle number 1, as there is always at least one vehicle in a crash:

<iframe src="/Final_Project/Figures/bokeh_year_factors.html" width="800" height="400"></iframe>
Figure 1: Bokeh plot for focus factors for vehicle 1 per year from 2013 to 2023.

It becomes evident, that especially driver *'inattention/distraction'* pays a great tribute to the total number of crashes.
Also *'failure to yield right of way'* has an influence.

Another Bokeh plot below shows the 14 most frequent vehicle types involved (for Vehicle 1).
Especially *'station wagon/sport utility vehicle (SUV)'* are present alongside *'sedan'*. This is to no surprise, as these cars are also the most common cars.
One thing that becomes evident is the huge shift around 2016 for some of the vehicle types. *'passenger vehicle'* drops significantly to a value of 0 from 2017 and *'sedan'* goes from 0 to a rather high value in 2016. 
The reason for this must be that they have changed the procedures for data collection in 2016 and thereby the categories, they are using.
This is not ideal and is something that we will have to keep in mind for the rest of the analysis.

<iframe src="/Final_Project/Figures/bokeh_year_vehicles.html" width="800" height="400"></iframe>
Figure 2: Bokeh plot for vehicle type 1 for the years from 2013 to 2023.



Put in some interesting comments



### Vehicle type

Some bokeh plots


# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

<small>A small element</small>

[A link](https://david.darn.es "A link")

Lorem ipsum dolor sit amet, consectetur adip* isicing elit, sed do eiusmod *tempor incididunt ut labore et dolore magna aliqua.

Duis aute irure dolor in [A link](https://david.darn.es "A link") reprehenderit in voluptate velit esse cillum **bold text** dolore eu fugiat nulla pariatur. Excepteur span element sint occaecat cupidatat non proident, sunt _italicised text_ in culpa qui officia deserunt mollit anim id `some code` est laborum.

* An item
* An item
* An item
* An item
* An item

1. Item one
2. Item two
3. Item three
4. Item four
5. Item five

> A simple blockquote

Some HTML...

``` html
<blockquote cite="http://www.imdb.com/title/tt0284978/quotes/qt1375101">
  <p>You planning a vacation, Mr. Sullivan?</p>
  <footer>
    <a href="http://www.imdb.com/title/tt0284978/quotes/qt1375101">Sunways Security Guard</a>
  </footer>
</blockquote>
```

...CSS...

``` css
blockquote {
  text-align: center;
  font-weight: bold;
}
blockquote footer {
  font-size: .8rem;
}
```

...and JavaScript

``` js
const blockquote = document.querySelector("blockquote")
const bolden = (keyString, string) =>
  string.replace(new RegExp(keyString, 'g'), '<strong>'+keyString+'</strong>')

blockquote.innerHTML = bolden("Mr. Sullivan", blockquote.innerHTML)
```

`Single line of code`

## HTML Includes

### Contact form

{% include site-form.html %}

``` html
{% raw %}{% include site-form.html %}{% endraw %}
```

### Demo map embed

{% include map.html id="1UT-2Z-Vg_MG_TrS5X2p8SthsJhc" title="Coffee shop map" %}

``` html
{% raw %}{% include map.html id="XXXXXX" title="Coffee shop map" %}{% endraw %}
```

### Button include

{% include button.html text="A button" link="https://david.darn.es" %}

{% include button.html text="A button with icon" link="https://twitter.com/daviddarnes" icon="twitter" %}

``` html
{% raw %}{% include button.html text="A button" link="https://david.darn.es" %}
{% include button.html text="A button with icon" link="https://twitter.com/daviddarnes" icon="twitter" %}{% endraw %}
```

### Icon include

{% include icon.html id="twitter" title="twitter" %} [{% include icon.html id="linkedin" title="twitter" %}](https://www.linkedin.com/in/daviddarnes)

``` html
{% raw %}{% include icon.html id="twitter" title="twitter" %}
[{% include icon.html id="linkedin" title="twitter" %}](https://www.linkedin.com/in/daviddarnes){% endraw %}
```

### Video include

{% include video.html id="zrkcGL5H3MU" title="Siteleaf tutorial video" %}

``` html
{% raw %}{% include video.html id="zrkcGL5H3MU" title="Siteleaf tutorial video" %}{% endraw %}
```


### Image includes

{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Image with caption" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Right aligned image" position="right" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Left aligned image" position="left" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/1600/800?image=894" alt="Image with just alt text" %}

``` html
{% raw %}{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Image with caption" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Right aligned image" position="right" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/600/800?image=894" caption="Left aligned image" position="left" width="300" height="800" %}

{% include figure.html image="https://picsum.photos/1600/800?image=894" alt="Image with just alt text" %}{% endraw %}
```
