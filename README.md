# farf
FaRF - Find and Replace substrings in many similarly-named files at once

## Purpose
This was a work in progress, but basically, let's say I had a file renaming problem. 
This directory has all the stuff I wanted, but the assets had arbitrary signatures inserted into them, which made them harder to deal with. But I still wanted to preserve parts of the filenames. 

So, with my love of absurd words, I thought of FARF, for find-and-rename-files in a directory. 

```python farf.py "./" " - [LEET H4XOR DEVBRO BRADLEYXYX]" ""```

Turns this:

```./asset01 - [LEET H4XOR DEVBRO BRADLEYXYX].png
./asset02 - [LEET H4XOR DEVBRO BRADLEYXYX].png
./asset03 - [LEET H4XOR DEVBRO BRADLEYXYX].png
./asset04 - [LEET H4XOR DEVBRO BRADLEYXYX].png
...
```
To this:

```./asset01.png
./asset02.png
./asset03.png
./asset04.png
...
```
