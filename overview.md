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
Starting out by investigating the number of crashes which historically have happened each year since 2013(Figure 1), a significant drop can be seen in 2020, which is interesting. This is very likely caused by the COVID pandemeic <a href="https://jknylaw.com/new-york-car-accident-lawyer/statistics/">[1]</a>, as this resulted in fewer cars on the elsewise very crowded roads caused by NYC being the most populated city in US <a href="https://jknylaw.com/new-york-car-accident-lawyer/statistics/">[2]</a>



<figure>
  <iframe src="/Final_Project/Figures/crashes_per_year.png" width="800" height="480"></iframe>
  <figcaption><i style="font-size: smaller;">Figure 1: Number of crashes reported in NYC in the years between 2013 and 2023</i></figcaption>
</figure>



### Contributing factors
Below on Figure 2, you can find a Bokeh plot showing the 14 most frequent contributing factors. You are able to click the different factors do display how they evolve over the years and compare which are more frequently appearing than others. 

<figure>
  <iframe src="/Final_Project/Figures/bokeh_year_factors.html" width="800" height="400"></iframe>
  <figcaption><i style="font-size: smaller;">Figure 2: Bokeh plot for focus factors for vehicle 1 per year from 2013 to 2023.</i></figcaption>
</figure>

It becomes evident, that especially driver *'inattention/distraction'* pays a great tribute to the total number of crashes.
Also *'failure to yield right of way'* has an influence.
Right of way means that the first vehicle coming has the right to drive first and if two vehicles arrive at the same time, the vehicle on the left should wait for the vehicle on the right to drive <a href="https://www.rubensteinandrynecki.com/blog/2024/01/right-of-way-car-accidents/">[3]</a>.
This is opposed to Denmark where yield lines are very common, meaning that it is always clear who should yield.
Struggling to find any material on safety concerns regarding yielding in intersections we are left with our own reflections. One could might think, that yield right of way can lead to confusion in some cases, and with a tiny amount of inattention, it can lead to an accident.
As stated in <a href="https://www.rubensteinandrynecki.com/blog/2024/01/right-of-way-car-accidents/">[3]</a>, it can be a struggle for people living out of town to drive in the heavy traffic of NYC leading to confusion about the rules.
However, we have not been able to find any data stating that yield lines are more safe than *'yield right of way'*.


The Bokeh plot on Figure 3 shows the 14 most frequent vehicle types involved (for Vehicle 1).
Especially *'station wagon/sport utility vehicle (SUV)'* are present alongside *'sedan'*. This is to no surprise, as these cars are also the most common cars.
One thing that becomes evident is the huge shift around 2016 for some of the vehicle types. *'Passenger vehicle'* drops significantly to a value of 0 from 2017 and *'sedan'* goes from 0 to a rather high value in 2016. 
The reason for this must be that they have changed the procedures for data collection in 2016 and thereby the categories, they are using.
This is not ideal and is something that we will have to keep in mind for the rest of the analysis.

<figure>
  <iframe src="/Final_Project/Figures/bokeh_year_vehicles.html" width="800" height="400"></iframe>
  <figcaption><i style="font-size: smaller;">Figure 3: Bokeh plot for vehicle type 1 for the years from 2013 to 2023.</i></figcaption>
</figure>




