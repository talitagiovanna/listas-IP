cronograma = {
    "25/05/2021" : "Introdução e apresentação da disciplina / História da Computação",
    "01/06/2021" : "Arquitetura de Computadores",
    "08/06/2021" : "Apresentação Visualização Interativa - Professor Nivan",
    "15/06/2021" : "Apresentação Cidades Inteligentes - Professor Kiev",
    "22/06/2021" : "Monitoria sobre GIT / Monitoria Desenvolvimento Web",
    "29/06/2021" : "Inteligência Artificial / Aprendizagem de Máquina - Professor Adriano Oliveira",
    "06/07/2021" : "Apresentação sobre Robótica - Professor Hansenclever",
    "13/07/2021" : "Apresentação Software Livre - Professor Castor / (Entrega Projeto web)",
    "20/07/2021" : "Monitoria sobre LaTeX",
    "27/07/2021" : "Apresentação sobre Mineração de Processos / (Entrega Projeto LaTeX)",
    "03/08/2021" : "Projeto de IA",
    "10/08/2021" : "Acompanhamento do projeto de IA",
    "17/08/2021" : "Acompanhamento do projeto de IA",
    "24/08/2021" : "Apresentação do projeto de IA"
}

data_informada = input()

if data_informada in cronograma:
    print(f"{data_informada} haverá aula de IC e o assunto será: {cronograma[data_informada]}")
else:
    print(f"{data_informada} não tem aula de IC")