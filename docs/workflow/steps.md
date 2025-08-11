# ML Workflow Step by Step

## 1. Collect data - "Get the ingredients"

You can't cook without ingredients.

In ML, your ingredients are the data - images, text, numbers, sensor reading, etc.

Example: If you are building a spam filter, your data might be thousands of emails labeled 'spam' or 'not spam'.

## 2. Clean/prepare data - "Wash and cut the vegetables"

Raw data is usually messy - it may have missing values, wrong formats, duplicates, or noise. You fix these problems so the model can learn properly.

Example: Removing broken email records, correcting typos, or converting all text to lowercase.

## 3. Choose a model - "Pick the recipe"

The model is the method or algorithm you will use to make predictions.

Example: [decision trees](../links/algo.md), [linear regression](../links/algo.md), [neural networks](../links/algo.md).

## 4. Train the model - "Cook the dish"

You give the model your training data so it can learn the patterns.

Example: Feed the model thousand of emails so it learns what spam looks like.

## 5. Evaluate the model - "Taste and adjust"

You test the model on new data it hasn't seen before to check if its good.

This is where you use accuracy, precision, recall and F1 score to judge performance.

If it's not good enough, you go back, tweak the recipe, or collect better data.

## 6. Deploy the model - "Serve the meal"

Since the model is good, you put it into real use so it can make predictions for actual users.

Example: Your spam filter now automatically sorts incoming emails in gmail.

In short, 

data --> clean --> Model --> Train --> Test --> Use in the real world