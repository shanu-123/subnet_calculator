#Subnet using tkinter
from subnetcal import *
import tkinter as tk


win = tk.Tk()
win.title("Subnet Calculator")
win.geometry("600x400")

ip = tk.StringVar(win)
subnet = tk.IntVar(win)
netw =tk.StringVar(win)
brod = tk.StringVar(win)
avail_host = tk.StringVar(win)
rang = tk.StringVar(win)

def clear():
	ip.set('')
	subnet.set(0)
	netw.set('')
	brod.set('')
	avail_host.set('')
	rang.set('')
	

def cal():
	ip_addr = [int(x) for x in ip.get().split(".")]
	sub = subnet.get()
	network_addr = net_addr(ip_addr,sub)
	lst = []
	lst1 = []
	for i in network_addr:
		lst.append(str(i))
	netw.set(".".join(lst))
	broadcast_addr = broad_addr(ip_addr,sub)
	for i in broadcast_addr:
		lst1.append(str(i))
	brod.set(".".join(lst1))
	no_avail,host_ip = available_host(ip_addr,sub)
	avail_host.set(f"Available: {no_avail} Actual avail: {host_ip}")
	network_addr[3] = int(network_addr[3]) + 1
	start_range = ".".join(map(str, network_addr))
	broadcast_addr[3] = int(broadcast_addr[3]) - 1
	end_range = ".".join(map(str, broadcast_addr))
	rang.set(f"{start_range}  '-'  {end_range}")



tk.Label(win,text = "IP Address").grid(row=0,column=0)
ipfield = tk.Entry(win,textvariable=ip)
ipfield.grid(row=0,column=1)

tk.Label(win, text="Subnet").grid(row=1, column=0)
subnetfield = tk.Entry(win, textvariable=subnet)
subnetfield.grid(row=1, column=1)


tk.Button(win,text="Calculate",command = cal).grid(row=3,column=0)
tk.Button(win,text="Clear",command = clear).grid(row=3,column=1)

tk.Label(win,text = "Network Address").grid(row=5,column=0)
netwfield = tk.Entry(win,textvariable=netw)
netwfield.grid(row=5,column=1)

tk.Label(win, text="Broadcast Address").grid(row=6, column=0)
brodfield = tk.Entry(win, textvariable=brod)
brodfield.grid(row=6, column=1)

tk.Label(win,text = "No of available IP").grid(row=7,column=0)
avail_hostfield = tk.Entry(win,textvariable=avail_host)
avail_hostfield.grid(row=7,column=1)

tk.Label(win,text = "Range").grid(row=8,column=0)
rangefield = tk.Entry(win,textvariable=rang)
rangefield.grid(row=8,column=1)

win.mainloop()
