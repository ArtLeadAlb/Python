# ### Importar e analisar tabelas


import pandas as pd
import numpy as np


caminho = input('Copie o caminho da tabela desejada e aperte enter: ')
tabela = pd.read_excel(f"{caminho}")


def estatistica_base(tabela):
    #rápida visualização dos dados
    print(tabela.shape)
    print(tabela.columns)
    print(tabela.head(5))
    print(tabela.tail(5))
    
    #resumo estatístico de cada coluna de números
    print(tabela.describe())
    print(tabela.dtypes)
    
    #mostra dados duplicados
    print(tabela.duplicated())
    
    #mostra quantos registros são nulos em determinada coluna
    print(tabela.isnull().sum())
    print(tabela.info())
    
    #correlação entre as colunas
    print(tabela.corr())


import matplotlib.pyplot as plt
import seaborn as sns

# ### Criar gráficos

# In[ ]:

def grafico(tabela):
    import matplotlib.pyplot as plt
    import seaborn as sns
    #plotar o gráfico
    #plt.scatter(x, y, bins = 1, alpha = 0.8) #bins->agrupamento de dados  alpha->opacidade
    plt.scatter(x=tabela['CR'], y=tabela['K_inf'])
    plt.xlabel('CR')
    plt.ylabel('K_inf')
    plt.title('CR x K_inf')
    #plt.legend()
    #mostrar o gráfico
    plt.show()


# ### Regressão linear com statsmodels

# In[5]:

import statsmodels.api as sm
def sm_RegressaoLinear(tabela):

    #Regressão linear       obs:  funcioina sem passar x como np.array e depois usar x=x.reshape[-1,1] ???
    coluna1 = input("nome da coluna 1: ")
    coluna2 = input("nome da coluna 2: ")
    x = tabela[coluna1]
    y = tabela[coluna2]

    #adicionar constante para dar certo
    x = sm.add_constant(x)

    #criar modelo
    modelo = sm.OLS(y, x)
    resultado = modelo.fit()

    #Mostra o resultado do modelo
    print('\n======== STATSMODELS ========\n')
    print(resultado.summary()) #R-squared determina a correlação entre as variáveis. 0->1
    print('\n======== TUDO CERTO! ========\n')




def RegLin_RandTree(tabela):
    # ### Regressão linear e árvore de decisão com sklearn
    from sklearn.model_selection import train_test_split
    
    # In[4]:

    coluna1 = input("nome da coluna 1: ")
    coluna2 = input("nome da coluna 2: ")
    x = tabela[coluna1]
    x = sm.add_constant(x)
    y = tabela[coluna2]
    
    #treino
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.35)

    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor

    #cria a inteligência artificial
    modelo1 = LinearRegression()
    modelo2 = RandomForestRegressor()

    #treino
    modelo1.fit(x_treino, y_treino)
    modelo2.fit(x_treino, y_treino)


    print('\n======== SCIKIT-LEARN ========\n')
    
    #pontuação do modelo
    score1 = modelo1.score(x_teste, y_teste)
    print(f'Regressão Linear -> R²: {score1}')

    score2 = modelo2.score(x_teste, y_teste)
    print(f'Árvore de Decisão -> R²: {score2}')
    
    #Sendo y=ax+b
    a = modelo1.coef_
    b = modelo1.intercept_
    print(f'Fórmula da Regressão Linear: y = {a}x + {b}')
             

# ### Visualização do aprendizado

# In[ ]:


    plt.scatter(tabela[coluna1], y, color = 'purple', label = 'Dados colhidos')
    plt.plot(tabela[coluna1], modelo1.predict(x), color = 'red', label = 'R.L.')
    plt.plot(tabela[coluna1], modelo2.predict(x), color = 'blue', label = 'A.D.')
    plt.legend()
    plt.show()


# ### Criando a previsão

# In[ ]:

    #nova variável independente

    valor_previsao =  float(input('Valor para Previsão: '))
    
    novo_x = np.array([valor_previsao],[valor_previsao])
#    novo_x = sm.add_constant(x, prepend = False, has_constant = 'skip')
    
    y_previsto1 = modelo1.predict(novo_x)

    print(f'Usando R.L. para o valor {valor_previsao} o resultado previsto é \n {y_previsto1}\n')
          
    y_previsto2 = modelo2.predict(novo_x)

    print(f'\nUsando A.D. para o valor {valor_previsao} o resultado previsto é \n{y_previsto2}')


    print('\n======== TUDO CERTO! ========\n')

    

