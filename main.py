import pandas as pd
import streamlit as st
import plotly.express as px

# Título da página
st.set_page_config(page_title="Imedic")

# Dicionário com informações sobre os medicamentos
medicamentos = {
    "Paracetamol": {
        "Descrição": "O paracetamol é um analgésico comum usado para aliviar a dor e reduzir a febre.",
        "Efeitos Colaterais": "Efeitos colaterais leves são raros, mas podem incluir reações alérgicas ou erupções cutâneas.",
        "Como Usar": "Tomar um comprimido de 500mg a 1g a cada 4 a 6 horas, conforme necessário.",
        "Dosagem": "Dose máxima diária de 4g."
    },
    "Ibuprofeno": {
        "Descrição": "O ibuprofeno é um anti-inflamatório não esteroidal (AINE) que ajuda a aliviar a dor, a febre e a inflamação.",
        "Efeitos Colaterais": "Efeitos colaterais comuns incluem desconforto gastrointestinal, úlceras e aumento do risco cardiovascular.",
        "Como Usar": "Tomar um comprimido de 200mg a 400mg a cada 4 a 6 horas, conforme necessário.",
        "Dosagem": "Dose máxima diária de 1.2g."
    },
    "Omeprazol": {
        "Descrição": "O omeprazol é um inibidor da bomba de prótons que reduz a produção de ácido no estômago, utilizado no tratamento de problemas gastrointestinais.",
        "Efeitos Colaterais": "Efeitos colaterais podem incluir dor abdominal, diarreia e aumento do risco de infecções.",
        "Como Usar": "Tomar um comprimido de 20mg a 40mg uma vez ao dia, de preferência antes do café da manhã.",
        "Dosagem": "Dose máxima diária de 40mg."
    },
    "Dipirona": {
        "Descrição": "A dipirona é um analgésico e antipirético usado para aliviar a dor e reduzir a febre.",
        "Efeitos Colaterais": "Efeitos colaterais podem incluir reações alérgicas, baixa pressão arterial e problemas de pele.",
        "Como Usar": "Tomar um comprimido de 500mg a 1g a cada 4 a 6 horas, conforme necessário.",
        "Dosagem": "Dose máxima diária de 4g."
    },
    "Alprazolam": {
        "Descrição": "O alprazolam também conhecido pelos nomes comerciais Xanax, Apraz, Frontal, entre outros, é um fármaco utilizado em distúrbios da ansiedade e agorafobia. Trata-se de uma benzodiazepina que estimula a ação do ácido gama-aminobutírico, reduzindo a ansiedade moderada e ansiedade associada a depressão.",
        "Efeitos Colaterais": "Efeitos colaterais incluem sonolência, tontura, perda de coordenação e dependência.",
        "Como Usar": "Tomar um comprimido de 0.25mg a 0.5mg, 2 a 3 vezes ao dia.",
        "Dosagem": "Dose máxima diária de 4mg."
    },
    "Ritalina": {
        "Descrição": "A Ritalina Trata o Transtorno de Déficit de Atenção e Hiperatividade (TDAH), Aumenta a concentração, Pode causar insônia e perda de apetite",
        "Efeitos Colaterais": "Efeitos colaterais podem incluir nervosismo, insônia, dor de cabeça e problemas gastrointestinais.",
        "Como Usar": "Tomar um comprimido de 5mg a 20mg, uma vez ao dia pela manhã.",
        "Dosagem": "Dose máxima diária de 60mg."
    },
    "Morfina": {
        "Descrição": "A morfina é um analgésico opioide utilizado para aliviar dores intensas.",
        "Efeitos Colaterais": "Efeitos colaterais incluem constipação, sonolência, náusea e risco de dependência.",
        "Como Usar": "A dosagem varia dependendo da situação clínica e da resposta do paciente. Deve ser administrada por um profissional de saúde.",
        "Dosagem": "Dose máxima de acordo com a prescrição médica."
    },
    "Clozapina": {
        "Descrição": "A clozapina é um antipsicótico atípico utilizado no tratamento de esquizofrenia.",
        "Efeitos Colaterais": "Efeitos colaterais podem incluir sedação, aumento de peso, tontura e risco de agranulocitose.",
        "Como Usar": "A dosagem inicial é de 12.5mg a 25mg, dividida em doses diárias. A dose é gradualmente aumentada sob supervisão médica.",
        "Dosagem": "Dose máxima de acordo com a prescrição médica."
    },
    "Bupropiona": {
        "Descrição": "A bupropiona é um antidepressivo utilizado para tratar depressão e auxiliar no tratamento de tabagismo.",
        "Efeitos Colaterais": "Efeitos colaterais incluem insônia, boca seca, aumento da pressão arterial e ansiedade.",
        "Como Usar": "A dosagem inicial é de 150mg uma vez ao dia. Pode ser aumentada para 300mg diários após alguns dias.",
        "Dosagem": "Dose máxima de 450mg diários."
    },
    "Venvanse": {
        "Descrição": "O Venvanse é um medicamento estimulante utilizado no tratamento de Transtorno de Déficit de Atenção e Hiperatividade (TDAH).",
        "Efeitos Colaterais": "Efeitos colaterais incluem insônia, perda de apetite, aumento da pressão arterial e nervosismo.",
        "Como Usar": "Tomar um comprimido de 30mg a 70mg uma vez ao dia pela manhã.",
        "Dosagem": "Dose máxima de acordo com a prescrição médica."
    },
    "Neosoro": {
        "Descrição": "O Neosoro é um descongestionante nasal utilizado para aliviar a congestão nasal.",
        "Efeitos Colaterais": "Efeitos colaterais podem incluir irritação nasal, ardor e congestão de rebote.",
        "Como Usar": "Aplicar 1 a 2 gotas em cada narina, 3 a 4 vezes ao dia.",
        "Dosagem": "Uso máximo de 7 dias."
    },
    "Fentanil": {
        "Descrição": "O fentanil é um analgésico opioide utilizado para aliviar dores intensas.",
        "Efeitos Colaterais": "Efeitos colaterais podem incluir constipação, sonolência, náusea e risco de dependência.",
        "Como Usar": "A dosagem varia dependendo da situação clínica e da resposta do paciente. Deve ser administrada por um profissional de saúde.",
        "Dosagem": "Dose máxima de acordo com a prescrição médica."
    },
}

