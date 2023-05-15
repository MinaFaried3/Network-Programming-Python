from time import ctime

import ntplib

c = ntplib.NTPClient()
response = c.request('europe.pool.ntp.org', version=3)
print(ctime(response.tx_time))
