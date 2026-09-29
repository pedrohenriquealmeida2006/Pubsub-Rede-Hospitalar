from pubsub import PubSub
from hospital import (
    EquipamentoMedico,
    EquipeMedica,
    CentralLeitos,
    SistemaLeitos,
    SistemaTriagem
)


sistema = PubSub()

monitor = EquipamentoMedico("Monitor Cardíaco", sistema)

equipe_medica = EquipeMedica("Equipe Médica")
central_leitos = CentralLeitos("Central de Regulação de Leitos")

sistema_leitos = SistemaLeitos(sistema)
sistema_triagem = SistemaTriagem(sistema)


sistema.subscribe(
    "SinaisVitaisCríticos",
    equipe_medica.nome
)

sistema.subscribe(
    "SinaisVitaisCríticos",
    central_leitos.nome
)

sistema.subscribe(
    "LeitoDisponível",
    central_leitos.nome
)

sistema.subscribe(
    "TriagemEmergência",
    equipe_medica.nome
)


monitor.enviar_alerta(
    "SinaisVitaisCríticos",
    "Paciente do leito 12 apresenta frequência cardíaca de 150 bpm."
)

sistema_leitos.informar_leito(
    "24",
    "UTI"
)

sistema_triagem.registrar_emergencia(
    "Carlos Silva",
    "Alta"
)


print("\n===== TESTE DE UNSUBSCRIBE =====")

sistema.unsubscribe(
    "SinaisVitaisCríticos",
    central_leitos.nome
)

monitor.enviar_alerta(
    "SinaisVitaisCríticos",
    "Paciente do leito 8 apresenta saturação de oxigênio muito baixa."
)