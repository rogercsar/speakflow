Visão Geral do Projeto:

A aplicação SpeakFlow foi projetada para ajudar os usuários a praticar a construção de frases em inglês, utilizando a tecnologia de ponta fornecida pelo modelo de linguagem GPT-2 da Hugging Face. Além disso, a aplicação oferece funcionalidades adicionais, como a tradução automática de frases e o armazenamento do histórico de frases geradas.

Tecnologias Utilizadas:

Streamlit: Framework para a criação de aplicativos web interativos em Python.

Transformers: Biblioteca da Hugging Face, utilizada para carregar e interagir com o modelo GPT-2.

Googletrans: Biblioteca de tradução que permite traduzir frases entre diferentes idiomas, como inglês e português.

JSON: Utilizado para salvar e carregar o histórico de frases geradas, garantindo que as informações persistam mesmo após a atualização da página.

Estrutura e Funcionalidades da Aplicação:

1. Geração de Frases
   
A função central da aplicação é a geração de frases em inglês. O usuário pode selecionar diferentes tópicos, como sujeito, verbo, alimentos, bebidas, lugares, entre outros. A combinação desses elementos gera um prompt que é então utilizado pelo modelo GPT-2 para criar uma frase coerente.
   
2. Tradução Automática
   
Uma vez que a frase em inglês é gerada, o usuário pode ver a tradução para o português, facilitando o entendimento e auxiliando no processo de aprendizado.
     
3. Histórico de Frases
   
O histórico de frases geradas é salvo localmente em um arquivo JSON, permitindo que os usuários revisitem frases anteriores. O histórico também pode ser gerenciado através de opções para deletar ou compartilhar frases específicas.
    
4. Gerenciamento do Histórico
   
Os usuários têm a capacidade de gerenciar o histórico de frases através de um menu interativo que permite deletar ou compartilhar frases. Essa funcionalidade é útil para manter o foco em frases relevantes e compartilhar progresso em plataformas sociais ou de comunicação.
