---
feature_text: |
  # <span class="white-text black-background">Location of crashes</span>
  #### <span class="white-text black-background">Analysis of where in NYC most crashes happens</span>
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

### Most unsafe postal codes 
Although the number of car accidents is largely related to human factors and errors, it is also interesting to look at the city planning itself. It is not inconceivable that the structure of the roads and architechture of the city could be to blame for the factors. 
On Figure 1, you can see a count of the number of car accidents between 2013 and 2023 divided into NYC's Postal Codes.
<figure>
  <iframe src="/Final_Project/Figures/crashesmap.html" width="850" height="520"></iframe>
  <figcaption><i style="font-size: smaller;">Figure 1: Map of NYC's postal codes and indication of number of crashes between 2013 and 2023</i></figcaption>
</figure>

 
A relatively even distribution is seen here, with the exception of postal code 11236 (Canarsie|Brooklyn) and an increased concentration around Manhattan and the transition to Queens. 
The reason why Canarsie is more exposed to car crashes could be that this covers the Broadway Junction where thw two big roads; Broadway and Atlantic Avenue meets, while Manhatan is the most densely populated borough of NYC (https://en.wikipedia.org/wiki/Manhattan, accessed 30-04-2024) which also could cause more frequent crashes.


### Specific roads
Another interesting factor for car accidents is the rest roads they take place on. On Figure 2, you can see the 10 roads where accidents most often occur.

<figure>
  <img src="/Final_Project/Figures/top 10 streets.png" width="800" height="auto">
  <figcaption><i style="font-size: smaller;">Figure 2: Bar plot ofs the 10 roads in NYC where the most car crashes happens</i></figcaption>
</figure>

Here it can be seen how there is an immediate connection with the fact that it is New York's largest and longest roads, such as Broadway, which appear most frequently in reports of car accidents. 
This is to be expected as more accidents will likely occur on a longer road. It is however important to be aware of that this might not indicate that it is statistically more dangerous to be on the road. To get an accurate evaluation of the chances of participating in a crash you would have to divide the number of drivers on the road with the number of crashes. In this analysis this approach haven’t been prioritized - but could be suggested as future work in a more in depth analysis. 



### Heatmap
From the analysis of "Vehicle type" we found that stationcars were especially unsafe when it comes to the frequency of crashes. On Figure 3 a zoom in on an heatmap can be seen, which displays an area in NYC where stationcars often result in crashes where at least one person is killed. 

<figure>
  <iframe src="/Final_Project/Figures/heatmaptest.html" width="1000" height="1000"></iframe>
  <figcaption><i style="font-size: smaller;">Figure 3: Heatmap of where stationcars most often crash resulting in killed people</i></figcaption>
</figure>
On the heatmap cutout, and if you zoom in and out yoursel, it can overall be concluded, that the density of fatal crashes is fairly evenly distributed all over NYC. Some areas/locations do however have more reported crashes as the ones displayed in Figure 3. These often have in common that they are either located around large roads or in densely populated areas. 

### Conclusion on location of crashes 
After having conducted an analysis of where the crashes (both fatal and non-fatal) happen in NYC, it is fair to conclude that no unexpected patterns appear. It can be concluded that crashes most often appear, when it either is a very densely populated area or you are on a big road/the intersection of several.  


