# Log Rank Test and T-tests

The log rank test is a non-parametric test for comparing the survival distributions of two groups. It is commonly used to test the difference in survival between two groups, such as treatment and control groups in a clinical trial.

The t-test is a parametric test for comparing the means of two groups. It is commonly used to test the difference in means between two groups, such as the mean of a treatment group versus the mean of a control group.

This repository contains code for performing log rank tests and t-tests in R and Python. The code is organized into two folders: R and Python.


### Python

The Python code is contained in the Python folder. It contains a single function, `logrank_test`, which performs the log rank test. The function takes two arguments: `time` and `event`. The `time` argument is a vector of times, and the `event` argument is a vector of events (0 or 1). The function returns a list containing the results of the test.

The Python code also contains a single function, `ttest`, which performs the t-test. The function takes two arguments: `x` and `y`. The `x` argument is a vector of values for the first group, and the `y` argument is a vector of values for the second group. The function returns a list containing the results of the test.

### R-  depreciated

The R code was contained in the R folder. It contains a single function, `logrank_test`, which performs the log rank test. The function takes two arguments: `time` and `event`. The `time` argument is a vector of times, and the `event` argument is a vector of events (0 or 1). The function returns a list containing the results of the test.

The R code also contains a single function, `ttest`, which performs the t-test. The function takes two arguments: `x` and `y`. The `x` argument is a vector of values for the first group, and the `y` argument is a vector of values for the second group. The function returns a list containing the results of the test.
