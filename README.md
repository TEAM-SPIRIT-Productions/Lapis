# Lapis
![Lapis](https://i.imgur.com/EqcM95J.png)  
Lapis is a Plug-n-Play Azure v316 Discord Bot that is powered by [Lazuli](https://github.com/TEAM-SPIRIT-Productions/Lazuli) and [discord.py](https://github.com/Rapptz/discord.py).

Lapis is inspired by the [MapleDiscBot](https://github.com/Bratah123/MapleDiscBot) project, but aims to be leaner and more layman-friendly.  
Lapis accesses character and inventory attributes in [AzureMSv316](https://github.com/SoulGirlJP/AzureV316)-based databases using the [Lazuli API](https://team-spirit-productions.github.io/Lazuli/reference/lazuli/).  


#### Current Status: **Released!**

## Usage Notes
This project is licensed under the AGPL-3.0 license. This means you're free to modify and distribute it, for both private and commercial use, under the condition that the complete source code for derivative works be made available under the same license.

Note that when a modified version is used to provide a service over a network, this counts as distribution under AGPL-3.0. For instance, if you wish to use Lapis for your public MapleStory Private Server Discord server, and swap out "Lapis" for "CastelaMS" (or whichever server name you desire) in the bot's responses, you ***must*** release the source code for the modified version that you're using.

## About v1.1.3
[CVE-2021-22570 - GitHub Advisory Database](https://github.com/advisories/GHSA-77rm-9x9h-xj3g)  
Following the release of the advisory (see above), we have updated dependencies to include the security patch(es).  
#### If you cloned/downloaded an earlier version, please update ASAP.  

*Note: `aiohttp` is a library used by `discord.py`, which is the basis for most Python-based bots for Discord, including `Lapis`*.  
### To grab the updates
1. Perform `git pull`
2. Grab the new dependencies  
    - For Global Environment:  
      - `pip install -r requirements.txt`  
    - For Virtual Environment:  
      - `venv/scripts/activate`  
      - `pip install -r requirements.txt`  


## Gallery
  ![character](https://cdn.discordapp.com/attachments/631249406775132182/795031817891610644/c76d5804a42f63accb448e8a9e8bf157.png)
  
  ![help](https://cdn.discordapp.com/attachments/631249406775132182/795031808512098334/42b4365e6b819a088fc59d01d11ef27c.png)
## Documentation
Kindly direct any problems or questions to the [Issues](https://github.com/TEAM-SPIRIT-Productions/Lapis/issues) page.  
You may refer to the [wiki](https://github.com/TEAM-SPIRIT-Productions/Lapis/wiki) for a quick start guide.

## Technical Details
*Inherited from Lazuli*

|  | Target Minimum | Target Maximum |
|---|----------------|----------------|
| Python | 3.7 | 3.10 |

NOTE: Please do **not** use Python versions older than 3.7 because:
1. f-strings are used - *requires 3.6 or newer*
2. Dictionaries are assumed to be ordered - *requires 3.6 or newer*
3. Discord.py library is used - *requires 3.6 or newer*
4. protobuf 3.20.1 is used - *requires 3.7 or newer*

### Disclaimer:
*Lapis is an open-source Discord Bot for easy management of a particular MapleStory server emulation project ([AzureMSv316](https://github.com/SoulGirlJP/AzureV316)). Lapis is non-monetised, provided as is, and is unaffiliated with NEXON. Every effort has been taken to ensure correctness and reliability of Lapis. We will not be liable for any special, direct, indirect, or consequential damages or any damages whatsoever resulting from loss of use, data or profits, whether in an action if contract, negligence or other tortious action, arising out of or in connection with the use of Lapis (in part or in whole).*
