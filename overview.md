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

A significant drop can be seen in 2020, which is interesting. This is very likely caused by the COVID pandemeic <a href="https://jknylaw.com/new-york-car-accident-lawyer/statistics/">[1]</a>, as this resulted in fewer cars on the elsewise very crowded roads caused by NYC being the most populated city in US <a href="https://jknylaw.com/new-york-car-accident-lawyer/statistics/">[2]</a>


<iframe src="/Final_Project/Figures/crashes_per_year.png" width="800" height="500"></iframe>

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





