import cv2
import mediapipe as mp
import pyttsx3
import speech_recognition as sr
import webbrowser


webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils
recon = sr.Recognizer()
resposta = ""
while True:

    verificador, frame = webcam.read()
    if not verificador:
        break
    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            robo = pyttsx3.init()
            robo.say("Olá seja bem vindo, deseja ouvir uma musica?")
            robo.setProperty("voice", b'brasil')
            robo.setProperty('rate', 140)
            robo.setProperty('volume', 1)
            robo.runAndWait()
            with sr.Microphone(1) as source:
                while True:

                    audio = recon.listen(source)
                    resposta = recon.recognize_google(audio, language='pt')
                    print("Texto reconhecido: ", resposta)
                    if resposta == "sim":
                        robo.setProperty("voice", b'brasil')
                        robo.setProperty('rate', 180)
                        robo.setProperty('volume', 1)
                        robo.runAndWait()
                        webbrowser.open('https://music.youtube.com/search?q=tudo+vira+reggae', autoraise=True)
                    elif resposta == "parar":
                        robo.setProperty("voice", b'brasil')
                        robo.setProperty('rate', 140)
                        robo.setProperty('volume', 1)
                        robo.say("OK! Encerrado o programa sera entao!")
                        robo.runAndWait()
                        break
            cv2.imshow("Rostos na webcam", frame)

            if cv2.waitKey(5) == 27:
                break
        webcam.release()
        cv2.destroyAllWindows()







