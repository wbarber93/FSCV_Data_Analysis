import matplotlib.pyplot as plt
import os

#name = input('100nm-5HT-glutamate-trode2-(3)_CV.txt')
#handle = open(name)
def function():
    
    x_axis = list()
    x_expon = list()
    x_dec = list()

    voltage_axis = list()
    voltage_expon = list()
    voltage_dec = list()

    current_axis = list()
    current_expon = list()
    current_dec = list()

# Assign each column to seperate lists
    for line in f:
        sep = line.split()
        voltage_axis.append(sep[0])
        current_axis.append(sep[1])


# Conversion of exponents to decinmals of Current
    for exp in current_axis:
        conv = exp.split('E')
        exp_num = float(conv[1])
        current_expon.append(10**exp_num)

        dec_num = float(conv[0])
        current_dec.append(dec_num)

# Creates list of exponents and decimals 
    for exp in voltage_axis:
        conv = exp.split('E')
        exp_num = float(conv[1])
        voltage_expon.append(10**exp_num)

        dec_num = float(conv[0])
        voltage_dec.append(dec_num)
    
# Multiples lists of decimals and exponents to give absolute float values
    final_current = [m*n for m, n in zip(current_dec, current_expon)]       
    final_voltage = [j*k for j, k in zip(voltage_dec, voltage_expon)]   
    
    print('The highest current value is: ')
    x_max = max(final_current) 
    print(x_max)

    plt.axhline(0, color='black')
    plt.xlabel('$Time$ (s)')
    plt.ylabel('$Current$ (nA)')
    plt.plot(final_voltage, final_current)
    plt.legend(loc=1)
    plt.savefig(filename+'.png', dpi=400)
    plt.clf()
        
#name = input()
#file = open(name)


directory = '/Users/Wayne/Desktop/Python'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        f = open(filename)
        print('File opened: ',filename)
        function()
        
    else: continue 



        