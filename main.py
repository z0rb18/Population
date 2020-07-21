import matplotlib.pyplot as plt
States=['lalaland', 'Washington', 'Michigan','Ohio','California']
Population=['0','2.6mil','10mil','11.23 mil','40.02mil']

plt.title('people living in states')
plt.xlabel('States')
plt.ylabel('Number of People Living in States')
plt.bar(States,Population,color='purple',label='Label for legend')



plt.show()