import matplotlib.pyplot as plt

my_data = [1, 2, 3]
my_labels = 'label1', 'label2', 'label3'
plt.pie(my_data, labels=my_labels, autopct='%1.1f%%')
plt.title('My Title')
plt.axis('equal')
plt.show()