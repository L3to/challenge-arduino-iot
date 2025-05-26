from ultralytics import YOLO

"""
Este script utiliza o modelo YOLO da biblioteca Ultralytics para realizar predições em imagens.

Fluxo do código:
1. Importa a classe YOLO da biblioteca ultralytics.
2. Carrega o modelo YOLO a partir do arquivo 'yolo12n.pt'.
3. Realiza predições em várias imagens ('demo.jpg', 'demo2.jpg', 'demo3.jpg', 'demo4.jpg'), salvando os resultados (imagem, texto e confiança) e exibindo as imagens com as detecções.

Parâmetros das predições:
- save (bool): Salva a imagem com as detecções.
- save_txt (bool): Salva as detecções em formato texto.
- save_conf (bool): Salva as confidências das detecções.
- show (bool): Exibe a imagem com as detecções.
- conf (float): Confiança mínima para considerar uma detecção.

Requisitos:
- ultralytics (YOLO)
- Arquivo do modelo 'yolo12n.pt'
- Imagens: 'demo.jpg', 'demo2.jpg', 'demo3.jpg', 'demo4.jpg'
"""
modelo = YOLO("yolo12n.pt")

modelo.predict(
    "demo.jpg", save=True, save_txt=True, save_conf=True, conf=0.5
)
modelo.predict(
    "demo2.jpg", save=True, save_txt=True, save_conf=True, conf=0.5
)
modelo.predict(
    "demo3.jpg", save=True, save_txt=True, save_conf=True, conf=0.5
)
modelo.predict(
    "demo4.jpg", save=True, save_txt=True, save_conf=True, conf=0.5
)
