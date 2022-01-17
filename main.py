from tkinter import *

# GUI Set Up
main = Tk()
main.title("My 3D Print Costs")
main.geometry("600x400")


# Main Headings
title = Label(main, text="My 3D Print Costs", font=("times", 28, "bold"))
mat = Label(main, text="Material Costs", font=("times", 18, "bold"))
lab = Label(main, text="Labor Costs", font=("times", 18, "bold"))
Mar = Label(main, text="Margins", font=("times", 18, "bold"))

# Material Costs Heading
filPrice = Label(main, text="Filament Price: ")
filPrice_field = Entry(main)
filWeight = Label(main, text="Filament Weight (g): ")
filWeight_field = Entry(main)
modWeight = Label(main, text="Model Weight (g): ")
modWeight_field = Entry(main)

# Labor Costs
priPrep = Label(main, text="Printer Preparation (time): ")
priPrep_field = Entry(main)
postProcess = Label(main, text="Postprocessing (time): ")
postProcess_field = Entry(main)

# Margin
percentMaterial = Label(main, text="Percent of Material Cost (%): ")
percentMaterial_field = Entry(main)

# buttons
calc = Button(main, text="Calculate")

# Widget Position Adjustments
title.grid(row=1, column=1)

mat.grid(row=2, column=0)
filPrice.grid(row=3, column=0)
filPrice_field.grid(row=3, column=1)
filWeight.grid(row=4, column=0)
filWeight_field.grid(row=4, column=1)
modWeight.grid(row=5, column=0)
modWeight_field.grid(row=5, column=1)

lab.grid(row=6, column=0)
priPrep.grid(row=7)
priPrep_field.grid(row=7, column=1)
postProcess.grid(row=8)
postProcess_field.grid(row=8, column=1)

Mar.grid(row=9, column=0)
percentMaterial.grid(row=10)
percentMaterial_field.grid(row=10, column=1)

calc.grid(row=11, column=1)

main.mainloop()
