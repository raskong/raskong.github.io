---
feature_text: |
  # <span class="white-text black-background">Vehicle type</span>
  #### <span class="white-text black-background">A overveiw of vehicle types in crashes</span>
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

On Figure 1 an investigation has ben made on whether the type of car involved in the crash has any importance. The three most often appearing types of car (station wagon, sedan and passenger vehicle) must be assumed to also be the type of transportation with the highest density in the city. Therefore, it is of no surprise that these appear more often than e.g. taxies and busses. 
<figure>
  <img src="/cartype_counts.png" width="100%" height="auto">
  <figcaption><i style="font-size: smaller;">Figure 1: Count of how often different cartypes are involved in crashes</i></figcaption>
</figure>


Looking at all the vehicle types individually and then investigating which day of the week most car crashes happen, it appears that some vehicles have few crashes in the weekends (Figure 2). Looking closer it seems, that what these vehicles have in common, is that they are all bigger sized vehicles such as *'box truck'*, *'bus'*, *'pick-up truck'*, *'tractor truck diesel'* and *'van'*. The reason for this could be that these cars are mainly related to when people are working, therefor higher in the weekdays.


<figure>
  <img src="/Final_Project/Figures/vehicles per weekday.png" alt="Description of Image" style="width:100%; height:auto;">
  <figcaption><i style="font-size: smaller;">Figure 2: The 15 most frequent car types involeved in crashes and the observations according to weekday</i></figcaption>
</figure>



Below (Figure 3) you can see how the count of crashes is distributied when the contributing factor is paired with the veihcle type. When looking at the data the plot presents, we once agian see some odd patterns around the vehicle type "passenger vehicle". This vehicle type have a counts of zero in the contributing factors "alcohol involment", "unsafe speed" and more. It was earlier pointed out that there was a posibility of, that "passenger vecihle" had been fully or partly exchanged with "sedan" in 2016. This could still be true, but then it looks like there have also been a change in the process of noting down the contributing factors.           


<figure>
  <img src="/Final_Project\Figures\Vehicle_type_X_contri_factor.png" alt="" style="width:100%; height:auto;">
  <figcaption><i style="font-size: smaller;">Figure 3: Scatterplot with variable size - paired count of Vehicle type vs contributing factor </i></figcaption>
</figure>

To gain a clearer understanding of whether certain types of vehicles are more destructive than others, we've created a scatterplot below on Figure 4. This plot compares the number of people injured to the vehicle type, normalized with respect to the total count of vehicles. When we look at the plot we don't se a great difference in the veicle type as a attribute to the of destrutive it is. There is mabye a small tendency that bigger cars are a bit safer.    

<figure>
  <img src="/Final_Project\Figures\Vehicle_type_X_Persons_injured_norm.png" alt="" style="width:100%; height:auto;">
  <figcaption><i style="font-size: smaller;">Figure 4:Scatterplot with variable size - paired count of Vehicle type vs persons injured</i></figcaption>
</figure>





To clarify the previous statement, here's another Scatterplot with variable size. It illustrates the relationship between vehicle type and the number of injured motorists. This plot reveals a small trend: smaller vehicles tend to have fewer injuries on average. This pattern points to, if you're involved in a crash, you're more likely to get injuries in a smaller vehicle. 

<figure>
  <img src="/Final_Project\Figures\Vehicle_type_X__injured_motor.png" alt="" style="width:100%; height:auto;">
  <figcaption><i style="font-size: smaller;">Figure 5:Scatterplot with variable size - paired count of Vehicle type vs motorist persons injured</i></figcaption>
</figure>

