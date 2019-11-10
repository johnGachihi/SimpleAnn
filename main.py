import pandas as pd
from util.math_ops import bind_between_0_1


"""Read Training Data"""
data = pd.read_csv("training_data.csv", header=None)

"""Bind values between 0 and 1"""
data = data.applymap(lambda value: bind_between_0_1(
    value, data.max().max(), data.min().min()))

"""Separate Target Output Data and Input Data"""
output_target = data.iloc[:, -1].values
input_data = data.drop(3, axis=1).values

"""Define Initial Weights"""
weights = [
    [[0.2, 0.3, 0.2],
     [0.1, 0.1, 0.1]],   [[0.5, 0.1]] ]

print(input_data)