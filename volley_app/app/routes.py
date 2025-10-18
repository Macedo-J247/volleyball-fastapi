from fastapi import FastAPI
from typing import Literal


manager = FastAPI(title="VolleyballManager")

# Endpoints destinados à administração dos jogadores no sistema.

@manager.get("/jogador")
def get_jogador(
    nome: str,
    email:str,
    sexo: str,
    idade: int,
    categoria: Literal['', '', '']
):
    # Descrição - Essa função cria um novo perfil (ID) para um jogador(a).
    return {
        "id_do_jogador": "mensagem"
    }

@manager.get("/jogador/{id_jogador}")
def get_id_jogador():
    # Descrição - Essa função busca o perfi de um jogador(a) com base no ID existente no sistema.
    return {
        "id_do_jogador": "id_jogador",
        "nome_do_jogador": "nome",
        "email_do_jogador": "email",
        "sexo_do_jogador": "sexo",
        "idade_do_jogador": "idade",
        "categoria_do_jogador": "categoria"
    }

@manager.put("/jogador/{id_jogador}")
def put_id_jogador(
    nome: str,
    categoria: Literal['', '', '']
):
    # Descrição - Essa função atualiza os dados de um jogador(a) com base no ID existente no sistema.
    return {
        "id_do_jogador": "mensagem"
    }

# Endpoints destinados à administração das partidas no sistema.

@manager.post("/partida")
def post_partida(
    id_jogador_organizador: int,
    local: str,
    data: str,
    hora: str,
    categoria: Literal['', '', ''],
    tipo: str,
    status: bool
):
    # Descrição - Essa função cria uma nova partida (de vôlei em questão) no sistema.
    return {
        "id_da_partida": "mensagem"
    }

@manager.get("/partida")
def get_partida():
    # Descrição - Essa função lista todas as partidas (de vôlei) existentes no sistema.
    return {
        "id_organizador_partida": "id_jogador",
        "local_da_partida": "local_partida",
        "data_da_partida": "data_partida",
        "hora_da_partida": "hora_partida",
        "categoria_da_partida": "categoria_partida",
        "tipo_da_partida": "tipo_partida",
        "status_da_partida": "status"
    }

@manager.get("/partida/{id_partida}")
def get_id_partida():
    # Descrição - Essa função exibe os detalhes de uma partida (de vôlei) existente no sistema.
    return {
        "id_partida_existente": "id_partida",
        "id_jogador_organizador": "id_jogador",
        "local_da_partida": "local_partida",
        "data_da_partida": "data_partida",
        "hora_da_partida": "hora_partida",
        "categoria_da_partida": "categoria_partida",
        "tipo_da_partida": "tipo_partida",
        "status_da_partida": "status"
    }

@manager.put("/partida/{id_partida}")
def put_id_partida(status: bool):
    # Descrição - Essa função atualiza os dados de uma partida (de vôlei) existente no sistema.
    return {
        "mensagem": status
    }

@manager.post("/partida/{id_partida}/adesao")
def post_aderir_id_partida(id_jogador: int):
    # Descrição - Essa função emite um pedido de adesão de um(a) jogador(a) à uma partida (de vôlei) existente no sistema.
    return {
        "mensagem": "status"
    }

@manager.put("/partida/{id_partida}/adesao/{id_adesao}")
def put_aderir_id_partida(status: bool):
    # Descrição - Essa função emite a resposta do(a) jogador(a) organizador(a) de uma partida (de vôlei)
    # sobre o pedido de adesão de um jogador(a).
    return {
        "id_jogador_organizador": status
    }

@manager.post("/partida/{id_partida}/desistencia")
def post_desistir_id_partida(id_jogador: int):
    # Descrição - Essa função registra a desistência de um jogador(a) de uma partida (de vôlei) existente no sistema.
    return {
        "mensagem": "mensagem"
    }

# Endpoints

@manager.post("/avaliacoes")
def post_avaliacao(
    id_avaliador: int,
    id_avaliado: int,
    id_partida: int,
    nota: int,
    comentario: str = ''
):
    # Descrição - Essa função registra a avaliação feita por um(a) jogador(a) para a partida (de vôlei)
    # e/ou aos jogadores(as) que estavam presentes
    return {
        "id_da_avaliação": "mensagem"
    }

@manager.get("/avaliacoes")
def get_avaliacoes():
    # Descrição - Essa função lista todas as avaliações feitas para as partidas (de vôlei) existentes no sistema.
    return {
        "id_das_avaliações": "avaliações"
    }
