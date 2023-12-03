from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Select Shape:')
        self.lbl2 = Label(win, text='Select Calculation:')
        self.t1 = StringVar()
        self.t2 = StringVar()
        shapes = ['Circle', 'Rectangle', 'Sphere', 'Cone']
        calculations = ['Area', 'Perimeter', 'Curved Area', 'Volume', 'Total Surface Area']
        self.shape_dropdown = OptionMenu(win, self.t1, *shapes)
        self.calculation_dropdown = OptionMenu(win, self.t2, *calculations)
        self.shape_dropdown.place(x=200, y=10)
        self.calculation_dropdown.place(x=200, y=50)
        self.lbl1.place(x=100, y=10)
        self.lbl2.place(x=100, y=50)
        self.dimension_label_1 = Label(win, text='Enter 1st Dimension:')
        self.dimension_label_1.place(x=100, y=90)
        self.dimension_entry_1 = Entry(win)
        self.dimension_entry_1.place(x=200, y=90)
        self.dimension_label_2 = Label(win, text='Enter 2nd Dimension:')
        self.dimension_label_2.place(x=100, y=110)
        self.dimension_entry_2 = Entry(win)
        self.dimension_entry_2.place(x=200, y=110)
        self.dimension_label_3 = Label(win, text='Enter 3rd Dimension:')
        self.dimension_label_3.place(x=100, y=130)
        self.dimension_entry_3 = Entry(win)
        self.dimension_entry_3.place(x=200, y=130)
        self.result_label = Label(win, text='')
        self.result_label.place(x=200, y=170)
        self.btn = Button(text='Submit', command=self.calculate)
        self.btn.place(x=200, y=210)

    def calculate(self):
        selected_shape = self.t1.get()
        selected_calculation = self.t2.get()
        d1 = self.dimension_entry_1.get()
        d2 = self.dimension_entry_2.get()
        d3 = self.dimension_entry_3.get()
        result = "Result: " 
        if selected_shape == 'Circle':
            if selected_calculation == 'Area':
                res = str(3.14 * float(d1)*float(d1))
                result += res
            elif selected_calculation == 'Perimeter':
                result += "no Perimeter Calculation"
            elif selected_calculation == 'Curved Area':
                result += "Circle Curved Area Calculation"
        elif selected_shape == 'Rectangle':
            if selected_calculation == 'Area':
                res = float(d1) * float(d2)
                result += str(res)
            elif selected_calculation == 'Perimeter':
                res = 2 * (float(d1) + float(d2))
                result += str(res)
            elif selected_calculation == 'Curved Area':
                result += "no Curved Area Calculation"
        elif selected_shape == 'Sphere':
            if selected_calculation == 'Volume':
                res = 1.33 * 3.14 * (float(d1) * float(d1) * float(d1))
                result += str(res)
            elif selected_calculation == 'Perimeter':
                result += "no Perimeter Calculation"
            elif selected_calculation == 'Area':
                result += "no Area Calculation"
            elif selected_calculation == 'Total Surface Area':
                res = 4 * 3.14 * (float(d1) * float(d1))
                result += str(res)
        elif selected_shape == 'Cone':
            if selected_calculation == 'Volume':
                res = 0.3333 * 3.14 * (float(d1) * float(d1)) * float(d2)
                result += str(res)
            elif selected_calculation == 'Perimeter':
                result += "no Perimeter Calculation"
            elif selected_calculation == 'Area':
                result += "no Area Calculation"
            elif selected_calculation == 'Total Surface Area':
                res = 3.14 * float(d1) * (float(d1) + float(d2))
                result += str(res)
        self.result_label.config(text=result)

window = Tk()
mywin = MyWindow(window)
window.title('Shape Calculator')
window.geometry("500x300+10+10")
window.mainloop()