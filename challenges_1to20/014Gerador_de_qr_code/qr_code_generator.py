import qrcode


class QRCodeGenerator:
    def generate_qr_code(self, data, file_name):
        # Cria um objeto QRCode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Adiciona os dados ao QRCode
        qr.add_data(data)
        qr.make(fit=True)

        # Cria uma imagem do QRCode
        img = qr.make_image(fill_color="black", back_color="white")

        # Salva a imagem do QRCode em um arquivo
        img.save(file_name)
