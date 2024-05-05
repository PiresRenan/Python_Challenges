from controller.tts_controller import TextToSpeechController


def main():
    print("Bem-vindo ao Conversor de Texto para Fala!")
    controller = TextToSpeechController()

    while True:
        user_input = input("Digite uma frase para converter em fala (ou 'sair' para encerrar): ")
        if user_input.lower() in ['sair', 'exit']:
            confirm = input("Deseja realmente sair? (Digite 'sim' para confirmar): ")
            if confirm.lower() == 'sim':
                print("Encerrando o programa...")
                break
            else:
                continue
        controller.convert_text_to_speech(user_input)


if __name__ == "__main__":
    main()
