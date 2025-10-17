from fastapi import FastAPI


manager = FastAPI(title="VolleyballManager")

# Endpoints destinados à administração dos jogadores no sistema.

@manager.get("/jogadores")
def get_jogador():
    # Descrição - Essa função cria um novo perfil (ID) para um jogador(a).
    pass

@manager.get("/jogadores/{id}")
def get_id_jogador():
    # Descrição - Essa função busca o perfi de um jogador(a) com base no ID existente no sistema.
    pass

@manager.put("/jogadores/{id}")
def put_id_jogador():
    # Descrição - Essa função atualiza os dados de um jogador(a) com base no ID existente no sistema.
    pass

# Endpoints destinados à administração das partidas no sistema.

@manager.post("/partidas")
def post_partida():
    # Descrição - Essa função cria uma nova partida (de vôlei em questão) no sistema.
    pass

@manager.get("/partidas")
def get_partida():
    # Descrição - Essa função lista todas as partidas (de vôlei) existentes no sistema.
    pass

@manager.get("/partidas/{id}")
def get_id_partida():
    # Descrição - Essa função exibe os detalhes de uma partida (de vôlei) existente no sistema.
    pass

@manager.put("/partidas/{id}")
def put_id_partida():
    # Descrição - Essa função atualiza os dados de uma partida (de vôlei) existente no sistema.
    pass

@manager.post("/partidas/{id}/adesao")
def post_aderir_id_partida():
    # Descrição - Essa função emite um pedido de adesão de um(a) jogador(a) à uma partida (de vôlei) existente no sistema.
    pass

@manager.put("/partidas/{id}/adesao/{id}")
def put_aderir_id_partida():
    # Descrição - Essa função emite a resposta do(a) jogador(a) organizador(a) de uma partida (de vôlei)
    # sobre o pedido de adesão de um jogador(a).
    pass

@manager.post("/partidas/{id}/desistencia")
def post_desistir_id_partida():
    # Descrição - Essa função registra a desistência de um jogador(a) de uma partida (de vôlei) existente no sistema.
    pass

# Endpoints

@manager.post("/avaliacoes")
def post_avaliacao():
    # Descrição - Essa função registra a avaliação feita por um(a) jogador(a) para a partida (de vôlei)
    # e/ou aos jogadores(as) que estavam presentes
    pass

@manager.get("/avaliacoes")
def get_avaliacoes():
    # Descrição - Essa função lista todas as avaliações feitas para as partidas (de vôlei) existentes no sistema.
    pass