# Título da página
st.title("Guia de Medicamentos")

# Conteúdo da página
st.write("Bem-vindo ao nosso guia dos melhores medicamentos!")

# Lista de medicamentos disponíveis
medicamento_selecionado = st.selectbox("Selecione um medicamento:", list(medicamentos.keys()))

# Exibe a descrição, efeitos colaterais, "Como Usar" e "Dosagem" do medicamento selecionado
st.write(f"**{medicamento_selecionado}**")
st.write("**Descrição:**", medicamentos[medicamento_selecionado]["Descrição"])
st.write("**Efeitos Colaterais:**", medicamentos[medicamento_selecionado]["Efeitos Colaterais"])
st.write("**Como Usar:**", medicamentos[medicamento_selecionado]["Como Usar"])
st.write("**Dosagem:**", medicamentos[medicamento_selecionado]["Dosagem"])

# Função para calcular o custo-benefício com base nas características do medicamento
def calcular_custo_beneficio(info):
    # Aqui você pode definir uma fórmula ou critérios para calcular o custo-benefício com base nas características do medicamento
    # Neste exemplo fictício, estou simplesmente atribuindo um valor aleatório entre 0 e 100
    return round((info.get("Custo", 30) / info.get("Beneficio", 1)) * 100, 2)

# Criando uma nova aba para exibir as informações de custo-benefício
if st.button("Custo-Benefício"):
    st.title("Custo-Benefício dos Medicamentos")

    # Calcula o custo-benefício para cada medicamento e cria um DataFrame
    data = []
    for nome, info in medicamentos.items():
        custo_beneficio = calcular_custo_beneficio(info)
        data.append({"Medicamento": nome, "Custo-Benefício": custo_beneficio})
    df = pd.DataFrame(data)

    # Exibe o DataFrame ordenado por Custo-Benefício
    st.write(df.sort_values("Custo-Benefício", ascending=False))

