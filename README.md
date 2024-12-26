# TFT Set 13 3 Star Jinx Analysis
Have you ever wonder how many gold do we have to spend to get 3-Star Jinx in TFT Set13? <br><br>
<img src="https://github.com/user-attachments/assets/261a36cc-8801-4ea2-9fcf-e04538878a24" width="100%" alt="Jinx">



## Overview
TFT is a game that heavily rely on a probability and statistic, In this repository we are gonna find out that how many gold do we need to spare for reroll to find 3-Star Jinx, this could also apply to every 5-Costs unit not only Jinx. <br><br>
If you can make 5-Cost Unit that have 3-Star, in that match it's a guarantee win at 1st place for you in that match. <br>
So that we can use this info to make the best decision for the best strategy and getting out of this elo hell. <br><br>
In this experiment we gonna test on patch 14.23 where 6-Cost doesn't exist in this patch <br>
But this test could also apply to patch 14.24 because 6-Cost chance are very low it doesn't affect the chance of 5-Cost units. <br>
Time of simulation is around 10 million time for getting close to the theoratical probability as much as possible. <br>
<br>



## Pool System
There are 5 type of unit in TFT. 1-Cost, 2-Cost, 3-Cost, 4-Cost, 5-Cost <br>
1-4 Cost Unit each champion have 18 unit in the pool <br>
&nbsp;&nbsp;5&nbsp;&nbsp;Cost Unit each champion have 9 unit in the pool <br>
If each champion unit is running out of pool, player won't be able to find that unit unless that unit is sold back to the pool <br><br>
1-Cost(14) : Amumu, Darius, Draven, Irelia, Lux, Maddie, Morgana, Powder, Singed, Steb, Trundle, Vex, Violet, Zyra <br>
2-Cost(13) : Akali, Camille, Leona, Nocturne, Rell, Renata, Sett, Tristana, Urgot, Vander, Vladimir, Zeri, Ziggs <br>
3-Cost(13) : Blitzcrank, Cassiopeia, Ezreal, Gangplank, Kogmaw, Loris, Nami, Nunu, Renni, Scar, Smeech, Swain, Twisted Fate <br>
4-Cost(12) : Ambessa, Corki, Dr Mundo, Ekko, Elise, Garen, Heimerdinger, Illaoi, Silco, Twitch, Vi, Zoe <br>
5-Cost(8)&nbsp;&nbsp; : Caitlyn, Jayce, Jinx, Leblanc, Malzahar, Mordekaiser, Rumble, Sevika <br><br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/8c7035b2-7e40-427d-9775-c986db586f0e" width="100%" alt="Pool">
</div>
<br>




## Unit System 
Every unit in every cost could upgrade to 1-Star, 2-Star, 3-Star. <br>
1-Star is a unit that can find the the pool <br>
2-Star is a combined of 1-Star 3 unit <br>
3-Star is a combined of 2-Star 3 unit (1-Star 9 unit) <br>
<br>



## Level System & Odds System
Chance of getting each cost in each level is different <br>
In this experiment we're gonna test from level 7 to 10, to see each level gold needed for finding 5-Cost 3-Star Unit <br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/bc4ee11a-0ee8-448f-a3a3-1d0f5be5f48e" width="100%" alt="Odds">
</div>
<br>



## Shop System
Each reroll player have 5 slot of random unit, player can buy unit from this shop.
<div align="center">
  <img src="https://github.com/user-attachments/assets/277f59ad-2a79-4f75-922d-e79fa5fc5654" width="100%" alt="Shop">
</div>
<br>



## Result from Simulation
### Level 7

### Level 8

### Level 9

### Level 10
<br>



## Conclusion
### Level 7

### Level 8

### Level 9

### Level 10
In this patch, the chance of getting the anomaly we’re looking for increase every trail because we’re selecting anomalies that we’re not looking for out of the pool. But if we look at the number of trails to get the anomaly, the chance is the same for every trial. <br>
The expected value of this patch from simulation is around 30 so it mean we most likely to get anomaly that we're looking for in trial 30, in that case we need a spare gold around 60 gold to get anomaly that we're looking for.

The expected value of this patch from simulation is around 60 so it mean we most likely to get anomaly that we're looking for in trial 60, in that case we need a spare gold around 120 gold to get anomaly that we're looking for.
<br><br>



## Source
<a href="https://tftactics.gg/champions/">TFT Set 13 Champions List</a>
<br>

<a href="https://tftactics.gg/db/rolling/">TFT Set 13 Rolling Chances</a>
<br>

