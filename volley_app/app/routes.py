from fastapi import FastAPI, HTTPException, status
from typing import List, Literal, Optional
from app import database


manager = FastAPI(title="VolleyballManager")

# Endpoints destinados à administração dos jogadores no sistema.

# Criar um novo jogador no sistema.
@manager.post("/jogador", response_model=database.Jogador, status_code=status.HTTP_201_CREATED)
def criar_jogador(jogador: database.Jogador):
    # Descrição - Essa função cria um novo perfil (ID) para um jogador(a).
    if any(j.id_number == jogador.id_number for j in database.jogadores):
        raise HTTPException(status_code=400, detail="Jogador já cadastrado no sistema.")
    database.jogadores.append(jogador)
    return jogador

# Listar jogadores existentes no sistema.
@manager.get("/jogador", response_model=List[database.Jogador])
def listar_jogadores():
    # Descrição - Essa função busca todos os jogadores(as) existente no sistema.
    return database.jogadores

# Buscar um jogador pelo ID.
@manager.get("/jogador/{id_jogador}", response_model=database.Jogador)
def buscar_jogador(id_jogador: int):
    for jogador in database.jogadores:
        if jogador.id_number == id_jogador:
            return jogador
    raise HTTPException(status_code=404, detail="Jogador não encontrado.")

# Atualizar os dados (nome e categoria) de um jogador pelo ID.
@manager.put("/jogador/{id_jogador}", response_model=database.Jogador)
def atualizar_jogador(id_jogador: int, nome: Optional[str] = None, categoria: Optional[str] = None):
    # Descrição - Essa função atualiza os dados de um jogador(a) com base no ID existente no sistema.
    for jogador in database.jogadores:
        if jogador.id_number == id_jogador:
            if nome:
                jogador.nome = nome
            if categoria:
                jogador.categoria = categoria
            return jogador
    raise HTTPException(status_code=404, detail="Jogador não encontrado.")

# Endpoints destinados à administração das partidas no sistema.

# Criar uma nova partida no sistema.
@manager.post("/partida", response_model=database.Partida, status_code=status.HTTP_201_CREATED)
def criar_partida(partida: database.Partida):
    # Descrição - Essa função cria uma nova partida (de vôlei em questão) no sistema.
    if any(p.id_number == partida.id_number for p in database.partidas):
        raise HTTPException(status_code=400, detail="Partida já cadastrada no sistema.")
    database.partidas.append(partida)
    return partida

# Listar partidas existentes no sistema
@manager.get("/partida", response_model=List[database.Partida])
def listar_partida():
    # Descrição - Essa função lista todas as partidas (de vôlei) existentes no sistema.
    return database.partidas

# Buscar partida no sistema pelo ID.
@manager.get("/partida/{id_partida}", response_model=database.Partida)
def buscar_partida(id_partida: int):
    # Descrição - Essa função exibe os detalhes de uma partida (de vôlei) existente no sistema.
    for partida in database.partidas:
        if partida.id_number == id_partida:
            return partida
    raise HTTPException(status_code=404, detail="Partida n]ao encontrada no sistema.")

# Atualizar o status de uma partida pelo ID.
@manager.put("/partida/{id_partida}", response_model=database.Partida)
def atualizar_partida(id_partida: int, status: str):
    # Descrição - Essa função atualiza os dados de uma partida (de vôlei) existente no sistema.
    for partida in database.partidas:
        if partida.id_number == id_partida:
            partida.status = status
            return partida
    raise HTTPException(status_code=404, detail="Partida não encontrada no sistema.")

# Endpoints destinados à adesões de jogadores em partidas (de vôlei)

# Aderir a uma partida.
@manager.post("/partida/{id_partida}/adesao", response_model=database.Adesao)
def aderir_partida(id_partida: int, adesao: database.Adesao):
    # Descrição - Essa função emite um pedido de adesão de um(a) jogador(a) à uma partida (de vôlei) existente no sistema.
    partida = next((p for p in database.partidas if p.id_number == id_partida), None)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada no sistema.")
    if partida.status == "Terminada":
        raise HTTPException(status_code=400, detail="Partida já encerrada.")
    if any(a.id_jogador == adesao.id_jogador and a.id_partida == id_partida for a in database.adesoes):
        raise HTTPException(status_code=400, detail="Jogador já foi incluso nessa partida.")
    database.adesoes.append(adesao)
    return adesao

# Emitir a resposta de um pedido de adesão em uma partida.
@manager.put("/partida/{id_partida}/adesao/{id_adesao}", response_model=database.Adesao)
def responder_pedido_adesao(id_partida: int, id_adesao: int, status: str):
    # Descrição - Essa função emite a resposta do(a) jogador(a) organizador(a) de uma partida (de vôlei)
    # sobre o pedido de adesão de um jogador(a).
    for adesao in database.adesoes:
        if adesao.id_number == id_adesao and adesao.id_partida == id_partida:
            adesao.status = status
            return adesao
    raise HTTPException(status_code=404, detail="Pedido de adesão não encontrada no sistema.")

# Desistir de uma partida.
@manager.post("/partida/{id_partida}/desistencia")
def desistir_partida(id_partida: int, id_jogador: int):
    # Descrição - Essa função registra a desistência de um jogador(a) de uma partida (de vôlei) existente no sistema.
    for adesao in database.adesoes:
        if adesao.id_partida == id_partida and adesao.id_jogador == id_jogador:
            database.adesoes.remove(adesao)
            return {
                "Mensagem": "Jogador desistiu da partida."
            }
    raise HTTPException(status_code=404, detail="Pedido de adesão não encontrada no sistema.")

# Endpoints destinados à avaliações

# Avaliar partida e seus jogadores.
@manager.post("/avaliacoes", response_model=database.Avaliacao, status_code=status.HTTP_201_CREATED)
def avaliar(avaliacao: database.Avaliacao):
    # Descrição - Essa função registra a avaliação feita por um(a) jogador(a) para a partida (de vôlei)
    # e/ou aos jogadores(as) que estavam presentes
    database.avaliacoes.append(avaliacao)
    return avaliacao

# Listar todas as avaliações existentes no sistema.
@manager.get("/avaliacoes", response_model=List[database.Avaliacao])
def listar_avaliacoes():
    # Descrição - Essa função lista todas as avaliações feitas para as partidas (de vôlei) existentes no sistema.
    return database.avaliacoes
