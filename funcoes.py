def configurarCamera(resolucao):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Não foi possivel abrir a camera")
        exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolucao[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolucao[1])
    cap.set(cv2.CAP_PROP_FPS, 60)

    return cap

def tirarFoto(frame, frames):
    frame_name = './frame' + str(frames//10) + '.jpg'
    #save frame
    cv2.imwrite(frame_name, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])

import cv2