import pandas as pd
import streamlit as st
import plotly.express as px

# ... (código anterior)

# Título da página
st.title("Guia de Medicamentos")

# Barra de pesquisa
medicamento_pesquisado = st.text_input("Pesquisar medicamento:")

# Botão de pesquisa
if st.button("Pesquisar"):
    if medicamento_pesquisado in medicamentos:
        st.write(f"**{medicamento_pesquisado}**")
        st.write("**Descrição:**", medicamentos[medicamento_pesquisado]["Descrição"])
        st.write("**Efeitos Colaterais:**", medicamentos[medicamento_pesquisado]["Efeitos Colaterais"])
        st.write("**Como Usar:**", medicamentos[medicamento_pesquisado]["Como Usar"])
        st.write("**Dosagem:**", medicamentos[medicamento_pesquisado]["Dosagem"])
    else:
        st.write("Medicamento não encontrado.")

# ... (código posterior)
import pandas as pd
import streamlit as st
import plotly.express as px


# ... (código anterior)

# Função fictícia para buscar informações de medicamentos em uma API
def buscar_informacoes_medicamento(nome_medicamento):
    if nome_medicamento in medicamentos:
        return medicamentos[nome_medicamento]
    else:
        return None


# Título da página
st.title("Guia de Saúde")

# Aba lateral com as opções
menu_options = ["Medicamentos", "Dependência Química", "Clínicas Psiquiátricas"]
selected_option = st.sidebar.selectbox("Selecione uma opção:", menu_options)

# Conteúdo da página baseado na opção selecionada
if selected_option == "Medicamentos":
    st.header("Guia de Medicamentos")

    st.write("""Um medicamento é uma droga usada para diagnosticar, curar, tratar ou prevenir doenças.[1][2] A terapia medicamentosa (farmacoterapia) é uma parte importante da área médica e depende da ciência da farmacologia para o avanço contínuo e da farmácia para o manejo adequado.

As drogas farmacêuticas são classificadas de várias maneiras. Uma das principais divisões é por nível de controle, que distingue os medicamentos prescritos (aqueles que o farmacêutico dispensa apenas por ordem de um médico ou enfermeiro qualificado) dos medicamentos de venda livre (aqueles que os consumidores podem solicitar por eles mesmos). Outra distinção importante é entre drogas tradicionais de moléculas pequenas, geralmente derivadas de síntese química, e biofármacos, que incluem proteínas recombinantes, vacinas, produtos sanguíneos usados ​​terapeuticamente (como IVIG), terapia gênica, anticorpos monoclonais e terapia celular (por exemplo, terapias com células-tronco). Outras formas de classificar os medicamentos são por modo de ação, via de administração, sistema biológico afetado ou efeitos terapêuticos. Um sistema de classificação elaborado e amplamente utilizado é o Sistema de Classificação Química Terapêutica Anatômica. A Organização Mundial da Saúde mantém uma lista de medicamentos essenciais.""")

