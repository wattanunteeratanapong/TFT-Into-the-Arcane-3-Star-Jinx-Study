# TFT Set 13 3-Star Jinx Analysis
Have you ever wonder how many gold do we have to spend to get 3-Star Jinx in TFT Set13? <br><br>
<img src="https://github.com/user-attachments/assets/261a36cc-8801-4ea2-9fcf-e04538878a24" width="100%" alt="Jinx"> <br><br>



## Overview & Control Variable
TFT is a game that heavily rely on a probability and statistic, In this repository we are gonna find out that how many gold do we need to spare for reroll to find 3-Star Jinx, this could also apply to every 5-Costs unit not only Jinx. <br><br>
If you can make 5-Cost Unit that have 3-Star, in that match it's a guarantee win at 1st place for you in that match. <br>
So that we can use this info to make the best decision for the best strategy and getting out of this elo hell. <br><br>
In this experiment we're gonna test how much gold to get 5-Cost 3-Star Unit on level 7-10, and experiment we gonna test on patch 14.23 where 6-Cost doesn't exist in this patch. 
But this test could also apply to patch 14.24 because 6-Cost chance are very low it doesn't affect the chance of 5-Cost units. <br><br>
And this experiment test only 1 player in real match other player can reduce the amount of 5-Cost Unit in the pool make it slightly easier to find 5-Cost Unit that we're looking for. 
And also this simulation didn't use special technique like picking same cost out of the pool, in real game player could apply this technique to make it easier to find unit that we want. 
And in the real game there are many factor that can increase a chance of getting 3-Star Jinx like champion duplicator, augment, selecting circle stage, etc.<br><br>
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
Every unit at every cost could upgrade to 1-Star, 2-Star, 3-Star. <br>
1-Star is a unit that can find the the pool <br>
2-Star is a combined of 1-Star 3 unit <br>
3-Star is a combined of 2-Star 3 unit (1-Star 9 unit) <br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/9afe14de-c758-4d75-b689-7159626c5518" width="100%" alt="Level">
</div>
<br>



## Level System & Odds System
Chance of getting each cost in each level is different <br>
As we can see 5-Cost Unite start to appear in the shop at level 7, so in this experiment we're gonna test from level 7 to 10, to see each level gold needed for finding 5-Cost 3-Star Unit <br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/bc4ee11a-0ee8-448f-a3a3-1d0f5be5f48e" width="100%" alt="Odds">
</div>
<br>



## Shop System
Each reroll player have 5 slot of random unit, player can buy unit from this shop, this mean in 1 reroll player have 5 times chance to get Jinx.
<div align="center">
  <img src="https://github.com/user-attachments/assets/277f59ad-2a79-4f75-922d-e79fa5fc5654" width="100%" alt="Shop">
</div>
<br>



## Result from Simulation
### Level 7

### Level 8

### Level 9

### Level 10

### Level 10 with 1 Champion Duplicator

### Level 10 with 2 Champion Duplicator

### Level 10 with 3 Champion Duplicator

### Level 10 with 4 Champion Duplicator

### Level 10 with 5 Champion Duplicator

### Level 10 with 6 Champion Duplicator
<br>



## Conclusion
From the simulation roll for Jinx lower than level 10 is a very bold move, it's best if we reach level 10. and the more champion duplicator we have the lower gold we have to spend to find Jinx. There are planty way to gain champion other than champion duplicator. <br> 

The expected value of this patch from simulation is around 60 so it mean we most likely to get anomaly that we're looking for in trial 60, in that case we need a spare gold around 120 gold to get anomaly that we're looking for.
<br><br>



## Source
<a href="https://tftactics.gg/champions/">TFT Set 13 Champions List</a>
<br>

<a href="https://tftactics.gg/db/rolling/">TFT Set 13 Rolling Chances</a>
<br>

<a href="https://youtu.be/smV58edQCiM?si=vSUk73VxSW5M6u2O">Jinx 5 บาท 3 ดาว!!! มาพร้อมสกิลลับ...โหดขนาดนี้ใครจะหยุดได้? (TFT Set 13)</a>
<br>
