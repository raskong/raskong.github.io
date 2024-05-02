---
title: Contributing Factor
feature_text: |
  ## <span class="white-text">A demo of Markdown and HTML includes</span>
feature_image: "https://www.bigbustours.com/en/new-york/things-to-do-in-new-york-at-night"
excerpt: "A demo of Markdown and HTML includes"
aside: false
---

<style>
  .white-text {
    color: white;
  }
</style>

On this page we will analyze the contributing factors for vehicle number 1 for the crashes in NYC. 

On the figure the 21 most frequent factors is shown on a bar plot. Unfortunately a very big part (around 1/3) of the observations has been labeled as *'unspecified'* which is unfortunate. 

{{ page.feature_text | markdownify }}
<iframe src="/Final_Project/Figures/factor_counts.png" width="800" height="500"></iframe>

Below the 20 most frequent contributing factors has been plotted per hours of the day as bar plots with. The *'unspecified'* label has been removed, as we did not find it interesting.

Some things can be observed on the plots. First of all, most of the categories follows the same pattern. The most crashes happen in the afternoon around hour 16 or 17, which could be due to rush hour when people are returning from work. Also a significant drop can be observed in the night, which is to no surprise either.

However, some categories show a different pattern.
*'alcohol involvement'* is almost the opposite of the other factors, as it mainly occurs at night time. However, it is to no surprise that drinking and driving happens after a night out.
Also *'unsafe speed'* has its high around midnight and so it seems, that when the roads are empty, people tend to drive faster.
The factor *'pavement slippery'* has its peak at 8 in the morning. This makes sense as the mornings are colder and in combination with morning rush hour it leads to more crashes.

Summing up it seems that nothing seems to any surprise in the data as all of the patterns make logically sense. This is two fold: 
1. No patterns are deemed very interesting or rise any questions for further exploration.
2. It proves that the data is somewhat reliable, as it follows expected patterns.

<iframe src="/Final_Project/Figures/crashfactors per hour.png" width="800" height="500"></iframe>








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
