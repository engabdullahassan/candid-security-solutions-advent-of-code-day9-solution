**Abdullah Hassan** 

+971568189886 |[ eng.abdullahmourad@gmail.com](mailto:eng.abdullahmourad@gmail.com)

**Candid Security Solutions – Advent of Code 9** 

1. **Introduction** 

This document outlines the approach and solution for the Advent of Code 2023 Day 9 challenge. The task involved extrapolating the next values in a given sequence of numbers and summing them up. ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.001.png)

2. **Problem Description** 

The challenge provided a series of sequences and required predicting the next value in each sequence. The sequences were: 

- [0, 3, 6, 9, 12, 15] 
- [1, 3, 6, 10, 15, 21] 
- [10, 13, 16, 21, 30, 45] 

The solution involves creating sequences of differences until all differences are zero, and then using these sequences to extrapolate the next value. ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.002.png)

3. **Approach** 

The approach used to solve the problem was as follows: 

1. **Calculate Differences**: For each sequence, calculate the differences between consecutive elements. 
1. **Iterate Until Zero Differences**: Repeat the calculation of differences until all values in the difference sequence are zero. 
1. **Extrapolate Next Value**: Once a sequence of zeros is reached, use the last difference to find the next value in the original sequence. 

For the first sequence [0, 3, 6, 9, 12, 15, 18]: 

- Differences: [3, 3, 3, 3, 3, 3, 3] 
- Differences of Differences: [0, 0, 0, 0, 0, 0] 
- Next Value: 18 + 3 = **21** 
- Final sequence: [0, 3, 6, 9, 12, 15, 18, 21] 

For the second sequence [1, 3, 6, 10, 15, 21, 28]: 

- Differences: [2, 3, 4, 5, 6, 7, 8] 
- Differences(1) of Differences: [1, 1, 1, 1, 1, 1] 
- Next Value: 28 + 8 = **36** 
- Final sequence: [1, 3, 6, 10, 15, 21, 28, 36] 

For the third sequence [10, 13, 16, 21, 30, 45, 68]: 

- Differences: [3, 3, 5, 9, 15, 23, 33] 
- Differences(1) of Differences: [0, 2, 4, 6, 8, 10] 
- Differences(2) of Differences(1): [2, 2, 2, 2, 2] 
- Next Value: 68 + 33 = **101** 
- Final sequence: [10, 13, 16, 21, 30, 45, 68, 101] 

Sum of all new extrapolated values = 21 + 36 + 101 = **158 ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.003.png)**

4. **Solution** 

The solution was implemented in Python. Below is the code that computes the next value for each sequence and sums them up. 

def extrapolate\_next\_value(sequence): ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.004.png)    history = [sequence] 

`    `while True: 

`        `last\_sequence = history[-1] 

- Calculate the differences between consecutive elements 

`        `differences = [last\_sequence[i+1] - last\_sequence[i] for i in ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.005.png)range(len(last\_sequence)-1)] 

`        `history.append(differences) 

- Check if all differences are zero 

`        `if all(diff == 0 for diff in differences): 

`            `break 

- Calculate the next value for each level from bottom to top ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.006.png)

`    `for i in range(len(history)-1, 0, -1): 

- Get the next value by adding the last element of the current level 
- to the corresponding difference from the level below ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.007.png)

`        `next\_value = history[i-1][-1] + history[i][-1] 

`        `history[i-1].append(next\_value) 

- Return the next value of the original sequence return history[0][-1] 

def main(): 

- Define the input sequences 

`    `input\_data = [ 

`        `[0, 3, 6, 9, 12, 15, 18], 

`        `[1, 3, 6, 10, 15, 21, 28], 

`        `[10, 13, 16, 21, 30, 45, 68] 

`    `] 

- Calculate the next values for each sequence 

`    `next\_values = [extrapolate\_next\_value(seq) for seq in input\_data] 

- Calculate the total sum of the next values ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.008.png)total\_sum = sum(next\_values) 
- Print the results 

  print("Next values:", next\_values) 

  print("The sum of the extrapolated next values is:", total\_sum) 

if \_\_name\_\_ == "\_\_main\_\_":     main() 

Results: ![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.009.png)

![](Aspose.Words.30e73627-252e-425f-8609-028f85adb370.010.png)

5. **Conclusion** 

By implementing the described approach, the next values for each sequence were accurately predicted as 21 for the first sequence, 36 for the second sequence, and 101 for the third sequence, along with their sum which was computed as 158. This method demonstrates an effective way to solve sequence extrapolation problems using iterative difference calculations. 
