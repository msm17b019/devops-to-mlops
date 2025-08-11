# Python Libraries

Python is like the swiss army knife of ML - its simple to write, has tons of ready made tools, and the ML community loves it.

It's not the fastest language - but it's the most practical for data work.

## pandas - data handling

Think of pandas as Excel for python, but much faster and more powerful.

Lets you store, clean and analyze data in tables (DataFrames)

Example: Load a csv of house prices, filter houses in Bengaluru, and find average price.

You use pandas when you want to load data, remove duplicates, fill missing values, or sort/filter rows.

## numpy - number crunching

numpy is like a super calculator for python.

handles arrays, matrices, and heavy math operations very fast.

Many ML tools use numpy behind the scenes.

You use numpy when you need fast math on big lists of numbers.

## matplotlib/seaborn - visualizing data

matplotlib is the basic drawing library (line charts, bar graphs, scatter plots)

seaborn is built on top of matplotlib but looks prettier and is easier for statistical graphs.

You use them when you want to understand your data visually - patterns, trends, correlations.

## scikit-learn - 'training simple ML models'

The easiest library to start doing ML in python.

Has ready-made algorithms for:
- [classification](../links/algo.md) (spam v/s not-spam)
- [regression](../links/algo.md) (predicting house prices)
- [clustering](../links/algo.md) (grouping customers)

Also has tools to split data, evaluate models, and preprocess features.

## Order of Learning

1. Start with pandas - play with loading and cleaning data
2. learn numpy basics - understand arrays, and operations
3. use matplotlib/seaborn - visualize your data
4. finally scikit-learn - train a small ML model
