# FlyScanner

Ferramenta pessoal de busca de passagens aéreas baratas, com interface em
CustomTkinter.

## Como rodar

```bash
pip install customtkinter
python interface.py
```

## Estrutura

```
flyscanner/
│   apis.py          -> carrega dinamicamente os módulos de apis_input/ e apis_output/
│   buscador.py       -> o "robô": roda em thread, consulta inputs, filtra e envia pros outputs
│   condicoes.py      -> filtros de busca (salvos em condicoes.json)
│   interface.py       -> a UI (rode este arquivo)
│   log.py            -> log central (arquivo log/flyscanner.log + fila em tempo real p/ UI)
│
├───apis_input/        -> uma api de entrada por arquivo (google_flight.py, skyscanner.py, decolar.py...)
└───apis_output/       -> uma api de saída por arquivo (terminal.py, telegram.py, whatsapp.py...)
```

## Como adicionar uma nova api de entrada

Crie `apis_input/nome_da_api.py` com:

```python
NOME = "Nome Amigável"
CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API", "tipo": "senha"},
]

def buscar(config: dict, condicoes: dict) -> list:
    # retorna lista de dicts no formato:
    # {"origem", "destino", "tipo_viagem", "data_ida", "data_volta",
    #  "valor", "moeda", "companhia", "link", "fonte"}
    ...
```

Ela aparece automaticamente na aba "Adicionar Inputs" da interface.

## Como adicionar uma nova api de saída

Crie `apis_output/nome_do_canal.py` com:

```python
NOME = "Nome Amigável"
CAMPOS_CONFIG = [...]  # pode ser [] se não precisa de config

def enviar(voo: dict, config: dict, log_callback=None) -> None:
    ...
```

Ela aparece automaticamente na aba "Retorno" da interface.

## Estado atual (versão de teste)

- Input real implementado: nenhum ainda (Google Flights não tem API pública
  oficial de preços). `google_flight.py` está em **modo simulado**, gerando
  voos aleatórios só para validar o fluxo completo. Troque o corpo de
  `buscar()` quando tiver um provedor real (Amadeus, RapidAPI/Skyscanner, etc).
- Output implementado de verdade: `terminal.py` (mostra na própria interface).
- Stubs (esqueletos prontos para implementar): `skyscanner.py`, `decolar.py`,
  `telegram.py`, `whatsapp.py`.

## Arquivos gerados em uso (não versionar)

- `condicoes.json` — filtros salvos
- `config_apis.json` — chaves/tokens e apis de saída ativas
- `log/flyscanner.log` — histórico de log
