# myBasic-python
Basic python programs to run as cron jobs in linux

# Installing

Latest/development library from GitHub:

* `git clone https://github.com/OZoneSQT/myBasic-python`

## Cron job, to run script on a schedule

This part, is what i wished Google told me, when 
learning about cron job's to add costum functions 
to run as a routine in the background

Edit crontab file, or create one if it doesn’t already exist.

```python
crontab -e
```

Then select "nano" as editing tool, navigate to the bottum 
of the file, where you add a line, in the example the 
program will run each night at 1 AM:

```python
# m h dom mon dow   command
  | |  |   |   |
  | |  |   |   +------- day of week (0-6) (sunday = 0)
  | |  |   +----------- month (1-12)
  | |  +--------------- day of month (1-31)
  | +------------------ hour (0-23)
  +-------------------- min (0-59)


  0 1 * * * /home/pi/myBasic-python/autoupdate.py
```

Press [ctrl] + [x] to exit the crontab file, then press [y] to 
confirm the changes to the file.

Then restart the system by pressing [enter] and returning 
to the terminal window.

```python
sudo reboot
```
