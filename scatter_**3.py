import matplotlib.pyplot as plt

x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds, edgecolor='none' , s=40)

plt.title("Nubers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("... of value",fontsize=14)



plt.show()