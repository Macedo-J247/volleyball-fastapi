from fastapi import FastAPI


manager = FastAPI(title="VolleyballManager")

# Endpoints destinados à administração dos jogadores no sistema.

@manager.get("/jogador")
def get_jogador():
    # Descrição - Essa função cria um novo perfil (ID) para um jogador(a).
    return {
        "id_do_jogador": "mensagem"
    }

@manager.get("/jogador/{id}")
def get_id_jogador():
    # Descrição - Essa função busca o perfi de um jogador(a) com base no ID existente no sistema.
    return {
        "id_do-jogador": "id",
        "nome_do_jogador": "nome",
        "email_do_jogador": "email",
        "sexo_do_jogador": "sexo",
        "idade_do_jogador": "idade",
        "categoria_do_jogador": "categoria"
    }

@manager.put("/jogador/{id}")
def put_id_jogador():
    # Descrição - Essa função atualiza os dados de um jogador(a) com base no ID existente no sistema.
    return {
        "id_do_jogador": "mensagem"
    }

# Endpoints destinados à administração das partidas no sistema.

@manager.post("/partida")
def post_partida():
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

@manager.get("/partida/{id}")
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

@manager.put("/partida/{id}")
def put_id_partida():
    # Descrição - Essa função atualiza os dados de uma partida (de vôlei) existente no sistema.
    return {
        "mensagem": "status"
    }

@manager.post("/partida/{id}/adesao")
def post_aderir_id_partida():
    # Descrição - Essa função emite um pedido de adesão de um(a) jogador(a) à uma partida (de vôlei) existente no sistema.
    return {
        "mensagem": "status"
    }

@manager.put("/partida/{id}/adesao/{id}")
def put_aderir_id_partida():
    # Descrição - Essa função emite a resposta do(a) jogador(a) organizador(a) de uma partida (de vôlei)
    # sobre o pedido de adesão de um jogador(a).
    return {
        "id_jogador_organizador": "status"
    }

@manager.post("/partida/{id}/desistencia")
def post_desistir_id_partida():
    # Descrição - Essa função registra a desistência de um jogador(a) de uma partida (de vôlei) existente no sistema.
    return {
        "mensagem": "mensagem"
    }

# Endpoints

@manager.post("/avaliacoes")
def post_avaliacao():
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
