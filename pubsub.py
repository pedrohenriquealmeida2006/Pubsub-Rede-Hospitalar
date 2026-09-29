class PubSub:

    def __init__(self):
        self.topicos = {}

    def subscribe(self, topico, assinante):
        if topico not in self.topicos:
            self.topicos[topico] = []

        self.topicos[topico].append(assinante)

        print(f"{assinante} se inscreveu no tópico '{topico}'.")

    def unsubscribe(self, topico, assinante):
        if topico in self.topicos and assinante in self.topicos[topico]:
            self.topicos[topico].remove(assinante)

            print(f"{assinante} cancelou a inscrição no tópico '{topico}'.")

    def publish(self, topico, mensagem):
        print(f"\n📢 Publicando no tópico '{topico}':")
        print(f"Mensagem: {mensagem}")

        if topico in self.topicos:
            for assinante in self.topicos[topico]:
                print(f"➡️ {assinante} recebeu a mensagem.")