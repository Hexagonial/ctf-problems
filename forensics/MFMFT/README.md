my first mft

# Name
MFMFT

## Category
Forensics/Programming

## Points
150 (Intermediate)

## Author
Hexagonial

## Description
I stole my boss' flash drive. Rumor has it that he keeps the password to the payroll database fragmented across the filenames of the contents of his USB drive. I have a segment of the NTFS Master File Table here - can you help me figure out the password? I would like to give myself a 200% raise.

Oh, this might help:

[0, 10, 17, 18, 5, 6, 15, 13, 9, 16, 12, 5, 11, 1, 14, 5, 7, 6, 7, 3, 2, 2, 10, 8, 4, 7]

Wrap what you find with `texsaw{}`! If the password is `password`, enter `texsaw{password}`.

## Solution
The file name for each entry in the MFT is stored 0xda bytes from the start of the entry (denoted by FILE0), and each entry is 0x400 bytes long. Each filename can simply be retrieved by the formula _i_*0x400+0xda where _i_ is the index.

You can find the basic structure of an NTFS MFT entry [here](https://www.futurelearn.com/info/courses/introduction-to-malware-investigations/0/steps/146529).

## Flag
`texsaw{34sy_brEezY_MFT_7b7f224587}`

### Notes:
Possible way to buff the challenge to make it harder: Make the filenames not all 1 character long. Forces players to actually parse the MFT for the file name lengths. Then, add bogus data via hexedit to make file names look longer than they actually are.
