import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gasolina.csv')
grafico = sns.lineplot(data = df, x='dia', y= 'venda')
grafico.set_title('Preço médio da gasolina', fontweight = 'bold')
grafico.legend(['Preço médio da gasolina em São Paulo nos primeiros dias de julho, 2021.'], 
               ncol=5,
               loc= 'upper center',
               bbox_to_anchor=(0.5, 1.2),
               frameon= False,)
grafico.set_xlabel('Dia', fontweight= 'bold')
grafico.set_ylabel('Preço', fontweight= 'bold')
plt.savefig('gasolina.png')
