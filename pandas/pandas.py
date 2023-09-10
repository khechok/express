import matplotlib.pyplot as plt 
 
figure, axes = plt.subplots() 
cc = plt.Circle(( 0.5 , 0.5 ), 0.4 ) 
 
axes.set_aspect( 1 ) 
axes.add_artist( cc ) 
plt.title( 'Uncolored Circle' ) 
plt.show()

