# Project-2
🍄 **README**

🌟 **Using Mushroom Dataset to Train Machine Learning Models to Predict if Mushrooms are Edible or Poisonous with integration into an AWS Lex Bot and Website**

📝 **Introduction:**
This README provides a comprehensive guide on using the Mushroom dataset to train machine learning models to predict if a mushroom is poisonous or edible, to implement a model into an AWS Lex Bot for mushroom identification, and to integrate the chatbot into an HTML/CSS website for user interaction.

📊 **Dataset:**
The Mushroom dataset contains various attributes of poisonous and edible mushrooms such as cap shape, cap surface, cap color, bruises, odor, gill attachment, gill spacing, etc. It serves as the foundation for training machine learning models to distinguish between edible and poisonous mushrooms.
[View dataset](/Resources/mushrooms.csv.ipynb)

📊 **Feature and Class Distributions:**
Exploratory data analysis was conducted to visualize feature and class distributions. This analysis provided insights into the dataset's characteristics and helped identify patterns or correlations that influence the model's training.
[View data analysis](/Data_Analysis.ipynb)
![Bubble Scatter Graph](/Images/bubble%20graph.png)
![Bar Graph](/Images/cute%20feat%20dist%20bar.png)
![E and P Graph](/Images/bar%20graph.png)

🔍 **Data Enhancement:**
The dataset allows for perfect classification of mushrooms as poisonous or edible with simple machine learning models. Given this, we explored adding synthetic noise to the training set to better simulate real world scenarios. We also explored reducing the dimensionality of the data, creating models that only took in 9 characteristics about the mushrooms. Both the models trained on the noisy data and the models trained on the smaller datasets still were able to perfectly predict whether a mushroom is poisonous or edible. 
[View model development](/Model_Development.ipynb)

🌲 **Decision Tree Classifier:**
Ultimately the Decision Tree Classifier requiring only 9 values was implemented into the AWS chatbot for user ease and given its perfect predictive capabilities in the training set. It had 100% accuracy in the training and testing set data as well as a precision, recall, and F1-score of 1.00. See the decision tree plotted below and confusion matrix below. Please refer to the kaggle dataset for what each node is referring to in the decision tree plot. 
[View model development](/Model_Development.ipynb)

![Decision Tree Plot](/Images/Mushrooms_simplified_decision_tree.png)

![Confusion Matrix for Decision Tree](/Images/Confusion_matrix_decision_tree.png)

💬 **AWS Lex Bot Development:**
An AWS Lex Bot was created to facilitate mushroom poisonous vs. edible differentiation through user interaction. Intents and slot types were defined for mushroom attributes, and Lambda functions in Python were implemented for bot fulfillment logic. 
[View JSON file for Bot Development](/JASON%20bot)

🌐 **Website Integration:**
To enhance user experience, the AWS Lex Bot was integrated into an HTML/CSS website. The website provides a user-friendly interface for interacting with the bot, allowing users to input mushroom attributes and receive identification results.
[View website code](/web_page_fungi.html)

🛠️ **Steps:**
1. **Data Preprocessing:** No data cleaning was required given the nature of the dataset. Synthetic noise was introduced to simulate real world conditions.
2. **Training Machine Learning Models:** Initialize and train the Machine learning models as appropriate.
3. **AWS Lex Bot Development:** Create an AWS Lex Bot with appropriate intents, slot types, and Lambda functions for fulfillment logic.
4. **Website Integration:** Develop an HTML/CSS website with a chat interface to interact with the AWS Lex Bot.
5. **Deployment:** Deploy the trained Decision Tree model into the AWS Lex Bot on AWS, and integrate the bot into the website. 

🚀 **Usage:**
1. Clone the repository and set up the environment.
2. Execute the provided scripts for model training, bot development, and website deployment.
3. Deploy the Decision Tree model, AWS Lex Bot, and website on their respective platforms.
4. Test the integrated system thoroughly to ensure proper functionality and user experience.

🛠️ **Next Steps:**
1. Train and validate Convolutional Neural Networks to parse out mushroom 
attributes
2. Setup pipeline to convert these attributes to a dataframe and run this
through the Decision Tree model to determine if poisonous or edible. 
3. Validate the current Decision Tree Model on exterior datasets. 
4. Expand the current machine learning models on more mushroom datasets. 

📌 **Note:**
- Regularly monitor and update the Decision Tree model, AWS Lex Bot, and website to maintain optimal performance and address any issues.
- Consider incorporating user feedback and suggestions to improve the bot's accuracy and usability.

🔗 **References:**
- [Mushroom Dataset on Kaggle](https://www.kaggle.com/uciml/mushroom-classification)
- [AWS Lex Documentation](https://docs.aws.amazon.com/lex/index.html)
- [HTML/CSS Tutorials](https://www.w3schools.com/html/) and [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

🙌 **Contributors:**
- John Parente Jr. 
- McKala Krauss
- Richard Varos
- Samuel Neal
- ChatGPT

Feel free to contribute to this project by submitting pull requests or reporting issues. Thank you for using our Mushroom Dataset with Decision Tree Classifier, AWS Lex Bot, and Website Integration!
