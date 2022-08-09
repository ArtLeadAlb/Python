import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tabela=pd.read_csv('advertising.csv')
print(tabela.corr())

sns.heatmap(tabela.corr(),cmap='cool',annot=True) #Cria um gráfico de calor com cores azuis e anotações
plt.show()

x=tabela[['TV','Radio','Jornal']] #colocar entre[[]] porque é uma tabela dentro da tabela
y=tabela['Vendas']

from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste=train_test_split(x,y,test_size=0.28) #aprendizado supervisionado

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
#cria a inteligência artificial
modelo_regressaolinear=LinearRegression()
modelo_arvoredecisao=RandomForestRegressor()

#treina a inteligência artificial
modelo_regressaolinear.fit(x_treino,y_treino)
modelo_arvoredecisao.fit(x_treino,y_treino)
#Preve os resultados
previsao_regressaolinear=modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao=modelo_arvoredecisao.predict(x_teste)

#compara os resultados com os valores ideais
from sklearn.metrics import r2_score
print(r2_score(y_teste,previsao_regressaolinear))
print(r2_score(y_teste,previsao_arvoredecisao))

#gráfico
tabela_aux=pd.DataFrame()
tabela_aux['y_test']=y_teste
tabela_aux['arvoredecisao']=previsao_arvoredecisao
tabela_aux['regressaolinear']=previsao_regressaolinear

#plotar gráfico da tabela_aux  criada
plt.figure(figsize=(16,9))
sns.lineplot(data=tabela_aux)
plt.show()
