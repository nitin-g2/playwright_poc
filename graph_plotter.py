import matplotlib.pyplot as plt
import csv
import datetime
import time
import pandas as pd
import numpy as np



cpu_line = []
memory_line = []
time_line = []
headers = ["container_name", "cpu_perc", "memory_perc", "mem_usage", "net_io", "block_io", "container_id", "time"]
with open('400.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        if row:
            c_perc, m_perc, t_val = row[1], row[2], row[-1] 
            x = time.strptime(t_val.split(',')[0],'%H:%M:%S')
            time_in_secs = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            cpu_line.append(float(c_perc[:-1]))
            memory_line.append(float(m_perc[:-1]))
            time_line.append(row[-1])



intermediate_dictionary = {"time": [i+1 for i in range(len(cpu_line))], 'CPU':cpu_line}
df1 = pd.DataFrame(intermediate_dictionary)
df2 = df1.set_index("time")
title = f"CPU:1_page:1_context:{len(cpu_line)}_iteratations"
plt.title(title)
df2.plot()
plt.savefig(f'{title}.png')

intermediate_dictionary = {"time": [i+1 for i in range(len(memory_line))], 'MEM':memory_line}
df1 = pd.DataFrame(intermediate_dictionary)
df2 = df1.set_index("time")
title = f"MEM:1_page:1_context:{len(memory_line)}_iteratations"
plt.title(title)
df2.plot()
plt.savefig(f'{title}.png')