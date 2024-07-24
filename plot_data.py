from matplotlib import pyplot as plt
import os


FILE_PATH='lohnsteuer.txt'

with open(FILE_PATH,'r') as r:
	lines = r.readlines()

print(f'parsing through {len(lines)} lines...')

salary_list = []
tax_list = []
percentage_list = []

for line in lines:
	salary = int(line.split(',')[0])/100
	tax = int(line.split(',')[1])/100
	percentage = round(tax/salary*100,2)
	salary_list.append(salary)
	tax_list.append(tax)
	percentage_list.append(percentage)

fig, ax = plt.subplots()

ax2 = ax.twinx()  # instantiate a second Axes that shares the same x-axis




color = 'tab:blue'
ax.plot(salary_list, tax_list, label='Einkommenssteuer', color=color)
ax.set_xlabel('Einkommen in €')
ax.set_ylabel('Einkommenssteuer in €')

color = 'tab:red'
ax2.plot(salary_list, percentage_list, label='Prozentuale Steuer', color=color)
ax2.set_ylabel('Einkommenssteuer in %')


plt.title('Einkommensteuer')
plt.legend()
plt.show()



