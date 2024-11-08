import tkinter as tk
from scipy.stats import logrank_test

def logrank_test_(group1, group2):
    """Conduct a logrank test."""
    t_statistic, p_value = logrank_test(group1, group2)
    return t_statistic, p_value

def logrank_test_gui():
    root = tk.Tk()
    root.title("Logrank Test")
    tk.Label(root, text="Group 1:").grid(row=0, column=0)
    tk.Label(root, text="Group 2:").grid(row=1, column=0)
    group1_entry = tk.Entry(root)
    group2_entry = tk.Entry(root)
    group1_entry.grid(row=0, column=1)
    group2_entry.grid(row=1, column=1)
    def run_test():
        group1 = [float(x) for x in group1_entry.get().split()]
        group2 = [float(x) for x in group2_entry.get().split()]
        t_statistic, p_value = logrank_test_(group1, group2)
        messagebox.showinfo("Result", "t-statistic: {}\np-value: {}".format(t_statistic, p_value))
    tk.Button(root, text="Run test", command=run_test).grid(row=2, column=1)
    root.mainloop()

