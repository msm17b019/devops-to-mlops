# Machine Learning Concepts

## Features (input data) - "like ingredients in a recipe"

Think of Features as the information you give the computer to help it make a decision.

Example: If you want to predict the predict the price of a house, your features could be:
- Size of the house (in square feet)
- No of bedrooms
- location
- Age of the house

## Labels (output data in supervised learning) - "like the dish you are trying to make from the ingredients"

Labels are the answers you want the computer to learn to predict.

Example:

In a house price prediction model --> label = actual price of the house

In an email spam filter --> label = "spam" or "not spam"

## Training and Testing datasets

Training dataset - The examples the computer learns from.

Testing datasets - New examples the computer hasn't seen before - used to check if it learned well.

Example: 

If you have 1000 photos of cats and dogs:

- Use 800 for training (teach the model)
- Use 200 for testing (see if it can guess correctly for new images)

Training is like studying before an exam. Testing is like the actual exam.

## Overfitting and Underfitting

Overfitting: The model learns too much detail from the training data, including noise and mistakes, and fails on new data. Like memorizing practice exam answers instead of understanding the concepts.

Underfitting: The model learns too little and can't even do well on training data. Like barely studying and hoping to guess the answers.

Good models learn patterns, not memorized answers.

## Accuracy, Precision, Recall and F1 score

There are ways to measure how good your model is - especially for classification problems.

### Accuracy

Hoe often the model is correct.

Example: If it predicts correctly 90 out of 100 times --> 90 % accuracy.

### Precision

Out of all the things the model said were "positive", how many were actually correct?

Example: If the model says 10 emails are spam, but only 8 really are --> precision 80 %.

### Recall

Out of all the actual "positive" things, how many did the model match?

Example: If there are 12 spam emails in total, and the model catches 8 --> Recall = 8/12 = approx 67 %

### F1 Score

F1 = 2 × (Precision × Recall) / (Precision + Recall)

A balance between precision and recall. Useful when both are important.

When F1 score is important?
- When your data is unbalanced (one category appears much more than the other)
- When missing a positive is as bad as or worse than a false alarm.

Examples: Detecting diseases, fraud detection, spam filtering.

### Summary

Accuracy: How often you are right overall

Precision: When you say "This is cat", how often are you right?

Recall: Out of all the cats, how many did you find.

F1 score: Balances the two so you are not just good at one.

### Still Confused???

Scenario: finding cats in photos

You have 100 photos
- 30 are cats (actual positives)
- 70 are not cats (actual negatives)

Your model make predictions:
- Says 25 photos are cats -> 20 are correct (Cats), 5 are wrong (actually dogs)
- Misses 10 real cats in the process

**Accuracy**: How many predictions were correct.

20 cats + 60 (non-cats) = 80

So, 80/100 = 80 % accuracy

Biggest probelm: Accuracy can be misleading if data is unbalanced (e.g., very few cats)

**Precision**: How much you trust positive predictions.

When the model says cats, how often is it right?

correct 'cat' predictions = 20
Total 'cat' predictions = 25

Precision = 20/25 = 80 %

Precision = Correctness of positive guesses.

**Recall**: How many actual positives you caught

Out of all the real cats, how many did the model find?

Correct cat predictions = 20
Total actual cats = 30

Recall = 20/30 = approx 67 %

Recall = coverage of actual positives.

**F1 Score**

F1 = 2 × (0.80 × 0.67) / (0.80 + 0.67) = approx 0.729 = approx 72.9 %

F1 score is like a refree between precision and recall - it won't let you win unless you are good at both.
