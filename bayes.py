import tkinter as tk
from tkinter import messagebox

class BayesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bayesian Probability Calculator")
        self.geometry("400x150")
        self.resizable(False, False)

        # Create labels and entry fields
        self.prior_label = tk.Label(self, text="Prior Probability:")
        self.prior_label.pack()
        self.prior_entry = tk.Entry(self)
        self.prior_entry.pack()

        self.likelihood_label = tk.Label(self, text="Likelihood:")
        self.likelihood_label.pack()
        self.likelihood_entry = tk.Entry(self)
        self.likelihood_entry.pack()

        self.posterior_label = tk.Label(self, text="Posterior Probability:")
        self.posterior_label.pack()
        self.posterior_entry = tk.Entry(self)
        self.posterior_entry.pack()

        # Create button to calculate
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        prior = float(self.prior_entry.get())
        likelihood = float(self.likelihood_entry.get())
        posterior = prior * likelihood
        self.posterior_entry.delete(0, tk.END)
        self.posterior_entry.insert(0, str(posterior))

if __name__ == "__main__":
    app = BayesApp()
    app.mainloop()
