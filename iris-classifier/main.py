#detecting iris-flowers using supervised learning

from sklearn.datasets import load_iris   #this has iris dataset so we dont need to download anything

iris = load_iris()   #loading the dataset

# print(type(iris))   #class
# print(iris.keys())   # we will use ,  data: measurements of flower, target: species of each flower stored as number (0,1,2)
# print(iris.feature_names)    #names of the measurements sepal len, sepal width, petal len, petal width
# print(iris.target_names)  #species setosa,versicolor,virginica
# print(iris.data[0])  #there are 150 entries in the dataset, so this will show the measurements of 1st flower
# print(iris.target[0])   #acc to the measurements, to which specie that flower relates
# print(iris.target_names[iris.target[0]])  #name of the specie of the given flower
# print(iris.data.shape)   #.shape : no. of rows and col data have  (150,4)
# print(iris.target.shape)  #(150,) this represents 1D array. { (150,) != (150,1)  (150,1) represents matrix with 150 rows and 1 col


#Converting to a DataFrame
import pandas as pd

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target_names[iris.target]   #adding species column

# print(df.head())   #prints the first 5 rows  [df.head(n) : prints n rows]     mainly used to inspect the beginning of a dataset.   df.tail(): last 5 entries

#Exploratory Data Analysis (EDA)
# print(df.info())   #information about each col
# print(df.describe())    #element count, mean, standard deviation, min, 25%,50%,75%,max in each col
# print(df.isnull().sum())   #checking out the missing values.  we are doing this b/c most ml algorithms cant train if input have missing values(NaN)
# print(df["species"].value_counts())   #count the no. of flowers in each species

#----------TRAINING MODEL------------

#split the data - we dont train the entire dataset. we split it into Traning set and Testing Set

from sklearn.model_selection import train_test_split

X = df.drop("species", axis=1)   #x (uppercase): Features (input var). x contains 4 measurements b/c species col is removed from it
y = df["species"]       #y (lowercase): Target or Label (what we want to predict). y contains flower species

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,   # 20% of the data is kept for testing
    random_state = 42  #ensures the split is the same every time you run the program. This makes your experiments reproducible.
)


#ML Algorith  
# k-Nearest Neighbors (k-NN) : b/c its intuitive. It doesnt learn qen loke some algo. instead it ans "Which training flowers are most similar to this new flower?"
# Then it lets those nearest neighbors "vote" on the species.
# eg if new flower's 3 nearest neighbors are - setosa setosa and versicolor , it will predict SETOSA. b/c it recieved 2/3 votes
# *This introduces a fundamental ML idea: similar inputs tend to have similar outputs.

from sklearn.neighbors import KNeighborsClassifier  #importing classifier

model = KNeighborsClassifier(n_neighbors=3)   #it will check 3 nearest neighbors of new flower. Why not k=1? b/c prediction becomes wrong immediately. Why not k=100? b/c we are checking in almost entire dataset.
model.fit(X_train, y_train)  # its not ai is learning. k-NN doesnt build a mathematical model during traning. k-NN mainly stores the training data (X_train) and stores corresponding labels (y_train)
#k-NN training is mostly remembering the training data

predictions = model.predict(X_test)   #gives one predicted species for each flower in X_test
#compare predictions:-
print(predictions[:5])   #NumPy array
print(y_test[:5])   #pandas Series


from sklearn.metrics import accuracy_score   #to measure the performance

accuracy = accuracy_score(y_test, predictions)
print(accuracy)


#------Visualizing the data-------
import matplotlib.pyplot as plt

# plt.scatter(
#     df["petal length (cm)"],
#     df["petal width (cm)"]
# )

# plt.xlabel("petal length")
# plt.ylabel("petal width")

# plt.show()   #plot the dots in the coordinates of the flower (all dots are in same color)


#Color each species diff.
colors = {
    "setosa": "red",
    "versicolor": "green",
    "virginica": "blue"
}

for species in df["species"].unique():   #return no duplicates
    subset = df[df["species"]==species]  #filtering. loop runs for each species separately one by one

    #each subset gets plotted with a diff. color
    plt.scatter(
        subset["petal length (cm)"],
        subset["petal width (cm)"],
        # subset["sepal length (cm)"],
        # subset["sepal width (cm)"],
        color=colors[species],
        label=species
    )

plt.xlabel("Petal length")
plt.ylabel("Petal Width")
plt.legend()

plt.show()