elif selected_option == "Dependência Química":
    st.header("Dependência Química")

    st.write("""Lidar com a dependência química é um desafio complexo que requer compreensão, suporte e tratamento adequado. Aqui está um exemplo de como um artigo sobre dependência química poderia ser estruturado:

Entendendo a Dependência Química: Causas, Sintomas e Tratamento

A dependência química é uma condição grave que afeta milhões de pessoas em todo o mundo. Neste artigo, exploraremos as causas subjacentes, os sintomas característicos e as opções de tratamento disponíveis para superar essa condição.

O Que é Dependência Química?

A dependência química, também conhecida como dependência de substâncias, é um transtorno mental caracterizado por um padrão compulsivo de uso de substâncias psicoativas, apesar das consequências negativas para a saúde e a vida da pessoa. Essas substâncias podem incluir álcool, drogas ilícitas e medicamentos prescritos.

Causas da Dependência Química

A dependência química é resultado de uma combinação complexa de fatores genéticos, ambientais, sociais e psicológicos. Pessoas com histórico familiar de dependência têm maior predisposição a desenvolvê-la, mas fatores como estresse, traumas e pressões sociais também desempenham um papel significativo.

Sintomas e Sinais de Dependência

Os sintomas da dependência química podem variar, mas geralmente incluem:

Tolerância: A necessidade de doses cada vez maiores da substância para alcançar os mesmos efeitos.

Abstinência: Sintomas físicos e psicológicos desconfortáveis quando a substância não é consumida.

Desejo incontrolável: Uma forte ânsia ou desejo persistente de usar a substância.

Perda de Controle: Incapacidade de controlar a quantidade ou frequência de uso.

Priorização da Substância: Dedicação excessiva de tempo para obter, usar ou se recuperar do uso da substância, negligenciando atividades importantes.

Opções de Tratamento

A dependência química é tratável, e a busca por ajuda é um passo corajoso na jornada para a recuperação. As opções de tratamento incluem:

Terapia Comportamental: Abordagens como a Terapia Cognitivo-Comportamental (TCC) ajudam a identificar padrões de pensamento e comportamento que contribuem para a dependência e ensinam estratégias para modificá-los.

Terapia de Grupo e Apoio Mútuo: Participar de grupos de apoio, como os Alcoólicos Anônimos (AA) e Narcóticos Anônimos (NA), oferece suporte emocional e camaradagem durante o processo de recuperação.

Tratamento Medicamentoso: Alguns medicamentos podem ser usados para reduzir os sintomas de abstinência e diminuir os desejos, tornando mais fácil para a pessoa interromper o uso da substância.

Tratamento Residencial ou Ambulatorial: Dependendo da gravidade da dependência, um programa de tratamento residencial (internação) ou ambulatorial pode ser recomendado.

Importância do Apoio e Prevenção

A prevenção desempenha um papel crucial na redução da dependência química. Programas de educação, conscientização e apoio social podem ajudar a reduzir os fatores de risco. Além disso, o apoio de amigos, familiares e profissionais de saúde é fundamental para ajudar aqueles que lutam contra a dependência a buscar ajuda e perseverar na recuperação.")
fissura ou craving;
dificuldade em controlar o uso;
síndrome de abstinência;
tolerância aumentada para a droga;
mudanças de comportamento.""")

elif selected_option == "Clínicas Psiquiátricas":
    st.header("Clínicas Psiquiátricas")

    st.write("""
    A história dos hospitais psiquiátricos como instituição de tratamento é ligada ao pensamento social e científico acerca dos doentes mentais em cada época.

    De 1848 até o início do século XX, instrumentos como camisas-de-força e quartos-fortes ou "prisões-acolchoadas", choques elétricos, operações no cérebro e outras verdadeiras torturas eram utilizados para controlar os cidadãos, no que se dizia ser a psiquiatria dita científica, principalmente os mais agressivos.

    Atualmente há relatos de que existam alguns lugares deste tipo, denúncias já foram feitas, mas nada foi comprovado. Mas recentemente há tratamentos farmacológicos e psicológicos - terapêuticos, baseados nas teorias de Freud e seu discípulo Carl G. Jung, que reduzem significativamente a necessidade da contenção física e a internação por longos períodos, dai a necessidade dos extintos "centros clínicos hospitalares" nos chamados tecnicamente de "Hospital-Dia" (termo médico moderno, já que o Brasil se modernizava com Getúlio Vargas, em 1945)" (extintos, pela moderna constituição de 1988, no Brasil).

    Dai os movimentos de massa das pessoas com essas necessidades, tentando o resgate histórico, para que tais clínicas especializadas sejam novamente ativadas, no lugar de um retrocesso histórico que houve, numa verdadeira cruzada de resgate de valores históricos, para benefício do povo brasileiro solapado pela constituição de 1988.
    """)
