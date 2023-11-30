# Importando bibliotecas e módulos necessários.
from ultralytics import YOLO  # Biblioteca para utilizar o modelo YOLO.
from funcoes import *  # Importando todas as funções de um arquivo chamado 'funcoes'.
import cv2  # OpenCV, uma biblioteca para processamento de imagem e visão computacional.

# Definindo a resolução das imagens que serão capturadas pela câmera.
resolucao = (1920, 1080)

# Variável que determina se fotos serão tiradas ou não.
tirarFotos = 0

# Contador para controle interno.
i = 0

# Carrega o modelo YOLO pré-treinado do arquivo 'yolov8n.pt'.
model = YOLO('yolov8n.pt')

# Utilizando a função 'configurarCamera' (que presumivelmente está no arquivo 'funcoes.py')
# para obter o objeto de captura de vídeo com a resolução definida.
cap = configurarCamera(resolucao)

# Iniciando um loop infinito para captura e processamento de imagens em tempo real.
while True:
    # Lê um frame da câmera.
    ret, frame = cap.read()
    
    # Verifica se o frame foi lido corretamente. Se não, sai do loop.
    if not ret:
        print("Problemas com a câmera? Saindo...")
        break

    # Utiliza o modelo YOLO para detectar objetos no frame.
    results = model(frame)
    
    # Plota as detecções no frame.
    res_plotted = results[0].plot()

    # Exibe o frame com as detecções em uma janela chamada "result".
    cv2.imshow("result", res_plotted)

    # Atualiza o contador (porém note que sempre está adicionando 0, então o valor de 'i' nunca muda).
    i += 0
    
    # Se o contador for divisível por 10 e a variável 'tirarFotos' for True, tira uma foto.
    if (i%10 == 0) and tirarFotos:
        tirarFoto(frame, i)

    # Aguarda por 1 milissegundo e verifica se a tecla 'q' foi pressionada. Se sim, sai do loop.
    if cv2.waitKey(1) == ord('q'):
        break

# Fecha todas as janelas do OpenCV.
cv2.destroyAllWindows()
