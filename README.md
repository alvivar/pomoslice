# pomoslice v0.1

Some times is kind of scary to think about time in this way. Hm.

```
usage: pomoslice.py [-h] -t HOURS -b BATCHES [-r REST_RATIO]

tool that time boxes hours into batches of work and rest

optional arguments:
  -h, --help            show this help message and exit
  -t HOURS, --hours HOURS
                        hours that you wanna work
  -b BATCHES, --batches BATCHES
                        batches of work & rest that you wanna do
  -r REST_RATIO, --rest-ratio REST_RATIO
                        percentage of the batch used for resting (default 25)
```

**$ pomoslice.py -t 8 -b 7**
```
In 8.0 hours,
you should work 7 batches of 52 minutes,
resting 17 minutes in between,
for a total of 6.1 effective hours!
```
