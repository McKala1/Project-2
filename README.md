# Project-2
🍄 **README**

🌟 **Using Mushroom Dataset with Random Forest Classifier, AWS Lex Bot, and Website Integration**

📝 **Introduction:**
This README provides a comprehensive guide on using the Mushroom dataset to train a Random Forest Classifier, deploying it as an AWS Lex Bot for mushroom identification, and integrating it into an HTML/CSS website for user interaction.

📊 **Dataset:**
The Mushroom dataset contains various attributes of mushrooms such as cap shape, cap surface, cap color, bruises, odor, gill attachment, gill spacing, etc. It serves as the foundation for training a Random Forest Classifier to distinguish between edible and poisonous mushrooms.

🔍 **Data Enhancement:**
To improve the dataset's diversity and model performance, synthetic noise was introduced to create variations in certain attributes. Additionally, new features were added to enrich the dataset and enhance the model's learning capabilities.

📊 **Feature and Class Distributions:**
Exploratory data analysis was conducted to visualize feature and class distributions. This analysis provided insights into the dataset's characteristics and helped identify patterns or correlations that influence the model's training.

🌲 **Random Forest Classifier:**
The Random Forest Classifier is a robust machine learning algorithm used for classification tasks. It constructs multiple decision trees during training and outputs the mode of the classes (classification) or mean prediction (regression) of the individual trees.

💬 **AWS Lex Bot Development:**
An AWS Lex Bot was created to facilitate mushroom identification through user interaction. Intents and slot types were defined for mushroom attributes, and Lambda functions in Python were implemented for bot fulfillment logic.

🌐 **Website Integration:**
To enhance user experience, the AWS Lex Bot was integrated into an HTML/CSS website. The website provides a user-friendly interface for interacting with the bot, allowing users to input mushroom attributes and receive identification results.

🛠️ **Steps:**
1. **Data Preprocessing:** Handle missing values, encode categorical variables, introduce synthetic noise, and add new features to the Mushroom dataset.
2. **Training Random Forest Classifier:** Initialize and train the Random Forest Classifier model using the enhanced dataset.
3. **AWS Lex Bot Development:** Create an AWS Lex Bot with appropriate intents, slot types, and Lambda functions for fulfillment logic.
4. **Website Integration:** Develop an HTML/CSS website with a chat interface to interact with the AWS Lex Bot.
5. **Deployment:** Deploy the trained Random Forest Classifier model and AWS Lex Bot on AWS, and host the website on a suitable web hosting platform.

🚀 **Usage:**
1. Clone the repository and set up the environment.
2. Execute the provided Python scripts for data preprocessing, model training, and bot development.
3. Deploy the Random Forest Classifier model, AWS Lex Bot, and website on their respective platforms.
4. Test the integrated system thoroughly to ensure proper functionality and user experience.

📌 **Note:**
- Regularly monitor and update the Random Forest Classifier model, AWS Lex Bot, and website to maintain optimal performance and address any issues.
- Consider incorporating user feedback and suggestions to improve the bot's accuracy and usability.

🔗 **References:**
- [Mushroom Dataset on Kaggle](https://www.kaggle.com/uciml/mushroom-classification)
- [AWS Lex Documentation](https://docs.aws.amazon.com/lex/index.html)
- [HTML/CSS Tutorials](https://www.w3schools.com/html/) and [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

🙌 **Contributors:**
- [Your Name/Organization]

Feel free to contribute to this project by submitting pull requests or reporting issues. Thank you for using our Mushroom Dataset with Random Forest Classifier, AWS Lex Bot, and Website Integration!
