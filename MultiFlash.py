# To push user input data to ASPEN, run the simulation and produce the flash plot as pdf
# A template simulation file with a flash drum [1 inlet stream & 2 outlet stream] to be made prior.
# Inlet stream name to be defined:"Input", liq outlet: "Liquid", Vap out: "Vapor"
# units used here: English --> simulation to have same unit!

#######################
import os #packing to use os functions like file directory navigation
import win32com.client as win32 #packaging to use COM for windows appliactions
import numpy as np
import matplotlib.pyplot as plt


aspen = win32.Dispatch('Apwn.Document.36.0') #argument apwn.document tells PGID for Aspen file
#34.0 ---> V8.8; 35.0 ---> V9.0; and 36.0 ---> V10.0
aspen.InitFromArchive2(os.path.abspath('data\Flash_Example.bkp'))
#tells the path for aspen file

T = np.linspace(100, 300, 5) #np array for temperatures

x_comp, y_comp = [], [] #empty list for initiation of mole fractions in vapor and liquid phase

print("Enter the component name to generate flash curve:")
comp_name=input()

for temperature in T:
    aspen.Tree.FindNode('\Data\Blocks\FLASH\Input\TEMP').Value = temperature #pushes the temperature to the "node" in aspen
    aspen.Engine.Run2() #for every temperature input the simulation is run

    x_comp.append(aspen.Tree.FindNode('\Data\Streams\LIQUID\Output\MOLEFRAC\MIXED\Comp_name').Value) #get the molefraction of liquid stream
    #if NameError occurs, directly copy past the node from eqaution oriented tab in ASPEN
    y_comp.append(aspen.Tree.FindNode('\Data\Streams\VAPOR\Output\MOLEFRAC\MIXED\Comp_name').Value) #get the mole fraction of vapor stream

#x and y lists will be filled with mole fraction values now
#using matplotlib to plot the results 
plt.plot(T, y_comp, T,  x_comp) #a single plot for multi lines
plt.legend(['vapor', 'liquid'])
plt.xlabel('Flash Temperature (degF)')
plt.ylabel(Comp_name, 'mole fraction')
plt.savefig('images/aspen-component-flash.pdf') #saves the file in pdf format
aspen.Close()


#DevBy:Jeevs
