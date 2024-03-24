
# Name
Buffet Overflow

## Category
pwn

## Points
150 (Intermediate)

## Author
Hexagonial

## Description (wip)
The grand opening of the all-new, revolutionary "webstraunt" has finally arrived!!! To celebrate, the webstraunt is holding several kinds of all-you-can-eat buffets for just $200, accessible right from your desktop! Give us a visit at `nc 3.23.56.243 9009` to place your reservation NOW!!!!!! 

Cookies might not be on the menu - but PIE is! 

\* Disclaimer: There may be security flaws in our ordering platform. Please remember that we are a small indie startup, and do not abuse the bugs.

## Solution
Exploit is in exploit.py
1. Leak relevant code addresses using FSV in the first input.
2. Calculate the address of secretMenu() using the leaked addresses (can find offset using gdb)
3. Overflow the return address to point to secretMenu().

If the player is able to pop a shell (such as via ROP) it should be a valid solution as well. Just need to make sure they cannot modify the flag file.

## Flag
`texsaw{n0t_web_NOR_a_r3st4urant_3adcdcd2}`

## Compiling the Program
`gcc -fno-stack-protector -m32 -pie -o webstraunt webstraunt.c`
