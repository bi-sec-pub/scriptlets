#!/bin/bash
input="inputfiledummys/networkranges.txt"
while IFS= read -r line
do
	nmap -sS -sV -p 80,8080,8443,8081,443,21,22,23,25,3389,1433,1521,2483,1526,3306,5432,5500,5800 --max-rate 1000 --min-rate 500 --max-hostgroup 64 --min-hostgroup 64 --max-rtt-timeout 80ms --max-retries 2 --open -oA "$line"_nmap_quick_sV "$line"/16
done < "$input"
