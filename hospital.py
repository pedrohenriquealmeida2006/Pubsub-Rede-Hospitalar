class EquipamentoMedico:

    def __init__(self, nome, pubsub):
        self.nome = nome
        self.pubsub = pubsub

    def enviar_alerta(self, topico, mensagem):
        print(f"\n {self.nome} está enviando um alerta...")
        self.pubsub.publish(topico, mensagem)


class EquipeMedica:

    def __init__(self, nome):
        self.nome = nome


class CentralLeitos:

    def __init__(self, nome):
        self.nome = nome


class SistemaLeitos:

    def __init__(self, pubsub):
        self.pubsub = pubsub

    def informar_leito(self, leito, setor):
        mensagem = f"Leito {leito} disponível no setor {setor}."

        print(f"\n️ Sistema de Leitos enviando informação...")
        self.pubsub.publish("LeitoDisponível", mensagem)


class SistemaTriagem:

    def __init__(self, pubsub):
        self.pubsub = pubsub

    def registrar_emergencia(self, paciente, prioridade):
        mensagem = (
            f"Paciente {paciente} classificado como "
            f"emergência. Prioridade: {prioridade}."
        )

        print(f"\n Sistema de Triagem enviando informação...")
        self.pubsub.publish("TriagemEmergência", mensagem)