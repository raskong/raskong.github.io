---
feature_text: |
  # <span class="white-text black-background">Contributing factor</span>
  ##### <span class="white-text black-background">Analysis of which factors influence the probability of car accidents</span>
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

On this page we will analyze the contributing factors for vehicle number 1 for the crashes in NYC. 

On Figure 1 the 21 most frequent factors is shown on a bar plot. Unfortunately a very big part (around 1/3) of the observations has been labeled as *'unspecified'* which is unfortunate. 


<figure>
  <img src="/factor_counts.png" alt="Description of Image" style="width:100%; height:auto;">
  <figcaption><i style="font-size: smaller;">Figure 1: Number of observations for the most frequent contributing factors.</i></figcaption>
</figure>


On Fiugre 2 the 20 most frequent contributing factors has been plotted per hours of the day as bar plots. The *'unspecified'* label has been removed, as we did not find it interesting.

Several things can be observed on the plots. First of all, most of the categories follow the same pattern. The most crashes happen in the afternoon around hour 16 or 17, which could be due to rush hour when people are returning from work. Also a significant drop can be observed in the night, which is to no surprise either, because most people are assumed to be sleeping.

However, some categories show a different pattern.
*'Alcohol involvement'* is almost the opposite of the other factors, as it mainly occurs at night time. However, it is to no surprise that drinking and driving happens after a night out.
Also *'unsafe speed'* has its high around midnight and so it seems, that when the roads are empty, people tend to drive faster.
The factor *'pavement slippery'* has its peak at 8 in the morning. This makes sense as the mornings are colder and in combination with morning rush hour it leads to more crashes.

Summing up it seems that nothing seems to any surprise in the data as all of the patterns make logically sense. The conclusions could be: 
1. No patterns are deemed very interesting or rise any questions for further exploration.
2. It proves that the data is somewhat reliable, as it follows expected patterns.


<figure>
  <img src="/Final_Project/Figures/crashfactors per hour.png" alt="Description of Image" style="width:100%; height:auto;">
  <figcaption><i style="font-size: smaller;">Figure 2: Contributing factors plotted for each hour of the day.</i></figcaption>
</figure>



# Alcohol involment
Due to the different pattern of *'alcohol involvement'* we chose to dive deeper into it by using a calendar plot.
What becomes evident og Figure 3 is, that there is a clear pattern of people drinking and driving in the weekends. What is also interesting is that the 1st of january is significantly higher.
<figure>
  <img src="/Final_Project/Figures/Alc_calender_plot.png" width="100%" height="auto">
  <figcaption><i style="font-size: smaller;">Figure 3: Crashes involving alcohol over the years.</i></figcaption>
</figure>

