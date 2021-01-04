# Lapis
![Lapis](https://i.imgur.com/EqcM95J.png)  
Lapis is a Plug-n-Play Azure v316 Discord Bot that is powered by [Lazuli](https://github.com/TEAM-SPIRIT-Productions/Lazuli) and [discord.py](https://github.com/Rapptz/discord.py).

Lapis is inspired by the [MapleDiscBot](https://github.com/Bratah123/MapleDiscBot) project, but aims to be leaner and more layman-friendly.  
Lapis accesses character and inventory attributes in [AzureMSv316](https://github.com/SoulGirlJP/AzureV316)-based databases using the [Lazuli API](https://team-spirit-productions.github.io/Lazuli/reference/lazuli/).  


#### Current Status: **Release Candidate 1 is out now!**
### TODO:
- [x] Working protoype - *Target goal for RC1*
- [ ] Unit Testing - *Target goal for RC2*
- [ ] Comprehensive Documentation - *Target goal for Release*

## Gallery
  ![character](https://cdn.discordapp.com/attachments/631249406775132182/795031817891610644/c76d5804a42f63accb448e8a9e8bf157.png)
  
  ![help](https://cdn.discordapp.com/attachments/631249406775132182/795031808512098334/42b4365e6b819a088fc59d01d11ef27c.png)
## Documentation:
Kindly direct any problems or questions to the [Issues](https://github.com/TEAM-SPIRIT-Productions/Lapis/issues) page.  
You will need to generate your `VENV` prior to use. Refer to [Lazuli's Wiki](https://github.com/TEAM-SPIRIT-Productions/Lazuli/wiki/Technical-Details#step-1-generate-the-virtual-environment) for details on how to do so.  

## Configuration
  ![config](https://media.discordapp.net/attachments/746519006961336370/795472281840517120/d2df4b78e7ef657d8c0e07076c1781ab.png?width=1003&height=348)
  - Prior to launching the bot, please navigate to config.json found in the `src` folder.
  - Here you will find various settings you have to fill out
  - First you MUST fill out the BOT_TOKEN section by obtaining a bot token from the [Discord Developer Portal](https://discord.com/developers/docs/intro).
  - The rest of the settings do not need to be filled out for it to work, however feel free to make the changes related to your server
  - If you do not know what you are doing keep `"USE_DEFAULT_DB"` to true.
    - If it is false, the settings below it would be used for ALL database calls
  - If you configure `ADD_ROLE` to true, you HAVE to fill out `ROLE_TO_ADD` which is the role id.

## Technical Details
*Inherited from Lazuli*
|  | Target Minimum | Target Maximum |
|---|---|---|
| Python | 3.6.12 | 3.6.12 |

NOTE: Please do **not** use Python versions other than 3.6 because:
1. f-strings are used - *requires 3.6 or newer*
2. Dictionaries are assumed to be ordered - *requires 3.6 or newer*
3. Discord.py library is used - *requires 3.6 or older*
