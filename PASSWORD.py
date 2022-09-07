"<<<<<!! RANDOM PASSWORD GENRATOR !!>>>>>"
# this will create strong password 

import random

samp_1 = "abcdefghijklmnopqrstuvwxyz"
samp_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
samp_3 = "0123456789"
samp_4 = "!@#$%^&*/?"


a = samp_1 + samp_2 + samp_3 + samp_4
leng_pass = 8 

password = "".join(random.sample(a,leng_pass))
print(password)
