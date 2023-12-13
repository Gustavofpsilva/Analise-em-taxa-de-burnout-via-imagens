Análise de Emoções em Imagens
Este script Python utiliza a biblioteca gradio para criar uma interface interativa que analisa emoções em imagens usando a biblioteca fer (Facial Emotion Recognition). O objetivo é detectar e imprimir as emoções presentes na imagem, juntamente com a emoção de maior pontuação.

Requisitos
Python 3.x
Bibliotecas: gradio, fer, opencv-python
Configuração Inicial
Instale as bibliotecas necessárias executando:

bash
Copy code
pip install gradio fer opencv-python
Certifique-se de que as dependências estão instaladas corretamente.

Uso
Execute o script:

bash
Copy code
python seu_script.py
A interface Gradio será iniciada, permitindo que você faça upload de uma imagem para análise.

O script utiliza a biblioteca fer para detectar emoções na imagem e imprime as emoções detectadas, bem como a emoção de maior pontuação.

As informações são registradas em um arquivo de texto chamado "Emotion.txt", incluindo a data e a hora da análise.

Observações
Detecção de Emoções: O script utiliza o modelo de detecção de emoções da biblioteca fer, que é baseado em MTCNN (Multi-task Cascaded Convolutional Networks).

Saída da Interface: A interface Gradio exibe as emoções detectadas e a emoção de maior pontuação.

Registro em Arquivo: As informações são registradas em um arquivo de texto para referência futura.
