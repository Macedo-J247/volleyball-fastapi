from fastapi.responses import HTMLResponse
from app import routes
import uvicorn

admin = routes.manager

@admin.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title> API de Match Making para Vôlei </title>
            <style>
                body { 
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background: #f7f9fb;
                    color: #222;
                }
                
                .container {
                    max-width: 820px;
                    margin: auto;
                }
                
                h1 {
                    color: #214a80;
                }
                
                .card {
                    background: #fff; 
                    border: 1px solid #e1e7ef; 
                    padding: 16px; 
                    border-radius: 8px; 
                    margin-bottom: 16px; 
                }
                
                label { 
                    display: block; 
                    margin-top: 8px; 
                    font-weight: 600; 
                }
                
                input, select, button { 
                    margin-top: 6px; 
                    padding: 8px; 
                    font-size: 14px; 
                    width: 100%; 
                    box-sizing: border-box; 
                }
                
                .row { 
                    display: flex; 
                    gap: 12px; 
                }
                
                .col { 
                    flex: 1;
                }
                
                .small { 
                    max-width: 200px; 
                }
                
                ul { 
                    padding-left: 18px; 
                }
                
                .meta { 
                    color: #666; 
                    font-size: 13px; 
                    margin-top: 8px; 
                }
            </style>
        </head>
        <body>
            <h1> Volleyball Manager V1 </h1>
            <p> [Status] -> Ativa </p>

            <div class="card">
                <h2> Principais endpoints existentes: </h2>
                <ul>
                    <li>
                        <a href="/jogador"> Jogadores </a>
                    </li>
                    <li>
                        <a href="/partida"> Partidas </a>
                    </li>
                    <li>
                        <a href="/avaliacoes"> Avaliações </a>
                    </li>
                </ul>
            </div>

            <div class="container">
                <h1>🏐 Criar Jogador</h1>

                <div class="card">
                    <form id="formJogador" onsubmit="event.preventDefault(); criarJogador();">
                        <div class="row">
                            <div class="col">
                                <label for="nome">Nome</label>
                                <input id="nome" name="nome" type="text" placeholder="Nome completo" required />
                            </div>

                            <div class="col small">
                                <label for="idade">Idade</label>
                                <input id="idade" name="idade" type="number" min="1" step="1" placeholder="Idade" required />
                            </div>
                        </div>

                        <div class="row">
                            <div class="col small">
                                <label for="sexo">Sexo</label>
                                <select id="sexo" name="sexo" required>
                                    <option value=""> Selecione </option>
                                    <option value="Masculino">Masculino</option>
                                    <option value="Feminino">Feminino</option>
                                    <option value="Não Informar">Não Informar</option>
                                </select>
                            </div>

                            <div class="col">
                                <label for="categoria"> Categoria </label>
                                <select id="categoria" name="categoria" required>
                                    <option value=""> Selecione </option>
                                    <option value="Novato">Novato</option>
                                    <option value="Amador">Amador</option>
                                    <option value="Profissional">Profissional</option>
                                </select>
                            </div>
                        </div>

                        <label for="email">Email (opcional)</label>
                        <input id="email" name="email" type="email" placeholder="email@exemplo.com" />

                        <div style="display:flex; gap:8px; margin-top:12px;">
                            <button type="submit">Criar Jogador</button>
                            <button type="button" onclick="limparFormulario()">Limpar</button>
                            <button type="button" onclick="listarJogadores()">Listar Jogadores</button>
                        </div>

                        <div class="meta">
                            Os campos id_number e avaliacoes são gerenciados pelo servidor.
                        </div>
                    </form>
                </div>

                <div class="card">
                    <h2>Lista de Jogadores</h2>
                    <ul id="listaJogadores">Carregando...</ul>
                </div>
            </div>

            <div class="container">
                <h1>🏐 Criar Partida</h1>

                <div class="card">
                    <form id="formPartida" onsubmit="event.preventDefault(); criarPartida();">
                        <div class="row">
                            <div class="col small">
                                <label for="id_organizador">ID Organizador</label>
                                <input id="id_organizador" name="id_organizador" type="number" min="1" required />
                            </div>

                            <div class="col">
                                <label for="local">Local</label>
                                <input id="local" name="local" type="text" placeholder="Nome da quadra / endereço" required />
                            </div>
                        </div>

                        <div class="row">
                            <div class="col small">
                                <label for="data">Data</label>
                                <input id="data" name="data" type="date" required />
                            </div>

                            <div class="col small">
                                <label for="hora">Hora</label>
                                <input id="hora" name="hora" type="time" required />
                            </div>

                            <div class="col small">
                                <label for="tipo">Tipo</label>
                                <select id="tipo" name="tipo" required>
                                    <option value="">-- selecione --</option>
                                    <option value="2x2">2x2</option>
                                    <option value="4x4">4x4</option>
                                    <option value="6x6">6x6</option>
                                </select>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col">
                                <label for="nivel_minimo">Nível mínimo</label>
                                <select id="nivel_minimo" name="nivel_minimo" required>
                                    <option value="">-- selecione --</option>
                                    <option value="Novato">Novato</option>
                                    <option value="Amador">Amador</option>
                                    <option value="Profissional">Profissional</option>
                                </select>
                            </div>

                            <div class="col small">
                                <label for="status">Status</label>
                                <select id="status" name="status" required>
                                    <option value="Em Espera">Em Espera</option>
                                    <option value="Em Andamento">Em Andamento</option>
                                    <option value="Terminada">Terminada</option>
                                </select>
                            </div>
                        </div>

                        <label for="jogadores">Jogadores iniciais IDs Opcional</label>
                        <input id="jogadores" name="jogadores" type="text" placeholder="IDs separados por vírgula, ex: 1,2,3" />

                        <div style="display:flex; gap:8px; margin-top:12px;">
                            <button type="submit">Criar Partida</button>
                            <button type="button" onclick="limparFormulario()">Limpar</button>
                            <button type="button" onclick="listarPartidas()">Listar Partidas</button>
                        </div>

                        <div class="meta">
                            O campo id_number é gerado pelo servidor. Jogadores é uma lista opcional de IDs.
                        </div>
                    </form>
                </div>

                <div class="card">
                    <h2>Lista de Partidas</h2>
                    <ul id="listaPartidas">Carregando...</ul>
                </div>
            </div>

            <div class="container">
                <h1>🏐 Registrar Avaliação</h1>

                <div class="card">
                    <form id="formAvaliacao" onsubmit="event.preventDefault(); criarAvaliacao();">
                        <div class="row">
                            <div class="col small">
                                <label for="id_avaliador">ID Avaliador</label>
                                <input id="id_avaliador" name="id_avaliador" type="number" min="1" required />
                            </div>

                            <div class="col small">
                                <label for="id_avaliado">ID Avaliado</label>
                                <input id="id_avaliado" name="id_avaliado" type="number" min="1" required />
                            </div>

                            <div class="col small">
                                <label for="id_partida">ID Partida</label>
                                <input id="id_partida" name="id_partida" type="number" min="1" required />
                            </div>

                            <div class="col small">
                                <label for="nota">Nota (1-10)</label>
                                <input id="nota" name="nota" type="number" min="1" max="10" required />
                            </div>
                        </div>

                        <label for="comentario">Comentário (opcional)</label>
                        <textarea id="comentario" name="comentario" rows="3" placeholder="Comentário opcional"></textarea>

                        <div style="display:flex; gap:8px; margin-top:12px;">
                            <button type="submit">Enviar Avaliação</button>
                            <button type="button" onclick="limparFormulario()">Limpar</button>
                            <button type="button" onclick="listarAvaliacoes()">Listar Avaliações</button>
                        </div>

                        <div class="meta">
                            O campo id_number da avaliação é atribuído pelo servidor. Preencha IDs existentes de jogadores/partidas.
                        </div>
                    </form>
                </div>

                <div class="card">
                    <h2>Lista de Avaliações</h2>
                    <ul id="listaAvaliacoes">Carregando...</ul>
                </div>
            </div>

            <div class="container">
                <h1>🏐 Solicitar Adesão</h1>

                <div class="card">
                    <form id="formAdesao" onsubmit="event.preventDefault(); enviarAdesao();">
                        <div class="row">
                            <div class="col small">
                                <label for="id_jogador">Jogador</label>
                                <select id="id_jogador" required>
                                    <option value="">Carregando jogadores...</option>
                                </select>
                            </div>

                            <div class="col small">
                                <label for="id_partida">Partida</label>
                                <select id="id_partida" required>
                                    <option value="">Carregando partidas...</option>
                                </select>
                            </div>

                            <div class="col small">
                                <label for="data_adesao">Data</label>
                                <input id="data_adesao" type="date" required />
                            </div>

                            <div class="col small">
                                <label for="hora_adesao">Hora</label>
                                <input id="hora_adesao" type="time" required />
                            </div>
                        </div>

                        <label for="status">Status inicial</label>
                        <select id="status" required>
                            <option value="Em Espera">Em Espera</option>
                            <option value="Aceita">Aceita</option>
                            <option value="Recusada">Recusada</option>
                        </select>

                        <label for="observacao">Observação (opcional)</label>
                        <textarea id="observacao" rows="3" placeholder="Alguma observação"></textarea>

                        <div style="display:flex; gap:8px; margin-top:12px;">
                            <button type="submit">Enviar Adesão</button>
                            <button type="button" onclick="limparFormulario()">Limpar</button>
                            <button type="button" onclick="listarAdesoes()">Listar Adesões</button>
                        </div>

                        <div class="meta">O campo id_number é gerado pelo servidor. Use IDs válidos de jogadores e partidas.</div>
                    </form>
                </div>

                <div class="card">
                    <h2>Respostas / Últimas ações</h2>
                    <div id="resultado">Nenhuma ação ainda.</div>
                </div>

                <div class="card">
                    <h2>Lista de Adesões</h2>
                    <ul id="listaAdesoes">Clique em "Listar Adesões" para carregar.</ul>
                </div>
            </div>

            <script>
                const API = "http://127.0.0.1:8000";

                async function criarJogador()
                {
                    const nome = document.getElementById("nome").value.trim();
                    const idade = parseInt(document.getElementById("idade").value, 10);
                    const sexo = document.getElementById("sexo").value;
                    const categoria = document.getElementById("categoria").value;
                    const email = document.getElementById("email").value.trim() || null;

                    if (!nome || !idade || !sexo || !categoria)
                    {
                        alert("Preencha todos os campos obrigatórios.");
                        return;
                    }

                    const payload = {
                        nome: nome,
                        idade: idade,
                        sexo: sexo,
                        categoria: categoria,
                        email: email
                    };

                    try
                    {
                        const res = await fetch(API + "/jogador", {
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify(payload)
                        });

                        if (!res.ok)
                        {
                            const err = await res.json().catch(() => ({ detail: "Erro" }));
                            alert("Erro: " + (err.detail || res.statusText));
                            return;
                        }

                        const novo = await res.json();
                        alert("Jogador criado: " + (novo.nome || novo.id_number || "OK"));
                        limparFormulario();
                        listarJogadores();
                    }
                    catch (e)
                    {
                        alert("Erro de conexão: " + e.message);
                    }
                }

                function limparFormulario()
                {
                    document.getElementById("formJogador").reset();
                }

                async function listarJogadores()
                {
                    try
                    {
                        const res = await fetch(API + "/jogador");
                        
                        if (!res.ok)
                        {
                            document.getElementById("listaJogadores").innerHTML = "<li>Não foi possível carregar jogadores.</li>";
                            return;
                        }
                    
                        const data = await res.json();
                        const ul = document.getElementById("listaJogadores");
                        ul.innerHTML = "";
                        if (!Array.isArray(data) || data.length === 0)
                        {
                            ul.innerHTML = "<li>Nenhum jogador cadastrado.</li>";
                            return;
                        }

                        data.forEach(j => {
                            const email = j.email ? j.email : "N/A";
                            const avaliacoes = (typeof j.avaliacoes !== 'undefined' && j.avaliacoes !== null) ? j.avaliacoes : 0;
                            const li = document.createElement("li");
                            li.textContent = `#${j.id_number} — ${j.nome}, ${j.idade} anos, ${j.sexo}, ${j.categoria} | email: ${email} | avaliações: ${avaliacoes}`;
                            ul.appendChild(li);
                        });
                    }
                    catch (e)
                    {
                        document.getElementById("listaJogadores").innerHTML = "<li>Erro ao buscar jogadores.</li>";
                    }
                }

                function parseJogadoresField(value)
                {
                    if (!value) return [];
                    return value.split(",").map(s => parseInt(s.trim(), 10)).filter(n => !isNaN(n));
                }

                async function criarPartida()
                {
                    const id_organizador = parseInt(document.getElementById("id_organizador").value, 10);
                    const local = document.getElementById("local").value.trim();
                    const data = document.getElementById("data").value;
                    const hora = document.getElementById("hora").value;
                    const tipo = document.getElementById("tipo").value;
                    const nivel_minimo = document.getElementById("nivel_minimo").value;
                    const status = document.getElementById("status").value;
                    const jogadores = parseJogadoresField(document.getElementById("jogadores").value);

                    if (!id_organizador || !local || !data || !hora || !tipo || !nivel_minimo || !status)
                    {
                        alert("Preencha todos os campos obrigatórios.");
                        return;
                    }

                    const payload = {
                        id_organizador: id_organizador,
                        local: local,
                        data: data,
                        hora: hora,
                        jogadores: jogadores,
                        tipo: tipo,
                        nivel_minino: nivel_minimo,
                        status: status
                    };

                    try {
                        const res = await fetch(API + "/partida", {
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify(payload)
                    });

                    if (!res.ok)
                    {
                        const err = await res.json().catch(() => ({ detail: res.statusText }));
                        alert("Erro: " + (err.detail || res.statusText));
                        return;
                    }

                    const novo = await res.json();
                    alert("Partida criada: #" + (novo.id_number || "OK"));
                    limparFormulario();
                    listarPartidas();
                    }
                    catch (e)
                    {
                        alert("Erro de conexão: " + e.message);
                    }
                }

                function limparFormulario()
                {
                    document.getElementById("formPartida").reset();
                }

                async function listarPartidas()
                {
                    try
                    {
                        const res = await fetch(API + "/partida");
                        if (!res.ok)
                        {
                            document.getElementById("listaPartidas").innerHTML = "<li>Não foi possível carregar partidas.</li>";
                            return;
                        }
                        const data = await res.json();
                        const ul = document.getElementById("listaPartidas");
                        ul.innerHTML = "";
                        if (!Array.isArray(data) || data.length === 0) {
                            ul.innerHTML = "<li>Nenhuma partida cadastrada.</li>";
                            return;
                        }

                        data.forEach(p => {
                            const jogs = Array.isArray(p.jogadores) ? p.jogadores.join(", ") : "N/A";
                            const li = document.createElement("li");
                            li.textContent = `#${p.id_number} — ${p.local} | ${p.data} ${p.hora} | ${p.tipo} | nível: ${p.nivel_minino || p.nivel_minimo || "N/A"} | status: ${p.status} | jogadores: ${jogs}`;
                            ul.appendChild(li);
                        });
                    }
                    catch (e)
                    {
                        document.getElementById("listaPartidas").innerHTML = "<li>Erro ao buscar partidas.</li>";
                    }
                }

                async function criarAvaliacao()
                {
                    const id_avaliador = parseInt(document.getElementById("id_avaliador").value, 10);
                    const id_avaliado = parseInt(document.getElementById("id_avaliado").value, 10);
                    const id_partida = parseInt(document.getElementById("id_partida").value, 10);
                    const nota = parseInt(document.getElementById("nota").value, 10);
                    const comentario = document.getElementById("comentario").value.trim() || null;

                    if (!id_avaliador || !id_avaliado || !id_partida || !nota)
                    {
                        alert("Preencha todos os campos obrigatórios.");
                        return;
                    }
                    
                    if (nota < 1 || nota > 10)
                    {
                        alert("A nota deve estar entre 1 e 10.");
                        return;
                    }

                    const payload = {
                        id_avaliador: id_avaliador,
                        id_avaliado: id_avaliado,
                        id_partida: id_partida,
                        nota: nota,
                        comentario: comentario
                    };

                    try
                    {
                        const res = await fetch(API + "/avaliacoes", {
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify(payload)
                        });

                        if (!res.ok)
                        {
                            const err = await res.json().catch(() => ({ detail: res.statusText }));
                            alert("Erro: " + (err.detail || res.statusText));
                            return;
                        }

                        const novo = await res.json();
                        alert("Avaliação registrada: ID " + (novo.id_number || "OK"));
                        limparFormulario();
                        listarAvaliacoes();
                    }
                    catch (e)
                    {
                        alert("Erro de conexão: " + e.message);
                    }
                }

                function limparFormulario()
                {
                    document.getElementById("formAvaliacao").reset();
                }

                async function listarAvaliacoes() {
                    try
                    {
                        const res = await fetch(API + "/avaliacoes");
                        if (!res.ok)
                        {
                            document.getElementById("listaAvaliacoes").innerHTML = "<li>Não foi possível carregar avaliações.</li>";
                            return;
                        }
                        const data = await res.json();
                        const ul = document.getElementById("listaAvaliacoes");
                        ul.innerHTML = "";
                        if (!Array.isArray(data) || data.length === 0)
                        {
                            ul.innerHTML = "<li>Nenhuma avaliação registrada.</li>";
                            return;
                        }

                        data.forEach(a => {
                            const com = a.comentario ? ` — ${a.comentario}` : "";
                            const li = document.createElement("li");
                            li.textContent = `#${a.id_number || "?"} — Avaliador:${a.id_avaliador} Avaliado:${a.id_avaliado} Partida:${a.id_partida} Nota:${a.nota}${com}`;
                            ul.appendChild(li);
                        });
                    }
                    catch (e)
                    {
                        document.getElementById("listaAvaliacoes").innerHTML = "<li>Erro ao buscar avaliações.</li>";
                    }
                }

                async function preencherSelects() {
                    try
                    {
                        const resJ = await fetch(API + "/jogador");
                    
                        if (resJ.ok)
                        {
                            const jogadores = await resJ.json();
                            const selJ = document.getElementById("id_jogador");
                            selJ.innerHTML = "<option value=''>-- selecione jogador --</option>";
                            jogadores.forEach(j => {
                                const opt = document.createElement("option");
                                opt.value = j.id_number;
                                opt.textContent = `#${j.id_number} — ${j.nome}`;
                                selJ.appendChild(opt);
                            });
                        }
                        else
                        {
                            document.getElementById("id_jogador").innerHTML = "<option value=''>Erro ao carregar</option>";
                        }
                    }
                    catch (e)
                    {
                        document.getElementById("id_jogador").innerHTML = "<option value=''>Erro de conexão</option>";
                    }

                    try
                    {
                        const resP = await fetch(API + "/partida");
                    
                        if (resP.ok)
                        {
                            const partidas = await resP.json();
                            const selP = document.getElementById("id_partida");
                            selP.innerHTML = "<option value=''>-- selecione partida --</option>";
                            partidas.forEach(p => {
                                const opt = document.createElement("option");
                                opt.value = p.id_number;
                                opt.textContent = `#${p.id_number} — ${p.local} (${p.data} ${p.hora}) [${p.status}]`;
                                selP.appendChild(opt);
                            });
                        }
                        else
                        {
                            document.getElementById("id_partida").innerHTML = "<option value=''>Erro ao carregar</option>";
                        }
                    }
                    catch (e)
                    {
                        document.getElementById("id_partida").innerHTML = "<option value=''>Erro de conexão</option>";
                    }
                }

                function limparFormulario() {
                    document.getElementById("formAdesao").reset();
                    document.getElementById("resultado").textContent = "Formulário limpo.";
                }

                async function enviarAdesao()
                {
                    const id_jogador = parseInt(document.getElementById("id_jogador").value, 10);
                    const id_partida = parseInt(document.getElementById("id_partida").value, 10);
                    const data_adesao = document.getElementById("data_adesao").value;
                    const hora_adesao = document.getElementById("hora_adesao").value;
                    const status = document.getElementById("status").value;
                    const observacao = document.getElementById("observacao").value.trim() || null;

                    if (!id_jogador || !id_partida || !data_adesao || !hora_adesao || !status)
                    {
                        alert("Preencha todos os campos obrigatórios.");
                        return;
                    }

                    const payload = {
                        id_jogador: id_jogador,
                        id_partida: id_partida,
                        data_adesao: data_adesao,
                        hora_adesao: hora_adesao,
                        status: status,
                        observacao: observacao
                    };

                    try
                    {
                        // POST para /partida/{id_partida}/adesao conforme sua rota existente
                        const res = await fetch(API + `/partida/${id_partida}/adesao`, {
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify(payload)
                        });

                        const resultadoEl = document.getElementById("resultado");

                        if (!res.ok)
                        {
                            const err = await res.json().catch(() => ({ detail: res.statusText }));
                            resultadoEl.textContent = "Erro: " + (err.detail || res.statusText);
                            return;
                        }

                        const novo = await res.json();
                        resultadoEl.textContent = `Adesão enviada: ID ${novo.id_number || "?"} — jogador ${novo.id_jogador} -> partida ${novo.id_partida} (status: ${novo.status})`;
                        limparFormulario();
                    }
                    catch (e)
                    {
                        document.getElementById("resultado").textContent = "Erro de conexão: " + e.message;
                    }
                }

                async function listarAdesoes() {
                    const ul = document.getElementById("listaAdesoes");
                    ul.innerHTML = "<li>Carregando...</li>";
                    try
                    {
                        const res = await fetch(API + "/adesoes");
                        if (!res.ok)
                        {
                            ul.innerHTML = `<li>Endpoint /adesoes indisponível (${res.status}). Se quiser, implemente GET /adesoes no servidor.</li>`;
                            return;
                        }
                        const data = await res.json();
                        ul.innerHTML = "";
                        if (!Array.isArray(data) || data.length === 0)
                        {
                            ul.innerHTML = "<li>Nenhuma adesão registrada.</li>";
                            return;
                        }
                        data.forEach(a => {
                            const obs = a.observacao ? ` — ${a.observacao}` : "";
                            const li = document.createElement("li");
                            li.textContent = `#${a.id_number || "?"} — Jogador:${a.id_jogador} Partida:${a.id_partida} ${a.data_adesao} ${a.hora_adesao} Status:${a.status}${obs}`;
                            ul.appendChild(li);
                        });
                    }
                    catch (e)
                    {
                        ul.innerHTML = "<li>Erro ao buscar adesões: " + e.message + "</li>";
                    }
                }

                preencherSelects();
            </script>
        </body>
    </html>
    """

def main():
    uvicorn.run('main:admin', host='127.0.0.1', port=8000, reload=True)


if __name__ == '__main__':
    main()
