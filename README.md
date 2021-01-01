# Lapis
![Lapis](https://i.imgur.com/EqcM95J.png)  
Lapis is a Plug-n-Play Azure v316 Discord Bot that is powered by [Lazuli](https://github.com/TEAM-SPIRIT-Productions/Lazuli) and [discord.py](https://github.com/Rapptz/discord.py).

Lapis is inspired by the [MapleDiscBot](https://github.com/Bratah123/MapleDiscBot) project, but aims to be leaner and more layman-friendly.  
Lapis accesses character and inventory attributes in [AzureMSv316](https://github.com/SoulGirlJP/AzureV316)-based databases using the [Lazuli API](https://team-spirit-productions.github.io/Lazuli/reference/lazuli/).  


#### Current Status: **Early Development**  ![20%](https://progress-bar.dev/20)

## Documentation:
Kindly direct any problems or questions to the [Issues](https://github.com/TEAM-SPIRIT-Productions/Lapis/issues) page.  
You will need to generate your `VENV` prior to use. Refer to [Lazuli's Wiki](https://github.com/TEAM-SPIRIT-Productions/Lazuli/wiki/Technical-Details#step-1-generate-the-virtual-environment) for details on how to do so.  

## Technical Details
*Inherited from Lazuli*
|  | Target Minimum | Target Maximum |
|---|---|---|
| Python | 3.6.12 | 3.6.12 |

NOTE: Please do **not** use Python versions other than 3.6 because:
1. f-strings are used - *requires 3.6 or newer*
2. dictionaries are assumed to be ordered - *requires 3.6 or newer*
3. Discord.py library is used - *requires 3.6 or older*
