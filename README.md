> **Man shall not live on bread alone,
> but on every word that comes out of the mouth of God. - Mathew 4:4**

# Bible
This is a command line python script, i wrote back in 2019 to aid my daily reading of the Holy Bible.

The Bible is not a single book. It a collection of books written at different time periods.

Reading the Bible cover to cover on your first attempt is sure to leave you confused.

> A 365 day chronological plan allows you to read the bible in the order the events happened.

This script prints out the Bible reading for the day and has other helpful features. See [Usage](#usage) below.

Works on both Linux and Windows with Python3 installed.
Uses standard library, No dependencies.

The reading plan itself was picked up from [biblestudytools.com](https://www.biblestudytools.com/bible-reading-plan/chronological.html).
If you're not command line savvy, I suggest you register on their site and track your progress there.

## Installation
1. Clone the repo.
2. Open your terminal / command prompt / Powershell.
3. Navigate to the script folder
4. For Linux users, make the script executable with ```chmod +x bible```
4. Execute script as ```./bible```

## Usage
Start a new plan with ```--start``` type 'y' when prompted.
```
$ ./bible --start
Start a new Bible plan.
Are you sure? (Y/N) y
Done. Praise the lord!
```

Now ```./bible``` will print the reading for today.
```
$ ./bible
Sun, 19 Mar 2023: Genesis 1-3

```

To check next days reading, use the ```--next``` option
```
$ ./bible --next
Sun 19 Mar 2023: Genesis 1-3 (Today)
Mon 20 Mar 2023: Genesis 4-7
```
You can also check next several days reading by providing a number like ```--next 3```
```
$ ./bible --next 3
Sun 19 Mar 2023: Genesis 1-3 (Today)
Mon 20 Mar 2023: Genesis 4-7 
Tue 21 Mar 2023: Genesis 8-11 
Wed 22 Mar 2023: Job 1-5
```

Similarly you can check the previous day reading with ```--prev```
```
$ ./bible --prev 2
Fri 17 Mar 2023: Job 17-20
Sat 18 Mar 2023: Job 21-23
Sun 19 Mar 2023: Job 24-28 (Today)
```

To get the reading for a specific date use the ```--date``` option with arguments year, month and date
```
$ ./bible --date 2013 3 14
Tue, 14 Mar 2023: Job 6-9

```

To see your reading progress, use ```-stats```
```
$ ./bible -stats
9 days (2.47%) of plan completed.
```
Every once in a while, you might miss several days of reading.

Rather than catching up, you can just continue from the last reading date. Use the ```--continue``` with arguments year, month and date.
Type y after confirming the date and reading.
```
$ ./bible --continue 2023 3 15
Continue reading from Wed Mar 15 2023: Job 10-13.
Confirm (Y/N) y
```

I like [bible-studys.org](https://bible-studys.org) for their explantations, commentary and historical context. So i added an option to print the direct website link for all books to be read.

Use ```--link``` on its own or with the ```--date``` option
```
$ ./bible --link
Sun, 19 Mar 2023: Genesis 1-3

Study links
https://bible-studys.org/genesis-chapter-1
https://bible-studys.org/genesis-chapter-2
https://bible-studys.org/genesis-chapter-3

```

**Ofcourse, if you forget these commands, use the ```--help``` option to print all commands.** Notice there was short options just like any linux terminal app.
```
$ ./bible -help
usage: bible [-h] [-l] [-stats] [-p [N] | -n [N] | -s | -c YYYY MM DD | -d YYYY MM DD]

Prints daily Bible reading using a Chronological 1 year plan

options:
  -h, --help            show this help message and exit
  -l, --links           Print study links
  -stats                Prints reading progress
  -p [N], --prev [N]    Print previous N days readings. N defaults to 1
  -n [N], --next [N]    Print next N days readings. N defaults to 1
  -s, --start           Create new plan
  -c YYYY MM DD, --continue YYYY MM DD
                        Continue reading from specified date
  -d YYYY MM DD, --date YYYY MM DD
                        Get reading for specified date

Be strong and courageous. Do not fear or be in dread of them, for it is the Lord your God who goes with you. He will not leave you or forsake you. - Deuteronomy 31:6
```

**For convenience, I have included ```bible-plan.pdf``` that contains the entire 365 days plan,
Each days reading on a seperate line.