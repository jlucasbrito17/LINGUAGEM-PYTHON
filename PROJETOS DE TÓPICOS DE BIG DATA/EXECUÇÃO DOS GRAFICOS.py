# Execução dos gráficos

# Iris

iris_rX = ["5.1","3.5","1.4","0.2"]
iris_rXX = random.sample(iris_rX,1)
iris_rY = ["5.1","3.5","1.4","0.2"]
iris_rYY = random.sample(iris_rY,1)
plt.scatter(iris_df[iris_rXX],iris_df[iris_rYY],color = "black", marker="o")
pyplot.xlabel(iris_rXX)
pyplot.ylabel(iris_rYY)
plt.title("Iris.data")
plt.legend([iris_rXX,iris_rYY])
plt.show()

# Wine

wine_rX = ["1","14.23",'1.71','2.43','15.6','127','2.8','3.06','.28','2.29','5.64','1.04','3.92','1065']
wine_rXX = random.sample(wine_rX,1)
wine_rY = ["1","14.23",'1.71','2.43','15.6','127','2.8','3.06','.28','2.29','5.64','1.04','3.92','1065']
wine_rYY = random.sample(wine_rY,1)
plt.scatter(wine_df[wine_rXX],wine_df[wine_rYY],color = "blue", marker="+")
pyplot.xlabel(wine_rXX)
pyplot.ylabel(wine_rYY)
plt.title("Wine.data")
plt.legend([wine_rXX,wine_rYY])
plt.show()

# Accelerometer (Winequality-Red)

accelerometer_rX = ['wconfid','pctid','x','y','z']
accelerometer_rXX = random.sample(accelerometer_rX,1)
accelerometer_rY = ['wconfid','pctid','x','y','z']
accelerometer_rYY = random.sample(accelerometer_rY,1)
plt.scatter(accelerometer_df[accelerometer_rXX],accelerometer_df[accelerometer_rYY],color = "yellow", marker="o")
pyplot.xlabel(accelerometer_rXX)
pyplot.ylabel(accelerometer_rYY)
plt.title("Accelerometer.csv")
plt.legend([accelerometer_rXX,accelerometer_rYY])
plt.show()

# Tetuan City Power Consumption

tetuancity_rX = ['Temperature','Humidity','Wind Speed','general diffuse flows','diffuse flows','Zone 1 Power Consumption','Zone 2  Power Consumption','Zone 3  Power Consumption']
tetuancity_rXX = random.sample(tetuancity_rX,1)
tetuancity_rY = ['Temperature','Humidity','Wind Speed','general diffuse flows','diffuse flows','Zone 1 Power Consumption','Zone 2  Power Consumption','Zone 3  Power Consumption']
tetuancity_rYY = random.sample(tetuancity_rY,1)
plt.scatter(tetuancity_df[tetuancity_rXX],tetuancity_df[tetuancity_rYY],color = "green", marker="*")
pyplot.xlabel(tetuancity_rXX)
pyplot.ylabel(tetuancity_rYY)
plt.title("Tetuan City power consuption.csv")
plt.legend([tetuancity_rXX,tetuancity_rYY])
plt.show()

# Pedal Me Bicycle Deliveries (Pedalme Edges)

pedalmeedges_rX = ['from','to','weight']
pedalmeedges_rXX = random.sample(pedalmeedges_rX,1)
pedalmeedges_rY = ['from','to','weight']
pedalmeedges_rYY = random.sample(pedalmeedges_rY,1)
plt.scatter(pedalmeedges_df[pedalmeedges_rXX],pedalmeedges_df[pedalmeedges_rYY], marker="*")
pyplot.xlabel(pedalmeedges_rXX)
pyplot.ylabel(pedalmeedges_rYY)
plt.title("Pedalme_edges.csv")
plt.legend([pedalmeedges_rXX,pedalmeedges_rYY])
plt.show()