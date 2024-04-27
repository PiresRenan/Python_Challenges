class CardGenerator:
    def generate_card(self, name, title, email, phone):
        # Define o comprimento máximo de cada linha
        line_length = 40

        # Quebra as informações do usuário conforme necessário
        name_lines = self.split_line(name, line_length)
        title_lines = self.split_line(title, line_length)
        email_lines = self.split_line(email, line_length)
        phone_lines = self.split_line(phone, line_length)

        # Encontra o número máximo de linhas em todas as informações
        max_lines = max(len(name_lines), len(title_lines), len(email_lines), len(phone_lines))

        # Constrói o cartão de visita formatado
        card = f"""
                {'-' * (line_length + 6)}
                {'| Nome:    ': <9} | {name_lines[0]:<{line_length - 8}} |
                {'| Cargo:   ': <9} | {title_lines[0]:<{line_length - 8}} |
                {'| Email:   ': <9} | {email_lines[0]:<{line_length - 8}} |
                {'| Telefone:': <9} | {phone_lines[0]:<{line_length - 10}} |
                {'-' * (line_length + 6)}
                """
        return card

    def split_line(self, text, line_length):
        # Divide o texto em várias linhas para manter o alinhamento
        lines = []
        while len(text) > line_length:
            # Encontra o índice do último espaço dentro do comprimento da linha
            last_space = text[:line_length].rfind(' ')
            lines.append(text[:last_space])
            text = text[last_space + 1:]
        lines.append(text)
        return lines
