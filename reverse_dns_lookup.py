#
# Written by: Nicholas Jelinek
# January 28th, 2021
#
# Insert a list of hostnames/FQDNs and return the IP address according to DNS
#
import socket 
import csv 
import re
import pandas as pd

host_list = open("C:\\path\\to\\input\\list.txt", "r")
hosts = host_list.read().splitlines()

results = {}

for item in hosts:
    try:
        ip_addr = socket.gethostbyaddr(item)
        results[item] = ip_addr
    except socket.gaierror:
        results[item] = "NO VALID HOST NAME"

    except socket.herror:
        results[item] = "No valid hostname"

df = pd.DataFrame(list(results.items()))
df.to_csv("C:\\path\\to\\csv\\file.csv")