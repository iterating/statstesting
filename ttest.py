import tkinter as tk
from tkinter import messagebox
import scipy.stats as stats

def one_sample_ttest(data, popmean):
    """Conduct a one-sample t-test."""
    t_statistic, p_value = stats.ttest_1samp(data, popmean)
    return t_statistic, p_value

def two_sample_ttest(data1, data2, equal_var=True):
    """Conduct a two-sample t-test."""
    t_statistic, p_value = stats.ttest_ind(data1, data2, equal_var=equal_var)
    return t_statistic, p_value

def paired_ttest(data1, data2):
    """Conduct a paired t-test."""
    t_statistic, p_value = stats.ttest_rel(data1, data2)
    return t_statistic, p_value

def one_sample_ttest_gui():
    root = tk.Tk()
    root.title("One sample t-test")
    tk.Label(root, text="Data:").grid(row=0, column=0)
    tk.Label(root, text="Population mean:").grid(row=1, column=0)
    data_entry = tk.Entry(root)
    mean_entry = tk.Entry(root)
    data_entry.grid(row=0, column=1)
    mean_entry.grid(row=1, column=1)
    def run_test():
        data = [float(x) for x in data_entry.get().split()]
        popmean = float(mean_entry.get())
        t_statistic, p_value = one_sample_ttest(data, popmean)
        messagebox.showinfo("Result", "t-statistic: {}\np-value: {}".format(t_statistic, p_value))
    tk.Button(root, text="Run test", command=run_test).grid(row=2, column=1)
    root.mainloop()

def two_sample_ttest_gui():
    root = tk.Tk()
    root.title("Two sample t-test")
    tk.Label(root, text="Data 1:").grid(row=0, column=0)
    tk.Label(root, text="Data 2:").grid(row=1, column=0)
    data1_entry = tk.Entry(root)
    data2_entry = tk.Entry(root)
    data1_entry.grid(row=0, column=1)
    data2_entry.grid(row=1, column=1)
    tk.Label(root, text="Equal variances?").grid(row=2, column=0)
    equal_var_var = tk.IntVar()
    tk.Radiobutton(root, text="Yes", variable=equal_var_var, value=True).grid(row=2, column=1)
    tk.Radiobutton(root, text="No", variable=equal_var_var, value=False).grid(row=2, column=2)
    def run_test():
        data1 = [float(x) for x in data1_entry.get().split()]
        data2 = [float(x) for x in data2_entry.get().split()]
        equal_var = equal_var_var.get()
        t_statistic, p_value = two_sample_ttest(data1, data2, equal_var)
        messagebox.showinfo("Result", "t-statistic: {}\np-value: {}".format(t_statistic, p_value))
    tk.Button(root, text="Run test", command=run_test).grid(row=3, column=1)
    root.mainloop()

def paired_ttest_gui():
    root = tk.Tk()
    root.title("Paired t-test")
    tk.Label(root, text="Data 1:").grid(row=0, column=0)
    tk.Label(root, text="Data 2:").grid(row=1, column=0)
    data1_entry = tk.Entry(root)
    data2_entry = tk.Entry(root)
    data1_entry.grid(row=0, column=1)
    data2_entry.grid(row=1, column=1)
    def run_test():
        data1 = [float(x) for x in data1_entry.get().split()]
        data2 = [float(x) for x in data2_entry.get().split()]
        t_statistic, p_value = paired_ttest(data1, data2)
        messagebox.showinfo("Result", "t-statistic: {}\np-value: {}".format(t_statistic, p_value))
    tk.Button(root, text="Run test", command=run_test).grid(row=2, column=1)
    root.mainloop()

