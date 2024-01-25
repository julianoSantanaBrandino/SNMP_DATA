#bibliotecas e variaveis
import os
import pandas as pd
import plotly_express as px
import plotly
import plotly.graph_objs as go



#endereço de onde se enconta aa pasta com os anexos

caminho_pasta = ('//dados/TECNICA/Tecnico Juliano docs/anexos SNMP')


#listando os arquivos presente na pasta ]
lista_arquivos = (os.listdir(caminho_pasta))
#print(lista_arquivos)


#selecionando apenas os arquivos desejados/gerando Dataframe
while True:
    startprog = (int(input('1 para compilar os arquivos...: ')))
    if (startprog == 1):
        for (arquivo) in (lista_arquivos):
            if ('Datalog') in (arquivo):
                #print(arquivo)
                tabela_total = (pd.DataFrame())
                tabela = (pd.read_csv(f'//dados/TECNICA/Tecnico Juliano docs/anexos SNMP/{arquivo}'))
                tabela_total = (tabela_total.append(tabela))
                tabela_total['Date/Time'] = (tabela_total['Date'] + '-' + tabela_total['Time'].astype(str))
                print(tabela_total)
                #criando os elementos para o grafico
                df_data = tabela_total['Date/Time']
                df_ent1 = tabela_total['InVolt1']
                df_out1 = tabela_total['OutVolt1']
                df_ent2 = tabela_total['InVolt2']
                df_out2 = tabela_total['OutVolt2']
                df_ent3 = tabela_total['InVolt3']
                df_out3 = tabela_total['OutVolt3']
                df_outPower1 = tabela_total['Load1']  # OutPower1
                df_outPower2 = tabela_total['Load2']  # OutPower2
                df_outPower3 = tabela_total['Load3']  # OutPower3
                df_infreq = tabela_total['InFreq']
                df_outfreq = tabela_total['OutFreq']
                #criando o grafico mult-linha
                fig = (go.Figure())
                cliente = (f'{arquivo}')

                fig.add_trace(go.Scatter(x=df_data, y=df_ent1, name='in  Volt 1, fase R', line=dict(color='red', width=1)))
                fig.add_trace(go.Scatter(x=df_data, y=df_ent2, name='in  Volt 2, fase S', line=dict(color='blue', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_ent3, name='in  Volt 3, fase T', line=dict(color='green', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_out1, name='out Volt 1, fase R', line=dict(color=' yellow', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_out2, name='out Volt 2, fase S', line=dict(color='orange', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_out3, name='out Volt 3, fase T', line=dict(color='violet', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_outPower1, name='out Power 1, fase R', line=dict(color='darkred', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_outPower2, name='out Power 2, fase S', line=dict(color='darkblue', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_outPower3, name='out Power 3, fase T', line=dict(color='darkgreen', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_infreq, name='In frequência', line=dict(color='pink', width=2)))
                fig.add_trace(go.Scatter(x=df_data, y=df_outfreq, name='Out Frequência Retif.', line=dict(color='teal', width=2)))
                fig.update_layout(title=cliente, xaxis_title='Data / hora', yaxis_title=' Volts V, Watt w, Hertz Hz ')
                #fig.show()
                plotly.offline.plot(fig, filename=cliente, auto_open= False)

            else:

                continue
    print('Finalizado arquivos compilados')