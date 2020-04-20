from django.shortcuts import render
'''
import csv

with open('static_data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
'''
#wardlist
ward = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F_N"
]
#dataset
p = [210847,
     140633,
     202922,
     382841,
     440335,
     250000
     ]
#p = [int(data[i][5]) for i in range(1,25)]

n1 = [5,
      12,
      9,
      18,
      5,
      0
    ]

n2 = [0,
      0,
      0,
      3,
      3,
      0
    ]

n3 = [1,
      3,
      3,
      3,
      2,
      0
    ]

def givecolor(n1,n2,n3,p):
    val = ((n1*1.5+n2*2.6+n3*3.6)/p)*100
    if n1 == 0 and n2 == 0 and n3 == 0:
        return "#00ff00"
    if val >=0.02:
        return "#ff0000"
    elif val>=0.01 and val<0.02:
        return "#ffa500"
    elif val>0 and val<0.01:
        return "#0000ff"

def index(request):
    context = {f'color_{ward[x]}':givecolor(n1[x], n2[x], n3[x], p[x]) for x in range(len(p))}
    return render(request, 'heatmap/index.html', context)
