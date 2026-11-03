# 📚 flyscanner

> 🏷️ **Inventário técnico do projeto**, gerado automaticamente em 03/11/2026 às 11:09 por *documentador.pyw* v1.0. Este arquivo é um retrato fiel dos arquivos analisados (sem interpretação por IA).
>
> 🛡️ **Integridade da extração:** ✅ completa

## 🧭 Sumário

- [📋 Resumo executivo](#sec-resumo)
- [🧰 Tecnologias detectadas](#sec-tech)
- [📊 Linguagens e métricas](#sec-langs)
- [🌳 Estrutura do projeto](#sec-tree)
- [🗂️ Índice de arquivos](#sec-index)
- [📄 Conteúdo dos arquivos](#sec-content)
- [🚫 Itens não incorporados](#sec-noinc)
- [✅ Integridade da extração](#sec-integ)

---

<a id="sec-resumo"></a>

## 📋 Resumo executivo

| Item | Valor |
|---|---|
| 📂 Raiz | `C:\Scripts\flyscanner` |
| 🕒 Gerado em | 2026-11-03 11:09:47 |
| 📁 Diretórios | 54 |
| 📄 Arquivos encontrados | 102 |
| 📝 Arquivos de texto incorporados | 52 |
| 🧮 Linhas de texto | 9.936 |
| 🖼️ Binários (somente metadados) | 49 |
| ⏭️ Ignorados | 1 |
| 🚫 Excluídos por regra | 1 |
| 🔗 Links simbólicos | 0 |
| ❌ Erros | 0 |
| 💾 Tamanho do texto | 366.2 KB |
| 🔑 SHA256 do conteúdo | `d30eb1427c9c1f8c53f8efc84152d2bf00e2a210c16c235f6cfa8cd4e470e1eb` |

<a id="sec-tech"></a>

## 🧰 Tecnologias detectadas

| Tecnologia | Evidência |
|---|---|
| 🔀 Git | `.gitignore` |

<a id="sec-langs"></a>

## 📊 Linguagens e métricas

| Linguagem | Arquivos | Linhas | Tamanho | Participação |
|---|---:|---:|---:|---|
| 🐍 Python | 17 | 5322 | 238.6 KB | `█████████████░░░░░░░` 65.1% |
| 📄 Outros | 26 | 1086 | 55.0 KB | `███░░░░░░░░░░░░░░░░░` 15.0% |
| 📄 Texto | 2 | 2814 | 48.6 KB | `███░░░░░░░░░░░░░░░░░` 13.3% |
| 📝 Markdown | 3 | 591 | 21.8 KB | `█░░░░░░░░░░░░░░░░░░░` 6.0% |
| 🧾 JSON | 3 | 98 | 1.9 KB | `░░░░░░░░░░░░░░░░░░░░` 0.5% |
| 🔀 Git | 1 | 25 | 404 B | `░░░░░░░░░░░░░░░░░░░░` 0.1% |

<a id="sec-tree"></a>

## 🌳 Estrutura do projeto

```text
flyscanner/
├── .git/
│   ├── hooks/
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── push-to-checkout.sample
│   │   ├── sendemail-validate.sample
│   │   └── update.sample
│   ├── info/
│   │   └── exclude
│   ├── logs/
│   │   ├── refs/
│   │   │   ├── heads/
│   │   │   │   └── main
│   │   │   └── remotes/
│   │   │       └── origin/
│   │   │           └── main
│   │   └── HEAD
│   ├── objects/
│   │   ├── 02/
│   │   │   └── c2a58090da1bcc7edda05bbed354cd4e2959fe
│   │   ├── 0a/
│   │   │   └── 21cadb7db0d5a0b6d525641c58adc983260e58
│   │   ├── 15/
│   │   │   └── f361958c53ce09aed9c6f63917ce96e5e1aabd
│   │   ├── 26/
│   │   │   └── 7184ae95e6d559acb11f4cd3b2e27a0275fd18
│   │   ├── 34/
│   │   │   └── 90333be399b1034574d8f42984af1370c1b0a2
│   │   ├── 3c/
│   │   │   └── b5ab6a4a922cdf86a82cd9f1f74baf436cad4f
│   │   ├── 3d/
│   │   │   └── 4f613f5ebf806773bdc2c250719fdf46cf6b08
│   │   ├── 3e/
│   │   │   └── e1babfd8b29475a4f04894ac5fb258a7919e12
│   │   ├── 48/
│   │   │   └── 08ab758e0ad4df48354f3f920aa9f615c819a3
│   │   ├── 4a/
│   │   │   └── eeb8b59d501eb6080ed23164da6be1e0079850
│   │   ├── 4c/
│   │   │   └── b59194d9990da0f832c6741a6ff84ecb7ac219
│   │   ├── 4f/
│   │   │   └── 2906b4e572fd76d207ed0a667539b34cc63611
│   │   ├── 71/
│   │   │   └── 01e22178f7038e1154467a94fc20b8e4d87bdd
│   │   ├── 79/
│   │   │   └── 85c21c3289843651cc22490b40ca745e415603
│   │   ├── 86/
│   │   │   ├── 175dcb48ee1954a58d9f14c2eae3acbdd36269
│   │   │   ├── 6a9cb297c595d94cd771ef2938a2a260385ffb
│   │   │   └── 95f65cb76456c198cb86201a8fdda1cac4e63e
│   │   ├── 92/
│   │   │   └── e006d60645684a7376aa0ded27fe185a5af8fc
│   │   ├── 9b/
│   │   │   └── ad42b8faf6b22b607983cf9b1ab7786b0471af
│   │   ├── a0/
│   │   │   └── 7c5b90093009e059e18ab5e49b34b15e7b53d9
│   │   ├── a1/
│   │   │   └── 13afef0488a9e43608c66f42ea94bbe596f482
│   │   ├── a7/
│   │   │   └── 00f8beea4e15ebe2af6cd99f1f6cd181afaf73
│   │   ├── b3/
│   │   │   ├── e05071d81501d67b3a780c907807b7801dfb95
│   │   │   └── fd2e138a904ac1fc9c2561077ae06958a87abb
│   │   ├── c2/
│   │   │   └── 4fac19c1f670939c0ddec004b2db9cd1bd8642
│   │   ├── c7/
│   │   │   └── 35132f8a2b16c20041a96c481e069af2e5ac88
│   │   ├── cf/
│   │   │   └── 1f721644db5a90e5490ef86b95a81240c95c71
│   │   ├── d2/
│   │   │   └── 7a1862a680c4199a941d73d0b8c017d092d392
│   │   ├── d4/
│   │   │   └── f2040909ea94981a7dd4de75597fbb00f486d4
│   │   ├── e0/
│   │   │   └── 44a12d30164e2feb5e07e156a15496bd9eb6e9
│   │   ├── e3/
│   │   │   └── 6c5104418c79a8e480a47abf1042a6113d6392
│   │   ├── e9/
│   │   │   └── 9cc6f5dc2db7a489e31270a93ca5d9178dc16f
│   │   ├── ec/
│   │   │   └── 7bc51918ab31e5999fcb0959988af8656572bf
│   │   ├── f4/
│   │   │   └── 97e5a7ad10065df025ab639a8e39338099c354
│   │   ├── info/
│   │   └── pack/
│   ├── refs/
│   │   ├── heads/
│   │   │   └── main
│   │   ├── remotes/
│   │   │   └── origin/
│   │   │       └── main
│   │   └── tags/
│   ├── COMMIT_EDITMSG
│   ├── config
│   ├── description
│   ├── HEAD
│   └── index
├── __pycache__/
│   ├── apis.cpython-314.pyc
│   ├── buscador.cpython-314.pyc
│   ├── condicoes.cpython-314.pyc
│   ├── historico.cpython-314.pyc
│   └── log.cpython-314.pyc
├── apis_input/
│   ├── __pycache__/
│   │   ├── aviasales.cpython-314.pyc
│   │   ├── decolar.cpython-314.pyc
│   │   ├── google_flight.cpython-314.pyc
│   │   ├── kiwi_tequila.cpython-314.pyc
│   │   ├── serpapi_flights.cpython-314.pyc
│   │   └── skyscanner.cpython-314.pyc
│   ├── aviasales.py
│   ├── decolar.py
│   ├── google_flight.py
│   ├── kiwi_tequila.py
│   ├── serpapi_flights.py
│   └── skyscanner.py
├── apis_output/
│   ├── __pycache__/
│   │   ├── markdown_export.cpython-314.pyc
│   │   ├── telegram.cpython-314.pyc
│   │   ├── terminal.cpython-314.pyc
│   │   └── whatsapp.cpython-314.pyc
│   ├── markdown_export.py
│   ├── telegram.py
│   ├── terminal.py
│   └── whatsapp.py
├── DOCS/
│   ├── Documentação Técnica e Arquitetural.txt
│   ├── PROMPT.md
│   ├── README.md
│   └── Resposta PROMPT.txt
├── evolution-api/  [EXCLUÍDO AUTOMATICAMENTE: Pasta Massiva (> 1000 arq)]
├── log/
│   └── flyscanner.log
├── .gitignore
├── apis.py
├── buscador.py
├── condicoes.json
├── condicoes.py
├── config_apis.json
├── DOCUMENTACAO_PROJETO.md  [SAÍDA GERADA PELA FERRAMENTA]
├── documentador.pyw  [ESTA FERRAMENTA]
├── historico.json
├── historico.py
├── interface.pyw
├── log.py
└── ofertas.md

54 diretórios, 102 arquivos
```

<a id="sec-index"></a>

## 🗂️ Índice de arquivos

| # | Tipo | Arquivo | Linguagem | Tamanho | Linhas | Situação |
|--:|:-:|---|---|--:|--:|---|
| 1 | 📄 | [`.git/hooks/applypatch-msg.sample`](#f-0) | Outros | 478 B | 15 | ✅ Incluído |
| 2 | 📄 | [`.git/hooks/commit-msg.sample`](#f-1) | Outros | 896 B | 24 | ✅ Incluído |
| 3 | 📄 | [`.git/hooks/fsmonitor-watchman.sample`](#f-2) | Outros | 4.6 KB | 174 | ✅ Incluído |
| 4 | 📄 | [`.git/hooks/post-update.sample`](#f-3) | Outros | 189 B | 8 | ✅ Incluído |
| 5 | 📄 | [`.git/hooks/pre-applypatch.sample`](#f-4) | Outros | 424 B | 14 | ✅ Incluído |
| 6 | 📄 | [`.git/hooks/pre-commit.sample`](#f-5) | Outros | 1.6 KB | 49 | ✅ Incluído |
| 7 | 📄 | [`.git/hooks/pre-merge-commit.sample`](#f-6) | Outros | 416 B | 13 | ✅ Incluído |
| 8 | 📄 | [`.git/hooks/pre-push.sample`](#f-7) | Outros | 1.3 KB | 53 | ✅ Incluído |
| 9 | 📄 | [`.git/hooks/pre-rebase.sample`](#f-8) | Outros | 4.8 KB | 169 | ✅ Incluído |
| 10 | 📄 | [`.git/hooks/pre-receive.sample`](#f-9) | Outros | 544 B | 24 | ✅ Incluído |
| 11 | 📄 | [`.git/hooks/prepare-commit-msg.sample`](#f-10) | Outros | 1.5 KB | 42 | ✅ Incluído |
| 12 | 📄 | [`.git/hooks/push-to-checkout.sample`](#f-11) | Outros | 2.7 KB | 78 | ✅ Incluído |
| 13 | 📄 | [`.git/hooks/sendemail-validate.sample`](#f-12) | Outros | 2.3 KB | 77 | ✅ Incluído |
| 14 | 📄 | [`.git/hooks/update.sample`](#f-13) | Outros | 3.6 KB | 128 | ✅ Incluído |
| 15 | 📄 | [`.git/info/exclude`](#f-14) | Outros | 240 B | 6 | ✅ Incluído |
| 16 | 📄 | [`.git/logs/refs/heads/main`](#f-15) | Outros | 165 B | 1 | ✅ Incluído |
| 17 | 📄 | [`.git/logs/refs/remotes/origin/main`](#f-16) | Outros | 150 B | 1 | ✅ Incluído |
| 18 | 📄 | [`.git/logs/HEAD`](#f-17) | Outros | 165 B | 1 | ✅ Incluído |
| 19 | 🖼️ | `.git/objects/02/c2a58090da1bcc7edda05bbed354cd4e2959fe` | Binário não identificado | 1.7 KB | - | 🖼️ Binário |
| 20 | 🖼️ | `.git/objects/0a/21cadb7db0d5a0b6d525641c58adc983260e58` | Binário não identificado | 722 B | - | 🖼️ Binário |
| 21 | 🖼️ | `.git/objects/15/f361958c53ce09aed9c6f63917ce96e5e1aabd` | Binário não identificado | 174 B | - | 🖼️ Binário |
| 22 | 🖼️ | `.git/objects/26/7184ae95e6d559acb11f4cd3b2e27a0275fd18` | Binário não identificado | 1002 B | - | 🖼️ Binário |
| 23 | 🖼️ | `.git/objects/34/90333be399b1034574d8f42984af1370c1b0a2` | Binário não identificado | 15.2 KB | - | 🖼️ Binário |
| 24 | 🖼️ | `.git/objects/3c/b5ab6a4a922cdf86a82cd9f1f74baf436cad4f` | Binário não identificado | 137 B | - | 🖼️ Binário |
| 25 | 🖼️ | `.git/objects/3d/4f613f5ebf806773bdc2c250719fdf46cf6b08` | Binário não identificado | 613 B | - | 🖼️ Binário |
| 26 | 🖼️ | `.git/objects/3e/e1babfd8b29475a4f04894ac5fb258a7919e12` | Binário não identificado | 55.4 KB | - | 🖼️ Binário |
| 27 | 🖼️ | `.git/objects/48/08ab758e0ad4df48354f3f920aa9f615c819a3` | Binário não identificado | 1.4 KB | - | 🖼️ Binário |
| 28 | 🖼️ | `.git/objects/4a/eeb8b59d501eb6080ed23164da6be1e0079850` | Binário não identificado | 2.3 KB | - | 🖼️ Binário |
| 29 | 🖼️ | `.git/objects/4c/b59194d9990da0f832c6741a6ff84ecb7ac219` | Binário não identificado | 2.1 KB | - | 🖼️ Binário |
| 30 | 🖼️ | `.git/objects/4f/2906b4e572fd76d207ed0a667539b34cc63611` | Binário não identificado | 136 B | - | 🖼️ Binário |
| 31 | 📄 | [`.git/objects/71/01e22178f7038e1154467a94fc20b8e4d87bdd`](#f-30) | Outros | 277 B | 4 | ✅ Incluído |
| 32 | 🖼️ | `.git/objects/79/85c21c3289843651cc22490b40ca745e415603` | Binário não identificado | 2.3 KB | - | 🖼️ Binário |
| 33 | 🖼️ | `.git/objects/86/175dcb48ee1954a58d9f14c2eae3acbdd36269` | Binário não identificado | 329 B | - | 🖼️ Binário |
| 34 | 🖼️ | `.git/objects/86/6a9cb297c595d94cd771ef2938a2a260385ffb` | Binário não identificado | 161 B | - | 🖼️ Binário |
| 35 | 🖼️ | `.git/objects/86/95f65cb76456c198cb86201a8fdda1cac4e63e` | Binário não identificado | 59 B | - | 🖼️ Binário |
| 36 | 🖼️ | `.git/objects/92/e006d60645684a7376aa0ded27fe185a5af8fc` | Binário não identificado | 233 B | - | 🖼️ Binário |
| 37 | 🖼️ | `.git/objects/9b/ad42b8faf6b22b607983cf9b1ab7786b0471af` | Binário não identificado | 1.6 KB | - | 🖼️ Binário |
| 38 | 🖼️ | `.git/objects/a0/7c5b90093009e059e18ab5e49b34b15e7b53d9` | Binário não identificado | 189 B | - | 🖼️ Binário |
| 39 | 🖼️ | `.git/objects/a1/13afef0488a9e43608c66f42ea94bbe596f482` | Binário não identificado | 2.3 KB | - | 🖼️ Binário |
| 40 | 🖼️ | `.git/objects/a7/00f8beea4e15ebe2af6cd99f1f6cd181afaf73` | Binário não identificado | 1.4 KB | - | 🖼️ Binário |
| 41 | 🖼️ | `.git/objects/b3/e05071d81501d67b3a780c907807b7801dfb95` | Binário não identificado | 1.0 KB | - | 🖼️ Binário |
| 42 | 🖼️ | `.git/objects/b3/fd2e138a904ac1fc9c2561077ae06958a87abb` | Binário não identificado | 1.2 KB | - | 🖼️ Binário |
| 43 | 🖼️ | `.git/objects/c2/4fac19c1f670939c0ddec004b2db9cd1bd8642` | Binário não identificado | 8.1 KB | - | 🖼️ Binário |
| 44 | 🖼️ | `.git/objects/c7/35132f8a2b16c20041a96c481e069af2e5ac88` | Binário não identificado | 911 B | - | 🖼️ Binário |
| 45 | 🖼️ | `.git/objects/cf/1f721644db5a90e5490ef86b95a81240c95c71` | Binário não identificado | 2.3 KB | - | 🖼️ Binário |
| 46 | 🖼️ | `.git/objects/d2/7a1862a680c4199a941d73d0b8c017d092d392` | Binário não identificado | 1.1 KB | - | 🖼️ Binário |
| 47 | 🖼️ | `.git/objects/d4/f2040909ea94981a7dd4de75597fbb00f486d4` | Binário não identificado | 492 B | - | 🖼️ Binário |
| 48 | 🖼️ | `.git/objects/e0/44a12d30164e2feb5e07e156a15496bd9eb6e9` | Binário não identificado | 2.2 KB | - | 🖼️ Binário |
| 49 | 🖼️ | `.git/objects/e3/6c5104418c79a8e480a47abf1042a6113d6392` | Binário não identificado | 1.3 KB | - | 🖼️ Binário |
| 50 | 🖼️ | `.git/objects/e9/9cc6f5dc2db7a489e31270a93ca5d9178dc16f` | Binário não identificado | 311 B | - | 🖼️ Binário |
| 51 | 🖼️ | `.git/objects/ec/7bc51918ab31e5999fcb0959988af8656572bf` | Binário não identificado | 106.6 KB | - | 🖼️ Binário |
| 52 | 🖼️ | `.git/objects/f4/97e5a7ad10065df025ab639a8e39338099c354` | Binário não identificado | 433 B | - | 🖼️ Binário |
| 53 | 📄 | [`.git/refs/heads/main`](#f-52) | Outros | 41 B | 1 | ✅ Incluído |
| 54 | 📄 | [`.git/refs/remotes/origin/main`](#f-53) | Outros | 41 B | 1 | ✅ Incluído |
| 55 | 📄 | [`.git/COMMIT_EDITMSG`](#f-54) | Outros | 12 B | 1 | ✅ Incluído |
| 56 | 📄 | [`.git/config`](#f-55) | Outros | 310 B | 13 | ✅ Incluído |
| 57 | 📄 | [`.git/description`](#f-56) | Outros | 73 B | 1 | ✅ Incluído |
| 58 | 📄 | [`.git/HEAD`](#f-57) | Outros | 21 B | 1 | ✅ Incluído |
| 59 | 🖼️ | `.git/index` | Binário não identificado | 2.6 KB | - | 🖼️ Binário |
| 60 | 🖼️ | `__pycache__/apis.cpython-314.pyc` | Bytecode Python | 7.0 KB | - | 🖼️ Binário |
| 61 | 🖼️ | `__pycache__/buscador.cpython-314.pyc` | Bytecode Python | 8.6 KB | - | 🖼️ Binário |
| 62 | 🖼️ | `__pycache__/condicoes.cpython-314.pyc` | Bytecode Python | 7.6 KB | - | 🖼️ Binário |
| 63 | 🖼️ | `__pycache__/historico.cpython-314.pyc` | Bytecode Python | 3.1 KB | - | 🖼️ Binário |
| 64 | 🖼️ | `__pycache__/log.cpython-314.pyc` | Bytecode Python | 6.1 KB | - | 🖼️ Binário |
| 65 | 🖼️ | `apis_input/__pycache__/aviasales.cpython-314.pyc` | Bytecode Python | 4.0 KB | - | 🖼️ Binário |
| 66 | 🖼️ | `apis_input/__pycache__/decolar.cpython-314.pyc` | Bytecode Python | 862 B | - | 🖼️ Binário |
| 67 | 🖼️ | `apis_input/__pycache__/google_flight.cpython-314.pyc` | Bytecode Python | 763 B | - | 🖼️ Binário |
| 68 | 🖼️ | `apis_input/__pycache__/kiwi_tequila.cpython-314.pyc` | Bytecode Python | 2.6 KB | - | 🖼️ Binário |
| 69 | 🖼️ | `apis_input/__pycache__/serpapi_flights.cpython-314.pyc` | Bytecode Python | 5.0 KB | - | 🖼️ Binário |
| 70 | 🖼️ | `apis_input/__pycache__/skyscanner.cpython-314.pyc` | Bytecode Python | 1015 B | - | 🖼️ Binário |
| 71 | 🐍 | [`apis_input/aviasales.py`](#f-70) | Python | 3.1 KB | 76 | ✅ Incluído |
| 72 | 🐍 | [`apis_input/decolar.py`](#f-71) | Python | 477 B | 18 | ✅ Incluído |
| 73 | 🐍 | [`apis_input/google_flight.py`](#f-72) | Python | 368 B | 14 | ✅ Incluído |
| 74 | 🐍 | [`apis_input/kiwi_tequila.py`](#f-73) | Python | 1.8 KB | 60 | ✅ Incluído |
| 75 | 🐍 | [`apis_input/serpapi_flights.py`](#f-74) | Python | 4.3 KB | 107 | ✅ Incluído |
| 76 | 🐍 | [`apis_input/skyscanner.py`](#f-75) | Python | 823 B | 24 | ✅ Incluído |
| 77 | 🖼️ | `apis_output/__pycache__/markdown_export.cpython-314.pyc` | Bytecode Python | 4.5 KB | - | 🖼️ Binário |
| 78 | 🖼️ | `apis_output/__pycache__/telegram.cpython-314.pyc` | Bytecode Python | 7.9 KB | - | 🖼️ Binário |
| 79 | 🖼️ | `apis_output/__pycache__/terminal.cpython-314.pyc` | Bytecode Python | 2.4 KB | - | 🖼️ Binário |
| 80 | 🖼️ | `apis_output/__pycache__/whatsapp.cpython-314.pyc` | Bytecode Python | 1.3 KB | - | 🖼️ Binário |
| 81 | 🐍 | [`apis_output/markdown_export.py`](#f-80) | Python | 2.9 KB | 71 | ✅ Incluído |
| 82 | 🐍 | [`apis_output/telegram.py`](#f-81) | Python | 5.9 KB | 130 | ✅ Incluído |
| 83 | 🐍 | [`apis_output/terminal.py`](#f-82) | Python | 1.3 KB | 40 | ✅ Incluído |
| 84 | 🐍 | [`apis_output/whatsapp.py`](#f-83) | Python | 5.3 KB | 155 | ✅ Incluído |
| 85 | 📄 | [`DOCS/Documentação Técnica e Arquitetural.txt`](#f-84) | Texto | 46.9 KB | 2804 | ✅ Incluído |
| 86 | 📝 | [`DOCS/PROMPT.md`](#f-85) | Markdown | 4.9 KB | 110 | ✅ Incluído |
| 87 | 📝 | [`DOCS/README.md`](#f-86) | Markdown | 2.3 KB | 74 | ✅ Incluído |
| 88 | 📄 | [`DOCS/Resposta PROMPT.txt`](#f-87) | Texto | 1.7 KB | 10 | ✅ Incluído |
| 89 | 📄 | [`log/flyscanner.log`](#f-88) | Outros | 28.3 KB | 187 | ✅ Incluído |
| 90 | 🔀 | [`.gitignore`](#f-89) | Git | 404 B | 25 | ✅ Incluído |
| 91 | 🐍 | [`apis.py`](#f-90) | Python | 4.1 KB | 113 | ✅ Incluído |
| 92 | 🐍 | [`buscador.py`](#f-91) | Python | 6.5 KB | 155 | ✅ Incluído |
| 93 | 🧾 | [`condicoes.json`](#f-92) | JSON | 286 B | 14 | ✅ Incluído |
| 94 | 🐍 | [`condicoes.py`](#f-93) | Python | 5.6 KB | 159 | ✅ Incluído |
| 95 | 🧾 | [`config_apis.json`](#f-94) | JSON | 1.3 KB | 66 | ✅ Incluído |
| 96 | ⏭️ | `DOCUMENTACAO_PROJETO.md` | Saída da ferramenta | 350.7 KB | - | ⏭️ Ignorado |
| 97 | 🐍 | [`documentador.pyw`](#f-96) | Python | 160.0 KB | 3377 | ✅ Incluído |
| 98 | 🧾 | [`historico.json`](#f-97) | JSON | 319 B | 18 | ✅ Incluído |
| 99 | 🐍 | [`historico.py`](#f-98) | Python | 2.2 KB | 64 | ✅ Incluído |
| 100 | 🐍 | [`interface.pyw`](#f-99) | Python | 31.0 KB | 658 | ✅ Incluído |
| 101 | 🐍 | [`log.py`](#f-100) | Python | 3.0 KB | 101 | ✅ Incluído |
| 102 | 📝 | [`ofertas.md`](#f-101) | Markdown | 14.6 KB | 407 | ✅ Incluído |

<a id="sec-content"></a>

## 📄 Conteúdo dos arquivos

<a id="f-0"></a>
<details>
<summary>📄 <b>.git/hooks/applypatch-msg.sample</b> — Outros · 478 B · 15 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:
```

</details>

<a id="f-1"></a>
<details>
<summary>📄 <b>.git/hooks/commit-msg.sample</b> — Outros · 896 B · 24 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}
```

</details>

<a id="f-2"></a>
<details>
<summary>📄 <b>.git/hooks/fsmonitor-watchman.sample</b> — Outros · 4.6 KB · 174 linhas · utf-8</summary>

```
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}
```

</details>

<a id="f-3"></a>
<details>
<summary>📄 <b>.git/hooks/post-update.sample</b> — Outros · 189 B · 8 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info
```

</details>

<a id="f-4"></a>
<details>
<summary>📄 <b>.git/hooks/pre-applypatch.sample</b> — Outros · 424 B · 14 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:
```

</details>

<a id="f-5"></a>
<details>
<summary>📄 <b>.git/hooks/pre-commit.sample</b> — Outros · 1.6 KB · 49 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff-index --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --
```

</details>

<a id="f-6"></a>
<details>
<summary>📄 <b>.git/hooks/pre-merge-commit.sample</b> — Outros · 416 B · 13 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:
```

</details>

<a id="f-7"></a>
<details>
<summary>📄 <b>.git/hooks/pre-push.sample</b> — Outros · 1.3 KB · 53 linhas · utf-8</summary>

```
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0
```

</details>

<a id="f-8"></a>
<details>
<summary>📄 <b>.git/hooks/pre-rebase.sample</b> — Outros · 4.8 KB · 169 linhas · utf-8</summary>

```
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END
```

</details>

<a id="f-9"></a>
<details>
<summary>📄 <b>.git/hooks/pre-receive.sample</b> — Outros · 544 B · 24 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi
```

</details>

<a id="f-10"></a>
<details>
<summary>📄 <b>.git/hooks/prepare-commit-msg.sample</b> — Outros · 1.5 KB · 42 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi
```

</details>

<a id="f-11"></a>
<details>
<summary>📄 <b>.git/hooks/push-to-checkout.sample</b> — Outros · 2.7 KB · 78 linhas · utf-8</summary>

```
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi
```

</details>

<a id="f-12"></a>
<details>
<summary>📄 <b>.git/hooks/sendemail-validate.sample</b> — Outros · 2.3 KB · 77 linhas · utf-8</summary>

```
#!/bin/sh

# An example hook script to validate a patch (and/or patch series) before
# sending it via email.
#
# The hook should exit with non-zero status after issuing an appropriate
# message if it wants to prevent the email(s) from being sent.
#
# To enable this hook, rename this file to "sendemail-validate".
#
# By default, it will only check that the patch(es) can be applied on top of
# the default upstream branch without conflicts in a secondary worktree. After
# validation (successful or not) of the last patch of a series, the worktree
# will be deleted.
#
# The following config variables can be set to change the default remote and
# remote ref that are used to apply the patches against:
#
#   sendemail.validateRemote (default: origin)
#   sendemail.validateRemoteRef (default: HEAD)
#
# Replace the TODO placeholders with appropriate checks according to your
# needs.

validate_cover_letter () {
	file="$1"
	# TODO: Replace with appropriate checks (e.g. spell checking).
	true
}

validate_patch () {
	file="$1"
	# Ensure that the patch applies without conflicts.
	git am -3 "$file" || return
	# TODO: Replace with appropriate checks for this patch
	# (e.g. checkpatch.pl).
	true
}

validate_series () {
	# TODO: Replace with appropriate checks for the whole series
	# (e.g. quick build, coding style checks, etc.).
	true
}

# main -------------------------------------------------------------------------

if test "$GIT_SENDEMAIL_FILE_COUNTER" = 1
then
	remote=$(git config --default origin --get sendemail.validateRemote) &&
	ref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&
	worktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&
	git worktree add -fd --checkout "$worktree" "refs/remotes/$remote/$ref" &&
	git config --replace-all sendemail.validateWorktree "$worktree"
else
	worktree=$(git config --get sendemail.validateWorktree)
fi || {
	echo "sendemail-validate: error: failed to prepare worktree" >&2
	exit 1
}

unset GIT_DIR GIT_WORK_TREE
cd "$worktree" &&

if grep -q "^diff --git " "$1"
then
	validate_patch "$1"
else
	validate_cover_letter "$1"
fi &&

if test "$GIT_SENDEMAIL_FILE_COUNTER" = "$GIT_SENDEMAIL_FILE_TOTAL"
then
	git config --unset-all sendemail.validateWorktree &&
	trap 'git worktree remove -ff "$worktree"' EXIT &&
	validate_series
fi
```

</details>

<a id="f-13"></a>
<details>
<summary>📄 <b>.git/hooks/update.sample</b> — Outros · 3.6 KB · 128 linhas · utf-8</summary>

```
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0
```

</details>

<a id="f-14"></a>
<details>
<summary>📄 <b>.git/info/exclude</b> — Outros · 240 B · 6 linhas · utf-8</summary>

```
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```

</details>

<a id="f-15"></a>
<details>
<summary>📄 <b>.git/logs/refs/heads/main</b> — Outros · 165 B · 1 linhas · utf-8</summary>

```
0000000000000000000000000000000000000000 3cb5ab6a4a922cdf86a82cd9f1f74baf436cad4f Pedro <joaopedrotavarres@gmail.com> 1793713948 -0300	commit (initial): Versão 1.0
```

</details>

<a id="f-16"></a>
<details>
<summary>📄 <b>.git/logs/refs/remotes/origin/main</b> — Outros · 150 B · 1 linhas · utf-8</summary>

```
0000000000000000000000000000000000000000 3cb5ab6a4a922cdf86a82cd9f1f74baf436cad4f Pedro <joaopedrotavarres@gmail.com> 1793713959 -0300	update by push
```

</details>

<a id="f-17"></a>
<details>
<summary>📄 <b>.git/logs/HEAD</b> — Outros · 165 B · 1 linhas · utf-8</summary>

```
0000000000000000000000000000000000000000 3cb5ab6a4a922cdf86a82cd9f1f74baf436cad4f Pedro <joaopedrotavarres@gmail.com> 1793713948 -0300	commit (initial): Versão 1.0
```

</details>

<a id="f-30"></a>
<details>
<summary>📄 <b>.git/objects/71/01e22178f7038e1154467a94fc20b8e4d87bdd</b> — Outros · 277 B · 4 linhas · cp1252 (heurística, não confirmada)</summary>

```
x}PÁJÃ@õ¼_ñX/
m="…Rmé¡M¡ÞJ	“d’.nv—Í¦XÄ¯ñà‡ôÇÜ¤'/Îiæ½á½7“k›ãþáñJJ)È©6SÆuá®¶¶ÖœUZÕ‡0q'1þ§Ä6t9´jœ…#OP&píéüsþ¶¨ºÐE¬´X¢˜¢íDôžëtõŠ'È¿œb6]mÒm6K×óå"nìb}Êâ@G–	dL›½óIŽ 5å¬{lÖ“(	ÓÍ²'‚r¶Ç[6’_#±¢ä
y×äo
k*U'(UFˆSl,·àãçxT’ÁùoéKš`Ù8Í›@máÉ±‡gÒ°b¶†¢ûQœ·G.­öÆNÏñ»ý/ÒŠuJ
```

</details>

<a id="f-52"></a>
<details>
<summary>📄 <b>.git/refs/heads/main</b> — Outros · 41 B · 1 linhas · utf-8</summary>

```
3cb5ab6a4a922cdf86a82cd9f1f74baf436cad4f
```

</details>

<a id="f-53"></a>
<details>
<summary>📄 <b>.git/refs/remotes/origin/main</b> — Outros · 41 B · 1 linhas · utf-8</summary>

```
3cb5ab6a4a922cdf86a82cd9f1f74baf436cad4f
```

</details>

<a id="f-54"></a>
<details>
<summary>📄 <b>.git/COMMIT_EDITMSG</b> — Outros · 12 B · 1 linhas · utf-8</summary>

```
Versão 1.0
```

</details>

<a id="f-55"></a>
<details>
<summary>📄 <b>.git/config</b> — Outros · 310 B · 13 linhas · utf-8</summary>

```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/pedro-tavares-dev/flyscanner.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

</details>

<a id="f-56"></a>
<details>
<summary>📄 <b>.git/description</b> — Outros · 73 B · 1 linhas · utf-8</summary>

```
Unnamed repository; edit this file 'description' to name the repository.
```

</details>

<a id="f-57"></a>
<details>
<summary>📄 <b>.git/HEAD</b> — Outros · 21 B · 1 linhas · utf-8</summary>

```
ref: refs/heads/main
```

</details>

<a id="f-70"></a>
<details>
<summary>🐍 <b>apis_input/aviasales.py</b> — Python · 3.1 KB · 76 linhas · utf-8</summary>

```python
"""
apis_input/aviasales.py
-----------------------
Integração com a API da Aviasales (via Travelpayouts).
Suporta múltiplos aeroportos gerando requisições combinadas.
"""
import requests
import log

NOME = "Aviasales"

CAMPOS_CONFIG = [
    {"chave": "token", "label": "Token da API (Travelpayouts)", "tipo": "senha"},
]

def buscar(config: dict, condicoes: dict) -> list:
    token = config.get("token")
    if not token:
        log.registrar_erro("Token da Aviasales não configurado.", origem=NOME)
        return []

    # Separa os aeroportos digitados ou cria lista com string vazia para rodar busca global
    origens_raw = condicoes.get("origem", "").strip()
    destinos_raw = condicoes.get("destino", "").strip()

    # Se estiver vazio, a lista recebe [""] para o loop acontecer. Se tiver, fatia as vírgulas.
    origens = [o.strip()[:3].upper() for o in origens_raw.split(",")] if origens_raw else [""]
    destinos = [d.strip()[:3].upper() for d in destinos_raw.split(",")] if destinos_raw else [""]
    moeda = condicoes.get("moeda", "BRL").upper()
    
    url = "https://api.travelpayouts.com/v1/prices/cheap"
    voos_totais = []

    # Faz uma varredura para cada combinação
    for origem in origens:
        for destino in destinos:
            params = {
                "token": token,
                "currency": moeda.lower()
            }
            # Só envia o parâmetro para a API se ele existir
            if origem: 
                params["origin"] = origem
            if destino: 
                params["destination"] = destino

            try:
                resp = requests.get(url, params=params)
                resp.raise_for_status()
                dados = resp.json()
                
                if dados.get("success"):
                    rotas = dados.get("data", {}).get(destino, {})
                    
                    for id_voo, voo in rotas.items():
                        data_ida_api = voo.get("departure_at", "")[:10]
                        data_link = data_ida_api.replace('-', '')[4:] 
                        link_checkout = f"https://www.aviasales.com/search/{origem}{data_link}{destino}1"
                        
                        voos_totais.append({
                            "origem": origem,
                            "destino": destino,
                            "tipo_viagem": "ida_volta" if voo.get("return_at") else "ida",
                            "data_ida": data_ida_api,
                            "data_volta": voo.get("return_at", "")[:10] if voo.get("return_at") else "",
                            "valor": float(voo.get("price", 0)),
                            "moeda": moeda,
                            "companhia": voo.get("airline", ""),
                            "link": link_checkout,
                            "fonte": NOME
                        })
            except requests.exceptions.RequestException as e:
                # Registra o erro específico daquela rota, mas continua buscando as outras
                log.registrar_aviso(f"Rota {origem}-{destino} falhou na Aviasales: {e}", origem=NOME)

    return voos_totais
```

</details>

<a id="f-71"></a>
<details>
<summary>🐍 <b>apis_input/decolar.py</b> — Python · 477 B · 18 linhas · utf-8</summary>

```python
"""
apis_input/decolar.py
-----------------------
Stub (esqueleto) para uma futura integração com Decolar/Despegar.
Siga o mesmo contrato de google_flight.py.
"""

NOME = "Decolar"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API", "tipo": "senha"},
    {"chave": "afiliado_id", "label": "ID de Afiliado", "tipo": "texto"},
]


def buscar(config: dict, condicoes: dict) -> list:
    # TODO: implementar chamada real à API/scraper da Decolar.
    return []
```

</details>

<a id="f-72"></a>
<details>
<summary>🐍 <b>apis_input/google_flight.py</b> — Python · 368 B · 14 linhas · utf-8</summary>

```python
"""
apis_input/google_flight.py
----------------------------
Stub limpo para integração futura do Google Flights.
"""
NOME = "Google Flights"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API", "tipo": "senha"},
]

def buscar(config: dict, condicoes: dict) -> list:
    # TODO: Implementar scraper real ou chamada via provedor externo.
    return []
```

</details>

<a id="f-73"></a>
<details>
<summary>🐍 <b>apis_input/kiwi_tequila.py</b> — Python · 1.8 KB · 60 linhas · utf-8</summary>

```python
"""
apis_input/kiwi_tequila.py
--------------------------
Integração com a API gratuita do Kiwi.com (Tequila).
Retorna links diretos para compra.
"""
import requests
import log

NOME = "Kiwi Tequila"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API (Tequila)", "tipo": "senha"},
]

def buscar(config: dict, condicoes: dict) -> list:
    api_key = config.get("api_key")
    if not api_key:
        log.registrar_erro("API Key do Kiwi não configurada.", origem=NOME)
        return []

    # Fallback estratégico para testes (ex: rotas de expansão global)
    origem = condicoes.get("origem", "GRU")
    destino = condicoes.get("destino", "JFK")
    data_ida = condicoes.get("data_ida", "10/12/2026") # Formato dd/mm/yyyy esperado pela Kiwi

    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": api_key}
    params = {
        "fly_from": origem,
        "fly_to": destino,
        "date_from": data_ida,
        "date_to": data_ida,
        "curr": "USD", # Padrão global
        "limit": 10
    }

    try:
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        dados = resp.json()

        voos = []
        for voo in dados.get("data", []):
            voos.append({
                "origem": voo.get("flyFrom"),
                "destino": voo.get("flyTo"),
                "tipo_viagem": "ida",
                "data_ida": voo.get("local_departure"),
                "data_volta": None,
                "valor": voo.get("price"),
                "moeda": "USD",
                "companhia": ",".join(voo.get("airlines", [])),
                "link": voo.get("deep_link"), # O bot já entrega o link de checkout
                "fonte": NOME
            })
        return voos
    except Exception as e:
        log.registrar_erro(f"Falha na requisição: {e}", origem=NOME)
        return []
```

</details>

<a id="f-74"></a>
<details>
<summary>🐍 <b>apis_input/serpapi_flights.py</b> — Python · 4.3 KB · 107 linhas · utf-8</summary>

```python
"""
apis_input/serpapi_flights.py
-----------------------------
Integração com SerpApi (Google Flights em tempo real).
Suporta múltiplas origens/destinos e converte datas automaticamente.
"""
import requests
import log

NOME = "Google Flights (SerpApi)"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API (SerpApi)", "tipo": "senha"},
]

def _formatar_data(data_br):
    """Converte DD/MM/AAAA para YYYY-MM-DD exigido pela API."""
    if not data_br: return ""
    partes = data_br.split("/")
    if len(partes) == 3: 
        return f"{partes[2]}-{partes[1]}-{partes[0]}"
    return data_br

def buscar(config: dict, condicoes: dict) -> list:
    # O .strip() de segurança que implementamos antes
    api_key = config.get("api_key", "").strip()
    if not api_key:
        log.registrar_erro("API Key do SerpApi não configurada.", origem=NOME)
        return []

    # Separa os aeroportos ou usa padrões de segurança para evitar loops infinitos
    origens_raw = condicoes.get("origem", "").strip()
    destinos_raw = condicoes.get("destino", "").strip()
    origens = [o.strip()[:3].upper() for o in origens_raw.split(",")] if origens_raw else ["GRU"]
    destinos = [d.strip()[:3].upper() for d in destinos_raw.split(",")] if destinos_raw else ["JFK"]
    
    data_ida = _formatar_data(condicoes.get("data_ida", ""))
    data_volta = _formatar_data(condicoes.get("data_volta", ""))
    tipo_viagem = condicoes.get("tipo_viagem", "ida")

    if not data_ida:
        log.registrar_erro("SerpApi exige que a data de ida seja preenchida nas condições.", origem=NOME)
        return []

    voos_totais = []
    url = "https://serpapi.com/search.json"

    for origem in origens:
        for destino in destinos:
            if not origem or not destino: continue
            
            params = {
                "engine": "google_flights",
                "departure_id": origem,
                "arrival_id": destino,
                "outbound_date": data_ida,
                "currency": condicoes.get("moeda", "BRL")[:3].upper(),
                "hl": "pt-br",
                "api_key": api_key
            }
            
            if tipo_viagem == "ida_volta" and data_volta:
                params["return_date"] = data_volta
                params["type"] = "1" # 1 = Ida e Volta no SerpApi
            else:
                params["type"] = "2" # 2 = Apenas Ida

            try:
                resp = requests.get(url, params=params)
                resp.raise_for_status()
                dados = resp.json()
                
                # Gera a query correta em inglês para a URL do Google Flights (otimizado fora do loop inferior)
                if tipo_viagem == "ida":
                    query_google = f"One way flights to {destino} from {origem} on {data_ida}"
                else:
                    query_google = f"Flights to {destino} from {origem} on {data_ida} return on {data_volta}"
                
                # Substitui os espaços por %20 para a URL não quebrar
                query_formatada = query_google.replace(" ", "%20")

                # A SerpApi divide os voos em "melhores" e "outros"
                lista_voos = dados.get("best_flights", []) + dados.get("other_flights", [])
                
                for voo in lista_voos:
                    preco = voo.get("price", 0)
                    if preco == 0: continue
                    
                    flights_arr = voo.get("flights", [{}])
                    companhia = flights_arr[0].get("airline", "Múltiplas") if flights_arr else "N/A"
                    
                    voos_totais.append({
                        "origem": origem,
                        "destino": destino,
                        "tipo_viagem": tipo_viagem,
                        "data_ida": condicoes.get("data_ida"),
                        "data_volta": condicoes.get("data_volta") if tipo_viagem == "ida_volta" else "",
                        "valor": float(preco),
                        "moeda": params["currency"],
                        "companhia": companhia,
                        "link": f"https://www.google.com/travel/flights?q={query_formatada}",
                        "fonte": NOME
                    })
            except Exception as e:
                log.registrar_aviso(f"Rota {origem}-{destino} falhou no SerpApi: {e}", origem=NOME)

    return voos_totais
```

</details>

<a id="f-75"></a>
<details>
<summary>🐍 <b>apis_input/skyscanner.py</b> — Python · 823 B · 24 linhas · utf-8</summary>

```python
"""
apis_input/skyscanner.py
--------------------------
Stub (esqueleto) para uma futura integração com a API do Skyscanner
(ex: via RapidAPI). Siga o mesmo contrato de google_flight.py.

Enquanto não for implementado de verdade, `buscar()` retorna lista
vazia e avisa no log que ainda não está pronto.
"""

NOME = "Skyscanner"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API (RapidAPI)", "tipo": "senha"},
    {"chave": "host", "label": "API Host", "tipo": "texto"},
]


def buscar(config: dict, condicoes: dict) -> list:
    # TODO: implementar chamada real à API do Skyscanner.
    # Deve retornar lista de dicts no mesmo formato usado em google_flight.py:
    # {"origem", "destino", "tipo_viagem", "data_ida", "data_volta",
    #  "valor", "moeda", "companhia", "link", "fonte"}
    return []
```

</details>

<a id="f-80"></a>
<details>
<summary>🐍 <b>apis_output/markdown_export.py</b> — Python · 2.9 KB · 71 linhas · utf-8</summary>

```python
"""
apis_output/markdown_export.py
------------------------------
Salva as passagens em um arquivo Markdown (.md) local,
com banners visuais das cidades de destino e tipografia limpa.
"""
import os
import datetime

NOME = "Exportar Markdown"

CAMPOS_CONFIG = [
    {"chave": "nome_arquivo", "label": "Nome do Arquivo (ex: ofertas.md)", "tipo": "texto"},
]

# Tradutor de siglas para a API de imagens buscar a foto certa
_CIDADES = {
    "GRU": "sao+paulo,city", "GIG": "rio+de+janeiro,city", "JFK": "new+york,city",
    "MCO": "orlando,city", "LIS": "lisbon,city", "OPO": "porto,city",
    "CDG": "paris,city", "MAD": "madrid,city"
}

def enviar(voo: dict, config: dict, log_callback=None) -> None:
    nome_arquivo = config.get("nome_arquivo", "passagens_encontradas.md").strip()
    if not nome_arquivo: nome_arquivo = "passagens_encontradas.md"
    if not nome_arquivo.endswith(".md"): nome_arquivo += ".md"

    caminho_arquivo = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), nome_arquivo)

    origem = voo.get("origem", "")
    destino = voo.get("destino", "")
    ida = voo.get("data_ida", "")
    volta = voo.get("data_volta", "")
    valor = voo.get("valor", 0)
    moeda = voo.get("moeda", "R$")
    cia = voo.get("companhia", "N/A")
    link = voo.get("link", "")
    score = int(voo.get("score", 0))

    valor_fmt = f"{float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    # Flags visuais e de Inteligência
    chamas = "🔥" * min((score // 10) + 1, 5) if score > 0 else ""
    badge_score = f" `SCORE {score}%` {chamas}" if score > 0 else ""
    tipo_txt = "Ida e Volta" if volta else "Apenas Ida"

    # Geração da Imagem Dinâmica (Banner Largo 800x250)
    # LoremFlickr é grátis e não exige chave. Ele usa a tag (ex: lisbon,city) para achar a foto.
    tag_imagem = _CIDADES.get(destino, f"{destino},landmark")
    url_imagem = f"https://loremflickr.com/800/250/{tag_imagem}/all"

    # Construção do Card Visual em Markdown
    md_text = f"## ✈️ {origem} ➔ {destino} {badge_score}\n\n"
    md_text += f"![Foto de {destino}]({url_imagem})\n\n"
    md_text += f"**{moeda} {valor_fmt}** | {cia} | {tipo_txt}\n\n"
    md_text += f"- **Ida:** {ida}\n"
    if volta:
        md_text += f"- **Volta:** {volta}\n"
    md_text += f"- **Capturado:** {datetime.datetime.now().strftime('%d/%m %H:%M')}\n\n"
    md_text += f"🔗 **[Finalizar Compra no Google Flights]({link})**\n"
    md_text += "---\n<br>\n\n"

    try:
        with open(caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(md_text)
            
        if log_callback:
            log_callback(f"Oferta visual {origem}->{destino} anexada ao log.", nivel="SUCESSO", origem=NOME)
    except Exception as e:
        if log_callback:
            log_callback(f"Erro ao salvar arquivo MD: {e}", nivel="ERRO", origem=NOME)
```

</details>

<a id="f-81"></a>
<details>
<summary>🐍 <b>apis_output/telegram.py</b> — Python · 5.9 KB · 130 linhas · utf-8</summary>

```python
"""
apis_output/telegram.py
-----------------------
Envia notificações de passagens para o Telegram usando templates dinâmicos.
Preparado para o futuro anexo de imagens globais (sendPhoto).
"""
import requests
import random
import log

NOME = "Telegram"

CAMPOS_CONFIG = [
    {"chave": "bot_token", "label": "Bot Token (@BotFather)", "tipo": "senha"},
    {"chave": "chat_id", "label": "Seu Chat ID", "tipo": "texto"},
    {"chave": "estilo", "label": "Estilo da Mensagem (1 a 10 ou 'aleatorio')", "tipo": "texto"},
]

# Banco de dados rápido para mapear aeroportos para Nomes e Bandeiras
_AEROPORTOS = {
    "GRU": {"cidade": "Guarulhos", "bandeira": "🇧🇷"},
    "GIG": {"cidade": "Rio de Janeiro", "bandeira": "🇧🇷"},
    "JFK": {"cidade": "Nova York", "bandeira": "🇺🇸"},
    "MCO": {"cidade": "Orlando", "bandeira": "🇺🇸"},
    "LIS": {"cidade": "Lisboa", "bandeira": "🇵🇹"},
    "OPO": {"cidade": "Porto", "bandeira": "🇵🇹"},
    "CDG": {"cidade": "Paris", "bandeira": "🇫🇷"},
}

def _formatar_moeda(valor):
    """Garante que 6796.0 vire 6.796,00"""
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def _gerar_mensagem(voo: dict, estilo: str) -> str:
    """Gera o texto com base no estilo escolhido ou sorteia um."""
    
    origem_cod = voo.get("origem", "")
    destino_cod = voo.get("destino", "")
    
    dados_origem = _AEROPORTOS.get(origem_cod, {"cidade": origem_cod, "bandeira": ""})
    dados_destino = _AEROPORTOS.get(destino_cod, {"cidade": destino_cod, "bandeira": ""})
    
    cid_orig = dados_origem["cidade"]
    cid_dest = dados_destino["cidade"]
    band_orig = dados_origem["bandeira"]
    band_dest = dados_destino["bandeira"]
    
    ida = voo.get("data_ida", "")
    volta = voo.get("data_volta", "Não definida")
    valor_fmt = _formatar_moeda(voo.get("valor", 0))
    moeda = voo.get("moeda", "R$")
    cia = voo.get("companhia", "N/A")
    link = voo.get("link", "")

    templates = {
        "1": f"✈️ Passagem encontrada!\nSaindo de {cid_orig} ({origem_cod}) para {cid_dest} ({destino_cod}) em {ida}, com retorno de {cid_dest} para {cid_orig} em {volta}.\n💰 Valor: {moeda} {valor_fmt}\n🛫 Companhia: {cia}\n🔗 Confira: {link}",
        
        "2": f"🚨 ALERTA DE PASSAGEM\n{cid_orig} {band_orig} → {cid_dest} {band_dest}\nIda: {ida}\nVolta: {volta}\n✈️ {cia}\n💵 {moeda} {valor_fmt}\n👉 Confira a oferta: {link}",
        
        "3": f"✈️ Achei uma passagem!\n{cid_orig} → {cid_dest}\n📅 Ida: {ida}\n📅 Volta: {volta}\n💰 {moeda} {valor_fmt}\n🛫 {cia}\n\n🔗 Link da passagem:\n{link}",
        
        "4": f"🔥 OPORTUNIDADE DE VOO\nEncontramos uma passagem de {cid_orig} para {cid_dest} por apenas {moeda} {valor_fmt}.\n\n✈️ {cia}\n🗓️ Ida: {ida}\n🗓️ Retorno: {volta}\n\n🔎 Ver passagem: {link}",
        
        "5": f"✈️ {origem_cod} → {destino_cod} | {ida} → {volta}\n{cia} | {moeda} {valor_fmt}\n🔗 {link}",
        
        "6": f"Encontramos uma passagem saindo de {cid_orig} para {cid_dest} no dia {ida}, com retorno no dia {volta}.\nO voo está sendo oferecido pela {cia} por {moeda} {valor_fmt}.\n\nConfira os detalhes: {link}",
        
        "7": f"🎯 Nova passagem encontrada!\n\n📍 {cid_orig} ({origem_cod}) → {cid_dest} ({destino_cod})\n📅 {ida} → {volta}\n✈️ {cia}\n💰 {moeda} {valor_fmt}\n\n🔗 Ver oferta: {link}",
        
        "8": f"{cid_orig} → {cid_dest}\n{ida} — {volta}\n\n{cia}\n{moeda} {valor_fmt}\n\nConsulte os detalhes da tarifa:\n{link}",
        
        "9": f"🔔 Nova passagem encontrada\n{origem_cod} → {destino_cod}\n{ida} a {volta}\n{cia}\n{moeda} {valor_fmt}\n\n🔗 Acessar: {link}",
        
        "10": f"✈️ Oferta de viagem encontrada\n\nOrigem: {cid_orig} ({origem_cod})\nDestino: {cid_dest} ({destino_cod})\nIda: {ida}\nVolta: {volta}\nCompanhia: {cia}\nValor: {moeda} {valor_fmt}\n\n🔗 Consulte a passagem: {link}"
    }

    estilo_str = str(estilo).strip().lower()
    if estilo_str not in templates:
        estilo_str = str(random.randint(1, 10))

    return templates[estilo_str]


def enviar(voo: dict, config: dict, log_callback=None) -> None:
    token = config.get("bot_token", "").strip()
    chat_id = config.get("chat_id", "").strip()
    estilo_escolhido = config.get("estilo", "aleatorio")
    
    if not token or not chat_id:
        if log_callback: log_callback("Telegram: Token ou Chat ID vazios.", nivel="ERRO", origem=NOME)
        return

    texto_final = _gerar_mensagem(voo, estilo_escolhido)

    # FUTURO: Dicionário de imagens globais
    db_imagens = {
        "JFK": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800", # NY
        "LIS": "https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=800", # Lisboa
    }
    
    imagem_url = db_imagens.get(voo.get("destino", ""))
    
    try:
        if imagem_url:
            # Se tiver imagem mapeada, envia como foto (o texto vai na legenda)
            url = f"https://api.telegram.org/bot{token}/sendPhoto"
            payload = {
                "chat_id": chat_id,
                "photo": imagem_url,
                "caption": texto_final,
                "parse_mode": "HTML"
            }
        else:
            # Se não tiver, envia apenas o texto limpo
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": texto_final,
                "parse_mode": "HTML",
                "disable_web_page_preview": True
            }

        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        if log_callback:
            log_callback(f"Notificação premium enviada: {voo.get('origem')}->{voo.get('destino')}", nivel="SUCESSO", origem=NOME)
            
    except Exception as e:
        if log_callback:
            log_callback(f"Falha ao notificar via Telegram: {e}", nivel="ERRO", origem=NOME)
```

</details>

<a id="f-82"></a>
<details>
<summary>🐍 <b>apis_output/terminal.py</b> — Python · 1.3 KB · 40 linhas · utf-8</summary>

```python
"""
apis_output/terminal.py
-------------------------
Primeira api de saída: um "terminal" dentro da própria interface
(uma caixa de texto na aba Retorno / ou na janela principal) que vai
mostrando as passagens encontradas que bateram com as condições.

Como a interface (interface.py) já escuta o log.py pra atualizar a tela,
aqui a gente simplesmente registra o voo encontrado como uma mensagem
de log tipo SUCESSO com origem "terminal". A interface filtra/realça
essas mensagens na área de "Passagens encontradas".
"""

import log

NOME = "Terminal"

CAMPOS_CONFIG = []  # não precisa de nenhuma configuração/chave


def _formatar(voo: dict) -> str:
    origem = voo.get("origem", "?")
    destino = voo.get("destino", "?")
    tipo = voo.get("tipo_viagem", "?")
    ida = voo.get("data_ida", "?")
    volta = voo.get("data_volta", "")
    valor = voo.get("valor", "?")
    moeda = voo.get("moeda", "")
    cia = voo.get("companhia", "?")
    fonte = voo.get("fonte", "?")

    trecho = f"{origem} -> {destino}"
    datas = f"ida {ida}" + (f" / volta {volta}" if volta and tipo == "ida_volta" else "")
    return f"✈ {trecho} | {datas} | {cia} | {moeda} {valor} | via {fonte}"


def enviar(voo: dict, config: dict, log_callback=None) -> None:
    mensagem = _formatar(voo)
    callback = log_callback or log.registrar
    callback(mensagem, "SUCESSO", "terminal")
```

</details>

<a id="f-83"></a>
<details>
<summary>🐍 <b>apis_output/whatsapp.py</b> — Python · 5.3 KB · 155 linhas · utf-8</summary>

````python
"""
apis_output/whatsapp.py
-------------------------
Envia as passagens encontradas via WhatsApp usando a Evolution API
(https://github.com/EvolutionAPI/evolution-api).

Fluxo (igual ao markdown_export.py):
1. Formata os dados do voo em um texto bonito (com emojis e a sintaxe de
   estilo do WhatsApp: *negrito*, _itálico_ etc).
2. Monta o payload esperado pelo endpoint de envio de texto da Evolution API.
3. Faz o POST para a instância configurada.

Endpoint usado: POST {url_base}/message/sendText/{instancia}
Header: apikey: {api_key}
Body:  {"number": "<DDI+numero>", "text": "<mensagem formatada>"}

Documentação de referência: https://doc.evolution-api.com/

OBS: o terreno está pronto (formatação + montagem da chamada HTTP), mas o
envio real está atrás de MODO_SIMULADO = True até validarmos a instância da
Evolution API (URL, nome da instância e apikey).
"""

import json
import urllib.request
import urllib.error

import log

NOME = "WhatsApp (Evolution API)"

CAMPOS_CONFIG = [
    {"chave": "url_base", "label": "URL da Evolution API (ex: http://localhost:8080)", "tipo": "texto"},
    {"chave": "instancia", "label": "Nome da Instância", "tipo": "texto"},
    {"chave": "api_key", "label": "API Key (apikey)", "tipo": "senha"},
    {"chave": "numero", "label": "Número de destino (com DDI, ex: 5511999999999)", "tipo": "texto"},
]

# Tradutor de siglas para nome de cidade "bonito" na mensagem
_CIDADES = {
    "GRU": "São Paulo", "GIG": "Rio de Janeiro", "JFK": "Nova York",
    "MCO": "Orlando", "LIS": "Lisboa", "OPO": "Porto",
    "CDG": "Paris", "MAD": "Madri",
}


def _formatar_mensagem(voo: dict) -> str:
    """Monta o texto da oferta formatado com a sintaxe de estilo do WhatsApp
    (*negrito*, _itálico_, ~tachado~, ``` monoespaçado ```)."""
    origem = voo.get("origem", "")
    destino = voo.get("destino", "")
    ida = voo.get("data_ida", "")
    volta = voo.get("data_volta", "")
    valor = voo.get("valor", 0)
    moeda = voo.get("moeda", "R$")
    cia = voo.get("companhia", "N/A")
    link = voo.get("link", "")
    score = int(voo.get("score", 0))

    valor_fmt = f"{float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    nome_destino = _CIDADES.get(destino, destino)
    nome_origem = _CIDADES.get(origem, origem)

    chamas = "🔥" * min((score // 10) + 1, 5) if score > 0 else ""
    tipo_txt = "Ida e Volta" if volta else "Apenas Ida"

    linhas = []
    linhas.append(f"✈️ *{nome_origem} ({origem}) ➔ {nome_destino} ({destino})*")
    if score > 0:
        linhas.append(f"_Score: {score}%_ {chamas}")
    linhas.append("")
    linhas.append(f"💰 *{moeda} {valor_fmt}*")
    linhas.append(f"🏷️ {cia} | {tipo_txt}")
    linhas.append("")
    linhas.append(f"🛫 Ida: {ida}")
    if volta:
        linhas.append(f"🛬 Volta: {volta}")
    linhas.append("")
    if link:
        linhas.append(f"🔗 {link}")

    return "\n".join(linhas)


def _montar_url(url_base: str, instancia: str) -> str:
    url_base = (url_base or "").strip().rstrip("/")
    instancia = (instancia or "").strip()
    return f"{url_base}/message/sendText/{instancia}"


def _enviar_para_evolution_api(url: str, api_key: str, numero: str, texto: str) -> None:
    """Faz o POST para a Evolution API. Lança exceção em caso de falha."""
    payload = {
        "number": numero,
        "text": texto,
    }

    dados = json.dumps(payload).encode("utf-8")
    requisicao = urllib.request.Request(
        url,
        data=dados,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "apikey": api_key,
        },
    )

    with urllib.request.urlopen(requisicao, timeout=15) as resposta:
        resposta.read()


def enviar(voo: dict, config: dict, log_callback=None) -> None:
    callback = log_callback or log.registrar
    config = config or {}

    url_base = config.get("url_base", "").strip()
    instancia = config.get("instancia", "").strip()
    api_key = config.get("api_key", "").strip()
    numero = config.get("numero", "").strip()

    if not url_base or not instancia or not api_key or not numero:
        callback(
            "WhatsApp (Evolution API) não configurado corretamente "
            "(preencha URL, Instância, API Key e Número).",
            "AVISO", "whatsapp",
        )
        return

    texto = _formatar_mensagem(voo)
    url = _montar_url(url_base, instancia)

    # Terreno pronto para o envio real. Enquanto a instância não for validada,
    # deixamos em modo simulado (apenas loga o que seria enviado).
    MODO_SIMULADO = True

    if MODO_SIMULADO:
        callback(
            f"[SIMULADO] Enviaria via Evolution API ({url}) para {numero}:\n{texto}",
            "INFO", "whatsapp",
        )
        return

    try:
        _enviar_para_evolution_api(url, api_key, numero, texto)
        callback(f"Oferta {voo.get('origem')}->{voo.get('destino')} enviada ao WhatsApp {numero}.",
                  "SUCESSO", "whatsapp")
    except urllib.error.HTTPError as e:
        corpo_erro = e.read().decode("utf-8", errors="ignore")
        callback(f"Erro HTTP ao enviar WhatsApp ({e.code}): {corpo_erro}", "ERRO", "whatsapp")
    except urllib.error.URLError as e:
        callback(f"Erro de conexão com a Evolution API: {e.reason}", "ERRO", "whatsapp")
    except Exception as e:
        callback(f"Erro inesperado ao enviar WhatsApp: {e}", "ERRO", "whatsapp")
````

</details>

<a id="f-84"></a>
<details>
<summary>📄 <b>DOCS/Documentação Técnica e Arquitetural.txt</b> — Texto · 46.9 KB · 2804 linhas · utf-8</summary>

````text
# FlyScanner

## Sistema pessoal de monitoramento e descoberta de passagens aéreas

**Linguagem:** Python
**Interface:** CustomTkinter
**Arquitetura:** modular, orientada a plugins por arquivos
**Execução inicial:** aplicação desktop local
**Saídas iniciais:** Terminal interno da aplicação
**Entradas iniciais:** Google Flights
**Objetivo:** consultar fontes de passagens aéreas, aplicar condições configuradas pelo usuário e encaminhar somente resultados relevantes para os canais de saída habilitados.

---

# 1. Visão geral

O **FlyScanner** é uma aplicação desktop desenvolvida em Python para monitoramento de preços e descoberta de passagens aéreas.

O sistema possui três responsabilidades fundamentais:

1. **Consultar APIs/fontes de entrada de passagens**
2. **Filtrar os resultados de acordo com condições definidas pelo usuário**
3. **Enviar os resultados aprovados para um ou mais canais de saída**

A aplicação deve funcionar continuamente enquanto o robô estiver ativo.

O usuário não precisa alterar o código-fonte para modificar uma busca. As configurações devem ser realizadas pela interface gráfica.

A arquitetura deve permitir adicionar novas fontes de entrada e novos canais de saída simplesmente criando um novo arquivo dentro da pasta correspondente.

---

# 2. Princípio arquitetural

O projeto segue o seguinte fluxo:

```text
┌─────────────────────┐
│     INTERFACE       │
│    interface.py     │
└──────────┬──────────┘
           │
           │ configurações
           ▼
┌─────────────────────┐
│       BUSCADOR      │
│     buscador.py     │
└──────────┬──────────┘
           │
           │ consulta
           ▼
┌─────────────────────┐
│       APIS.PY       │
│   Gerenciador/API   │
└───────┬─────────┬───┘
        │         │
        ▼         ▼
   INPUTS       CONDIÇÕES
 APIs aéreas    condicoes.py
        │         │
        └────┬────┘
             │
             │ resultado aprovado
             ▼
       APIS DE OUTPUT
             │
             ▼
       terminal.py
       telegram.py
       whatsapp.py
       etc.
             
             +
             
           LOG.PY
             │
             ▼
      Janela de Logs
```

O princípio central é:

> **Interface configura. Buscador executa. APIs conectam. Condições filtram. Outputs entregam. Log registra.**

Cada componente deve possuir uma responsabilidade clara.

---

# 3. Estrutura oficial do projeto

A estrutura inicial é:

```text
C:\Scripts\flyscanner
│
│   apis.py
│   buscador.py
│   condicoes.py
│   interface.py
│   log.py
│
├───apis_input
│       google_flight.py
│       skyscanner.py
│       decolar.py
│       etc...
│
└───apis_output
        terminal.py
        telegram.py
        whatsapp.py
```

Essa estrutura deve ser mantida como padrão do projeto.

Novas integrações devem ser adicionadas nas pastas correspondentes, evitando espalhar arquivos pela raiz.

---

# 4. Responsabilidade de cada arquivo

## 4.1 `interface.py`

É a camada gráfica principal.

Responsabilidades:

* iniciar a aplicação;
* criar a janela principal;
* criar as duas janelas/seções principais;
* apresentar configurações;
* detectar APIs disponíveis;
* apresentar formulários específicos das APIs;
* permitir configurar condições;
* permitir configurar outputs;
* iniciar o robô;
* parar o robô;
* mostrar estado atual do robô;
* encaminhar mensagens/logs para `log.py`.

`interface.py` **não deve realizar consultas diretamente às APIs**.

Não deve conter lógica específica de Google Flights, Telegram, Skyscanner etc.

A interface apenas coleta/configura informações e delega a execução aos módulos responsáveis.

---

# 5. Janela 1 — Buscar Passagens

A primeira janela será denominada:

**Buscar Passagens**

Ela possuirá três tópicos principais:

```text
BUSCAR PASSAGENS

1. APIs de Entrada
2. Condições
3. Retorno
```

Além dos tópicos, deverá possuir controles gerais:

```text
[ RODAR ROBÔ ]

[ PARAR ROBÔ ]

Status: PARADO
```

---

# 6. Tópico 1 — APIs de Entrada

Este tópico representa as fontes utilizadas pelo FlyScanner para obter informações de voos.

Exemplo inicial:

```text
Google Flights
```

Futuramente:

```text
Google Flights
Skyscanner
Decolar
Kayak
Amadeus
Duffel
outras fontes
```

A interface **não deve possuir uma lista fixa codificada manualmente**.

Ela deve consultar:

```text
C:\Scripts\flyscanner\apis_input
```

e identificar os arquivos `.py`.

Exemplo:

```text
apis_input/
    google_flight.py
    skyscanner.py
    decolar.py
```

A interface deve interpretar:

```text
google_flight.py
```

como:

```text
Google Flight
```

e disponibilizá-lo como uma opção configurável.

---

# 7. Descoberta automática das APIs

O sistema deve utilizar descoberta dinâmica.

Conceitualmente:

```python
from pathlib import Path

PASTA_INPUT = Path(__file__).parent / "apis_input"

arquivos = PASTA_INPUT.glob("*.py")
```

O sistema deve ignorar:

```text
__init__.py
```

caso esse arquivo venha a existir.

A ideia é:

> Criou um novo arquivo de API → colocou na pasta → o FlyScanner passa a enxergá-lo.

Não deve ser necessário alterar `interface.py` toda vez que uma nova API for adicionada.

---

# 8. Configuração de cada API

Cada API de entrada pode possuir configurações próprias.

Exemplo:

```text
Google Flights

API:
[ Google Flights ]

Chave/API Key:
[____________________________]

Token:
[____________________________]

URL:
[____________________________]

Intervalo de consulta:
[ 30 minutos ]

Outras configurações:
[____________________________]

[ SALVAR CONFIGURAÇÃO ]
```

Outra API poderá possuir campos completamente diferentes.

Por isso, a interface deve permitir que cada módulo declare quais configurações necessita.

Exemplo conceitual:

```python
CONFIG_FIELDS = [
    "api_key",
    "token",
    "endpoint",
    "timeout"
]
```

Uma API diferente poderia declarar:

```python
CONFIG_FIELDS = [
    "api_key",
    "affiliate_id",
    "currency"
]
```

O `interface.py` deverá construir os campos dinamicamente.

---

# 9. Regra importante sobre credenciais

Chaves, tokens e credenciais **não devem ser colocados diretamente dentro dos arquivos Python das APIs**.

Errado:

```python
API_KEY = "123456789"
```

A configuração deve vir da aplicação.

O arquivo:

```text
google_flight.py
```

deve conter a implementação da integração, enquanto as credenciais devem ser fornecidas pelo sistema de configuração.

Isso permite trocar credenciais sem modificar o código.

---

# 10. Tópico 2 — Condições

O segundo tópico contém os filtros da busca.

As condições são **opcionais**.

Isso significa que um campo vazio não deve restringir a pesquisa.

Exemplo:

```text
Origem:
[ Rio de Janeiro ]

Destino:
[ ]

Mês:
[ ]

Ano:
[ ]

Tipo:
[ ]

Preço mínimo:
[ ]

Preço máximo:
[ ]
```

Nesse caso, somente a origem restringe a pesquisa.

---

# 11. Conceito fundamental das condições

As condições funcionam como um filtro lógico.

Exemplo:

```text
Origem = Rio de Janeiro
```

significa:

```text
ACEITAR qualquer resultado cuja origem corresponda
a Rio de Janeiro.
```

Não significa:

```text
procurar somente uma passagem específica.
```

Portanto, quanto menos condições forem preenchidas, mais abrangente será a busca.

---

# 12. Exemplo de filtro amplo

Configuração:

```text
Origem:
Rio de Janeiro

Destino:
vazio

Data:
vazio

Preço:
vazio
```

Resultado:

```text
Rio de Janeiro → São Paulo
Rio de Janeiro → Lisboa
Rio de Janeiro → Nova York
Rio de Janeiro → Buenos Aires
Rio de Janeiro → Santiago
...
```

O robô deve encaminhar os resultados que correspondem à condição.

---

# 13. Exemplo de filtro específico

Configuração:

```text
Origem:
Rio de Janeiro

Destino:
Lisboa

Mês:
Dezembro

Ano:
2026

Tipo:
Ida e volta

Preço máximo:
R$ 3.000
```

O resultado somente será considerado válido se satisfizer todas as condições preenchidas.

Formalmente:

```text
origem == Rio de Janeiro
AND
destino == Lisboa
AND
mês == dezembro
AND
ano == 2026
AND
tipo == ida_e_volta
AND
preço <= 3000
```

Se qualquer condição obrigatória configurada não for satisfeita:

```text
resultado = REJEITADO
```

Se todas forem satisfeitas:

```text
resultado = APROVADO
```

---

# 14. Campos previstos para Condições

A implementação inicial deve permitir:

### Origem

Exemplos:

```text
Rio de Janeiro
São Paulo
GIG
GRU
```

### Destino

Exemplos:

```text
Lisboa
Portugal
LIS
```

### Tipo de viagem

```text
Qualquer
Somente ida
Ida e volta
```

### Data

Possibilidades futuras:

```text
Data específica
Data inicial
Data final
```

### Mês

```text
Janeiro
Fevereiro
...
Dezembro
```

### Ano

```text
2026
2027
2028
...
```

### Preço mínimo

Opcional.

### Preço máximo

Opcional.

### Moeda

Inicialmente:

```text
BRL
```

Futuramente:

```text
BRL
USD
EUR
GBP
...
```

---

# 15. Salvar condições

O botão:

```text
[ SALVAR ]
```

deve validar os campos e armazenar a configuração atual.

A função de armazenamento pertence conceitualmente ao módulo:

```text
condicoes.py
```

Entretanto, o arquivo `condicoes.py` deve ser entendido como **módulo responsável pelo modelo, validação e manipulação das condições**, e não como um arquivo Python que será fisicamente reescrito toda vez que o usuário clicar em "Salvar".

A configuração persistente deverá futuramente ser armazenada em um formato apropriado, como:

```text
JSON
```

ou outro armazenamento local.

Exemplo conceitual:

```json
{
    "origin": "Rio de Janeiro",
    "destination": "Lisboa",
    "trip_type": "round_trip",
    "month": 12,
    "year": 2026,
    "min_price": null,
    "max_price": 3000
}
```

O código continua em:

```text
condicoes.py
```

e os dados ficam separados do código.

Isso evita que a aplicação modifique o próprio código-fonte.

---

# 16. Tópico 3 — Retorno

O terceiro tópico determina para onde os resultados aprovados serão enviados.

Inicialmente:

```text
Terminal
```

Futuramente:

```text
Terminal
Telegram
WhatsApp
Email
Web
Blog
Discord
etc.
```

Assim como ocorre com APIs de entrada, a interface deve descobrir automaticamente os arquivos presentes em:

```text
C:\Scripts\flyscanner\apis_output
```

Exemplo:

```text
apis_output/
    terminal.py
    telegram.py
    whatsapp.py
```

A interface deverá apresentar:

```text
Retornos disponíveis:

☑ Terminal
☐ Telegram
☐ WhatsApp
```

---

# 17. Arquivos de Output

Cada arquivo da pasta `apis_output` representa um canal de saída.

Exemplo:

```text
terminal.py
```

é responsável pelo output no terminal/interface.

No futuro:

```text
telegram.py
```

será responsável por:

* token do bot;
* chat ID;
* conexão;
* envio da mensagem;
* tratamento de erro.

A interface não deve implementar a lógica do Telegram.

Ela apenas configura e ativa o módulo.

---

# 18. Formato normalizado dos resultados

Todas as APIs de entrada podem retornar informações em formatos diferentes.

Por isso, `apis.py` deverá funcionar como camada de normalização.

Por exemplo, uma API pode retornar:

```python
{
    "from": "GIG",
    "to": "LIS",
    "price": 2850
}
```

Outra pode retornar:

```python
{
    "origin": "Rio de Janeiro",
    "destination": "Lisbon",
    "amount": 2850.00
}
```

O restante do sistema não deve precisar conhecer essas diferenças.

O resultado deve ser convertido para um formato interno padronizado.

Exemplo:

```python
flight = {
    "origin": "GIG",
    "destination": "LIS",
    "departure": "...",
    "return": "...",
    "price": 2850.00,
    "currency": "BRL",
    "airline": "...",
    "stops": 0,
    "source": "Google Flights",
    "url": "..."
}
```

Esse objeto passa a ser o contrato entre:

```text
API → Condições → Output
```

---

# 19. `apis.py`

`apis.py` é o **gerenciador das integrações**.

Ele não deve conter a implementação específica de cada API.

Sua responsabilidade é:

1. descobrir APIs disponíveis;
2. carregar os módulos;
3. validar se possuem a estrutura esperada;
4. inicializar configurações;
5. executar consultas;
6. normalizar resultados;
7. encaminhar erros;
8. entregar resultados ao `buscador.py`.

Fluxo:

```text
buscador.py
     ↓
   apis.py
     ↓
google_flight.py
     ↓
resultado bruto
     ↓
apis.py
     ↓
resultado normalizado
     ↓
buscador.py
```

---

# 20. Contrato das APIs de entrada

Toda API adicionada ao diretório:

```text
apis_input
```

deve seguir um contrato mínimo.

Conceitualmente:

```python
class FlightAPI:

    name = "Google Flights"

    def configure(self, config):
        pass

    def search(self, conditions):
        pass

    def test_connection(self):
        pass
```

O nome exato da implementação poderá mudar durante o desenvolvimento, mas o princípio deve ser preservado.

Uma API precisa informar ao sistema:

* nome;
* configurações necessárias;
* capacidade de testar conexão;
* método de consulta;
* resultado;
* erros.

---

# 21. Teste de conexão

Cada API de entrada deve possuir uma operação de teste.

Exemplo:

```text
Google Flights

API Key:
**************

[ TESTAR CONEXÃO ]
```

Possíveis resultados:

```text
✓ API conectada
```

ou:

```text
✗ Falha na autenticação
```

ou:

```text
✗ Timeout
```

ou:

```text
✗ Endpoint indisponível
```

Esses eventos também devem ser enviados para `log.py`.

---

# 22. `buscador.py`

`buscador.py` é o **núcleo operacional do FlyScanner**.

É o robô.

Ele deve:

1. receber as configurações da interface;
2. identificar APIs de entrada habilitadas;
3. obter as condições;
4. obter os outputs habilitados;
5. iniciar o ciclo de consulta;
6. consultar as APIs;
7. receber resultados;
8. enviar resultados para o filtro;
9. verificar resultados aprovados;
10. eliminar duplicações;
11. enviar resultados para os outputs;
12. registrar absolutamente tudo no sistema de logs.

---

# 23. Fluxo operacional completo

Quando o usuário clicar:

```text
[ RODAR ROBÔ ]
```

o fluxo deverá ser:

```text
INTERFACE
   │
   ├── APIs configuradas
   ├── Condições
   └── Outputs
          │
          ▼
     BUSCADOR.PY
          │
          ▼
     APIS.PY
          │
          ▼
    API DE ENTRADA
          │
          ▼
    Dados encontrados
          │
          ▼
     CONDICOES.PY
          │
      ┌───┴────┐
      │        │
   REJEITA   APROVA
      │        │
      │        ▼
      │    DEDUPLICAÇÃO
      │        │
      │        ▼
      │     OUTPUT
      │
      ▼
     LOG
```

---

# 24. Ciclo de consulta

O robô não deve executar uma única consulta e terminar.

Ele deverá trabalhar em ciclo.

Exemplo:

```text
INICIAR
   ↓
Consultar API
   ↓
Receber resultados
   ↓
Filtrar
   ↓
Enviar resultados novos
   ↓
Registrar logs
   ↓
Aguardar intervalo
   ↓
Consultar novamente
   ↓
...
```

O intervalo de consulta deverá ser configurável por API ou globalmente, conforme a implementação futura.

---

# 25. Detecção de mudança de preço

Esse é um dos conceitos centrais do FlyScanner.

O sistema não deve simplesmente mandar repetidamente a mesma passagem a cada consulta.

Exemplo:

Primeira consulta:

```text
GIG → LIS
R$ 3.200
```

Resultado aprovado.

O sistema registra esse estado.

Segunda consulta:

```text
GIG → LIS
R$ 3.200
```

Nenhuma mudança.

Por padrão:

```text
não enviar novamente
```

Terceira consulta:

```text
GIG → LIS
R$ 2.950
```

O preço mudou.

Então:

```text
OUTPUT
↓
Nova passagem/preço detectado
GIG → LIS
R$ 2.950
```

---

# 26. Estado anterior

O buscador deverá manter um estado das passagens observadas.

Exemplo conceitual:

```python
{
    "GIG-LIS-2026-12-10-2026-12-20": {
        "price": 3200,
        "last_seen": "..."
    }
}
```

Na nova consulta:

```text
Preço anterior: 3200
Preço atual: 2950
```

Logo:

```text
MUDANÇA DETECTADA
```

---

# 27. Primeira execução

Deve existir uma regra clara para a primeira consulta.

Quando uma passagem é encontrada pela primeira vez:

```text
não existe estado anterior
```

O sistema pode considerá-la:

```text
NOVA
```

e enviá-la ao output.

Depois:

```text
estado atual = preço observado
```

Isso permite que o usuário receba imediatamente oportunidades encontradas.

---

# 28. Duplicação

O sistema deve diferenciar:

```text
mesmo voo
```

de:

```text
mesmo preço
```

Uma chave de identificação pode considerar:

```text
origem
destino
data de ida
data de volta
companhia
voo
```

Dependendo da quantidade de informações fornecidas pela API.

Exemplo:

```text
GIG
LIS
2026-12-10
2026-12-20
LATAM
```

forma uma identidade de viagem.

A URL, preço ou horário podem mudar sem necessariamente representar uma nova viagem.

---

# 29. `condicoes.py`

Responsabilidades:

* representar condições;
* validar condições;
* salvar condições;
* carregar condições;
* aplicar filtros;
* determinar se um voo satisfaz os critérios.

Exemplo conceitual:

```python
def matches(flight, conditions):
    ...
```

Resultado:

```python
True
```

ou:

```python
False
```

---

# 30. Regra de filtros vazios

Campo vazio:

```text
não filtra.
```

Exemplo:

```text
Origem = GIG
Destino = vazio
Preço máximo = vazio
```

Somente:

```text
origem == GIG
```

é considerado.

Isso é obrigatório para preservar a característica de busca ampla.

---

# 31. `log.py`

`log.py` é responsável pelo sistema de logs.

A segunda janela da aplicação será dedicada exclusivamente a isso.

O princípio do log é:

> **Tudo que acontece dentro do robô deve ser observável.**

Não deve haver ações importantes ocorrendo silenciosamente.

---

# 32. Janela 2 — Log

A janela será denominada:

**Log**

Exemplo visual:

```text
┌───────────────────────────────────────────────┐
│ FLYSCANNER — LOG                              │
├───────────────────────────────────────────────┤
│ [11:20:01] Sistema iniciado                  │
│ [11:20:03] Google Flights carregado           │
│ [11:20:04] Configuração validada             │
│ [11:20:05] API conectada                      │
│ [11:20:06] Consulta iniciada                  │
│ [11:20:08] 34 resultados recebidos            │
│ [11:20:08] 29 resultados rejeitados           │
│ [11:20:08] 5 resultados aprovados             │
│ [11:20:08] Novo voo detectado                 │
│ [11:20:08] GIG → LIS — R$ 2.890              │
│ [11:20:09] Resultado enviado para Terminal    │
│ [11:20:09] Consulta finalizada                │
│ [11:20:10] Próxima consulta em 30 minutos     │
└───────────────────────────────────────────────┘
```

---

# 33. Eventos que devem gerar log

Praticamente todos os eventos relevantes.

### Sistema

```text
Aplicação iniciada
Aplicação encerrada
Robô iniciado
Robô parado
Configuração carregada
Configuração salva
```

### APIs

```text
API carregada
API não encontrada
API indisponível
API conectada
Falha de autenticação
Token inválido
API Key inválida
Timeout
Erro HTTP
Erro de parsing
Resposta inválida
```

### Consultas

```text
Consulta iniciada
Consulta finalizada
Tempo da consulta
Quantidade de resultados
Consulta vazia
Consulta atrasada
Consulta interrompida
```

### Condições

```text
Condições carregadas
Resultado aprovado
Resultado rejeitado
Motivo da rejeição
```

### Passagens

```text
Nova passagem
Mudança de preço
Preço aumentado
Preço reduzido
Passagem duplicada
Passagem enviada
```

### Outputs

```text
Output iniciado
Output indisponível
Falha no envio
Envio concluído
Telegram conectado
Terminal conectado
```

---

# 34. Níveis de log

O sistema deve trabalhar com níveis.

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Exemplo:

```text
[INFO] Consulta iniciada
[DEBUG] URL consultada: ...
[INFO] 52 resultados encontrados
[WARNING] API demorou 15 segundos
[ERROR] Falha de autenticação
[CRITICAL] Nenhuma API de entrada disponível
```

Na interface, o usuário poderá futuramente filtrar os níveis.

---

# 35. Interface gráfica

A interface será construída utilizando:

```python
CustomTkinter
```

A aplicação deve ter aparência moderna, limpa e funcional.

A interface não deve concentrar lógica de negócio.

Arquitetura:

```text
interface.py
     │
     ├── coleta configurações
     │
     ├── mostra informações
     │
     └── controla execução
              │
              ▼
          buscador.py
```

---

# 36. Organização visual

A primeira janela deve possuir uma estrutura aproximadamente:

```text
┌──────────────────────────────────────────────────────┐
│                    FLYSCANNER                        │
├──────────────────────────────────────────────────────┤
│                                                      │
│  1. APIs DE ENTRADA                                  │
│                                                      │
│  API: [ Google Flights ▼ ]                           │
│                                                      │
│  [Configurações da API]                              │
│                                                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  2. CONDIÇÕES                                        │
│                                                      │
│  Origem:       [________________]                    │
│  Destino:      [________________]                    │
│  Tipo:         [Ida e volta ▼]                       │
│  Mês:          [Dezembro ▼]                          │
│  Ano:          [2026 ▼]                              │
│  Preço mínimo: [________]                            │
│  Preço máximo: [________]                            │
│                                                      │
│                         [ SALVAR CONDIÇÕES ]          │
│                                                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  3. RETORNO                                          │
│                                                      │
│  ☑ Terminal                                          │
│  ☐ Telegram                                          │
│  ☐ WhatsApp                                         │
│                                                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│       [ ▶ RODAR ROBÔ ]     [ ■ PARAR ROBÔ ]          │
│                                                      │
│       Status: PARADO                                 │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

# 37. Estado do robô

A interface deve sempre informar o estado atual.

Estados mínimos:

```text
PARADO
INICIANDO
CONECTANDO
CONSULTANDO
AGUARDANDO
ERRO
FINALIZANDO
```

Exemplo:

```text
Status: CONSULTANDO GOOGLE FLIGHTS
```

Depois:

```text
Status: AGUARDANDO PRÓXIMA CONSULTA
```

---

# 38. Execução em segundo plano

O botão:

```text
RODAR ROBÔ
```

não pode congelar a interface.

O buscador deverá executar em uma thread/processo apropriado.

Conceitualmente:

```text
THREAD DA INTERFACE
        │
        ├── mantém janela responsiva
        │
        ▼
THREAD DO BUSCADOR
        │
        ├── consulta API
        ├── filtra
        ├── envia
        └── registra logs
```

A interface nunca deve ficar travada enquanto uma API estiver esperando resposta.

---

# 39. Comunicação entre threads

O buscador não deve manipular diretamente widgets do CustomTkinter.

Errado:

```python
label.configure(text="Consulta concluída")
```

dentro da thread do buscador.

O buscador deve emitir um evento/log:

```python
logger.info("Consulta concluída")
```

e a interface receber essa informação de forma segura.

---

# 40. Comunicação entre módulos

A arquitetura deve ser baseada em fluxo de dados.

```text
INTERFACE
    ↓
CONFIGURAÇÃO
    ↓
BUSCADOR
    ↓
APIS
    ↓
RESULTADO NORMALIZADO
    ↓
CONDIÇÕES
    ↓
RESULTADOS APROVADOS
    ↓
OUTPUTS
    ↓
LOG
```

Nenhum módulo deve depender diretamente da implementação interna de outro.

---

# 41. Regras para adicionar uma nova API de entrada

Para adicionar:

```text
Skyscanner
```

deve-se criar:

```text
C:\Scripts\flyscanner\apis_input\skyscanner.py
```

O arquivo deverá implementar o contrato de API definido pelo projeto.

Depois:

```text
Executar FlyScanner
```

O sistema deverá detectar:

```text
skyscanner.py
```

e apresentar:

```text
Skyscanner
```

na seção:

```text
APIs DE ENTRADA
```

Não deverá ser necessário editar:

```text
interface.py
```

para adicionar a opção manualmente.

---

# 42. Regras para adicionar novo Output

Para adicionar Telegram:

```text
C:\Scripts\flyscanner\apis_output\telegram.py
```

O sistema detecta o arquivo.

A interface apresenta:

```text
☐ Telegram
```

Ao selecionar Telegram, a interface deve carregar os campos exigidos pelo módulo.

Exemplo:

```text
Bot Token:
[________________________]

Chat ID:
[________________________]

[ TESTAR TELEGRAM ]
```

---

# 43. Não criar código específico no `interface.py`

Evitar:

```python
if api == "telegram":
    ...
elif api == "whatsapp":
    ...
elif api == "discord":
    ...
```

Esse modelo destruiria a modularidade do projeto.

O correto é:

```text
interface
    ↓
descobre módulos
    ↓
módulo declara configuração
    ↓
interface monta formulário
```

O mesmo princípio vale para APIs de entrada.

---

# 44. `apis.py` como camada intermediária

O `apis.py` existe justamente para evitar que:

```text
buscador.py
```

precise conhecer:

```text
google_flight.py
skyscanner.py
decolar.py
...
```

e também para evitar que:

```text
interface.py
```

precise conhecer a implementação dessas APIs.

O relacionamento deverá ser:

```text
interface
     ↓
apis.py
     ↓
api específica
```

---

# 45. Tratamento de erros

Nenhum erro de API deve derrubar o robô inteiro sem necessidade.

Exemplo:

```text
Google Flights
      ↓
Timeout
```

O sistema deve:

```text
registrar erro
↓
informar log
↓
aguardar
↓
tentar novamente
```

Não:

```text
crash
↓
fechar FlyScanner
```

Erros fatais devem ser tratados separadamente.

---

# 46. Falha de uma API

Se futuramente houver:

```text
Google Flights
Skyscanner
Decolar
```

e o Skyscanner falhar:

```text
Google Flights → funcionando
Skyscanner → ERROR
Decolar → funcionando
```

O sistema não deverá necessariamente interromper as demais fontes.

O erro deverá aparecer no log:

```text
[ERROR] Skyscanner indisponível
```

enquanto as outras continuam funcionando.

---

# 47. Múltiplas APIs de entrada

Futuramente o usuário poderá ativar:

```text
☑ Google Flights
☑ Skyscanner
☑ Decolar
```

O buscador deverá consultar todas as fontes habilitadas.

Os resultados devem passar pelo mesmo pipeline:

```text
Google Flights ─┐
Skyscanner ─────┼──→ NORMALIZAÇÃO → CONDIÇÕES
Decolar ────────┘
```

Isso permite comparar resultados provenientes de fontes diferentes.

---

# 48. Múltiplos Outputs

Da mesma forma:

```text
☑ Terminal
☑ Telegram
☑ Email
```

Um resultado aprovado poderá ser enviado para todos os outputs ativos.

Fluxo:

```text
Resultado aprovado
       │
       ├──→ Terminal
       ├──→ Telegram
       └──→ Email
```

Um erro em um output não deve necessariamente impedir os demais.

---

# 49. Regra de independência

Cada módulo deve falhar isoladamente sempre que possível.

Exemplo:

```text
Telegram ERROR
```

não deve causar:

```text
Terminal ERROR
```

nem:

```text
Buscador ERROR
```

A exceção deve ser registrada.

---

# 50. Segurança

Credenciais nunca devem aparecer integralmente no log.

Errado:

```text
[INFO] Token: 123456789ABC
```

Correto:

```text
[INFO] Token configurado: ********ABC
```

Da mesma forma, API Keys devem ser mascaradas.

---

# 51. Configurações

A aplicação deverá separar:

### Código

```text
.py
```

### Configuração

```text
dados/configuração local
```

### Estado

```text
preços observados
últimas consultas
etc.
```

### Logs

```text
eventos da aplicação
```

Mesmo que a primeira versão seja extremamente simples, essa separação deve ser mantida conceitualmente.

---

# 52. Persistência

A primeira versão pode utilizar arquivos locais simples.

Exemplo:

```text
config.json
```

ou estrutura equivalente.

O objetivo é permitir:

```text
abrir FlyScanner
↓
configurações continuam disponíveis
```

sem exigir que o usuário configure tudo novamente.

---

# 53. Configuração x estado

São conceitos diferentes.

### Configuração

O usuário definiu:

```text
Origem = GIG
Destino = LIS
Preço máximo = 3000
```

### Estado

O robô descobriu:

```text
Último preço observado = R$ 2.950
Última consulta = 11:20
```

Não misturar esses dois conceitos.

---

# 54. Fluxo ao iniciar aplicação

Ao abrir:

```text
interface.py
```

o sistema deverá:

```text
1. Iniciar aplicação
2. Inicializar logger
3. Procurar APIs de entrada
4. Procurar APIs de saída
5. Carregar configurações
6. Carregar condições
7. Montar interface
8. Mostrar status PARADO
```

---

# 55. Fluxo ao clicar em "Rodar Robô"

```text
Usuário
  ↓
RODAR ROBÔ
  ↓
validar configuração
  ↓
existem APIs?
  ↓
SIM
  ↓
existe output?
  ↓
SIM
  ↓
carregar condições
  ↓
iniciar buscador
  ↓
testar APIs
  ↓
iniciar consultas
```

Caso falhe:

```text
configuração inválida
        ↓
não iniciar robô
        ↓
mostrar erro
        ↓
registrar log
```

---

# 56. Fluxo de uma consulta

```text
[INÍCIO DA CONSULTA]

        ↓

Selecionar API

        ↓

Executar consulta

        ↓

Receber resposta

        ↓

Validar resposta

        ↓

Normalizar dados

        ↓

Aplicar condições

        ↓

Resultado corresponde?

     ┌──────┴──────┐
     │             │
    NÃO           SIM
     │             │
     ▼             ▼
    LOG       verificar estado
                   │
                   ▼
             é resultado novo?
                   │
             ┌─────┴─────┐
             │           │
            NÃO         SIM
             │           │
             ▼           ▼
            LOG      enviar output
                         │
                         ▼
                        LOG

        ↓

finalizar consulta

        ↓

aguardar próximo ciclo
```

---

# 57. Mudança de preço

Quando uma passagem já conhecida sofrer alteração:

```text
Preço anterior: R$ 3.200
Preço atual:    R$ 2.850
```

o sistema deverá registrar:

```text
[INFO] Mudança de preço detectada
[INFO] GIG → LIS
[INFO] Anterior: R$ 3.200
[INFO] Atual: R$ 2.850
[INFO] Variação: -R$ 350
```

e enviar o resultado ao output.

---

# 58. Aumento de preço

Também deve ser possível registrar:

```text
R$ 2.850 → R$ 3.100
```

Mesmo que o preço tenha piorado, trata-se de uma mudança.

A decisão sobre **quais mudanças devem gerar alerta** deverá ficar configurável no futuro.

Exemplo futuro:

```text
☑ Avisar somente redução de preço
☐ Avisar qualquer alteração
```

---

# 59. Evolução futura dos filtros

A arquitetura deve permitir futuramente:

```text
Número máximo de escalas
Companhia aérea
Aeroporto
Bagagem
Horário mínimo
Horário máximo
Duração máxima
Duração mínima
Classe
Aeroporto de conexão
Quantidade de passageiros
Dias de permanência
Flexibilidade de datas
```

Esses campos não devem ser implementados prematuramente.

A primeira versão deve permanecer simples.

---

# 60. Evolução futura dos Outputs

A arquitetura permite adicionar:

```text
terminal.py
telegram.py
whatsapp.py
email.py
discord.py
web.py
blog.py
```

Cada módulo deverá possuir sua própria implementação.

O restante do sistema não deve precisar conhecer detalhes do serviço.

---

# 61. Terminal como primeiro Output

Na versão inicial, o terminal/output será implementado dentro da própria interface.

Exemplo:

```text
┌─────────────────────────────────────────────┐
│ RESULTADOS                                  │
├─────────────────────────────────────────────┤
│                                             │
│ [11:32] NOVO VOO                            │
│                                             │
│ Rio de Janeiro (GIG)                        │
│ → Lisboa (LIS)                              │
│                                             │
│ Ida: 10/12/2026                             │
│ Volta: 20/12/2026                           │
│ Preço: R$ 2.890                             │
│ Fonte: Google Flights                       │
│                                             │
└─────────────────────────────────────────────┘
```

Esse output deve ser tratado como um módulo.

Futuramente poderá ser substituído/complementado por Telegram etc.

---

# 62. Diferença entre Log e Output

São conceitos diferentes.

### Output

É destinado ao usuário final.

Exemplo:

```text
GIG → LIS
R$ 2.890
```

### Log

É destinado ao diagnóstico e acompanhamento do sistema.

Exemplo:

```text
[11:32:04] API respondeu em 2.31s
[11:32:04] 47 resultados recebidos
[11:32:04] 41 resultados rejeitados
[11:32:04] 6 resultados aprovados
[11:32:04] 1 mudança de preço detectada
```

Uma passagem pode aparecer nos dois, mas com finalidades diferentes.

---

# 63. Regras de manutenção

Ao modificar o projeto:

### Se alterar interface

Modificar:

```text
interface.py
```

Não colocar lógica de consulta ali.

### Se alterar filtro

Modificar:

```text
condicoes.py
```

### Se alterar mecanismo de consulta

Modificar:

```text
buscador.py
```

ou a API específica.

### Se adicionar uma nova API

Criar:

```text
apis_input/nova_api.py
```

### Se adicionar um novo output

Criar:

```text
apis_output/novo_output.py
```

### Se alterar sistema de logs

Modificar:

```text
log.py
```

### Se alterar descoberta/conexão entre APIs

Modificar:

```text
apis.py
```

---

# 64. Regra fundamental de arquitetura

Não resolver um problema de um módulo dentro de outro módulo.

Exemplo:

Se Telegram possui um problema:

```text
NÃO corrigir colocando código Telegram em buscador.py.
```

Corrigir:

```text
apis_output/telegram.py
```

Se o problema é filtragem:

```text
condicoes.py
```

Se o problema é descoberta dos módulos:

```text
apis.py
```

Essa disciplina é essencial para manter o projeto pequeno mesmo quando crescer.

---

# 65. Consulta das pastas

A aplicação deverá tratar as pastas como sistemas de plugins.

## Entrada

```text
C:\Scripts\flyscanner\apis_input
```

## Saída

```text
C:\Scripts\flyscanner\apis_output
```

Ao inicializar:

```text
Scan apis_input
        ↓
Encontrar *.py
        ↓
Carregar módulos válidos
```

e:

```text
Scan apis_output
        ↓
Encontrar *.py
        ↓
Carregar módulos válidos
```

O sistema deverá registrar no log:

```text
[INFO] Procurando APIs de entrada...
[INFO] 3 APIs encontradas
[INFO] Google Flights carregado
[INFO] Skyscanner carregado
[INFO] Decolar carregado
```

---

# 66. API inválida

Se existir:

```text
apis_input/teste.py
```

mas o arquivo não implementar o contrato esperado:

```text
[WARNING] Módulo teste.py ignorado: contrato inválido
```

O programa não deve necessariamente fechar.

Isso permite que arquivos experimentais existam sem quebrar a aplicação inteira.

---

# 67. Convenção de nomes

Arquivos:

```text
snake_case.py
```

Exemplos:

```text
google_flight.py
skyscanner.py
decolar.py
telegram.py
whatsapp.py
```

Evitar:

```text
GoogleFlight.py
Google Flights.py
google-flight.py
```

---

# 68. Princípio de baixo acoplamento

O projeto deve manter baixo acoplamento.

Exemplo:

```text
Google Flights
```

não deve saber que existe:

```text
Telegram
```

Telegram não deve saber que existe:

```text
Skyscanner
```

E Skyscanner não deve saber como:

```text
condicoes.py
```

funciona internamente.

Todos se comunicam através dos contratos definidos pelo sistema.

---

# 69. Princípio de alta coesão

Cada módulo deve fazer uma coisa.

```text
interface.py
→ interface

buscador.py
→ execução do robô

apis.py
→ gerenciamento das integrações

condicoes.py
→ filtragem

log.py
→ observabilidade

apis_input/*
→ consulta de fontes

apis_output/*
→ entrega de resultados
```

---

# 70. Primeira versão — MVP

A primeira versão não deve tentar implementar tudo.

### Implementar:

```text
✓ CustomTkinter
✓ Janela Buscar Passagens
✓ Janela Log
✓ Descoberta automática de APIs
✓ Google Flights
✓ Configuração da API
✓ Condições
✓ Salvar condições
✓ Output Terminal
✓ Botão Rodar
✓ Botão Parar
✓ Thread do buscador
✓ Sistema de logs
✓ Tratamento básico de erros
✓ Consulta recorrente
✓ Detecção básica de novos resultados
✓ Detecção básica de alteração de preço
```

### Não implementar ainda:

```text
✗ Telegram
✗ WhatsApp
✗ Email
✗ Web
✗ Banco de dados complexo
✗ Sistema de usuários
✗ Login
✗ Cloud
✗ Dashboard web
✗ Machine Learning
✗ IA desnecessária
```

O objetivo inicial é provar o pipeline.

---

# 71. Pipeline mínimo funcional

O MVP deverá conseguir fazer:

```text
Usuário abre FlyScanner
        ↓
Configura Google Flights
        ↓
Configura:
GIG → LIS
Dezembro/2026
Ida e volta
Até R$ 3.000
        ↓
Seleciona Terminal
        ↓
RODAR ROBÔ
        ↓
Buscador consulta API
        ↓
Recebe resultados
        ↓
Normaliza
        ↓
Condicoes.py filtra
        ↓
Encontra:
GIG → LIS
R$ 2.890
        ↓
Terminal recebe
        ↓
Log registra tudo
        ↓
Aguarda
        ↓
Consulta novamente
```

Esse é o **caminho crítico do projeto**.

---

# 72. Arquitetura conceitual definitiva

O FlyScanner deve evoluir mantendo esta estrutura:

```text
                         ┌──────────────┐
                         │   INTERFACE  │
                         │ interface.py │
                         └──────┬───────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
                ▼               ▼               ▼
             INPUTS         CONDIÇÕES        OUTPUTS
                │               │               │
                ▼               ▼               ▼
             apis.py       condicoes.py    apis.py
                │                               │
        ┌───────┼────────┐              ┌───────┼───────┐
        ▼       ▼        ▼              ▼       ▼       ▼
     Google  Sky...   Decolar       Terminal Telegram WhatsApp
        │       │        │              │       │       │
        └───────┴────────┘              └───────┴───────┘
                │                               │
                └──────────────┬────────────────┘
                               │
                               ▼
                         buscador.py
                               │
                               ▼
                            log.py
                               │
                               ▼
                         JANELA DE LOG
```

---

# 73. Regra de ouro para futuras implementações

Antes de adicionar qualquer funcionalidade, responder:

### 1. Isso é interface?

→ `interface.py`

### 2. Isso é execução do robô?

→ `buscador.py`

### 3. Isso é gerenciamento de integração?

→ `apis.py`

### 4. Isso é filtro/condição?

→ `condicoes.py`

### 5. Isso é log?

→ `log.py`

### 6. É uma nova fonte de passagens?

→ `apis_input/nova_api.py`

### 7. É um novo canal de saída?

→ `apis_output/novo_output.py`

Se uma funcionalidade não se encaixa claramente em nenhum desses pontos, **não criar código aleatoriamente**. Primeiro definir a responsabilidade arquitetural.

---

# 74. Filosofia do projeto

O FlyScanner não deve ser projetado como um sistema gigantesco.

A filosofia é:

```text
SIMPLES
+
MODULAR
+
OBSERVÁVEL
+
EXTENSÍVEL
```

O projeto é pessoal e será mantido pelo próprio desenvolvedor.

Portanto, não há necessidade inicial de:

```text
microserviços
Docker
Kubernetes
Redis
RabbitMQ
PostgreSQL
AWS
arquitetura distribuída
```

A menos que uma necessidade concreta apareça posteriormente.

A complexidade deve ser introduzida **somente quando resolver um problema real**.

---

# 75. Regra para evolução

A evolução esperada é:

```text
VERSÃO 1
Google Flights
+
Condições
+
Terminal
+
Logs
```

↓

```text
VERSÃO 2
+ Skyscanner
+ Decolar
+ comparação entre fontes
```

↓

```text
VERSÃO 3
+ Telegram
+ Email
```

↓

```text
VERSÃO 4
+ Web
+ Dashboard
```

↓

```text
VERSÃO 5
+ histórico de preços
+ estatísticas
+ gráficos
```

↓

```text
VERSÃO FUTURA
+ inteligência sobre preços
+ identificação de oportunidades
+ automações avançadas
```

A estrutura original deve continuar sendo preservada mesmo com a evolução.

---

# 76. Definição resumida dos componentes

| Componente         | Responsabilidade                                |
| ------------------ | ----------------------------------------------- |
| `interface.py`     | Interface gráfica e interação com usuário       |
| `buscador.py`      | Motor/robô de execução                          |
| `apis.py`          | Gerenciamento e conexão das integrações         |
| `condicoes.py`     | Modelo, persistência e aplicação dos filtros    |
| `log.py`           | Sistema de logs e comunicação com janela de log |
| `apis_input/*.py`  | Fontes de dados de passagens                    |
| `apis_output/*.py` | Canais de entrega dos resultados                |

---

# 77. Regra final

O FlyScanner deve sempre preservar este fluxo:

```text
CONFIGURAR
    ↓
CONSULTAR
    ↓
NORMALIZAR
    ↓
FILTRAR
    ↓
COMPARAR
    ↓
DECIDIR SE É NOVO/ALTERADO
    ↓
ENVIAR
    ↓
REGISTRAR
    ↓
REPETIR
```

A interface é apenas a camada de controle.

O `buscador.py` é o cérebro operacional.

As APIs de entrada são os sensores.

`condicoes.py` é o filtro.

As APIs de saída são os canais de comunicação.

`log.py` é a observabilidade do sistema.

`apis.py` é a camada que mantém as integrações desacopladas do restante da aplicação.

Essa separação deve ser preservada em todas as versões futuras do FlyScanner.
````

</details>

<a id="f-85"></a>
<details>
<summary>📝 <b>DOCS/PROMPT.md</b> — Markdown · 4.9 KB · 110 linhas · utf-8</summary>

```markdown
Faça uma interface com Custom Tkinter (PYTHON), que a gente ira configurar inputs de apis (de vendas de passagens aéreas).

Vamos começar pelo Google flights. E um output para saÍdas, na versão teste por exemplo, vamos usar um terminal na propria interface que ele vai mostrando la as passagens que retornar. Mas com o decorrer de novas versões, vamos ir introduzindo outras apis de saída, como telegram, web, blog, etc...

Basicamente o cerne do projeto é esse, a intenção é criar a minha ferramenta de busca de passagens baratas pois gosto de viajar, e como sou desenvolvedor quero criar a minha versão.



A estrutura inicial ficará assim:



C:\\Scripts\\flyscanner

│   apis.py

│   buscador.py

│   condicoes.py

│   interface.py

│   log.py

│

├───apis\_input

│       decolar.py

│       etc...txt

│       google\_flight.py

│       skyscanner.py

│

└───apis\_output

        telegram.py

        terminal.py

        whatsapp.py



Simples e prático né ? Não vou colocar no mercado, eu que vou dar manutenção então a organização será ESSA.



Interface terá por enquanto duas (2) JANELAS. Janela Buscar Passagens terá três tópicos. Adicionar inputs, onde colocaremos: chave da api, configurações relacionadas a apis, tokens (e tudo necessário pra api conseguir fazer consultas)... os egundo topico vai ser as Condições, onde colocaremos filtros que a api vai se basear pra buscar e retornar as passagens ex: pra um pais especifico, se é ida ou/+ volta, período, saida de onde, mes, ano, valor minimo, valor maximo e salvar.

Tudo opcional, literalmente filtros, quanto mais filtros mais especifica é a passagem que ele vai buscar e retornar para o output.

Exemplo: se eu buscar só SAÍDA de Rio de Janeiro, ele vai ir me retornando TODAS com essa condição. quando ele detectar da api de input que tem uma mudança de preço em alguma passagem com ESSA caracteristica, ele vai retornar para o output. 

Agora se eu colocar, Rio de Janeiro pra Lisboa, em dezembro, ida e volta, por menos de R$3.000,00, ele só vai me retornar algo pro output quando bater todas essas especificidades, caso contrario não vai retornar nada. 

E o Terceiro Tópico será Retorno, onde colocaremos qual input de saída será usada, terminal, telegram(futuramente), email(futuramente) etc...



Botões de rodar robô, onde ele lerá tudo preenchido na interface e ficará em segundo plano consultando essas apis de entrada, olhando pras condições cadastradas e jogando nas apis de saída.



A janela 2 por enquanto será a de log, onde tudo q o robo fizer, cada erro de api, cada chave errada, cada consulta errada, cada passagem encontrada QUALQUER COISA, ele vai jogar ali, qualquer coisa mesmo, se a consulta atrasar, tempo de consulta, tempo que a api ta, se a api ta ativa, se um desenvolvedor bater o dedinho ele vai avisar e vai jogar ali, a janela de log é só pra isso.



E só.



A estrutura que te mandei ja é auto expllicativa mas vamos lá..:



* O script *interface.py* vai ser a ui, onde vamos clicar e abrir a ui.



* O script *log.py* vai ser onde vamos colocar todas as especificações da janela que vai ter de log dentro do interface, e também os retornos etc.



* O script *condicoes.py* vai ser usado pra gravar as condições que o tópico 2 da interface vai gravar, então a interface vai gravar nesse script e toda consulta que as apis fizerem elas vão usar condicoes.py pra ser o filtro, se corresponde com oque foi colocado no tópico de condições..



* O script apis.py, vai ser o conector do interface com as apis tanto de saida quanto de entrada que ficarão em pastas, eles não ficarão ao lado do interface.py : "C:\\Scripts\\flyscanner\\apis.py"

&#x09;"C:\\Scripts\\flyscanner\\interface.py"

&#x09;"C:\\Scripts\\flyscanner\\apis\_input"

&#x09;"C:\\Scripts\\flyscanner\\apis\_output"

&#x09;E ele vai conectar os scripts de apis de entrada com o interface, e os scripts de apis de saída tambem com o interface, ou seja, quando quisermos e quando o 	projeto for evoluindo eu vou criar um script especifico para o determinado serviço ex: skyscanner.py e vou jogar lá na pasta apis\_input. e ai ele vai ficar 	disponivel lá no topico 1 pra configurar na interface, o mesmo vale pra apis de saída, se eu quiser implementar uma saída que vai me mandar mensagem no 	telegram com os voos, eu vou criar o telegram.py e jogar la no apis\_output, e ele vai ficar la disponivel pra clicar e configurar no topico 3 do interface.



* o *buscador.py vai ser o robô que vai ficar pegar tudo q ta no interface cadastrado, apis de entrada, condições e apis de saída, e ficar consultando as apis de entrada, mandando pro script de condições.py, jogando pra api de saída e mandando tudo q ta fazendo pro log jogar na tela.*





```

</details>

<a id="f-86"></a>
<details>
<summary>📝 <b>DOCS/README.md</b> — Markdown · 2.3 KB · 74 linhas · utf-8</summary>

````markdown
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
````

</details>

<a id="f-87"></a>
<details>
<summary>📄 <b>DOCS/Resposta PROMPT.txt</b> — Texto · 1.7 KB · 10 linhas · utf-8</summary>

```text
Montei o projeto completo exatamente na estrutura que você descreveu. Resumo do que está em cada peça:

interface.py — a UI (CustomTkinter). Janela "FlyScanner" com as 3 abas (Adicionar Inputs, Condições, Retorno), botão Rodar/Parar Robô, uma caixa de "terminal" já embutida mostrando as passagens encontradas; e uma segunda janela de Log em tempo real.
apis.py — carrega dinamicamente qualquer arquivo .py que você jogar em apis_input/ ou apis_output/, desde que siga o "contrato" (variáveis NOME, CAMPOS_CONFIG e função buscar()/enviar()). É por isso que a interface já gera os campos de configuração sozinha, sem precisar mexer em código.
condicoes.py — salva os filtros em condicoes.json e tem passagem_atende(), a função que decide se um voo bate com o que você configurou (tudo opcional, como você descreveu).
log.py — log central em arquivo + fila em tempo real, usado tanto pela janela de Log quanto pela caixa de "terminal" da janela principal.
buscador.py — o robô, roda em thread separada, faz o ciclo: consulta inputs → filtra com condições → dispara nos outputs → loga cada passo (erro de api, chave errada, tempo de consulta etc).
apis_input/google_flight.py — implementado em modo simulado (o Google não tem API pública oficial de preços), já retornando voos falsos no formato certo pra validar o fluxo inteiro. skyscanner.py e decolar.py ficaram como esqueletos prontos pra você preencher.
apis_output/terminal.py — implementado de verdade (joga no log/terminal). telegram.py e whatsapp.py ficaram como esqueletos.
Testei o fluxo completo (sem GUI, já que este ambiente é headless) rodando busca → filtro → envio, e funcionou certinho. Rode localmente com pip install customtkinter && python interface.py.s
```

</details>

<a id="f-88"></a>
<details>
<summary>📄 <b>log/flyscanner.log</b> — Outros · 28.3 KB · 187 linhas · utf-8</summary>

```
[2026-09-17 14:40:59] [INFO] [log] Log limpo pelo usuário.
[2026-09-17 14:41:01] [INFO] [buscador] Robô parado pelo usuário.
[2026-09-17 14:41:01] [INFO] [buscador] Loop do robô encerrado.
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: aviasales.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: decolar.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: google_flight.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: kiwi_tequila.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: serpapi_flights.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: skyscanner.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: markdown_export.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: telegram.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: terminal.py
[2026-09-17 15:10:13] [INFO] [apis] Módulo carregado: whatsapp.py
[2026-09-17 15:10:15] [INFO] [interface] Interface iniciada.
[2026-09-17 15:11:12] [SUCESSO] [interface] Condições salvas: Orig=LIS, OPO | Dest=GIG, GRU,  | Tipo=ida | Mês=12 | Ano=2026 | Ida=27/12/2026 | Min=1000.00 | Max=8000.00
[2026-09-17 15:11:13] [SUCESSO] [interface] Inputs salvos. APIs ativas: Google Flights (SerpApi)
[2026-09-17 15:11:13] [SUCESSO] [interface] Condições salvas: Orig=LIS, OPO | Dest=GIG, GRU,  | Tipo=ida | Mês=12 | Ano=2026 | Ida=27/12/2026 | Min=1000.00 | Max=8000.00
[2026-09-17 15:11:13] [SUCESSO] [interface] Retornos salvos. Saídas ativas: Exportar Markdown
[2026-09-17 15:11:13] [SUCESSO] [buscador] Robô iniciado.
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: aviasales.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: decolar.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: google_flight.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: kiwi_tequila.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: serpapi_flights.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: skyscanner.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: markdown_export.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: telegram.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: terminal.py
[2026-09-17 15:11:13] [INFO] [apis] Módulo carregado: whatsapp.py
[2026-09-17 15:11:13] [INFO] [buscador] Iniciando novo ciclo de consultas.
[2026-09-17 15:11:15] [INFO] [buscador] Google Flights (SerpApi): 41 voo(s) retornado(s) em 1.55s.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 4806.0, 'moeda': 'BRL', 'companhia': 'Azul', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 30}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7503.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 4740.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 30}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 5970.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 12}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 5995.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 11}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6396.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 5}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6568.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 2}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6659.0, 'moeda': 'BRL', 'companhia': 'Air Europa', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 1}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7793.0, 'moeda': 'BRL', 'companhia': 'LATAM', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 3593.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 38}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 4764.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 15}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 4573.0, 'moeda': 'BRL', 'companhia': 'Royal Air Maroc', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 18}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 5004.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 10}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 5227.0, 'moeda': 'BRL', 'companhia': 'Iberia', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 5}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'LIS', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6137.0, 'moeda': 'BRL', 'companhia': 'LATAM', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem LIS->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7226.0, 'moeda': 'BRL', 'companhia': 'KLM', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 2}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7259.0, 'moeda': 'BRL', 'companhia': 'Air France', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 2}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7596.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7607.0, 'moeda': 'BRL', 'companhia': 'Iberia', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6063.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 18}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6489.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 12}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6499.0, 'moeda': 'BRL', 'companhia': 'Air Europa', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 11}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6661.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 9}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6785.0, 'moeda': 'BRL', 'companhia': 'Iberia', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 7}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6789.0, 'moeda': 'BRL', 'companhia': 'KLM', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 7}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6789.0, 'moeda': 'BRL', 'companhia': 'Air France', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 7}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GIG salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 4318.0, 'moeda': 'BRL', 'companhia': 'Air Europa', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 25}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 4596.0, 'moeda': 'BRL', 'companhia': 'Iberia', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 19}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 4608.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 19}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 4274.0, 'moeda': 'BRL', 'companhia': 'Royal Air Maroc', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 24}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 5344.0, 'moeda': 'BRL', 'companhia': 'Lufthansa', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 3}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6349.0, 'moeda': 'BRL', 'companhia': 'Lufthansa', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GRU', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6390.0, 'moeda': 'BRL', 'companhia': 'Lufthansa', 'link': 'https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 15:11:15] [SUCESSO] [Exportar Markdown] Passagem OPO->GRU salva em ofertas.md.
[2026-09-17 15:11:15] [INFO] [buscador] Ciclo finalizado. Próxima consulta em 60s.
[2026-09-17 15:11:45] [INFO] [buscador] Robô parado pelo usuário.
[2026-09-17 15:11:45] [INFO] [buscador] Loop do robô encerrado.
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: aviasales.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: decolar.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: google_flight.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: kiwi_tequila.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: serpapi_flights.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: skyscanner.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: markdown_export.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: telegram.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: terminal.py
[2026-09-17 16:35:12] [INFO] [apis] Módulo carregado: whatsapp.py
[2026-09-17 16:35:20] [INFO] [interface] Interface iniciada.
[2026-09-17 16:36:06] [SUCESSO] [interface] Condições salvas: Orig=OPO | Dest=GIG | Tipo=ida | Mês=12 | Ano=2026 | Ida=27/12/2026 | Min=1000.00 | Max=9000.00
[2026-09-17 16:36:43] [SUCESSO] [interface] Retornos salvos. Saídas ativas: Exportar Markdown
[2026-09-17 16:36:45] [SUCESSO] [interface] Inputs salvos. APIs ativas: Google Flights (SerpApi)
[2026-09-17 16:36:45] [SUCESSO] [interface] Condições salvas: Orig=OPO | Dest=GIG | Tipo=ida | Mês=12 | Ano=2026 | Ida=27/12/2026 | Min=1000.00 | Max=9000.00
[2026-09-17 16:36:45] [SUCESSO] [interface] Retornos salvos. Saídas ativas: Exportar Markdown
[2026-09-17 16:36:45] [SUCESSO] [buscador] Robô iniciado.
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: aviasales.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: decolar.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: google_flight.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: kiwi_tequila.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: serpapi_flights.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: skyscanner.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: markdown_export.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: telegram.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: terminal.py
[2026-09-17 16:36:45] [INFO] [apis] Módulo carregado: whatsapp.py
[2026-09-17 16:36:45] [INFO] [buscador] Iniciando novo ciclo de consultas.
[2026-09-17 16:36:51] [INFO] [buscador] Google Flights (SerpApi): 12 voo(s) retornado(s) em 5.26s.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7208.0, 'moeda': 'BRL', 'companhia': 'KLM', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 1}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7246.0, 'moeda': 'BRL', 'companhia': 'Air France', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 1}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7576.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 7587.0, 'moeda': 'BRL', 'companhia': 'Iberia', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6048.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 17}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6213.0, 'moeda': 'BRL', 'companhia': 'Air Europa', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 15}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6472.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 11}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6767.0, 'moeda': 'BRL', 'companhia': 'Iberia', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 7}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6771.0, 'moeda': 'BRL', 'companhia': 'KLM', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 6}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 6801.0, 'moeda': 'BRL', 'companhia': 'Air France', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 6}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [SUCESSO] [buscador] Passagem bateu com as condições: {'origem': 'OPO', 'destino': 'GIG', 'tipo_viagem': 'ida', 'data_ida': '27/12/2026', 'data_volta': '', 'valor': 8780.0, 'moeda': 'BRL', 'companhia': 'Tap Air Portugal', 'link': 'https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27', 'fonte': 'Google Flights (SerpApi)', 'score': 0}
[2026-09-17 16:36:51] [SUCESSO] [Exportar Markdown] Oferta visual OPO->GIG anexada ao log.
[2026-09-17 16:36:51] [INFO] [buscador] Ciclo finalizado. Próxima consulta em 60s.
[2026-09-17 16:37:06] [INFO] [buscador] Robô parado pelo usuário.
[2026-09-17 16:37:06] [INFO] [buscador] Loop do robô encerrado.
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: aviasales.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: decolar.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: google_flight.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: kiwi_tequila.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: serpapi_flights.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: skyscanner.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: markdown_export.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: telegram.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: terminal.py
[2026-09-17 16:55:12] [INFO] [apis] Módulo carregado: whatsapp.py
[2026-09-17 16:55:14] [INFO] [interface] Interface iniciada.
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: aviasales.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: decolar.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: google_flight.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: kiwi_tequila.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: serpapi_flights.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: skyscanner.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: markdown_export.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: telegram.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: terminal.py
[2026-09-17 16:58:00] [INFO] [apis] Módulo carregado: whatsapp.py
[2026-09-17 16:58:02] [INFO] [interface] Interface iniciada.
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: aviasales.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: decolar.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: google_flight.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: kiwi_tequila.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: serpapi_flights.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: skyscanner.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: markdown_export.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: telegram.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: terminal.py
[2026-09-17 16:58:36] [INFO] [apis] Módulo carregado: whatsapp.py
[2026-09-17 16:58:38] [INFO] [interface] Interface iniciada.
```

</details>

<a id="f-89"></a>
<details>
<summary>🔀 <b>.gitignore</b> — Git · 404 B · 25 linhas · utf-8</summary>

```gitignore
# Ambientes Virtuais e Dependências
venv/
env/
.venv/
node_modules/

# Caches e Compilados Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Variáveis de Ambiente e Configurações Locais
.env
.vscode/
.idea/

# Temporários e saídas pesadas do Documentador (DOCUMENTACAO_PROJETO.md é versionado)
*.gravando_tmp
TREE_PROJETO*
CONTEUDO_PROJETO*
RELATORIO_EXTRACAO*
PROMPT_IA*
PACOTE_FUSAO_1_2_3*
PACOTE_FINAL*
```

</details>

<a id="f-90"></a>
<details>
<summary>🐍 <b>apis.py</b> — Python · 4.1 KB · 113 linhas · utf-8</summary>

```python
"""
apis.py
-------
Ponte entre a interface e as pastas apis_input/ e apis_output/.

Cada arquivo .py dentro de apis_input/ ou apis_output/ é carregado
dinamicamente aqui. Pra um script novo aparecer na interface, basta
jogar o arquivo na pasta certa e seguir o "contrato" abaixo — não
precisa mexer em mais nada.

CONTRATO DE UMA API DE ENTRADA (apis_input/*.py)
--------------------------------------------------
NOME = "Google Flights"                # nome amigável, mostrado na interface
CAMPOS_CONFIG = [                      # campos que a interface vai desenhar
    {"chave": "api_key", "label": "Chave da API", "tipo": "senha"},
    {"chave": "regiao", "label": "Região", "tipo": "texto"},
]

def buscar(config: dict, condicoes: dict) -> list[dict]:
    '''Retorna uma lista de voos (dicts), já brutos, sem filtrar.
    O buscador.py aplica condicoes.passagem_atende() em cada um.'''
    ...

CONTRATO DE UMA API DE SAÍDA (apis_output/*.py)
--------------------------------------------------
NOME = "Terminal"
CAMPOS_CONFIG = [...]                  # igual acima, pode ser [] se não precisa config

def enviar(voo: dict, config: dict, log_callback=None) -> None:
    '''Recebe um voo que já passou pelas condições e entrega no destino.'''
    ...

Tipos de campo suportados em CAMPOS_CONFIG: "texto", "senha", "numero".
"""

import importlib.util
import os
import sys

import log

PASTA_INPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apis_input")
PASTA_OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apis_output")


def _carregar_modulos(pasta: str) -> dict:
    """
    Varre a pasta, importa cada .py como módulo e retorna um dict
    {nome_do_arquivo_sem_extensao: modulo}.
    Ignora arquivos que não sejam .py, comecem com "_" ou dêem erro ao importar
    (o erro vai pro log em vez de derrubar a interface).
    """
    modulos = {}
    if not os.path.isdir(pasta):
        return modulos

    for nome_arquivo in sorted(os.listdir(pasta)):
        if not nome_arquivo.endswith(".py") or nome_arquivo.startswith("_"):
            continue

        nome_modulo = nome_arquivo[:-3]
        caminho = os.path.join(pasta, nome_arquivo)

        try:
            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = modulo
            spec.loader.exec_module(modulo)

            if not hasattr(modulo, "NOME"):
                modulo.NOME = nome_modulo.replace("_", " ").title()
            if not hasattr(modulo, "CAMPOS_CONFIG"):
                modulo.CAMPOS_CONFIG = []

            modulos[nome_modulo] = modulo
            log.registrar(f"Módulo carregado: {nome_arquivo}", nivel="INFO", origem="apis")
        except Exception as exc:
            log.registrar_erro(f"Falha ao carregar {nome_arquivo}: {exc}", origem="apis")

    return modulos


def listar_apis_input() -> dict:
    """Retorna {chave: modulo} de tudo que está em apis_input/."""
    return _carregar_modulos(PASTA_INPUT)


def listar_apis_output() -> dict:
    """Retorna {chave: modulo} de tudo que está em apis_output/."""
    return _carregar_modulos(PASTA_OUTPUT)


def buscar_em(modulo, config: dict, condicoes: dict) -> list:
    """Chama modulo.buscar() com segurança, logando qualquer erro."""
    try:
        if not hasattr(modulo, "buscar"):
            log.registrar_erro(f"{modulo.NOME} não implementa buscar()", origem="apis")
            return []
        return modulo.buscar(config or {}, condicoes or {}) or []
    except Exception as exc:
        log.registrar_erro(f"Erro consultando {modulo.NOME}: {exc}", origem=getattr(modulo, "NOME", "apis"))
        return []


def enviar_para(modulo, voo: dict, config: dict) -> None:
    """Chama modulo.enviar() com segurança, logando qualquer erro."""
    try:
        if not hasattr(modulo, "enviar"):
            log.registrar_erro(f"{modulo.NOME} não implementa enviar()", origem="apis")
            return
        modulo.enviar(voo, config or {}, log_callback=log.registrar)
    except Exception as exc:
        log.registrar_erro(f"Erro enviando via {modulo.NOME}: {exc}", origem=getattr(modulo, "NOME", "apis"))
```

</details>

<a id="f-91"></a>
<details>
<summary>🐍 <b>buscador.py</b> — Python · 6.5 KB · 155 linhas · utf-8</summary>

```python
"""
buscador.py
-----------
O "robô". Roda em uma thread separada (pra não travar a interface),
lendo periodicamente:
  1) as apis de entrada configuradas (e suas config/tokens);
  2) as condições cadastradas (condicoes.py);
  3) as apis de saída selecionadas (e suas config);

E fica em loop: consulta cada api_input -> filtra cada voo retornado
com condicoes.passagem_atende() -> se bater, manda pra cada api_output
configurada -> tudo isso reportando passo a passo pro log.py.

Também controla deduplicação simples (não fica reenviando o mesmíssimo
voo a cada ciclo).
"""

import threading
import time

import apis
import condicoes as condicoes_mod
import log
import historico


class Robo:
    def __init__(self, intervalo_segundos: int = 60):
        # Esse intervalo agora atua como um "Intervalo Global" entre as consultas
        self.intervalo_segundos = intervalo_segundos
        self._thread = None
        self._parar_evento = threading.Event()
        self._rodando = False
        self._voos_ja_enviados = set()  # chave simples pra evitar duplicar

        # Preenchidos via configurar() antes de start()
        self.apis_input_selecionadas = {}   # {chave_modulo: config_dict}
        self.apis_output_selecionadas = {}  # {chave_modulo: config_dict}

    def configurar(self, apis_input_selecionadas: dict, apis_output_selecionadas: dict):
        """
        apis_input_selecionadas: {"google_flight": {"api_key": "...", "intervalo_minutos": 60, "ultima_execucao": 0}, ...}
        apis_output_selecionadas: {"terminal": {}, "telegram": {"bot_token": "...", "chat_id": "..."}}
        """
        self.apis_input_selecionadas = apis_input_selecionadas or {}
        self.apis_output_selecionadas = apis_output_selecionadas or {}

    @property
    def rodando(self) -> bool:
        return self._rodando

    def start(self):
        if self._rodando:
            log.registrar_aviso("Robô já está rodando.", origem="buscador")
            return

        if not self.apis_input_selecionadas:
            log.registrar_erro("Nenhuma api de entrada configurada. Robô não iniciado.", origem="buscador")
            return
        if not self.apis_output_selecionadas:
            log.registrar_erro("Nenhuma api de saída configurada. Robô não iniciado.", origem="buscador")
            return

        self._parar_evento.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._rodando = True
        self._thread.start()
        log.registrar_sucesso("Robô iniciado.", origem="buscador")

    def stop(self):
        if not self._rodando:
            return
        self._parar_evento.set()
        self._rodando = False
        log.registrar("Robô parado pelo usuário.", nivel="INFO", origem="buscador")

    def _chave_voo(self, voo: dict) -> tuple:
        return (
            voo.get("origem"), voo.get("destino"), voo.get("data_ida"),
            voo.get("data_volta"), voo.get("valor"), voo.get("companhia"), voo.get("fonte"),
        )

    def _loop(self):
        modulos_input = apis.listar_apis_input()
        modulos_output = apis.listar_apis_output()

        fila_apis = list(self.apis_input_selecionadas.keys())
        indice_atual = 0

        while not self._parar_evento.is_set():
            condicoes_atuais = condicoes_mod.carregar()

            if not fila_apis:
                log.registrar_erro("Fila de APIs vazia. Loop interrompido.", origem="buscador")
                break 

            # 1. Pega a API da vez
            chave_input = fila_apis[indice_atual]
            config_input = self.apis_input_selecionadas[chave_input]

            agora = time.time()
            intervalo_api_segundos = config_input.get("intervalo_minutos", 60) * 60
            ultima_exec = config_input.get("ultima_execucao", 0)

            # 2. Avalia o Cooldown
            if (agora - ultima_exec) >= intervalo_api_segundos:
                modulo_input = modulos_input.get(chave_input)
                
                if modulo_input:
                    inicio = time.time()
                    voos = apis.buscar_em(modulo_input, config_input, condicoes_atuais)
                    duracao = round(time.time() - inicio, 2)
                    
                    log.registrar(f"{modulo_input.NOME}: {len(voos)} voos retornados em {duracao}s.", nivel="INFO", origem="buscador")

                    for voo in voos:
                        voo = historico.processar_score(voo)

                        if not condicoes_mod.passagem_atende(voo, condicoes_atuais):
                            continue

                        chave = self._chave_voo(voo)
                        if chave in self._voos_ja_enviados:
                            continue
                        self._voos_ja_enviados.add(chave)

                        log.registrar(f"Passagem bateu com as condições: {voo}", nivel="SUCESSO", origem="buscador")

                        for chave_output, config_output in self.apis_output_selecionadas.items():
                            modulo_output = modulos_output.get(chave_output)
                            if modulo_output:
                                apis.enviar_para(modulo_output, voo, config_output)
                            else:
                                log.registrar_erro(f"Api de saída '{chave_output}' não encontrada.", origem="buscador")

                    # Registra que a API foi consumida
                    self.apis_input_selecionadas[chave_input]["ultima_execucao"] = time.time()

                    # O robô descansa pelo intervalo global apenas quando UMA API FOI EXECUTADA
                    if not self._parar_evento.is_set():
                        log.registrar(f"Aguardando {self.intervalo_segundos}s para a próxima consulta na fila...", nivel="INFO", origem="buscador")
                        self._parar_evento.wait(self.intervalo_segundos)
                else:
                    log.registrar_erro(f"Api de entrada '{chave_input}' não encontrada em apis_input/.", origem="buscador")

            # 3. Avança a fila para a próxima API, independentemente de a anterior ter rodado ou não
            indice_atual = (indice_atual + 1) % len(fila_apis)
            
            # Se todas as APIs estiverem em cooldown, evita um loop infinito enlouquecido da CPU
            # Um mini-sleep de 1 segundo mantém o programa saudável até que alguma API esfrie.
            if not self._parar_evento.is_set():
                 time.sleep(1)

        self._rodando = False
        log.registrar("Loop do robô encerrado.", nivel="INFO", origem="buscador")
```

</details>

<a id="f-92"></a>
<details>
<summary>🧾 <b>condicoes.json</b> — JSON · 286 B · 14 linhas · utf-8</summary>

```json
{
  "origem": "OPO",
  "destino": "GIG",
  "tipo_viagem": "ida",
  "mes": "12",
  "ano": "2026",
  "data_ida": "27/12/2026",
  "data_volta": "",
  "valor_minimo": "1000.00",
  "valor_maximo": "9000.00",
  "moeda": "BRL",
  "observacoes": "",
  "apenas_menor_preco": false
}
```

</details>

<a id="f-93"></a>
<details>
<summary>🐍 <b>condicoes.py</b> — Python · 5.6 KB · 159 linhas · utf-8</summary>

```python
"""
condicoes.py
------------
Guarda e avalia as "Condições" (filtros) que o tópico 2 da interface
configura. Tudo é opcional: quanto mais campos preenchidos, mais
específica é a passagem que o buscador vai deixar passar pro output.

As condições são persistidas em condicoes.json (na raiz do projeto),
e o buscador.py lê esse arquivo pra saber o que validar a cada voo
retornado pelas apis_input.
"""

import json
import os

ARQUIVO_CONDICOES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "condicoes.json")

# Campos suportados. Todos opcionais (None ou "" = sem filtro nesse campo).
CAMPOS_PADRAO = {
    "origem": "",          # ex: "Rio de Janeiro (GIG)"
    "destino": "",         # ex: "Lisboa (LIS)"
    "tipo_viagem": "",     # "ida", "ida_volta" ou "" (sem filtro)
    "mes": "",             # ex: "12" (dezembro)
    "ano": "",             # ex: "2025"
    "data_ida": "",        # opcional, formato livre "DD/MM/AAAA"
    "data_volta": "",      # opcional
    "valor_minimo": "",    # string numérica, ex: "0"
    "valor_maximo": "",    # string numérica, ex: "3000"
    "moeda": "BRL",
    "observacoes": "",     # anotação livre do usuário sobre esse filtro
}


def carregar() -> dict:
    """Carrega as condições salvas. Se não existir arquivo, retorna padrão vazio."""
    if not os.path.exists(ARQUIVO_CONDICOES):
        return dict(CAMPOS_PADRAO)
    try:
        with open(ARQUIVO_CONDICOES, "r", encoding="utf-8") as f:
            dados = json.load(f)
        completo = dict(CAMPOS_PADRAO)
        completo.update(dados)
        return completo
    except (json.JSONDecodeError, OSError):
        return dict(CAMPOS_PADRAO)


def salvar(condicoes: dict) -> None:
    """Salva as condições vindas da interface (tópico 2)."""
    completo = dict(CAMPOS_PADRAO)
    completo.update(condicoes or {})
    with open(ARQUIVO_CONDICOES, "w", encoding="utf-8") as f:
        json.dump(completo, f, ensure_ascii=False, indent=2)


def _texto_bate(filtro: str, valor: str) -> bool:
    """
    Compara texto ignorando maiúsculas/minúsculas.
    Agora suporta múltiplos valores separados por vírgula na interface (Ex: LIS, OPO).
    Filtro vazio = sempre bate.
    """
    if not filtro:
        return True
    if not valor:
        return False
        
    # Separa os filtros por vírgula e limpa os espaços
    termos_filtro = [t.strip().lower() for t in filtro.split(",") if t.strip()]
    valor_voo = valor.strip().lower()
    
    # Se a origem/destino do voo bater com qualquer um dos itens separados por vírgula, passa
    for termo in termos_filtro:
        if termo in valor_voo or valor_voo in termo:
            return True
            
    return False


def _numero(valor):
    try:
        return float(str(valor).replace(",", ".").strip())
    except (ValueError, TypeError):
        return None


def passagem_atende(voo: dict, condicoes: dict = None) -> bool:
    """
    Verifica se um voo (dict retornado por uma api_input) atende às
    condições configuradas. Estrutura esperada de `voo` (chaves opcionais,
    cada api_input deve tentar preencher o máximo possível):

    {
        "origem": "Rio de Janeiro (GIG)",
        "destino": "Lisboa (LIS)",
        "tipo_viagem": "ida_volta",
        "data_ida": "10/12/2025",
        "data_volta": "20/12/2025",
        "valor": 2850.00,
        "moeda": "BRL",
        "companhia": "TAP",
        "link": "https://...",
    }

    Regra: campo de condição vazio = não filtra por ele.
    Campo de condição preenchido, mas o voo não tem essa informação = não bate
    (não arriscamos falso positivo).
    """
    condicoes = condicoes or carregar()

    if not _texto_bate(condicoes.get("origem", ""), voo.get("origem", "")):
        return False
    if not _texto_bate(condicoes.get("destino", ""), voo.get("destino", "")):
        return False

    tipo_filtro = (condicoes.get("tipo_viagem") or "").strip().lower()
    if tipo_filtro:
        if (voo.get("tipo_viagem") or "").strip().lower() != tipo_filtro:
            return False

    mes_filtro = (condicoes.get("mes") or "").strip()
    ano_filtro = (condicoes.get("ano") or "").strip()
    if mes_filtro or ano_filtro:
        data_ida = voo.get("data_ida", "")
        partes = data_ida.split("/") if data_ida else []
        if len(partes) != 3:
            return False
        _, mes_voo, ano_voo = partes
        if mes_filtro and mes_filtro.zfill(2) != mes_voo.zfill(2):
            return False
        if ano_filtro and ano_filtro != ano_voo:
            return False

    if condicoes.get("data_ida") and condicoes["data_ida"] != voo.get("data_ida", ""):
        return False
    if condicoes.get("data_volta") and condicoes["data_volta"] != voo.get("data_volta", ""):
        return False

    valor_min = _numero(condicoes.get("valor_minimo"))
    valor_max = _numero(condicoes.get("valor_maximo"))
    valor_voo = _numero(voo.get("valor"))

    if (valor_min is not None or valor_max is not None) and valor_voo is None:
        return False
    if valor_min is not None and valor_voo < valor_min:
        return False
    if valor_max is not None and valor_voo > valor_max:
        return False
    
    # Filtro de Menor Preço Histórico
    # Se o checkbox estiver marcado, a passagem PRECISA ter uma pontuação mínima (ex: 10 pontos/10% mais barata)
    exige_historico = str(condicoes.get("apenas_menor_preco", "false")).lower() == "true"
    
    if exige_historico:
        score = int(voo.get("score", 0))
        # Define o nível de exigência. 10 = só deixa passar se for 10% mais barato que a média local.
        if score < 10:
            return False

    return True
```

</details>

<a id="f-94"></a>
<details>
<summary>🧾 <b>config_apis.json</b> — JSON · 1.3 KB · 66 linhas · utf-8</summary>

```json
{
  "input": {
    "aviasales": {
      "intervalo_minutos": 60,
      "token": "f573ae43b54b441be9625200394b982a"
    },
    "decolar": {
      "intervalo_minutos": 60,
      "api_key": "",
      "afiliado_id": ""
    },
    "google_flight": {
      "intervalo_minutos": 60,
      "api_key": ""
    },
    "kiwi_tequila": {
      "intervalo_minutos": 60,
      "api_key": ""
    },
    "serpapi_flights": {
      "intervalo_minutos": 60,
      "api_key": "ef923504e83d24d7de3bfb613c70689fcb560b539aedc6f363cec77f6a4ce7c9"
    },
    "skyscanner": {
      "intervalo_minutos": 60,
      "api_key": "",
      "host": ""
    }
  },
  "output": {
    "telegram": {
      "bot_token": "",
      "chat_id": "",
      "estilo": ""
    },
    "terminal": {},
    "whatsapp": {
      "numero": "",
      "token": ""
    },
    "markdown_export": {
      "nome_arquivo": "ofertas.md"
    }
  },
  "output_ativas": [
    "markdown_export",
    "terminal"
  ],
  "input_ativas": [
    "serpapi_flights"
  ],
  "ordem_inputs": [
    "aviasales",
    "serpapi_flights",
    "decolar",
    "google_flight",
    "kiwi_tequila",
    "skyscanner"
  ],
  "ordem_outputs": [
    "markdown_export",
    "terminal",
    "telegram",
    "whatsapp"
  ]
}
```

</details>

<a id="f-96"></a>
<details>
<summary>🐍 <b>documentador.pyw</b> — Python · 160.0 KB · 3377 linhas · utf-8</summary>

``````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Documentador Universal de Projetos  —  v2
=========================================

Arquivo único e portátil (requer apenas: pip install customtkinter). Copie para a raiz do
projeto que deseja documentar e execute:

    python documentador.pyw

A raiz do projeto é a pasta onde ESTE arquivo está (não o diretório de trabalho do
terminal). A ferramenta é somente leitura em relação ao projeto: nunca executa, importa,
move, renomeia ou apaga arquivos inspecionados. Nenhuma IA é executada.

Novidades da v2
---------------
* Interface em barra lateral com pipeline, cartões de métricas, abas, busca (Ctrl+F),
  avisos (toasts), temas claro/escuro e botão "EXECUTAR TUDO".
* Extração paralela (várias threads) e varredura mais rápida.
* Regras de exclusão múltiplas (nomes, curingas, caminhos) com atalhos por tecnologia.
* Configurações persistentes (por projeto) em ~/.documentador_universal/config.json.
* Gerador de DOCUMENTACAO_PROJETO.md bonito (emojis, tabelas, estatísticas, blocos
  recolhíveis) — gerado localmente, sem IA.
* Gravação atômica (sem arquivos pela metade) e autoteste ampliado.

Publicação: botão «SUBIR PRO GITHUB» no topo (git + gh); se o Markdown final já foi gerado, sobe junto.

Modo de verificação (sem interface):  python documentador_universal.py --selftest
"""

import atexit
import codecs
import fnmatch
import hashlib
import html
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

try:
    import customtkinter as ctk
    import tkinter as tk
    from tkinter import filedialog, messagebox
except Exception:  # sem CustomTkinter/Tk: o modo --selftest continua funcionando
    ctk = None
    tk = None

# ----------------------------------------------------------------------------
# Constantes e configuração
# ----------------------------------------------------------------------------

APP_TITLE = "Documentador de Projetos"
APP_VERSION = "1.0"

if getattr(sys, "frozen", False):  # executável empacotado
    SCRIPT_PATH = Path(os.path.abspath(sys.executable))
else:
    SCRIPT_PATH = Path(os.path.abspath(__file__))
ROOT = SCRIPT_PATH.parent  # raiz do projeto = pasta do script

# Diretórios volumosos conhecidos: usados SÓ para detecção/aviso. Nada é excluído por padrão.
HEAVY_DIRS = [
    ".git", ".svn", ".hg", "node_modules", ".venv", "venv", "env",
    "__pycache__", "dist", "build", ".idea", ".vscode", ".mypy_cache",
    ".pytest_cache", ".tox", "target", "vendor", ".next", ".nuxt", "bower_components",
    ".gradle", "obj", "bin", ".cache", "coverage",
]

# Lista de exclusões prontas (caixas de seleção na janela de opções). Marcou = qualquer
# pasta/arquivo com esse nome, em qualquer nível do projeto, é pulado. Nada vem marcado
# por padrão; use "Marcar recomendados" para um começo rápido.
PRESET_GROUPS = [
    ("🔀 Controle de versão e IDEs", [
        (".git/", "repositório Git (milhares de objetos)"), (".svn/", "Subversion"),
        (".hg/", "Mercurial"), (".idea/", "JetBrains / PyCharm"),
        (".vscode/", "VS Code"), (".vs/", "Visual Studio")]),
    ("🐍 Python e ambientes virtuais", [
        ("venv/", "ambiente virtual"), (".venv/", "ambiente virtual"), ("env/", "ambiente virtual"),
        ("__pycache__/", "bytecode compilado"), (".mypy_cache/", "cache do mypy"),
        (".pytest_cache/", "cache do pytest"), (".ruff_cache/", "cache do ruff"),
        (".tox/", "ambientes do tox"), (".nox/", "ambientes do nox"),
        (".ipynb_checkpoints/", "checkpoints do Jupyter"), ("*.egg-info/", "metadados de pacote"),
        (".eggs/", "eggs do setuptools"), ("site-packages/", "pacotes instalados"),
        ("htmlcov/", "relatório de cobertura")]),
    ("🟩 Node e front-end", [
        ("node_modules/", "dependências npm (às vezes 50 mil arquivos)"), (".next/", "build do Next.js"),
        (".nuxt/", "build do Nuxt"), (".svelte-kit/", "build do SvelteKit"), (".angular/", "cache do Angular"),
        (".parcel-cache/", "cache do Parcel"), (".turbo/", "cache do Turborepo"),
        (".yarn/", "cache do Yarn"), (".pnpm-store/", "store do pnpm"),
        ("bower_components/", "dependências Bower")]),
    ("🏗️ Build, saída e dependências", [
        ("dist/", "saída de build"), ("build/", "saída de build"), ("target/", "Maven / Rust"),
        ("out/", "saída de build"), ("bin/", "binários compilados"), ("obj/", ".NET intermediário"),
        (".gradle/", "cache do Gradle"), ("coverage/", "cobertura de testes"),
        ("vendor/", "dependências (PHP/Go/Ruby)"), ("Pods/", "CocoaPods"),
        ("DerivedData/", "Xcode"), (".terraform/", "plugins do Terraform")]),
    ("🧠 Caches e temporários", [
        (".cache/", "cache genérico"), ("cache/", "cache genérico"), ("tmp/", "temporários"),
        ("temp/", "temporários"), (".tmp/", "temporários"), ("logs/", "pasta de logs")]),
    ("🌐 Navegador, Selenium e drivers", [
        ("chrome_profile/", "perfil do Chrome (Selenium)"), ("chrome-profile/", "perfil do Chrome"),
        ("selenium_profile/", "perfil do Selenium"), ("browser_profile/", "perfil de navegador"),
        ("user-data/", "user-data-dir do navegador"), (".wdm/", "cache do webdriver-manager"),
        ("Cache/", "cache de navegador"), ("Code Cache/", "cache de código do Chromium"),
        ("GPUCache/", "cache de GPU do Chromium"), ("Service Worker/", "service workers"),
        ("IndexedDB/", "banco do navegador")]),
    ("🗑️ Arquivos descartáveis", [
        ("*.log", "arquivos de log"), ("*.pyc", "bytecode Python"), ("*.tmp", "temporários"),
        ("*.bak", "backups"), ("*.swp", "swap do Vim"), (".DS_Store", "lixo do macOS"),
        ("Thumbs.db", "lixo do Windows"), ("*.min.js", "JS minificado"), ("*.min.css", "CSS minificado"),
        ("*.map", "source maps")]),
]
PRESET_ALL = [p for _, items in PRESET_GROUPS for p, _ in items]
PRESET_RECOMMENDED = {
    ".git/", ".svn/", ".hg/", ".idea/", ".vscode/", ".vs/", "venv/", ".venv/", "env/", "__pycache__/",
    ".mypy_cache/", ".pytest_cache/", ".ruff_cache/", ".tox/", ".ipynb_checkpoints/", "*.egg-info/",
    "node_modules/", ".next/", ".nuxt/", ".parcel-cache/", ".turbo/", "dist/", "build/", "target/",
    ".gradle/", "coverage/", ".cache/", ".wdm/", "chrome_profile/", "chrome-profile/", "selenium_profile/",
    "browser_profile/", "Code Cache/", "GPUCache/", "*.pyc", ".DS_Store", "Thumbs.db",
}

# Saídas geradas por esta ferramenta (reconhecidas pelo nome).
OUTPUT_RE = re.compile(
    r"^(TREE_PROJETO|CONTEUDO_PROJETO|RELATORIO_EXTRACAO|PROMPT_IA|PACOTE_FUSAO_1_2_3|PACOTE_FINAL|"
    r"DOCUMENTACAO_PROJETO)(_PARTE_\d{3,})?(_REMONTADO)?\.(txt|md)$", re.IGNORECASE)

SENSITIVE_SUFFIXES = (".pem", ".key", ".pfx", ".p12", ".jks", ".keystore", ".ppk", ".kdbx")
SENSITIVE_PREFIXES = ("id_rsa", "id_dsa", "id_ecdsa", "id_ed25519")
SENSITIVE_NAMES = {".env", ".npmrc", ".pypirc", ".netrc", ".htpasswd", "wp-config.php",
                   "credentials", "credentials.json", "secrets.json", "secrets.yml",
                   "secrets.yaml", "service-account.json"}

PREVIEW_LIMIT = 300_000          # apenas a PRÉ-VISUALIZAÇÃO na janela; cópia/export usam tudo
CLIPBOARD_WARN_CHARS = 8_000_000
SEP = "=" * 60

CONFIG_DIR = Path(os.environ.get("DOCUMENTADOR_CONFIG_DIR") or (Path.home() / ".documentador_universal"))
CONFIG_FILE = CONFIG_DIR / "config.json"
DEFAULT_CFG = dict(
    rules_text="", excl_checked=[], sens=False, selfign=False, maxmb=0.0, part=0, workers=0,
    md_emoji=True, md_collapse=True, md_contents=True, md_tree=True, md_stats=True,
    appearance="System", scale=1.0, heavy_limit=1000, heavy_action="ask", project_version=1.0,
    autotest_before_push=False,  # resquício: roda o teste automatizado antes do push (ainda não implementado)
)
GLOBAL_CFG_KEYS = {"appearance", "scale", "workers", "part", "md_emoji", "md_collapse",
                   "md_contents", "md_tree", "md_stats", "heavy_limit", "heavy_action"}

STRONG_SIGNATURES = [
    (b"\x89PNG\r\n\x1a\n", "Imagem PNG"), (b"\xff\xd8\xff", "Imagem JPEG"),
    (b"GIF87a", "Imagem GIF"), (b"GIF89a", "Imagem GIF"), (b"%PDF", "Documento PDF"),
    (b"PK\x03\x04", "Arquivo ZIP/OOXML/JAR"), (b"\x7fELF", "Executável ELF"),
    (b"Rar!", "Arquivo RAR"), (b"7z\xbc\xaf\x27\x1c", "Arquivo 7z"),
    (b"\x1f\x8b", "Arquivo GZIP"), (b"\xd0\xcf\x11\xe0", "Documento OLE (Office antigo)"),
    (b"SQLite format 3\x00", "Banco de dados SQLite"),
]
WEAK_SIGNATURES = [
    (b"MZ", "Executável/DLL Windows (PE)"), (b"BM", "Imagem BMP"),
    (b"RIFF", "Contêiner RIFF (WAV/AVI/WEBP)"), (b"\x00\x00\x01\x00", "Ícone ICO"),
    (b"wOFF", "Fonte WOFF"), (b"wOF2", "Fonte WOFF2"), (b"OTTO", "Fonte OpenType"),
    (b"\x00\x01\x00\x00", "Fonte TrueType"),
]
BINARY_EXT = {
    ".png": "Imagem PNG", ".jpg": "Imagem JPEG", ".jpeg": "Imagem JPEG", ".gif": "Imagem GIF",
    ".bmp": "Imagem BMP", ".ico": "Ícone", ".webp": "Imagem WEBP", ".exe": "Executável",
    ".dll": "Biblioteca dinâmica", ".so": "Biblioteca compartilhada", ".zip": "Arquivo ZIP",
    ".rar": "Arquivo RAR", ".7z": "Arquivo 7z", ".gz": "Arquivo GZIP", ".tar": "Arquivo TAR",
    ".ttf": "Fonte TrueType", ".otf": "Fonte OpenType", ".woff": "Fonte WOFF",
    ".woff2": "Fonte WOFF2", ".pdf": "Documento PDF", ".pyc": "Bytecode Python",
    ".class": "Bytecode Java", ".jar": "Arquivo JAR", ".mp3": "Áudio MP3", ".mp4": "Vídeo MP4",
    ".wav": "Áudio WAV", ".db": "Banco de dados", ".sqlite": "Banco SQLite",
    ".docx": "Documento Word", ".xlsx": "Planilha Excel", ".pptx": "Apresentação PowerPoint",
}

# Linguagens: extensão -> (cerca Markdown, nome, emoji)
LANGS = {
    ".py": ("python", "Python", "🐍"), ".pyw": ("python", "Python", "🐍"),
    ".js": ("javascript", "JavaScript", "🟨"), ".mjs": ("javascript", "JavaScript", "🟨"),
    ".cjs": ("javascript", "JavaScript", "🟨"), ".jsx": ("jsx", "React (JSX)", "⚛️"),
    ".ts": ("typescript", "TypeScript", "🔷"), ".tsx": ("tsx", "React (TSX)", "⚛️"),
    ".vue": ("vue", "Vue", "💚"), ".svelte": ("svelte", "Svelte", "🧡"),
    ".php": ("php", "PHP", "🐘"), ".java": ("java", "Java", "☕"), ".kt": ("kotlin", "Kotlin", "🟣"),
    ".cs": ("csharp", "C#", "🟪"), ".vb": ("vbnet", "VB.NET", "🟦"),
    ".c": ("c", "C", "🔧"), ".h": ("c", "C/C++ (header)", "🔧"),
    ".cpp": ("cpp", "C++", "⚙️"), ".cc": ("cpp", "C++", "⚙️"), ".hpp": ("cpp", "C++", "⚙️"),
    ".go": ("go", "Go", "🐹"), ".rs": ("rust", "Rust", "🦀"), ".rb": ("ruby", "Ruby", "💎"),
    ".swift": ("swift", "Swift", "🧡"), ".dart": ("dart", "Dart", "🎯"), ".lua": ("lua", "Lua", "🌙"),
    ".r": ("r", "R", "📈"), ".pl": ("perl", "Perl", "🐪"), ".scala": ("scala", "Scala", "🔺"),
    ".sh": ("bash", "Shell", "🐚"), ".bash": ("bash", "Shell", "🐚"), ".zsh": ("bash", "Shell", "🐚"),
    ".bat": ("batch", "Batch", "🪟"), ".cmd": ("batch", "Batch", "🪟"),
    ".ps1": ("powershell", "PowerShell", "🪟"),
    ".html": ("html", "HTML", "🌐"), ".htm": ("html", "HTML", "🌐"),
    ".css": ("css", "CSS", "🎨"), ".scss": ("scss", "SCSS", "🎨"), ".sass": ("sass", "Sass", "🎨"),
    ".less": ("less", "Less", "🎨"), ".sql": ("sql", "SQL", "🗄️"),
    ".json": ("json", "JSON", "🧾"), ".yml": ("yaml", "YAML", "⚙️"), ".yaml": ("yaml", "YAML", "⚙️"),
    ".toml": ("toml", "TOML", "⚙️"), ".ini": ("ini", "INI", "⚙️"), ".cfg": ("ini", "Config", "⚙️"),
    ".conf": ("ini", "Config", "⚙️"), ".xml": ("xml", "XML", "📰"), ".csv": ("csv", "CSV", "📊"),
    ".md": ("markdown", "Markdown", "📝"), ".rst": ("rst", "reStructuredText", "📝"),
    ".txt": ("text", "Texto", "📄"), ".gradle": ("groovy", "Gradle", "🐘"),
    ".proto": ("protobuf", "Protobuf", "📡"), ".graphql": ("graphql", "GraphQL", "🔮"),
}
SPECIAL_NAMES = {
    "dockerfile": ("dockerfile", "Docker", "🐳"), "makefile": ("makefile", "Makefile", "🛠️"),
    ".gitignore": ("gitignore", "Git", "🔀"), ".gitattributes": ("gitattributes", "Git", "🔀"),
    ".env": ("dotenv", "Variáveis de ambiente", "🔐"), ".editorconfig": ("ini", "Config", "⚙️"),
}
TECH_MARKERS = {
    "package.json": "🟩 Node.js / npm", "yarn.lock": "🧶 Yarn", "pnpm-lock.yaml": "📦 pnpm",
    "tsconfig.json": "🔷 TypeScript", "vite.config.js": "⚡ Vite", "vite.config.ts": "⚡ Vite",
    "webpack.config.js": "📦 Webpack", "next.config.js": "▲ Next.js", "angular.json": "🅰️ Angular",
    "requirements.txt": "🐍 Python (pip)", "pyproject.toml": "🐍 Python (pyproject)",
    "setup.py": "🐍 Python (setuptools)", "pipfile": "🐍 Python (Pipenv)",
    "manage.py": "🎸 Django", "pom.xml": "☕ Java (Maven)", "build.gradle": "🐘 Gradle",
    "build.gradle.kts": "🐘 Gradle (Kotlin)", "composer.json": "🐘 PHP (Composer)",
    "artisan": "🅻 Laravel", "gemfile": "💎 Ruby (Bundler)", "cargo.toml": "🦀 Rust (Cargo)",
    "go.mod": "🐹 Go modules", "dockerfile": "🐳 Docker", "docker-compose.yml": "🐳 Docker Compose",
    "docker-compose.yaml": "🐳 Docker Compose", "makefile": "🛠️ Make", "cmakelists.txt": "🛠️ CMake",
    "pubspec.yaml": "🎯 Flutter / Dart", "wp-config.php": "📰 WordPress", ".gitignore": "🔀 Git",
}
TECH_EXT = {".csproj": "🟪 .NET (csproj)", ".sln": "🟪 .NET (solução)", ".vbproj": "🟦 VB.NET (vbproj)"}


class Cancelled(Exception):
    pass


def human_size(n):
    if n is None:
        return "?"
    n = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return f"{int(n)} B" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def human_time(sec):
    sec = int(sec)
    return f"{sec // 60:02d}:{sec % 60:02d}"


def longpath(p):
    """No Windows, caminhos longos exigem o prefixo \\\\?\\."""
    p = str(p)
    if os.name == "nt" and len(p) >= 240 and not p.startswith("\\\\?\\"):
        return "\\\\?\\" + os.path.abspath(p)
    return p


def is_sensitive(name):
    n = name.lower()
    return (n in SENSITIVE_NAMES or n.startswith(".env.") or n.endswith(SENSITIVE_SUFFIXES)
            or n.startswith(SENSITIVE_PREFIXES))


def fence_for(text):
    """Cerca Markdown mais longa que qualquer sequência de crases no texto."""
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def lang_of(name):
    low = name.lower()
    if low in SPECIAL_NAMES:
        return SPECIAL_NAMES[low]
    if low.startswith(".env"):
        return SPECIAL_NAMES[".env"]
    return LANGS.get(os.path.splitext(low)[1], ("", "Outros", "📄"))


class AtomicWriter:
    """Grava em arquivo temporário e só então substitui o destino (sem arquivos pela metade)."""

    def __init__(self, path):
        self.path = Path(path)
        self.tmp = self.path.with_name(self.path.name + ".gravando_tmp")
        self.f = None

    def __enter__(self):
        self.f = open(longpath(self.tmp), "w", encoding="utf-8", newline="")
        return self.f

    def __exit__(self, et, ev, tb):
        try:
            self.f.close()
        finally:
            if et is None:
                os.replace(longpath(self.tmp), longpath(self.path))
            else:
                try:
                    os.remove(longpath(self.tmp))
                except OSError:
                    pass
        return False


# ----------------------------------------------------------------------------
# Configurações persistentes
# ----------------------------------------------------------------------------

def _root_key(root):
    return os.path.normcase(os.path.abspath(str(root)))


def load_config(root, path=None):
    path = Path(path or CONFIG_FILE)
    cfg = dict(DEFAULT_CFG)
    cfg["excl_checked"] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        merged = dict(data.get("global", {}))
        merged.update(data.get("projects", {}).get(_root_key(root), {}))
        for k, v in merged.items():
            if k not in DEFAULT_CFG:
                continue
            try:
                d = DEFAULT_CFG[k]
                if isinstance(d, list):
                    cfg[k] = [str(x) for x in v] if isinstance(v, list) else []
                elif isinstance(d, bool):
                    cfg[k] = bool(v)
                elif isinstance(d, float):
                    cfg[k] = float(v)
                elif isinstance(d, int):
                    cfg[k] = int(v)
                else:
                    cfg[k] = str(v)
            except (TypeError, ValueError):
                pass
    except (OSError, ValueError):
        pass
    cfg["scale"] = min(1.6, max(0.7, cfg["scale"]))
    return cfg


def save_config(root, cfg, path=None):
    path = Path(path or CONFIG_FILE)
    try:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            data = {}
        data.setdefault("global", {})
        data.setdefault("projects", {})
        for k, v in cfg.items():
            if k in GLOBAL_CFG_KEYS:
                data["global"][k] = v
        data["projects"][_root_key(root)] = {k: v for k, v in cfg.items() if k not in GLOBAL_CFG_KEYS}
        path.parent.mkdir(parents=True, exist_ok=True)
        with AtomicWriter(path) as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except (OSError, TypeError, ValueError):
        return False


# ----------------------------------------------------------------------------
# Regras de exclusão
# ----------------------------------------------------------------------------

def parse_rules(text):
    """Uma regra por linha (ou separadas por vírgula). '#' inicia comentário.
    'nome/' = só diretórios; 'a/b' ou 'a/**/b' = caminho relativo; '*.log' = curinga no nome."""
    lines = text.splitlines() if isinstance(text, str) else list(text)
    rules, seen = [], set()
    for line in lines:
        for part in line.split(","):
            s = part.strip().replace("\\", "/")
            if not s or s.startswith("#"):
                continue
            display = s
            dir_only = s.endswith("/")
            s = s.strip("/")
            while s.startswith("./"):
                s = s[2:]
            if not s:
                continue
            key = (s.lower(), dir_only)
            if key in seen:
                continue
            seen.add(key)
            rules.append((s.lower(), dir_only, display))
    return rules


def effective_rules(cfg):
    """Regras marcadas na lista + regras digitadas à mão."""
    return parse_rules(list(cfg.get("excl_checked", [])) + cfg.get("rules_text", "").splitlines())


def match_rule(rules, name, rel, is_dir):
    """Retorna o texto da regra que casou (ou None)."""
    if not rules:
        return None
    nl, rl = name.lower(), rel.lower()
    for pat, dir_only, display in rules:
        if dir_only and not is_dir:
            continue
        if "/" in pat:
            if fnmatch.fnmatchcase(rl, pat):
                return display
        elif fnmatch.fnmatchcase(nl, pat):
            return display
    return None


# ----------------------------------------------------------------------------
# A) Varredura / TREE
# ----------------------------------------------------------------------------

class ScanResult:
    def __init__(self, root, rules):
        self.root = Path(root)
        self.rules = list(rules)
        self.entries = []        # um dict por arquivo/link, na ordem da TREE
        self.dirs = 0
        self.files = 0
        self.symlinks = 0
        self.errors = []         # (caminho_relativo, mensagem)
        self.excluded_dirs = []  # caminhos relativos de diretórios excluídos
        self.excluded_rules = {}  # rel -> regra que casou
        self.heavy = {}          # diretório volumoso detectado -> nº de arquivos dentro
        self.tree_text = ""
        self.when = datetime.now()


def _is_link(entry):
    try:
        if entry.is_symlink():
            return True
    except OSError:
        pass
    isj = getattr(os.path, "isjunction", None)  # Python 3.12+
    if isj:
        try:
            return bool(isj(entry.path))
        except OSError:
            return False
    return False


def scan_project(root, opts, self_path, cancel, progress=None, app_ask_heavy=None):
    """Percorre o projeto SEM seguir links e sem limites arbitrários."""
    root = Path(root)
    res = ScanResult(root, opts.rules)
    rules = res.rules
    self_norm = os.path.normcase(os.path.abspath(self_path)) if self_path else None
    visited = {os.path.normcase(os.path.realpath(str(root)))}
    lines = [f"{root.name or str(root)}/"]
    counter = [0]
    clock = [0.0]

    def list_dir(path):
        try:
            with os.scandir(longpath(path)) as it:
                return list(it), None
        except OSError as exc:
            return [], f"{exc.__class__.__name__}: {exc}"

    def fast_count(path, limit, current_count):
        try:
            with os.scandir(longpath(path)) as it:
                for e in it:
                    if cancel.is_set():
                        raise Cancelled()
                    if e.is_dir(follow_symlinks=False):
                        fast_count(e.path, limit, current_count)
                        if current_count[0] > limit: return
                    else:
                        current_count[0] += 1
                        if current_count[0] > limit: return
        except OSError:
            pass

    def walk(items, prefix, relparts, heavy):
        if cancel.is_set():
            raise Cancelled()
        classified = []
        for e in items:
            try:
                d = e.is_dir(follow_symlinks=False)
            except OSError:
                d = False
            classified.append((e, d))
        dirs = sorted([c for c in classified if c[1]], key=lambda c: (c[0].name.lower(), c[0].name))
        others = sorted([c for c in classified if not c[1]], key=lambda c: (c[0].name.lower(), c[0].name))
        ordered = dirs + others
        for i, (e, is_dir) in enumerate(ordered):
            last = i == len(ordered) - 1
            conn = "└── " if last else "├── "
            child_prefix = prefix + ("    " if last else "│   ")
            rel_parts = relparts + [e.name]
            rel = "/".join(rel_parts)
            full = e.path
            counter[0] += 1
            if progress and counter[0] % 200 == 0:
                now = time.time()
                if now - clock[0] > 0.1:
                    clock[0] = now
                    progress(counter[0], None, f"Varrendo... {counter[0]} itens")

            # ---- links simbólicos / junctions: nunca seguidos
            if _is_link(e):
                try:
                    target = os.readlink(full)
                except OSError:
                    target = "?"
                res.symlinks += 1
                tgt_dir = os.path.isdir(full)
                if tgt_dir:
                    lines.append(f"{prefix}{conn}{e.name}/ -> {target}  [LINK SIMBÓLICO PARA DIRETÓRIO — não percorrido]")
                else:
                    lines.append(f"{prefix}{conn}{e.name} -> {target}  [LINK SIMBÓLICO]")
                try:
                    size = e.stat(follow_symlinks=False).st_size
                except OSError:
                    size = None
                res.entries.append(dict(rel=rel, name=e.name, path=full, kind="symlink",
                                        status="link", size=size, target=target,
                                        target_is_dir=tgt_dir, heavy=heavy))
                continue

            rule = match_rule(rules, e.name, rel, is_dir)

            # ---- diretórios reais
            if is_dir:
                if rule:
                    lines.append(f"{prefix}{conn}{e.name}/  [EXCLUÍDO POR REGRA: {rule}]")
                    res.excluded_dirs.append(rel)
                    res.excluded_rules[rel] = rule
                    continue
                
                if opts.heavy_action != "read" and len(rel_parts) <= 3:
                    fc = [0]
                    fast_count(full, opts.heavy_limit, fc)
                    if fc[0] > opts.heavy_limit:
                        if opts.heavy_action == "ignore":
                            lines.append(f"{prefix}{conn}{e.name}/  [EXCLUÍDO AUTOMATICAMENTE: Pasta Massiva (> {opts.heavy_limit} arq)]")
                            res.excluded_dirs.append(rel)
                            res.excluded_rules[rel] = f"Pasta Massiva (> {opts.heavy_limit} arquivos)"
                            continue
                        elif opts.heavy_action == "ask" and app_ask_heavy:
                            ans = app_ask_heavy(rel, opts.heavy_limit)
                            if ans:
                                lines.append(f"{prefix}{conn}{e.name}/  [EXCLUÍDO PELO USUÁRIO: Pasta Massiva]")
                                res.excluded_dirs.append(rel)
                                res.excluded_rules[rel] = "Pasta Massiva (Escolha do Usuário)"
                                continue

                rp = os.path.normcase(os.path.realpath(full))
                if rp in visited:
                    lines.append(f"{prefix}{conn}{e.name}/  [JÁ VISITADO / CICLO — não percorrido]")
                    res.errors.append((rel, "diretório já visitado (ciclo ou duplicidade); não percorrido novamente"))
                    continue
                visited.add(rp)
                sub, err = list_dir(full)
                note = f"  [INACESSÍVEL: {err}]" if err else ""
                lines.append(f"{prefix}{conn}{e.name}/{note}")
                res.dirs += 1
                h = heavy
                if h is None and e.name.lower() in HEAVY_DIRS:
                    h = rel
                    res.heavy.setdefault(h, 0)
                if err:
                    res.errors.append((rel, "diretório inacessível: " + err))
                    continue
                walk(sub, child_prefix, rel_parts, h)
                continue

            # ---- arquivos
            size, err = None, None
            try:
                size = e.stat(follow_symlinks=False).st_size
            except OSError as exc:
                err = f"{exc.__class__.__name__}: {exc}"
                res.errors.append((rel, "não foi possível obter metadados: " + err))
            status, notes = "file", []
            if self_norm and os.path.normcase(os.path.abspath(full)) == self_norm:
                status = "self"
                notes.append("[ESTA FERRAMENTA]")
            elif OUTPUT_RE.match(e.name):
                status = "output"
                notes.append("[SAÍDA GERADA PELA FERRAMENTA]")
            elif rule:
                status = "excluded"
                notes.append(f"[EXCLUÍDO POR REGRA: {rule}]")
            if err:
                notes.append("[ERRO DE METADADOS]")
            lines.append(f"{prefix}{conn}{e.name}" + ("  " + " ".join(notes) if notes else ""))
            res.files += 1
            if heavy:
                res.heavy[heavy] = res.heavy.get(heavy, 0) + 1
            res.entries.append(dict(rel=rel, name=e.name, path=full, kind="file",
                                    status=status, size=size, heavy=heavy, rule=rule))

    items, err = list_dir(root)
    if err:
        res.errors.append((".", "raiz inacessível: " + err))
    walk(items, "", [], None)
    summary = f"{res.dirs} diretórios, {res.files} arquivos"
    if res.symlinks:
        summary += f", {res.symlinks} links simbólicos"
    lines.append("")
    lines.append(summary)
    res.tree_text = "\n".join(lines)
    return res


# ----------------------------------------------------------------------------
# B) Leitura segura de arquivos
# ----------------------------------------------------------------------------

def describe_binary(raw, name):
    head = raw[:64]
    for sig, desc in STRONG_SIGNATURES + WEAK_SIGNATURES:
        if head.startswith(sig):
            return desc
    ext = os.path.splitext(name)[1].lower()
    return BINARY_EXT.get(ext, "Binário não identificado")


def decode_bytes(raw, name=""):
    """Classifica e decodifica com segurança. Retorna dict:
       kind: 'text' | 'binary' | 'undecodable'; text; encoding; verified; note; type."""
    out = dict(kind="text", text="", encoding="vazio", verified=True, note="", type="")
    if not raw:
        return out
    try:  # BOMs primeiro (UTF-16/32 contêm bytes nulos)
        if raw.startswith(codecs.BOM_UTF32_LE) or raw.startswith(codecs.BOM_UTF32_BE):
            text = raw.decode("utf-32")
            le = raw.startswith(codecs.BOM_UTF32_LE)
            out.update(text=text, encoding="utf-32 (com BOM)",
                       verified=text.encode("utf-32-le" if le else "utf-32-be") == raw[4:])
            return out
        if raw.startswith(codecs.BOM_UTF16_LE) or raw.startswith(codecs.BOM_UTF16_BE):
            text = raw.decode("utf-16")
            le = raw.startswith(codecs.BOM_UTF16_LE)
            out.update(text=text, encoding="utf-16 (com BOM)",
                       verified=text.encode("utf-16-le" if le else "utf-16-be") == raw[2:])
            return out
    except UnicodeDecodeError:
        pass
    head = raw[:8192]
    for sig, desc in STRONG_SIGNATURES:
        if raw.startswith(sig):
            return dict(out, kind="binary", type=desc, note="assinatura de formato binário")
    if b"\x00" in head:
        return dict(out, kind="binary", type=describe_binary(raw, name), note="bytes nulos detectados")
    ctrl = sum(1 for b in head if b < 32 and b not in (9, 10, 12, 13, 27))
    if ctrl / max(1, len(head)) > 0.10:
        return dict(out, kind="binary", type=describe_binary(raw, name), note="alta proporção de bytes de controle")
    if raw.startswith(codecs.BOM_UTF8):
        try:
            text = raw[3:].decode("utf-8")
            out.update(text=text, encoding="utf-8 (com BOM)",
                       verified=(codecs.BOM_UTF8 + text.encode("utf-8")) == raw)
            return out
        except UnicodeDecodeError:
            pass
    try:
        text = raw.decode("utf-8")
        out.update(text=text, encoding="utf-8", verified=text.encode("utf-8") == raw)
        return out
    except UnicodeDecodeError:
        pass
    try:
        text = raw.decode("cp1252")
        out.update(text=text, encoding="cp1252 (heurística, não confirmada)",
                   verified=text.encode("cp1252") == raw,
                   note="não é UTF-8 válido; decodificado como Windows-1252")
        return out
    except UnicodeDecodeError:
        return dict(out, kind="undecodable",
                    note="não é UTF-8 válido nem Windows-1252; decodificar poderia corromper o conteúdo")


def block_for_text(rel, name, enc, raw, text, verified, note=""):
    """Retorna (bloco, offset_bytes_do_corpo, bytes_do_corpo, sha256)."""
    if text == "":
        flag = "vazio"
    else:
        flag = "sim" if text.endswith(("\n", "\r")) else "não"
    sha = hashlib.sha256(raw).hexdigest()
    meta = [
        f"CODIFICAÇÃO: {enc}",
        f"TAMANHO: {len(raw)} bytes",
        f"SHA256 (bytes originais): {sha}",
        f"TERMINA COM QUEBRA DE LINHA: {flag}",
    ]
    if not verified:
        meta.append("AVISO: verificação de reconstrução dos bytes FALHOU")
    if note:
        meta.append(f"OBSERVAÇÃO: {note}")
    head = f"{SEP}\nARQUIVO: {name}\nCAMINHO RELATIVO: {rel}\n" + "\n".join(meta) + f"\n{SEP}\n"
    body = text + ("\n" if flag == "não" else "")
    block = head + body + f"<<< FIM DO ARQUIVO: {rel} >>>\n\n"
    return block, len(head.encode("utf-8")), len(text.encode("utf-8")), sha


def block_for_meta(rel, name, size, tipo, reason, extra=None):
    ext = os.path.splitext(name)[1] or "(sem extensão)"
    meta = [
        "CONTEÚDO NÃO INCORPORADO: sim",
        f"EXTENSÃO: {ext}",
        f"TAMANHO: {size if size is not None else '?'} bytes",
        f"TIPO: {tipo}",
        f"MOTIVO: {reason}",
    ] + (extra or [])
    return (f"{SEP}\nARQUIVO: {name}\nCAMINHO RELATIVO: {rel}\n" + "\n".join(meta)
            + f"\n{SEP}\n<<< FIM DO ARQUIVO: {rel} >>>\n\n")


class ContentStore:
    """Guarda resultados em arquivo temporário (não em memória)."""

    def __init__(self):
        fd, self.path = tempfile.mkstemp(prefix="documentador_", suffix=".tmp")
        self._f = os.fdopen(fd, "wb")
        self.index = []
        self.total_bytes = 0
        self.total_chars = 0
        self._sha = hashlib.sha256()
        self.sha = None
        atexit.register(self.cleanup)

    def append(self, rel, label, text, meta=None):
        data = text.encode("utf-8")
        self.index.append(dict(rel=rel, label=label, offset=self.total_bytes,
                               nbytes=len(data), nchars=len(text), meta=meta or {}))
        self._f.write(data)
        self._sha.update(data)
        self.total_bytes += len(data)
        self.total_chars += len(text)

    def finish(self):
        self._f.close()
        self.sha = self._sha.hexdigest()

    def read_block(self, i):
        b = self.index[i]
        with open(self.path, "rb") as f:
            f.seek(b["offset"])
            return f.read(b["nbytes"]).decode("utf-8")

    def read_slice(self, i, off, n):
        b = self.index[i]
        with open(self.path, "rb") as f:
            f.seek(b["offset"] + off)
            return f.read(n).decode("utf-8")

    def read_all(self):
        with open(self.path, "rb") as f:
            return f.read().decode("utf-8")

    def read_preview(self, limit):
        parts, n = [], 0
        for i in range(len(self.index)):
            t = self.read_block(i)
            parts.append(t)
            n += len(t)
            if n >= limit:
                break
        return "".join(parts), n < self.total_chars

    def cleanup(self):
        try:
            if not self._f.closed:
                self._f.close()
        except Exception:
            pass
        try:
            if os.path.exists(self.path):
                os.remove(self.path)
        except OSError:
            pass


class Options:
    def __init__(self, rules=(), exclude_sensitive=False, ignore_self=False, max_bytes=0,
                 part_chars=0, workers=0, md_emoji=True, md_collapse=True, md_contents=True,
                 md_tree=True, md_stats=True, heavy_limit=1000, heavy_action="ask"):
        self.rules = list(rules)
        self.exclude_sensitive = exclude_sensitive
        self.ignore_self = ignore_self
        self.max_bytes = max_bytes
        self.part_chars = part_chars
        self.workers = workers
        self.md_emoji, self.md_collapse = md_emoji, md_collapse
        self.md_contents, self.md_tree, self.md_stats = md_contents, md_tree, md_stats
        self.heavy_limit = heavy_limit
        self.heavy_action = heavy_action

    @classmethod
    def from_cfg(cls, c):
        return cls(effective_rules(c), c["sens"], c["selfign"],
                   int(c["maxmb"] * 1024 * 1024), c["part"], c["workers"], c["md_emoji"],
                   c["md_collapse"], c["md_contents"], c["md_tree"], c["md_stats"],
                   c.get("heavy_limit", 1000), c.get("heavy_action", "ask"))


class Stats:
    def __init__(self):
        self.ok = []            # (rel, encoding)
        self.binary = []        # (rel, tipo, size)
        self.ignored = []       # (rel, motivo)
        self.excluded = []      # (rel, regra)
        self.errors = []        # (rel, motivo)
        self.nonutf8 = []
        self.unverified = []
        self.sensitive = []
        self.links = []
        self.langs = {}         # nome -> [arquivos, bytes, linhas, emoji]
        self.text_bytes = 0
        self.started = datetime.now()
        self.finished = None


def process_entry(rec, opts):
    """Trabalho puro (thread-safe) sobre UM arquivo. Retorna dict para o consolidador."""
    rel, name, size = rec["rel"], rec["name"], rec["size"]
    sens = is_sensitive(name)

    def meta(kind, label, tipo, reason, extra=None, sz=None):
        return dict(kind=kind, label=label, sens=sens, reason=reason, type=tipo,
                    size=size if sz is None else sz,
                    text=block_for_meta(rel, name, size if sz is None else sz, tipo, reason, extra),
                    meta=dict(kind=label, type=tipo, reason=reason, size=size if sz is None else sz))

    if rec["status"] == "output":
        return meta("ignored", "ignorado", "Saída da ferramenta",
                    "saída gerada pela própria ferramenta (evita contaminar execuções seguintes)")
    if rec["kind"] == "symlink":
        r = meta("link", "link", "Link simbólico", "link simbólico/junction não seguido (evita ciclos e duplicação)",
                 [f"DESTINO: {rec.get('target', '?')}"])
        r["target"] = rec.get("target", "?")
        return r
    if rec["status"] == "excluded":
        r = meta("excluded", "excluído", "Excluído por regra",
                 f"excluído por regra de exclusão: {rec.get('rule')}")
        r["rule"] = rec.get("rule")
        return r
    if sens and opts.exclude_sensitive:
        return meta("ignored", "ignorado", "Possivelmente sensível",
                    "arquivo potencialmente sensível excluído por configuração explícita")
    if rec["status"] == "self" and opts.ignore_self:
        return meta("ignored", "ignorado", "Script da ferramenta", "a própria ferramenta, ignorada por configuração")
    if opts.max_bytes and size is not None and size > opts.max_bytes:
        return meta("ignored", "ignorado", "Arquivo grande",
                    f"maior que o limite configurado ({human_size(opts.max_bytes)})")
    try:
        with open(longpath(rec["path"]), "rb") as f:
            raw = f.read()
    except OSError as exc:
        return meta("error", "erro", "Ilegível", f"erro de leitura ({exc.__class__.__name__}: {exc})")
    info = decode_bytes(raw, name)
    if info["kind"] == "text":
        text = info["text"]
        block, boff, blen, sha = block_for_text(rel, name, info["encoding"], raw, text, info["verified"], info["note"])
        lang = lang_of(name)
        lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
        return dict(kind="text", label="texto", sens=sens, text=block, size=len(raw),
                    enc=info["encoding"], verified=info["verified"], lang=lang, lines=lines,
                    meta=dict(kind="texto", size=len(raw), enc=info["encoding"], sha=sha,
                              body_off=boff, body_len=blen, lang=lang[1], fence=lang[0],
                              emoji=lang[2], lines=lines))
    if info["kind"] == "binary":
        return meta("binary", "binário", info["type"],
                    "arquivo binário — bytes não inseridos no documento (" + info["note"] + ")", sz=len(raw))
    return meta("error", "erro", "Texto não decodificável", info["note"], sz=len(raw))


def _absorb(store, stats, rec, r):
    rel, k = rec["rel"], r["kind"]
    if r["sens"]:
        stats.sensitive.append(rel)
    if k == "text":
        stats.ok.append((rel, r["enc"]))
        stats.text_bytes += r["size"]
        if not r["enc"].startswith(("utf-8", "vazio")):
            stats.nonutf8.append((rel, r["enc"]))
        if not r["verified"]:
            stats.unverified.append(rel)
        _, lname, emoji = r["lang"]
        cur = stats.langs.setdefault(lname, [0, 0, 0, emoji])
        cur[0] += 1
        cur[1] += r["size"]
        cur[2] += r["lines"]
    elif k == "binary":
        stats.binary.append((rel, r["type"], r["size"]))
    elif k == "ignored":
        stats.ignored.append((rel, r["reason"]))
    elif k == "excluded":
        stats.excluded.append((rel, r.get("rule")))
    elif k == "link":
        stats.links.append((rel, r["target"]))
    else:
        stats.errors.append((rel, r["reason"]))
    store.append(rel, r["label"], r["text"], meta=r["meta"])


def _batches(entries, max_count, max_bytes=64 * 1024 * 1024):
    batch, nbytes = [], 0
    for rec in entries:
        batch.append(rec)
        nbytes += rec["size"] or 0
        if len(batch) >= max_count or nbytes >= max_bytes:
            yield batch
            batch, nbytes = [], 0
    if batch:
        yield batch


def extract_contents(scan, opts, cancel, progress=None):
    """Lê, decodifica e hash dos arquivos em paralelo; a ordem do resultado é sempre a da TREE."""
    store, stats = ContentStore(), Stats()
    entries = scan.entries
    total = len(entries)
    workers = opts.workers or min(8, (os.cpu_count() or 2) * 2)
    done, last = 0, 0.0
    t0 = time.time()
    try:
        ex = ThreadPoolExecutor(max_workers=workers) if workers > 1 else None
        try:
            for batch in _batches(entries, max(16, workers * 8)):
                if cancel.is_set():
                    raise Cancelled()
                if ex:
                    results = list(ex.map(lambda r: process_entry(r, opts), batch))
                else:
                    results = [process_entry(r, opts) for r in batch]
                for rec, res in zip(batch, results):
                    _absorb(store, stats, rec, res)
                done += len(batch)
                now = time.time()
                if progress and (now - last > 0.1 or done == total):
                    rate = done / max(0.001, now - t0)
                    progress(done, total, f"Lendo arquivos {done}/{total}  ·  {rate:.0f} arq/s")
                    last = now
        finally:
            if ex:
                ex.shutdown(wait=True)
        store.finish()
    except BaseException:
        store.cleanup()
        raise
    stats.finished = datetime.now()
    return store, stats


# ----------------------------------------------------------------------------
# C) Relatório
# ----------------------------------------------------------------------------

def build_report(scan, stats, store, opts):
    L = []
    add = L.append
    add("RELATÓRIO DA EXTRAÇÃO")
    add("=" * 60)
    add(f"Raiz do projeto : {scan.root}")
    add(f"Ferramenta      : {SCRIPT_PATH.name} (v{APP_VERSION})")
    add(f"TREE gerada em  : {scan.when:%Y-%m-%d %H:%M:%S}")
    add(f"Conteúdo gerado : {stats.finished:%Y-%m-%d %H:%M:%S}")
    add("")
    add("CONFIGURAÇÃO UTILIZADA")
    add("-" * 60)
    add("Regras de exclusão            : " + (", ".join(r[2] for r in scan.rules) or "(nenhuma — varredura completa)"))
    add(f"Excluir arquivos sensíveis    : {'sim' if opts.exclude_sensitive else 'não'}")
    add(f"Ignorar a própria ferramenta  : {'sim' if opts.ignore_self else 'não'}")
    add("Limite por arquivo            : " + (human_size(opts.max_bytes) if opts.max_bytes else "(sem limite)"))
    add("")
    add("TOTAIS")
    add("-" * 60)
    add(f"Diretórios encontrados (percorridos)   : {scan.dirs}")
    add(f"Arquivos encontrados                   : {scan.files}")
    add(f"Links simbólicos/junctions             : {scan.symlinks}")
    add(f"Arquivos de texto extraídos            : {len(stats.ok)}")
    add(f"Arquivos binários identificados        : {len(stats.binary)}")
    add(f"Itens ignorados por configuração/regra : {len(stats.ignored)}")
    add(f"Arquivos excluídos por regra           : {len(stats.excluded)}")
    add(f"Arquivos com erro                      : {len(stats.errors)}")
    add(f"Diretórios excluídos da varredura      : {len(scan.excluded_dirs)}")
    add(f"Caminhos com problema na varredura     : {len(scan.errors)}")
    add(f"Tamanho do texto extraído (original)   : {human_size(stats.text_bytes)} ({stats.text_bytes} bytes)")
    add(f"Tamanho do resultado B (UTF-8)         : {human_size(store.total_bytes)} ({store.total_chars} caracteres)")
    add(f"SHA256 do resultado B                  : {store.sha}")
    add("")

    def section(title, rows, fmt):
        add(title)
        add("-" * 60)
        if rows:
            for r in rows:
                add("  " + fmt(r))
        else:
            add("  (nenhum)")
        add("")

    section("DIRETÓRIOS EXCLUÍDOS DA VARREDURA (visíveis e configuráveis)", scan.excluded_dirs,
            lambda r: f"{r}/  [regra: {scan.excluded_rules.get(r)}]")
    section("ARQUIVOS EXCLUÍDOS POR REGRA", stats.excluded, lambda r: f"{r[0]}  [regra: {r[1]}]")
    heavy = [(k, v) for k, v in sorted(scan.heavy.items())]
    section("DIRETÓRIOS VOLUMOSOS PRESENTES NA EXTRAÇÃO (considere excluí-los se não forem relevantes)",
            heavy, lambda r: f"{r[0]}/  ({r[1]} arquivos dentro)")
    section("PROBLEMAS NA VARREDURA (caminhos não inspecionados)", scan.errors, lambda r: f"{r[0]}: {r[1]}")
    section("ERROS NA EXTRAÇÃO DE CONTEÚDO", stats.errors, lambda r: f"{r[0]}: {r[1]}")
    section("ARQUIVOS POTENCIALMENTE SENSÍVEIS ENCONTRADOS", stats.sensitive,
            lambda r: r + ("  [conteúdo EXCLUÍDO]" if opts.exclude_sensitive else "  [conteúdo INCLUÍDO — revise antes de compartilhar]"))
    section("ARQUIVOS BINÁRIOS (apenas metadados)", stats.binary,
            lambda r: f"{r[0]}  |  {r[1]}  |  {human_size(r[2])}")
    section("ITENS IGNORADOS", stats.ignored, lambda r: f"{r[0]}: {r[1]}")
    section("LINKS SIMBÓLICOS (não seguidos)", stats.links, lambda r: f"{r[0]} -> {r[1]}")
    section("ARQUIVOS DE TEXTO EM CODIFICAÇÃO DIFERENTE DE UTF-8", stats.nonutf8, lambda r: f"{r[0]}: {r[1]}")
    section("ARQUIVOS CUJA VERIFICAÇÃO DE RECONSTRUÇÃO FALHOU", stats.unverified, str)
    problems = bool(scan.errors or stats.errors or stats.unverified)
    add("CONCLUSÃO")
    add("-" * 60)
    add("Extração COM RESSALVAS: há caminhos com erro; o inventário não é 100% integral."
        if problems else "Extração concluída sem erros de leitura.")
    if scan.excluded_dirs or stats.excluded or opts.exclude_sensitive or stats.ignored:
        add("Atenção: há exclusões/ignorados configurados; o inventário reflete essas escolhas.")
    return "\n".join(L) + "\n"


# ----------------------------------------------------------------------------
# D) Exportação dividida e remontagem
# ----------------------------------------------------------------------------

def plan_parts(index, limit):
    """Divide em partes preferencialmente entre arquivos. Um bloco maior que o
    limite é fatiado em segmentos (cada um em sua própria parte)."""
    parts, cur, cur_len = [], [], 0
    for i, b in enumerate(index):
        n = b["nchars"]
        if n > limit:
            if cur:
                parts.append(cur)
                cur, cur_len = [], 0
            m = -(-n // limit)
            for k in range(m):
                parts.append([(i, k * limit, min(n, (k + 1) * limit), k + 1, m)])
            continue
        if cur and cur_len + n > limit:
            parts.append(cur)
            cur, cur_len = [], 0
        cur.append((i, 0, n, 1, 1))
        cur_len += n
    if cur:
        parts.append(cur)
    return parts


def piece_text(store, piece):
    i, s, e, k, m = piece
    rel = store.index[i]["rel"]
    text = store.read_block(i)
    if m > 1:
        text = text[s:e]
    if k > 1:
        text = f"<<<CONTINUACAO_SEGMENTO {k}/{m}: {rel}>>>\n" + text
    if k < m:
        text = text + f"\n<<<FIM_SEGMENTO {k}/{m}: {rel}>>>\n"
    return text


MIOLO_BEGIN = "#### INÍCIO DO MIOLO ####\n"
MIOLO_END = "\n#### FIM DO MIOLO ####"


def write_store_file(store, path):
    """Grava o store inteiro em um único arquivo (atômico)."""
    with AtomicWriter(path) as f:
        for i in range(len(store.index)):
            f.write(store.read_block(i))
    return Path(path).stat().st_size


def write_content_files(store, directory, base="CONTEUDO_PROJETO", part_chars=0, progress=None, ext=".txt"):
    """Escreve o resultado B. Retorna lista de (caminho, bytes)."""
    directory = Path(directory)
    written = []
    if part_chars <= 0:
        path = directory / f"{base}{ext}"  # <-- ALTERADO
        written.append((path, write_store_file(store, path)))
        return written
    parts = plan_parts(store.index, part_chars)
    n = len(parts)
    for pi, pieces in enumerate(parts, 1):
        path = directory / f"{base}_PARTE_{pi:03d}{ext}"  # <-- ALTERADO
        header = (f"#### DOCUMENTADOR | {base} | PARTE {pi:03d} DE {n:03d} ####\n"
                  f"#### SHA256 DO CONTEUDO COMPLETO: {store.sha} | PARTES: {n} ####\n"
                  + MIOLO_BEGIN)
        with AtomicWriter(path) as f:
            f.write(header)
            for pc in pieces:
                f.write(piece_text(store, pc))
            f.write(MIOLO_END + "\n")
        written.append((path, path.stat().st_size))
        if progress:
            progress(pi, n, f"Parte {pi}/{n} gravada")
    return written


def remount_parts(paths):
    """Remonta partes em ordem. Retorna (texto, sha_confere, mensagem)."""
    found = {}
    total = sha = None
    for p in paths:
        with open(p, "rb") as f:
            text = f.read().decode("utf-8")
        m = re.match(r"#### DOCUMENTADOR \| .*? \| PARTE (\d+) DE (\d+) ####\n"
                     r"#### SHA256 DO CONTEUDO COMPLETO: ([0-9a-f]{64}) \| PARTES: (\d+) ####\n", text)
        if not m:
            raise ValueError(f"Cabeçalho de parte inválido em {p}")
        num, tot, h = int(m.group(1)), int(m.group(2)), m.group(3)
        if total is None:
            total, sha = tot, h
        elif (tot, h) != (total, sha):
            raise ValueError("As partes pertencem a extrações diferentes.")
        s = text.index(MIOLO_BEGIN) + len(MIOLO_BEGIN)
        e = text.rindex(MIOLO_END)
        found[num] = text[s:e]
    missing = [i for i in range(1, (total or 0) + 1) if i not in found]
    if missing:
        raise ValueError("Partes ausentes: " + ", ".join(f"{i:03d}" for i in missing))
    joined = "".join(found[i] for i in sorted(found))
    joined = re.sub(r"\n<<<FIM_SEGMENTO [^\n]*>>>\n<<<CONTINUACAO_SEGMENTO [^\n]*>>>\n", "", joined)
    ok = hashlib.sha256(joined.encode("utf-8")).hexdigest() == sha
    return joined, ok, f"{total} partes remontadas; SHA256 {'confere' if ok else 'NÃO confere'}"


# ----------------------------------------------------------------------------
# E) Prompt padrão para IA (texto estático; os dados vão em seções delimitadas)
# ----------------------------------------------------------------------------

SEC_BEGIN = "##### INÍCIO: "
SEC_END = "##### FIM: "
SEC_TREE = "TREE DO PROJETO"
SEC_REPORT = "RELATÓRIO DA EXTRAÇÃO"
SEC_CONTENT = "CONTEÚDO INTEGRAL DOS ARQUIVOS"
SEC_PREV = "DOCUMENTAÇÃO ANTERIOR (DOCUMENTACAO.md)"
SEC_MANIFEST = "MANIFESTO DO PACOTE"


def build_prompt(mode="DOC"):
    """Prompt padrão em português com opções DOC ou COD."""
    if mode == "COD":
        return f'''# TAREFA: Assumir o contexto do projeto para edições e implementações futuras

Você é um engenheiro de software sênior e meu assistente de programação. Abaixo, forneço a árvore (TREE) e os códigos atualizados de cada arquivo do meu projeto. 
Sua tarefa agora é ler e gravar na sua memória temporária como o projeto funciona, suas hierarquias e seus requirements. A partir deste pacote, você terá consciência total do estado atual do projeto.

## COMO OS DADOS CHEGAM

Os dados vêm em seções delimitadas por `{SEC_BEGIN}NOME DA SEÇÃO #####` e `{SEC_END}NOME DA SEÇÃO #####`. 
Você receberá {SEC_MANIFEST}, {SEC_TREE}, {SEC_REPORT} e {SEC_CONTENT}. O arquivo mandado é o documento e a base definitiva.

## DIRETRIZES DE RESPOSTA (REGRA DE OURO)

1. **A Base Definitiva**: Ignore memórias de outros chats. Cada pergunta e cada resposta daqui pra frente deve ser rigorosamente baseada no código enviado aqui.
2. **Fidelidade Total**: Mantenha sempre a fidelidade do código. Você deve ler e considerar TODO o código fornecido. O código que você ler deve ser exato e rigorosamente o mesmo.
3. **Criação de Arquivos**: Caso precise criar um arquivo, me fale o caminho exato da TREE onde vou criar ele.
4. **Edição de Arquivos**: Caso for editar, me fale o caminho e o nome do arquivo que vou editar.
5. **Máxima Facilidade de Cópia e Cola (Ctrl+F)**:
   - Quando disser para eu procurar um trecho de código, seja extremamente exato. Mostre claramente como o bloco "está hoje" e como "deve ficar".
   - **MUITO IMPORTANTE**: O bloco de busca do código atual deve ser feito exclusivamente para eu copiar e colar direto no `Ctrl+F` do VS Code. 
   - **NÃO COLOQUE** textos ou comentários inventados que dificultem isso (por exemplo, não coloque `// edite isso` ou `// resto do código` dentro do trecho original), pois se você adicionar isso, quando eu pesquisar no VS Code ele não vai achar. Seja conciso.

## ENTREGA

Não gere nenhuma documentação agora. Responda apenas confirmando que você leu o código, entendeu a estrutura e está pronto para receber minha primeira solicitação de edição ou implementação.
'''

    # O fallback é o modo DOC original
    return f'''# TAREFA: criar ou atualizar o arquivo DOCUMENTACAO.md de um projeto de software

Você é um engenheiro de software e redator técnico. Vou fornecer o inventário de um projeto: a TREE da estrutura, o conteúdo integral dos arquivos, o relatório da extração e, quando existir, a documentação anterior. Sua tarefa é produzir o arquivo `DOCUMENTACAO.md` COMPLETO e ATUALIZADO.

O projeto pode estar em qualquer linguagem (Python, PHP, JavaScript, Java, C#, C, C++, web, automações, desktop etc.). Não presuma linguagem, framework ou estrutura: descubra-os pelas evidências.

## COMO OS DADOS CHEGAM

Os dados vêm em seções delimitadas por linhas como `{SEC_BEGIN}NOME DA SEÇÃO #####` e `{SEC_END}NOME DA SEÇÃO #####`, neste pacote ou em mensagens seguintes (possivelmente em partes numeradas; aguarde todas antes de responder). Seções possíveis: {SEC_MANIFEST}, {SEC_TREE}, {SEC_REPORT}, {SEC_CONTENT} e {SEC_PREV}. Leia primeiro o {SEC_MANIFEST}, se existir: ele informa o que foi incluído e se a extração é completa ou PARCIAL.

## CENÁRIO A — não há seção "{SEC_PREV}"

Baseie-se EXCLUSIVAMENTE nas informações fornecidas e produza documentação técnica completa, incluindo, quando houver evidência:
- Visão geral do projeto.
- Estrutura completa de diretórios e arquivos.
- Responsabilidade de cada módulo, arquivo e componente.
- Tecnologias, linguagens e dependências detectadas.
- Arquitetura e relações entre componentes (somente as comprovadas pelo código).
- Fluxos de execução e funcionamento identificáveis.
- Configurações e variáveis de ambiente relevantes.
- Instruções de instalação e execução (somente se sustentadas pelos arquivos).
- Endpoints, interfaces, rotas e integrações, se existirem.
- Banco de dados e estruturas de persistência, se identificáveis.
- Limitações, problemas observados e informações que não puderam ser confirmadas.
- A TREE completa e o conteúdo integral de todos os arquivos de texto extraídos.

## CENÁRIO B — há seção "{SEC_PREV}"

Compare a documentação anterior com o estado atual do projeto e identifique, quando possível: arquivos novos; arquivos removidos; arquivos renomeados ou movidos (quando a relação puder ser inferida); alterações de conteúdo; mudanças na estrutura de diretórios; funcionalidades adicionadas ou removidas; informações desatualizadas; mudanças de dependências, configurações e arquitetura.

A documentação anterior é referência HISTÓRICA, não fonte de verdade quando contradiz o código atual. Preserve informações úteis que não podem ser recuperadas do código (decisões arquiteturais, contexto de negócio, procedimentos manuais) enquanto continuarem válidas. Se houver contradições, SINALIZE-AS em vez de inventar uma resolução.

## REGRAS OBRIGATÓRIAS

1. **Não invente** comportamentos, funcionalidades, dependências, comandos ou instruções de execução. Sem evidência suficiente, registre a incerteza explicitamente.
2. **Retorne o `DOCUMENTACAO.md` COMPLETO e atualizado**, nunca apenas uma lista de alterações ou um resumo das diferenças. O arquivo final deve ser autossuficiente.
3. O arquivo final deve conter, separados claramente: (a) a documentação técnica explicativa; (b) a TREE integral, exatamente como extraída; (c) o conteúdo INTEGRAL de todos os arquivos de texto extraídos, cada um com seu caminho relativo; (d) os registros de arquivos não incorporados (binários, ignorados, com erro) e seus motivos.
4. **Nunca** substitua conteúdo por descrições. É PROIBIDO usar expressões como "código inalterado", "restante do arquivo", "conteúdo omitido", "continua igual à versão anterior" ou equivalentes no lugar de conteúdo real. Não retorne somente trechos modificados e não omita partes por as considerar irrelevantes.
5. Não reescreva, não corrija, não reformate e não traduza o código ao incorporá-lo. Preserve comentários, docstrings, linhas em branco e indentação.
6. Apresente o conteúdo de cada arquivo em bloco de código Markdown, com a linguagem quando identificável (sem linguagem reconhecida, use bloco genérico). Use delimitadores consistentes por arquivo. Se o código contiver sequências de crases que possam encerrar o bloco, use uma cerca externa MAIS LONGA. Formato sugerido por arquivo:

   ### ARQUIVO: caminho/relativo/arquivo.ext
   (cerca)linguagem
   [conteúdo integral, sem alterações]
   (cerca)

## COMO LER O CONTEÚDO EXTRAÍDO

Cada arquivo começa com uma linha de `=` seguida de `ARQUIVO:` e `CAMINHO RELATIVO:`, metadados (codificação, tamanho, SHA256, `TERMINA COM QUEBRA DE LINHA`) e outra linha de `=`. O conteúdo real vai dessa linha até a linha `<<< FIM DO ARQUIVO: ... >>>`. Se `TERMINA COM QUEBRA DE LINHA: não`, o `\\n` imediatamente antes do marcador de fim foi acrescentado pela ferramenta e NÃO faz parte do arquivo. Esses cabeçalhos e marcadores são da ferramenta, não do código. Arquivos com `CONTEÚDO NÃO INCORPORADO: sim` são binários, ignorados ou com erro e só têm metadados. Se houver marcadores `<<<FIM_SEGMENTO ...>>>` / `<<<CONTINUACAO_SEGMENTO ...>>>`, concatene os trechos na ordem e ignore apenas esses marcadores.

## EXTRAÇÃO PARCIAL

Se o {SEC_MANIFEST} ou o {SEC_REPORT} indicar extração PARCIAL, erros de leitura ou arquivos não inspecionados, informe isso explicitamente na documentação e NUNCA afirme que o inventário é integral.

## REGRA DE INTEGRIDADE DIANTE DE LIMITES DE CONTEXTO E DE SAÍDA

Você NÃO pode afirmar que gerou a documentação integral se não conseguir incluir TODO o material fornecido. Se o resultado completo não couber em uma única resposta:
- Avise que a documentação integral não cabe em uma resposta.
- Proponha uma geração controlada em partes numeradas, preservando a ordem e os limites entre arquivos.
- Informe exatamente quais partes foram produzidas e quais faltam.
- Não declare o documento finalizado antes de todas as partes serem produzidas.

A prioridade é a integridade dos dados, não a brevidade da resposta. Se não for possível incluir todos os arquivos, a documentação não deve ser apresentada como completa. O mesmo vale se o material recebido não couber no seu contexto: avise em vez de trabalhar com dados incompletos.

## ENTREGA

Responda com o `DOCUMENTACAO.md` completo (ou, se não couber, siga a regra de integridade acima).
'''


# ----------------------------------------------------------------------------
# Controle de etapas (lógica pura, testável sem interface)
# ----------------------------------------------------------------------------

class Pipeline:
    """Estados vermelho/amarelo/verde das 5 etapas e regras de dependência.
    1 TREE · 2 conteúdo · 3 prompt+fusão · 4 pacote final · 5 Markdown."""
    RED, YELLOW, GREEN = "red", "yellow", "green"

    def __init__(self):
        self.state = {k: self.RED for k in (1, 2, 3, 4, 5)}
        self.fusion_ready = False

    def green(self, *stages):
        return all(self.state[s] == self.GREEN for s in stages)

    def invalidate_from(self, n):
        """Volta a vermelho a etapa n e as posteriores (o Markdown cai junto se n <= 2)."""
        changed = []
        for k in range(n, 5):
            if self.state[k] != self.RED:
                changed.append(k)
                self.state[k] = self.RED
        if n <= 2 and self.state[5] != self.RED:
            changed.append(5)
            self.state[5] = self.RED
        if n <= 3:
            self.fusion_ready = False
        return changed

    def allowed(self, prev_attached=False):
        g = self.green
        return {
            "tree": True,
            "copy_tree": g(1), "save_tree": g(1),
            "content": g(1),
            "copy_content": g(2), "save_content": g(2),
            "copy_report": g(2), "save_report": g(2),
            "prompt": g(1, 2),
            "copy_prompt": g(3), "save_prompt": g(3),
            "fuse": g(1, 2, 3),
            "copy_pkg": self.fusion_ready, "save_pkg": self.fusion_ready,
            "attach": True, "detach": prev_attached,
            "final": g(1, 2, 3),
            "copy_final": g(4), "save_final": g(4),
            "md": g(1, 2), "copy_md": g(5), "save_md": g(5),
            "run_all": True, "options": True, "remount": True,
        }


# ----------------------------------------------------------------------------
# Pacotes de contexto (fusão 1+2+3 e união final)
# ----------------------------------------------------------------------------

def build_package(kind, scan, store, stats, report, prompt, prev, partial_notes,
                  cancel, progress=None):
    """Monta o pacote como um ContentStore (arquivo temporário), para permitir
    cópia, exportação e divisão em partes sem truncar nada.
    kind: 'fusao' (etapas 1+2+3) ou 'final' (inclui documentação anterior, se houver).
    prev: dict(name, path, text, size, sha) ou None."""
    pkg = ContentStore()
    try:
        def add(label, text):
            pkg.append(label, "pacote", text)

        def begin(title):
            add(f"[{title}]", f"{SEC_BEGIN}{title} #####\n")

        def end(title):
            add(f"[/{title}]", f"{SEC_END}{title} #####\n\n")

        tree_sha = hashlib.sha256(scan.tree_text.encode("utf-8")).hexdigest()
        if kind == "fusao":
            prev_line = "NÃO INCLUÍDA (pacote da fusão das etapas 1, 2 e 3, sem documentação anterior)."
            scen = "Cenário A (não há seção de documentação anterior)."
        elif prev:
            prev_line = (f"INCLUÍDA integralmente: {prev['name']} ({prev['size']} bytes, "
                         f"SHA256 {prev['sha']}).")
            scen = "Cenário B (atualizar a documentação anterior)."
        else:
            prev_line = "NÃO ANEXADA — o usuário confirmou que deseja criar a documentação inicial."
            scen = "Cenário A (criar documentação inicial)."
        integrity = "COMPLETA" if not partial_notes else "PARCIAL — " + "; ".join(partial_notes)

        add("[PROMPT]", prompt.rstrip("\n") + "\n\n")
        manifest = [
            f"Gerado em: {datetime.now():%Y-%m-%d %H:%M:%S}",
            f"Raiz do projeto: {scan.root}",
            f"Tipo de pacote: {'fusão das etapas 1, 2 e 3' if kind == 'fusao' else 'união final (etapas 1 a 4)'}",
            f"Cenário aplicável: {scen}",
            f"Integridade da extração: {integrity}",
            "Regras de exclusão: " + (", ".join(r[2] for r in scan.rules) or "(nenhuma)"),
            f"Diretórios: {scan.dirs} | Arquivos: {scan.files} | Links: {scan.symlinks}",
            f"Arquivos de texto incluídos: {len(stats.ok)} | Binários (metadados): {len(stats.binary)} | "
            f"Ignorados: {len(stats.ignored)} | Excluídos por regra: {len(stats.excluded)} | Com erro: {len(stats.errors)}",
            f"SHA256 da TREE: {tree_sha}",
            f"SHA256 do conteúdo extraído: {store.sha}",
            f"Documentação anterior: {prev_line}",
            f"Seções: {SEC_TREE}; {SEC_REPORT}; {SEC_CONTENT}" + (f"; {SEC_PREV}" if (kind == 'final' and prev) else ""),
            "Observação: este pacote apenas reúne dados e instruções; nenhuma IA foi executada e nenhuma documentação foi gerada por esta ferramenta.",
        ]
        begin(SEC_MANIFEST)
        add("[MANIFESTO]", "\n".join(manifest) + "\n")
        end(SEC_MANIFEST)

        begin(SEC_TREE)
        add("[TREE]", scan.tree_text + "\n")
        end(SEC_TREE)

        begin(SEC_REPORT)
        add("[RELATÓRIO]", report if report.endswith("\n") else report + "\n")
        end(SEC_REPORT)

        begin(SEC_CONTENT)
        total = len(store.index)
        for i, b in enumerate(store.index):
            if cancel.is_set():
                raise Cancelled()
            pkg.append(b["rel"], "conteúdo", store.read_block(i))
            if progress and (i % 25 == 0 or i == total - 1):
                progress(i + 1, total, f"Montando pacote {i + 1}/{total}")
        end(SEC_CONTENT)

        if kind == "final" and prev:
            begin(SEC_PREV)
            text = prev["text"]
            add("[DOC ANTERIOR]", text if text.endswith("\n") else text + "\n")
            end(SEC_PREV)
        pkg.finish()
    except BaseException:
        pkg.cleanup()
        raise
    return pkg


def read_previous_doc(path):
    """Lê a documentação anterior sem modificá-la. Lança ValueError/OSError."""
    raw = Path(path).read_bytes()
    info = decode_bytes(raw, Path(path).name)
    if info["kind"] != "text":
        raise ValueError("O arquivo não é texto legível (" + (info["note"] or info["kind"]) + ").")
    return dict(name=Path(path).name, path=str(path), text=info["text"], size=len(raw),
                sha=hashlib.sha256(raw).hexdigest(), encoding=info["encoding"])


# ----------------------------------------------------------------------------
# F) Gerador de Markdown final (local, sem IA) — bonito, com emojis e tabelas
# ----------------------------------------------------------------------------

def build_markdown(scan, store, stats, opts, prev, partial, cancel, progress=None):
    """Gera DOCUMENTACAO_PROJETO.md como um ContentStore. Inventário estruturado do projeto:
    resumo, tecnologias, métricas por linguagem, TREE, índice, conteúdo integral (blocos
    recolhíveis), itens não incorporados, alertas de sensíveis e integridade."""
    md = ContentStore()
    emo = opts.md_emoji

    def E(x):
        return x + " " if emo else ""

    def cell(s):
        return str(s).replace("|", "\\|").replace("\n", " ")

    def code(s):
        return "`" + str(s).replace("`", "'") + "`"

    def add(t):
        md.append("md", "md", t)

    try:
        name = scan.root.name or str(scan.root)
        now = datetime.now()
        parcial = bool(partial)
        total_lines = sum(v[2] for v in stats.langs.values())
        sections = [("resumo", "Resumo executivo", "📋"), ("tech", "Tecnologias detectadas", "🧰")]
        if opts.md_stats:
            sections.append(("langs", "Linguagens e métricas", "📊"))
        if opts.md_tree:
            sections.append(("tree", "Estrutura do projeto", "🌳"))
        sections.append(("index", "Índice de arquivos", "🗂️"))
        if opts.md_contents:
            sections.append(("content", "Conteúdo dos arquivos", "📄"))
        sections.append(("noinc", "Itens não incorporados", "🚫"))
        if stats.sensitive:
            sections.append(("sens", "Arquivos sensíveis", "🔐"))
        sections.append(("integ", "Integridade da extração", "✅"))
        if prev:
            sections.append(("prev", "Documentação anterior", "🕰️"))
        meta_of = {k: (t, e) for k, t, e in sections}

        def head(key):
            t, e = meta_of[key]
            return f'<a id="sec-{key}"></a>\n\n## {E(e)}{t}\n\n'

        # ---- cabeçalho
        add(f"# {E('📚')}{name}\n\n")
        add(f"> {E('🏷️')}**Inventário técnico do projeto**, gerado automaticamente em "
            f"{now:%d/%m/%Y às %H:%M} por *{SCRIPT_PATH.name}* v{APP_VERSION}. "
            f"Este arquivo é um retrato fiel dos arquivos analisados (sem interpretação por IA).\n>\n")
        status = ("⚠️ PARCIAL — " + "; ".join(partial)) if parcial else "✅ completa"
        if not emo:
            status = ("PARCIAL — " + "; ".join(partial)) if parcial else "completa"
        add(f"> {E('🛡️')}**Integridade da extração:** {status}\n\n")
        add(f"## {E('🧭')}Sumário\n\n")
        for k, t, e in sections:
            add(f"- [{E(e)}{t}](#sec-{k})\n")
        add("\n---\n\n")

        # ---- resumo
        add(head("resumo"))
        add("| Item | Valor |\n|---|---|\n")

        def row(emoji, label, value):
            add(f"| {E(emoji)}{label} | {value} |\n")
        row("📂", "Raiz", code(scan.root))
        row("🕒", "Gerado em", f"{now:%Y-%m-%d %H:%M:%S}")
        row("📁", "Diretórios", scan.dirs)
        row("📄", "Arquivos encontrados", scan.files)
        row("📝", "Arquivos de texto incorporados", len(stats.ok))
        row("🧮", "Linhas de texto", f"{total_lines:,}".replace(",", "."))
        row("🖼️", "Binários (somente metadados)", len(stats.binary))
        row("⏭️", "Ignorados", len(stats.ignored))
        row("🚫", "Excluídos por regra", len(stats.excluded) + len(scan.excluded_dirs))
        row("🔗", "Links simbólicos", scan.symlinks)
        row("❌", "Erros", len(stats.errors) + len(scan.errors))
        row("💾", "Tamanho do texto", human_size(stats.text_bytes))
        row("🔑", "SHA256 do conteúdo", code(store.sha))
        add("\n")

        # ---- tecnologias
        add(head("tech"))
        techs = {}
        for rec in scan.entries:
            low = rec["name"].lower()
            t = TECH_MARKERS.get(low) or TECH_EXT.get(os.path.splitext(low)[1])
            if t is None and rec["rel"].lower().startswith(".github/workflows/"):
                t = "🤖 GitHub Actions"
            if t:
                techs.setdefault(t, []).append(rec["rel"])
        if techs:
            add("| Tecnologia | Evidência |\n|---|---|\n")
            for t, rels in sorted(techs.items()):
                ev = ", ".join(code(r) for r in rels[:3]) + (f" (+{len(rels) - 3})" if len(rels) > 3 else "")
                tt = t if emo else t.split(" ", 1)[1]
                add(f"| {tt} | {ev} |\n")
        else:
            add("_Nenhum marcador de tecnologia conhecido foi detectado._\n")
        add("\n")

        # ---- linguagens
        if opts.md_stats:
            add(head("langs"))
            if stats.langs:
                tot = max(1, sum(v[1] for v in stats.langs.values()))
                add("| Linguagem | Arquivos | Linhas | Tamanho | Participação |\n|---|---:|---:|---:|---|\n")
                for lname, (nf, nb, nl, em) in sorted(stats.langs.items(), key=lambda kv: -kv[1][1]):
                    pct = nb * 100 / tot
                    filled = int(round(pct / 5))
                    bar = "█" * filled + "░" * (20 - filled)
                    add(f"| {E(em)}{lname} | {nf} | {nl} | {human_size(nb)} | `{bar}` {pct:.1f}% |\n")
            else:
                add("_Nenhum arquivo de texto incorporado._\n")
            add("\n")

        # ---- tree
        if opts.md_tree:
            add(head("tree"))
            fc = fence_for(scan.tree_text)
            add(f"{fc}text\n{scan.tree_text}\n{fc}\n\n")

        # ---- índice
        add(head("index"))
        add("| # | Tipo | Arquivo | Linguagem | Tamanho | Linhas | Situação |\n|--:|:-:|---|---|--:|--:|---|\n")
        sit_emo = {"texto": "✅ Incluído", "binário": "🖼️ Binário", "ignorado": "⏭️ Ignorado",
                   "excluído": "🚫 Excluído", "link": "🔗 Link", "erro": "❌ Erro"}
        sit_txt = {"texto": "Incluído", "binário": "Binário", "ignorado": "Ignorado",
                   "excluído": "Excluído", "link": "Link", "erro": "Erro"}
        for i, b in enumerate(store.index):
            m = b["meta"]
            label = b["label"]
            if label == "texto":
                icon, lang, lines = m.get("emoji", "📄"), m.get("lang", "-"), m.get("lines", 0)
            else:
                icon = {"binário": "🖼️", "ignorado": "⏭️", "excluído": "🚫", "link": "🔗", "erro": "❌"}.get(label, "📄")
                lang, lines = m.get("type", "-"), "-"
            size = human_size(m.get("size")) if m.get("size") is not None else "?"
            if opts.md_contents and label == "texto":
                fcell = f"[{code(b['rel'])}](#f-{i})"
            else:
                fcell = code(b["rel"])
            sit = (sit_emo if emo else sit_txt).get(label, label)
            add(f"| {i + 1} | {icon if emo else ''} | {fcell} | {cell(lang)} | {size} | {lines} | {sit} |\n")
        add("\n")

        # ---- conteúdo
        if opts.md_contents:
            add(head("content"))
            total = len(store.index)
            for i, b in enumerate(store.index):
                if cancel.is_set():
                    raise Cancelled()
                if progress and (i % 20 == 0 or i == total - 1):
                    progress(i + 1, total, f"Gerando Markdown {i + 1}/{total}")
                if b["label"] != "texto":
                    continue
                m = b["meta"]
                body = store.read_slice(i, m["body_off"], m["body_len"])
                info = f"{m['lang']} · {human_size(m['size'])} · {m['lines']} linhas · {m['enc']}"
                title = html.escape(b["rel"])
                if opts.md_collapse:
                    add(f'<a id="f-{i}"></a>\n<details>\n<summary>{E(m["emoji"])}<b>{title}</b> — {html.escape(info)}</summary>\n\n')
                else:
                    add(f'<a id="f-{i}"></a>\n\n### {E(m["emoji"])}{title}\n\n_{info}_\n\n')
                if body == "":
                    add("_(arquivo vazio)_\n")
                else:
                    fc = fence_for(body)
                    add(f"{fc}{m['fence']}\n{body}{'' if body.endswith(chr(10)) else chr(10)}{fc}\n")
                add("\n</details>\n\n" if opts.md_collapse else "\n")

        # ---- não incorporados
        add(head("noinc"))
        add(f"### {E('🖼️')}Binários ({len(stats.binary)})\n\n")
        if stats.binary:
            add("| Arquivo | Tipo | Tamanho |\n|---|---|--:|\n")
            for rel, tipo, size in stats.binary:
                add(f"| {code(rel)} | {cell(tipo)} | {human_size(size)} |\n")
        else:
            add("_Nenhum._\n")
        add(f"\n### {E('🚫')}Excluídos por regra ({len(stats.excluded) + len(scan.excluded_dirs)})\n\n")
        excl = [(r + "/", scan.excluded_rules.get(r)) for r in scan.excluded_dirs] + list(stats.excluded)
        if excl:
            add("| Caminho | Regra |\n|---|---|\n")
            for rel, rule in excl:
                add(f"| {code(rel)} | {code(rule)} |\n")
        else:
            add("_Nenhum._\n")
        add(f"\n### {E('⏭️')}Ignorados ({len(stats.ignored)})\n\n")
        if stats.ignored:
            add("| Arquivo | Motivo |\n|---|---|\n")
            for rel, reason in stats.ignored:
                add(f"| {code(rel)} | {cell(reason)} |\n")
        else:
            add("_Nenhum._\n")
        add(f"\n### {E('🔗')}Links simbólicos ({len(stats.links)})\n\n")
        if stats.links:
            for rel, tgt in stats.links:
                add(f"- {code(rel)} → {code(tgt)}\n")
        else:
            add("_Nenhum._\n")
        add(f"\n### {E('❌')}Erros ({len(stats.errors) + len(scan.errors)})\n\n")
        errs = list(scan.errors) + list(stats.errors)
        if errs:
            for rel, reason in errs:
                add(f"- {code(rel)}: {reason}\n")
        else:
            add("_Nenhum._\n")
        add("\n")

        # ---- sensíveis
        if stats.sensitive:
            add(head("sens"))
            incl = not opts.exclude_sensitive
            add("> [!WARNING]\n> Foram encontrados arquivos potencialmente sensíveis"
                + (" e o conteúdo deles **foi incluído** neste documento. Revise antes de compartilhar.\n\n"
                   if incl else "; o conteúdo deles foi **excluído** por configuração.\n\n"))
            for rel in stats.sensitive:
                add(f"- {E('🔐')}{code(rel)}\n")
            add("\n")

        # ---- integridade
        add(head("integ"))
        add("| Verificação | Resultado |\n|---|---|\n")
        add(f"| {E('🔑')}SHA256 do conteúdo extraído | {code(store.sha)} |\n")
        add(f"| {E('🌳')}SHA256 da TREE | {code(hashlib.sha256(scan.tree_text.encode('utf-8')).hexdigest())} |\n")
        add(f"| {E('🛡️')}Situação | {status} |\n")
        add(f"| {E('📏')}Regras de exclusão | {cell(', '.join(r[2] for r in scan.rules) or 'nenhuma')} |\n")
        nonutf = len(stats.nonutf8)
        add(f"| {E('🔤')}Arquivos fora de UTF-8 | {nonutf}" + (" — " + ", ".join(code(r) for r, _ in stats.nonutf8[:5]) if nonutf else "") + " |\n")
        add(f"| {E('🧪')}Falhas de verificação de bytes | {len(stats.unverified)} |\n\n")

        # ---- documentação anterior
        if prev:
            add(head("prev"))
            add(f"_Arquivo anexado:_ {code(prev['name'])} · {human_size(prev['size'])} · SHA256 {code(prev['sha'])}\n\n"
                "<details>\n<summary>Mostrar documentação anterior (referência histórica)</summary>\n\n")
            fc = fence_for(prev["text"])
            add(f"{fc}markdown\n{prev['text']}{'' if prev['text'].endswith(chr(10)) else chr(10)}{fc}\n\n</details>\n\n")

        add(f"---\n\n<sub>{E('📚')}Gerado por {SCRIPT_PATH.name} v{APP_VERSION} · {now:%Y-%m-%d %H:%M:%S}</sub>\n")
        md.finish()
    except BaseException:
        md.cleanup()
        raise
    return md


# ----------------------------------------------------------------------------
# G) Publicação no GitHub (antigo push.py) + teste automatizado (resquício)
# ----------------------------------------------------------------------------

PUSH_DOC_NAME = "DOCUMENTACAO_PROJETO.md"
DEFAULT_COMMIT_MSG = "Update automático"
GITIGNORE_DEFAULT = """# Ambientes Virtuais e Dependências
venv/
env/
.venv/
node_modules/

# Caches e Compilados Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Variáveis de Ambiente e Configurações Locais
.env
.vscode/
.idea/

# Temporários e saídas pesadas do Documentador (DOCUMENTACAO_PROJETO.md é versionado)
*.gravando_tmp
TREE_PROJETO*
CONTEUDO_PROJETO*
RELATORIO_EXTRACAO*
PROMPT_IA*
PACOTE_FUSAO_1_2_3*
PACOTE_FINAL*
"""

MIT_LICENSE_TEMPLATE = """MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def ensure_license(root):
    """Cria uma licença MIT padrão se nenhuma licença existir. Retorna True se criou."""
    for name in ("LICENSE", "LICENSE.txt", "LICENSE.md"):
        if (Path(root) / name).exists():
            return False
    # Tenta pegar o nome do usuario do git local
    code, out, _ = git_run(["git", "config", "user.name"], root)
    author = out.strip() if code == 0 and out.strip() else "Contributors"
    year = datetime.now().year
    
    p = Path(root) / "LICENSE"
    p.write_text(MIT_LICENSE_TEMPLATE.format(year=year, author=author), encoding="utf-8", newline="\n")
    return True


def git_run(args, cwd, timeout=600):
    """Executa um comando (lista de argumentos, sem shell). Retorna (código, stdout, stderr)."""
    try:
        r = subprocess.run(
            args, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=timeout, stdin=subprocess.DEVNULL, env=dict(os.environ, GIT_TERMINAL_PROMPT="0"),
            creationflags=0x08000000 if os.name == "nt" else 0)  # sem janela de console no Windows
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"comando não encontrado: {args[0]}"
    except subprocess.TimeoutExpired:
        return 124, "", "tempo esgotado"


def ensure_gitignore(root):
    """Cria um .gitignore padrão se não existir. Retorna True se criou."""
    p = Path(root) / ".gitignore"
    if p.exists():
        return False
    p.write_text(GITIGNORE_DEFAULT, encoding="utf-8", newline="\n")
    return True


def git_has_remote(root):
    if not (Path(root) / ".git").exists():
        return False
    code, out, _ = git_run(["git", "remote"], root, 30)
    return code == 0 and bool(out.strip())


def git_publish(root, msg, doc_store=None, doc_name=PUSH_DOC_NAME, log=None, public=True):
    """Sobe o projeto (e, se doc_store for dado, grava e inclui o Markdown gerado).
    Fluxo do antigo push.py: .gitignore -> init -> add -> commit -> (gh repo create) -> push.
    Retorna dict(ok, committed, pushed, created_remote, doc_included, error, log)."""
    root = Path(root)
    lines = []

    def L(t):
        lines.append(t)
        if log:
            log(t)

    res = dict(ok=False, committed=False, pushed=False, created_remote=False,
               doc_included=False, error="", log=lines)

    def fail(t):
        res["error"] = t
        L("✖ " + t)
        return res

    def run(args, what=None):
        L("$ " + " ".join(args))
        code, out, err = git_run(args, root)
        if code != 0 and what:
            fail(f"{what}: {err or out or 'código ' + str(code)}")
        return code, out, err

    if shutil.which("git") is None:
        return fail("Git não encontrado no PATH. Instale em https://git-scm.com/")
    if ensure_gitignore(root):
        L("📄 .gitignore padrão criado.")
    if ensure_license(root):
        L("⚖️ Licença MIT padrão criada.")
    if doc_store is not None:
        write_store_file(doc_store, root / doc_name)
        res["doc_included"] = True
        L(f"📝 {doc_name} gravado na raiz do projeto.")
    if not (root / ".git").exists():
        L("📦 Inicializando repositório Git local...")
        if run(["git", "init"], "git init")[0] != 0:
            return res
        run(["git", "branch", "-M", "main"])
    if run(["git", "add", "-A"], "git add")[0] != 0:
        return res
    code, out, err = run(["git", "status", "--porcelain"], "git status")
    if code != 0:
        return res
    if out.strip():
        if run(["git", "commit", "-m", msg or DEFAULT_COMMIT_MSG], "git commit")[0] != 0:
            return res
        res["committed"] = True
        L("✅ Commit criado.")
    else:
        L("ℹ️ Nenhuma alteração nova para commitar.")
    if not git_has_remote(root):
        if shutil.which("gh") is None:
            return fail("Sem repositório remoto e o GitHub CLI (gh) não foi encontrado. "
                        "Instale em https://cli.github.com/ e rode «gh auth login».")
        L(f"🔗 Criando repositório '{root.name}' ({'público' if public else 'privado'}) no GitHub...")
        if run(["gh", "repo", "create", root.name, "--public" if public else "--private",
                "--source=.", "--remote=origin"], "gh repo create")[0] != 0:
            return res
        res["created_remote"] = True
        L("✅ Repositório criado.")
    code, branch, _ = git_run(["git", "branch", "--show-current"], root, 30)
    branch = branch.strip() or "main"
    L("☁️ Enviando para a nuvem...")
    if run(["git", "push", "-u", "origin", branch], "git push")[0] != 0:
        return res
    res["pushed"] = res["ok"] = True
    L("✅ Código no ar.")
    return res


def run_autotest(root, log=None):
    """RESQUÍCIO — teste automatizado (a implementar).
    Contrato: True = passou, False = reprovou (cancela o push se cfg['autotest_before_push']),
    None = ainda não implementado."""
    if log:
        log("Teste automatizado ainda não implementado.")
    return None


# ----------------------------------------------------------------------------
# Interface gráfica (CustomTkinter) — barra lateral, abas, cartões e avisos
# ----------------------------------------------------------------------------

STATE_COLORS = {"red": "#e5534b", "yellow": "#e3a008", "green": "#3fb950", "partial": "#d4a72c"}
STATE_TEXT = {"red": "Pendente", "yellow": "Processando…", "green": "Concluído", "partial": "Parcial"}
MONO = "Consolas" if os.name == "nt" else ("Menlo" if sys.platform == "darwin" else "DejaVu Sans Mono")

BTN_STYLES = {
    "primary": (("#2f6bff", "#2f6bff"), ("#1f4fd1", "#4a82ff"), "white"),
    "secondary": (("#d7dce6", "#2d3340"), ("#c3cada", "#3a4252"), ("gray10", "gray90")),
    "success": (("#2da04f", "#2a9148"), ("#23853f", "#35ad59"), "white"),
    "danger": (("#d6453d", "#c0453f"), ("#b53730", "#df5a52"), "white"),
    "ghost": (("transparent", "transparent"), ("#d7dce6", "#2d3340"), ("gray10", "gray90")),
}

RULES_HELP = ("Uma regra por linha (ou separadas por vírgula).  nome/ → só diretórios com esse nome, em qualquer nível  ·  "
              "*.log → curinga no nome  ·  src/legado ou docs/**/*.png → caminho relativo  ·  # comentário.  "
              "Sem regras, NADA é excluído. Toda exclusão aparece na TREE e no relatório.")


def mk_btn(parent, text, command, kind="secondary", width=0, height=30):
    fg, hv, tc = BTN_STYLES[kind]
    kw = dict(text=text, command=command, height=height, corner_radius=8, fg_color=fg, hover_color=hv,
              text_color=tc, font=ctk.CTkFont(size=12, weight="bold"))
    if width:
        kw["width"] = width
    return ctk.CTkButton(parent, **kw)


class StatCard:
    def __init__(self, parent, icon, label):
        self.frame = ctk.CTkFrame(parent, corner_radius=12)
        self.value = ctk.CTkLabel(self.frame, text="—", font=ctk.CTkFont(size=20, weight="bold"))
        self.value.pack(padx=12, pady=(8, 0))
        ctk.CTkLabel(self.frame, text=f"{icon} {label}", font=ctk.CTkFont(size=11),
                     text_color=("gray35", "gray65")).pack(padx=12, pady=(0, 8))

    def set(self, value, color=None):
        self.value.configure(text=str(value), text_color=color or ("gray10", "gray95"))


class Step:
    """Cartão de uma etapa do pipeline na barra lateral."""

    def __init__(self, parent, n, title, on_run, on_open):
        self.frame = ctk.CTkFrame(parent, corner_radius=10)
        self.frame.pack(fill="x", padx=10, pady=3)
        self.frame.grid_columnconfigure(1, weight=1)
        self.dot = ctk.CTkLabel(self.frame, text="●", width=24, font=ctk.CTkFont(size=22), text_color=STATE_COLORS["red"])
        self.dot.grid(row=0, column=0, rowspan=2, padx=(8, 2), pady=6)
        self.title = ctk.CTkLabel(self.frame, text=f"{n}  {title}", anchor="w", font=ctk.CTkFont(size=13, weight="bold"))
        self.title.grid(row=0, column=1, sticky="ew", pady=(6, 0))
        self.state = ctk.CTkLabel(self.frame, text=STATE_TEXT["red"], anchor="w", font=ctk.CTkFont(size=11),
                                  text_color=("gray35", "gray65"), wraplength=150, justify="left")
        self.state.grid(row=1, column=1, sticky="ew", pady=(0, 6))
        self.run = mk_btn(self.frame, "▶", on_run, "primary", width=34, height=30)
        self.run.grid(row=0, column=2, rowspan=2, padx=8)
        for w in (self.frame, self.dot, self.title, self.state):
            w.bind("<Button-1>", lambda e: on_open())

    def show(self, state, msg=""):
        self.dot.configure(text_color=STATE_COLORS[state])
        base = STATE_TEXT[state]
        self.state.configure(text=f"{base} · {msg}" if msg and state != "red" else (msg or base))


class Pane:
    """Aba com barra de ações, informação, busca e caixa de texto somente leitura."""

    def __init__(self, app, parent, colorize=None):
        self.app = app
        self.colorize = colorize
        self.frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.frame.pack(fill="both", expand=True)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        top = ctk.CTkFrame(self.frame, fg_color="transparent")
        top.grid(row=0, column=0, sticky="ew", pady=(2, 4))
        top.grid_columnconfigure(0, weight=1)
        self.bar = ctk.CTkFrame(top, fg_color="transparent")
        self.bar.grid(row=0, column=0, sticky="w")
        fb = ctk.CTkFrame(top, fg_color="transparent")
        fb.grid(row=0, column=1, sticky="e")
        self.find_var = tk.StringVar()
        self.find_entry = ctk.CTkEntry(fb, textvariable=self.find_var, width=180, height=28, placeholder_text="🔎 buscar na prévia")
        self.find_entry.pack(side="left", padx=2)
        self.find_lbl = ctk.CTkLabel(fb, text="", width=70, font=ctk.CTkFont(size=11))
        self.find_lbl.pack(side="left")
        self.find_entry.bind("<Return>", lambda e: self.find())
        self.find_entry.bind("<KeyRelease>", lambda e: self.find(reset=True) if e.keysym != "Return" else None)
        self.info = ctk.CTkLabel(self.frame, text="", anchor="w", justify="left", wraplength=1000,
                                 text_color=("gray30", "gray70"))
        self.info.grid(row=1, column=0, sticky="ew", padx=4)
        self.box = ctk.CTkTextbox(self.frame, wrap="none", font=(MONO, 12), corner_radius=10)
        self.box.grid(row=2, column=0, sticky="nsew", pady=(4, 0))
        self._pos = "1.0"
        for tag, kw in (("hit", dict(background="#e3a008", foreground="black")),
                        ("warn", dict(foreground="#e3a008")), ("err", dict(foreground="#e5534b")),
                        ("link", dict(foreground="#39c5cf")), ("tool", dict(foreground="#a371f7")),
                        ("h", dict(foreground="#58a6ff"))):
            self.box.tag_config(tag, **kw)

        def guard(ev):  # somente leitura, mas permite selecionar/copiar/navegar
            if ev.keysym in ("Left", "Right", "Up", "Down", "Home", "End", "Prior", "Next"):
                return None
            if ev.state & 0x4 or ev.state & 0x8:  # Ctrl / Cmd
                return None
            return "break"
        self.box.bind("<Key>", guard)

    def button(self, key, text, command, kind="secondary", width=0):
        b = mk_btn(self.bar, text, command, kind, width)
        b.pack(side="left", padx=3)
        self.app.btn[key] = b
        return b

    def set_text(self, text, truncated_total=None, mode=None):
        tb = self.box._textbox
        tb.delete("1.0", "end")
        if truncated_total:
            text += (f"\n\n⚠ PRÉ-VISUALIZAÇÃO LIMITADA A ~{PREVIEW_LIMIT} CARACTERES. O resultado completo "
                     f"({truncated_total} caracteres) está preservado; copiar/salvar usam o conteúdo integral.\n")
        if text:
            tb.insert("1.0", text)
            if mode and len(text) < 600_000:
                self._tags(text, mode)
        self.find_lbl.configure(text="")
        self._pos = "1.0"

    def _tags(self, text, mode):
        tb = self.box._textbox
        for n, line in enumerate(text.split("\n"), 1):
            tag = None
            if mode == "tree":
                if "[EXCLU" in line or "[JÁ VISITADO" in line:
                    tag = "warn"
                elif "[LINK" in line:
                    tag = "link"
                elif "[ESTA FERRAMENTA]" in line or "[SAÍDA" in line:
                    tag = "tool"
                elif "[INACESS" in line or "[ERRO" in line:
                    tag = "err"
            elif mode == "md" and line.startswith("#"):
                tag = "h"
            elif mode == "report" and line and line.isupper() and not line.startswith(" "):
                tag = "h"
            if tag:
                tb.tag_add(tag, f"{n}.0", f"{n}.end")

    def find(self, reset=False):
        tb = self.box._textbox
        term = self.find_var.get()
        tb.tag_remove("hit", "1.0", "end")
        if reset:
            self._pos = "1.0"
        if not term:
            self.find_lbl.configure(text="")
            return
        idx, n = "1.0", 0
        while n < 3000:
            idx = tb.search(term, idx, nocase=True, stopindex="end")
            if not idx:
                break
            end = f"{idx}+{len(term)}c"
            tb.tag_add("hit", idx, end)
            n += 1
            idx = end
        if not n:
            self.find_lbl.configure(text="0 result.")
            return
        nxt = tb.search(term, self._pos, nocase=True, stopindex="end") or tb.search(term, "1.0", nocase=True, stopindex="end")
        if nxt:
            tb.see(nxt)
            self._pos = f"{nxt}+{len(term)}c"
        self.find_lbl.configure(text=f"{n}{'+' if n >= 3000 else ''} result.")


_CTkBase = ctk.CTk if ctk is not None else object

class PromptModeDialog:
    """Caixa de diálogo para escolher entre o prompt DOC e o COD."""
    def __init__(self, parent):
        self.top = ctk.CTkToplevel(parent)
        self.top.title("Escolha o Modo do Prompt")
        self.top.geometry("450x260")
        self.top.transient(parent)
        self.result = None
        
        # Centraliza a janela
        self.top.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 225
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 130
        self.top.geometry(f"+{x}+{y}")
        
        lbl = ctk.CTkLabel(self.top, text="Qual prompt você deseja gerar?", font=ctk.CTkFont(size=14, weight="bold"))
        lbl.pack(pady=(20, 15))
        
        btn_doc = ctk.CTkButton(self.top, text="DOC — Gerar Documentação Final\n(Prompt padrão para documentar o projeto)", 
                                command=lambda: self.set_res("DOC"), height=50, 
                                fg_color="#2f6bff", hover_color="#1f4fd1", font=ctk.CTkFont(weight="bold"))
        btn_doc.pack(pady=10, fill="x", padx=30)
        
        btn_cod = ctk.CTkButton(self.top, text="COD — Edição e Implementação\n(Prompt para a IA ler, memorizar e ajudar no código)", 
                                command=lambda: self.set_res("COD"), height=50, 
                                fg_color="#e3a008", hover_color="#c98a00", text_color="black", font=ctk.CTkFont(weight="bold"))
        btn_cod.pack(pady=10, fill="x", padx=30)
        
        self.top.grab_set()
        parent.wait_window(self.top)
        
    def set_res(self, val):
        self.result = val
        self.top.destroy()

class App(_CTkBase):
    ALIAS = {"s1": "tree", "s2": "content", "s3": "prompt", "s4": "final", "s5": "md"}

    def __init__(self):
        self.cfg = load_config(ROOT)
        ctk.set_appearance_mode(self.cfg["appearance"])
        ctk.set_widget_scaling(self.cfg["scale"])
        ctk.set_window_scaling(self.cfg["scale"])
        super().__init__()
        self.title(f"📚 {APP_TITLE} — {ROOT}")
        self.geometry("1440x900")
        self.minsize(1080, 680)
        self.q = queue.Queue()
        self.cancel = threading.Event()
        self.busy = False
        self.closing = False
        self.t0 = 0.0
        self.pl = Pipeline()
        self.cur_stage = None
        self.scan = None
        self.partial1, self.partial2 = [], []
        self.store = self.stats = None
        self.report = ""
        self.prompt = None
        self.pkg123 = None
        self.prev = None
        self.final = None
        self.mdstore = None
        self.heavy_found = []
        self.btn = {}
        self._build()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.bind_all("<Control-f>", self.focus_find)
        self.bind_all("<Control-Return>", lambda e: self.on_run_all())
        self.after(80, self.poll)
        self.refresh()
        self.update_cards()
        self.status(f"Raiz do projeto: {ROOT}")

    # ------------------------------------------------------------ infraestrutura
    def ui(self, fn):
        self.q.put(fn)

    def call_ui(self, fn):
        """Chamado de threads de trabalho: executa fn na thread da interface e espera."""
        ev, box = threading.Event(), {}

        def wrapper():
            try:
                box["res"] = fn()
            except BaseException as exc:  # repassado à thread de trabalho
                box["exc"] = exc
            finally:
                ev.set()
        self.q.put(wrapper)
        while not ev.wait(0.1):
            if self.closing:
                raise Cancelled()
        if "exc" in box:
            raise box["exc"]
        return box.get("res")

    def poll(self):
        if self.closing:
            return
        try:
            while True:
                self.q.get_nowait()()
        except queue.Empty:
            pass
        if self.busy:
            self.elapsed_lbl.configure(text=f"⏱ {human_time(time.time() - self.t0)}")
        self.after(80, self.poll)

    def status(self, text):
        self.status_lbl.configure(text=text)

    def prog(self, cur, total, text):
        self.ui(lambda: self.set_progress(cur, total, text))

    def set_progress(self, cur, total, text):
        self.status(text)
        if total:
            if self.pbar.cget("mode") != "determinate":
                self.pbar.stop()
                self.pbar.configure(mode="determinate")
            self.pbar.set(min(1.0, cur / total))

    def toast(self, msg, kind="info", ms=3800):
        colors = {"info": "#2f6bff", "ok": "#2da04f", "warn": "#c98a00", "err": "#c0453f"}
        t = ctk.CTkLabel(self, text="  " + msg + "  ", fg_color=colors[kind], text_color="white", corner_radius=10,
                         font=ctk.CTkFont(size=13, weight="bold"), wraplength=520, justify="left")
        t.place(relx=0.985, rely=0.93, anchor="se")
        t.lift()
        self.after(ms, t.destroy)

    def refresh(self):
        allowed = self.pl.allowed(self.prev is not None)
        for k, b in self.btn.items():
            key = self.ALIAS.get(k, k)
            if key == "heavy":
                ok = self.pl.green(1) and bool(self.heavy_found)
            else:
                ok = allowed.get(key, True)
            b.configure(state="normal" if (ok and not self.busy) else "disabled")
        self.btn_cancel.configure(state="normal" if self.busy else "disabled")
        with_doc = bool(self.mdstore and self.pl.green(5))
        fg, hv, _ = BTN_STYLES["success" if with_doc else "primary"]
        self.btn["github"].configure(
            text="☁  SUBIR PRO GITHUB + DOCUMENTAÇÃO" if with_doc else "☁  SUBIR PRO GITHUB",
            fg_color=fg, hover_color=hv)
        self.github_hint.configure(
            text=(f"Vai subir o projeto + {PUSH_DOC_NAME} (já gerado)." if with_doc
                  else "Sobe o projeto como está (não exige nenhuma etapa)."))

    def stage(self, n, state, msg="", partial=False):
        self.pl.state[n] = state
        self.steps[n].show("partial" if (partial and state == "green") else state, msg)
        self.refresh()

    def begin_stage(self, n, msg="Processando…"):
        """(thread da interface) descarta dados da etapa n e marca como em andamento."""
        self.cur_stage = n
        if n == 5:
            self.clear_md()
        else:
            self.clear_data(n)
        self.stage(n, "yellow", msg)

    def run_job(self, fn, label="Processando…"):
        if self.busy:
            return
        self.cancel.clear()
        self.busy = True
        self.t0 = time.time()
        self.status(label)
        self.pbar.configure(mode="indeterminate")
        self.pbar.start()
        self.refresh()
        try:
            threading.stack_size(64 * 1024 * 1024)  # árvores muito profundas
        except Exception:
            pass

        def target():
            try:
                fn()
            except Cancelled:
                self.ui(lambda: self.job_failed("CANCELADO pelo usuário.", None))
            except Exception as exc:
                tb = traceback.format_exc()
                self.ui(lambda: self.job_failed(f"FALHA: {exc}", tb))
            finally:
                self.ui(self.job_finished)
        threading.Thread(target=target, daemon=True).start()
        try:
            threading.stack_size(0)
        except Exception:
            pass

    def job_failed(self, msg, tb):
        n = self.cur_stage
        if n:
            if n == 5:
                self.clear_md()
            else:
                self.clear_data(n)
            self.stage(n, "red", msg)
        self.status(msg)
        self.toast(msg, "warn" if msg.startswith("CANCEL") else "err", 6000)
        if tb:
            messagebox.showerror(APP_TITLE, msg + "\n\n" + tb[-1500:])

    def job_finished(self):
        self.pbar.stop()
        self.pbar.configure(mode="determinate")
        self.pbar.set(0)
        self.busy = False
        self.elapsed_lbl.configure(text=f"⏱ {human_time(time.time() - self.t0)}")
        self.refresh()

    def on_close(self):
        self.closing = True
        self.cancel.set()
        save_config(ROOT, self.cfg)
        for s in (self.store, self.pkg123, self.final, self.mdstore):
            if s:
                s.cleanup()
        self.destroy()

    # ------------------------------------------------------------ invalidação
    def clear_md(self):
        if self.mdstore:
            self.mdstore.cleanup()
        self.mdstore = None
        self.panes["md"].set_text("")
        self.panes["md"].info.configure(text="")
        if self.pl.state[5] != "red":
            self.pl.state[5] = "red"
            self.steps[5].show("red", "Invalidado.")

    def clear_data(self, level, reason="Invalidado: uma etapa anterior foi regenerada."):
        """Descarta dados da etapa `level` em diante e volta os indicadores a vermelho."""
        changed = self.pl.invalidate_from(level)
        if level <= 1:
            self.scan, self.partial1, self.heavy_found = None, [], []
            self.panes["tree"].set_text("")
            self.panes["tree"].info.configure(text="")
        if level <= 2:
            if self.store:
                self.store.cleanup()
            self.store = self.stats = None
            self.report, self.partial2 = "", []
            for k in ("content", "report"):
                self.panes[k].set_text("")
                self.panes[k].info.configure(text="")
        if level <= 3:
            self.prompt = None
            if self.pkg123:
                self.pkg123.cleanup()
            self.pkg123 = None
            for k in ("prompt", "pkg"):
                self.panes[k].set_text("")
                self.panes[k].info.configure(text="")
        if level <= 4:
            if self.final:
                self.final.cleanup()
            self.final = None
            self.panes["final"].set_text("")
        if level <= 2 and self.mdstore:
            self.mdstore.cleanup()
            self.mdstore = None
            self.panes["md"].set_text("")
            self.panes["md"].info.configure(text="")
        for n in changed:
            self.steps[n].show("red", reason if n != level else "")
        self.update_cards()
        self.refresh()

    # ------------------------------------------------------------ construção
    def _build(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ---- barra lateral
        side = ctk.CTkScrollableFrame(self, width=300, corner_radius=0)
        side.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(side, text="📚 Documentador", font=ctk.CTkFont(size=24, weight="bold")).pack(anchor="w", padx=16, pady=(16, 0))
        ctk.CTkLabel(side, text=f"Universal · v{APP_VERSION}", text_color=("gray35", "gray65")).pack(anchor="w", padx=18)
        ctk.CTkLabel(side, text=f"📂 {ROOT}", anchor="w", justify="left", wraplength=270, font=ctk.CTkFont(size=11),
                     text_color=("gray30", "gray70")).pack(fill="x", padx=18, pady=(6, 10))
        ctk.CTkLabel(side, text="PIPELINE", anchor="w", font=ctk.CTkFont(size=11, weight="bold"),
                     text_color=("gray40", "gray60")).pack(fill="x", padx=18)
        self.steps = {}
        specs = [(1, "🌳 TREE", self.on_tree, "tree", "s1"),
                 (2, "📄 Conteúdo", self.on_content, "content", "s2"),
                 (3, "🧠 Prompt + fusão", self.on_step3, "prompt", "s3"),
                 (4, "📎 Pacote final", self.on_final, "final", "s4"),
                 (5, "📝 Markdown final", self.on_md, "md", "s5")]
        self._tab_of = {1: "🌳 TREE", 2: "📄 Conteúdo", 3: "🧠 Prompt", 4: "📎 Pacote final", 5: "📝 Markdown"}
        for n, title, cmd, _, alias in specs:
            st = Step(side, n, title, cmd, lambda n=n: self.tabs.set(self._tab_of[n]))
            self.steps[n] = st
            self.btn[alias] = st.run
            st.show("red", "Não iniciado.")
        mk = mk_btn(side, "⚡  EXECUTAR TUDO   (Ctrl+Enter)", self.on_run_all, "success", height=44)
        mk.pack(fill="x", padx=12, pady=(14, 4))
        self.btn["run_all"] = mk
        self.btn_cancel = mk_btn(side, "⛔  CANCELAR", self.cancel.set, "danger", height=32)
        self.btn_cancel.pack(fill="x", padx=12, pady=2)
        self.btn_cancel.configure(state="disabled")
        ctk.CTkFrame(side, fg_color="transparent").pack(fill="both", expand=True)
        self.btn["options"] = mk_btn(side, "⚙  Opções e exclusões", self.on_options, "secondary", height=34)
        self.btn["options"].pack(fill="x", padx=12, pady=2)
        self.btn["remount"] = mk_btn(side, "🧩  Remontar partes…", self.on_remount, "secondary", height=34)
        self.btn["remount"].pack(fill="x", padx=12, pady=2)
        self.theme_seg = ctk.CTkSegmentedButton(side, values=["Claro", "Escuro", "Sistema"], command=self.on_theme)
        self.theme_seg.set({"Light": "Claro", "Dark": "Escuro"}.get(self.cfg["appearance"], "Sistema"))
        self.theme_seg.pack(fill="x", padx=12, pady=(6, 14))

        # ---- área principal
        main = ctk.CTkFrame(self, fg_color="transparent")
        main.grid(row=0, column=1, sticky="nsew", padx=12, pady=10)
        main.grid_columnconfigure(0, weight=1)
        main.grid_rowconfigure(2, weight=1)
        topbar = ctk.CTkFrame(main, fg_color="transparent")
        topbar.grid(row=0, column=0, sticky="ew", pady=(0, 8))
        self.btn["github"] = mk_btn(topbar, "☁  SUBIR PRO GITHUB", self.on_github, "primary", height=38)
        self.btn["github"].pack(side="left", padx=(0, 6))
        self.btn["autotest"] = mk_btn(topbar, "🧪  Teste automatizado", self.on_autotest, "secondary", height=38)
        self.btn["autotest"].pack(side="left", padx=6)
        self.github_hint = ctk.CTkLabel(topbar, text="", anchor="w", text_color=("gray30", "gray70"))
        self.github_hint.pack(side="left", padx=10)
        cards = ctk.CTkFrame(main, fg_color="transparent")
        cards.grid(row=1, column=0, sticky="ew")
        self.cards = {}
        for i, (k, icon, label) in enumerate([("dirs", "📁", "Diretórios"), ("files", "📄", "Arquivos"),
                                              ("text", "📝", "Texto"), ("bin", "🖼️", "Binários"),
                                              ("skip", "🚫", "Ignorados/Excl."), ("size", "💾", "Tamanho"),
                                              ("integ", "🛡️", "Integridade")]):
            c = StatCard(cards, icon, label)
            c.frame.grid(row=0, column=i, sticky="ew", padx=4)
            cards.grid_columnconfigure(i, weight=1, uniform="cards")
            self.cards[k] = c

        self.tabs = ctk.CTkTabview(main, corner_radius=12)
        self.tabs.grid(row=2, column=0, sticky="nsew", pady=(8, 6))
        self.panes = {}

        def pane(key, tab, colorize=None):
            p = Pane(self, self.tabs.add(tab), colorize)
            self.panes[key] = p
            return p
        p = pane("tree", "🌳 TREE")
        p.button("tree", "GERAR TREE", self.on_tree, "primary")
        p.button("copy_tree", "📋 Copiar", self.on_copy_tree)
        p.button("save_tree", "💾 Salvar", self.on_save_tree)
        p.button("heavy", "🧹 Excluir volumosos e refazer", self.on_heavy)
        p = pane("content", "📄 Conteúdo")
        p.button("content", "EXTRAIR CONTEÚDO", self.on_content, "primary")
        p.button("copy_content", "📋 Copiar", self.on_copy_content)
        p.button("save_content", "💾 Salvar (partes)", self.on_save_content)
        p = pane("report", "📊 Relatório")
        p.button("copy_report", "📋 Copiar", lambda: self.copy_text(self.report, "Relatório"))
        p.button("save_report", "💾 Salvar", lambda: self.save_text("RELATORIO_EXTRACAO.txt", self.report, "Salvar relatório"))
        p = pane("prompt", "🧠 Prompt")
        p.button("prompt", "GERAR PROMPT", self.on_prompt, "primary")
        p.button("copy_prompt", "📋 Copiar", lambda: self.copy_text(self.prompt, "Prompt"))
        p.button("save_prompt", "💾 Salvar", lambda: self.save_text("PROMPT_IA.txt", self.prompt, "Salvar prompt"))
        p = pane("pkg", "📦 Pacote 1+2+3")
        p.button("fuse", "FUNDIR 1+2+3", self.on_fuse, "primary")
        p.button("copy_pkg", "📋 Copiar", self.on_copy_pkg)
        p.button("save_pkg", "💾 Salvar (partes)", self.on_save_pkg)
        p = pane("final", "📎 Pacote final")
        p.button("attach", "📎 ANEXAR DOCUMENTACAO.MD", self.on_attach)
        p.button("detach", "✖ Remover anexo", self.on_detach)
        p.button("final", "UNIR TUDO", self.on_final, "primary")
        p.button("copy_final", "📋 Copiar", self.on_copy_final)
        p.button("save_final", "💾 Salvar (partes)", self.on_save_final)
        cand = ROOT / "DOCUMENTACAO.md"
        p.info.configure(text=(f"📎 Detectado {cand.name} na raiz — use ANEXAR para incluí-lo." if cand.is_file()
                               else "Sem anexo, o pacote final servirá para criar a documentação inicial."))
        p = pane("md", "📝 Markdown")
        p.button("md", "GERAR MARKDOWN", self.on_md, "primary")
        p.button("copy_md", "📋 Copiar", self.on_copy_md)
        p.button("save_md", "💾 Salvar .md", self.on_save_md, "success")

        foot = ctk.CTkFrame(main, fg_color="transparent")
        foot.grid(row=3, column=0, sticky="ew")
        foot.grid_columnconfigure(1, weight=1)
        self.pbar = ctk.CTkProgressBar(foot, width=240, height=12)
        self.pbar.set(0)
        self.pbar.grid(row=0, column=0, padx=4)
        self.status_lbl = ctk.CTkLabel(foot, text="", anchor="w")
        self.status_lbl.grid(row=0, column=1, sticky="ew", padx=8)
        self.elapsed_lbl = ctk.CTkLabel(foot, text="⏱ 00:00", font=ctk.CTkFont(size=12))
        self.elapsed_lbl.grid(row=0, column=2, padx=6)

    def focus_find(self, _e=None):
        name = self.tabs.get()
        for k, p in self.panes.items():
            if self.tabs._name_list and self.tabs.tab(name) is p.frame.master:
                p.find_entry.focus_set()
                return

    def on_theme(self, v):
        mode = {"Claro": "Light", "Escuro": "Dark"}.get(v, "System")
        self.cfg["appearance"] = mode
        ctk.set_appearance_mode(mode)
        save_config(ROOT, self.cfg)

    def update_cards(self):
        c = self.cards
        sc, st = self.scan, self.stats
        c["dirs"].set(sc.dirs if sc else "—")
        c["files"].set(sc.files if sc else "—")
        c["text"].set(len(st.ok) if st else "—")
        c["bin"].set(len(st.binary) if st else "—")
        c["skip"].set((len(st.ignored) + len(st.excluded) + len(sc.excluded_dirs)) if (st and sc) else "—")
        c["size"].set(human_size(st.text_bytes) if st else "—")
        if st and sc:
            partial = bool(self.partial1 or self.partial2)
            c["integ"].set("PARCIAL" if partial else "COMPLETA", STATE_COLORS["partial" if partial else "green"])
        else:
            c["integ"].set("—")

    # ------------------------------------------------------------ opções
    def on_options(self):
        cfg = self.cfg
        win = ctk.CTkToplevel(self)
        win.title("⚙ Opções e exclusões")
        win.geometry("900x700")
        win.transient(self)
        win.after(150, win.grab_set)
        tabs = ctk.CTkTabview(win)
        tabs.pack(fill="both", expand=True, padx=12, pady=(12, 4))
        t1, t2, t3, t4 = (tabs.add(n) for n in ("🚫 Exclusões", "📄 Conteúdo", "📤 Exportação / Markdown", "🎨 Aparência"))

        # -- exclusões
        t1.grid_columnconfigure(0, weight=3, uniform="ex")
        t1.grid_columnconfigure(1, weight=2, uniform="ex")
        t1.grid_rowconfigure(2, weight=1)
        ctk.CTkLabel(t1, text="Marque o que deve ser ignorado: qualquer pasta/arquivo com esse nome, em QUALQUER nível do "
                              "projeto, será pulado (e listado na TREE como excluído).",
                     anchor="w", justify="left", wraplength=520).grid(row=0, column=0, sticky="ew", padx=(0, 8))
        ctk.CTkLabel(t1, text="Regras personalizadas", anchor="w", font=ctk.CTkFont(size=13, weight="bold")).grid(
            row=0, column=1, sticky="w")
        chk_vars = {}
        tb_ = ctk.CTkFrame(t1, fg_color="transparent")
        tb_.grid(row=1, column=0, sticky="w", pady=4)
        count_lbl = ctk.CTkLabel(t1, text="", anchor="w")
        count_lbl.grid(row=3, column=0, columnspan=2, sticky="ew")
        rules_box = ctk.CTkTextbox(t1, font=(MONO, 12))
        rules_box.grid(row=2, column=1, sticky="nsew", pady=4)
        rules_box.insert("1.0", cfg["rules_text"])
        ctk.CTkLabel(t1, text=RULES_HELP, anchor="w", justify="left", wraplength=360,
                     text_color=("gray30", "gray70")).grid(row=1, column=1, sticky="w")

        def upd(_e=None):
            n_ = sum(1 for v in chk_vars.values() if v.get())
            count_lbl.configure(text=f"✔ {n_} item(ns) marcado(s) + "
                                     f"{len(parse_rules(rules_box.get('1.0', 'end')))} regra(s) personalizada(s)")

        def set_all(pred):
            for p_, v in chk_vars.items():
                v.set(pred(p_))
            upd()
        mk_btn(tb_, "☑ Marcar recomendados", lambda: set_all(lambda p_: p_ in PRESET_RECOMMENDED), "primary", height=28).pack(side="left", padx=2)
        mk_btn(tb_, "☑ Todos", lambda: set_all(lambda p_: True), "secondary", height=28).pack(side="left", padx=2)
        mk_btn(tb_, "☐ Nenhum", lambda: set_all(lambda p_: False), "secondary", height=28).pack(side="left", padx=2)
        pf = ctk.CTkScrollableFrame(t1)
        pf.grid(row=2, column=0, sticky="nsew", padx=(0, 8), pady=4)
        checked = set(cfg["excl_checked"])
        for title_, items_ in PRESET_GROUPS:
            ctk.CTkLabel(pf, text=title_, anchor="w", font=ctk.CTkFont(size=13, weight="bold")).pack(fill="x", pady=(10, 2))
            for pat_, desc_ in items_:
                v = tk.BooleanVar(value=pat_ in checked)
                chk_vars[pat_] = v
                ctk.CTkCheckBox(pf, text=f"{pat_}   —  {desc_}", variable=v, command=upd,
                                font=ctk.CTkFont(size=12)).pack(anchor="w", padx=6, pady=2)
        rules_box.bind("<KeyRelease>", upd)
        upd()

        # -- conteúdo
        sens = tk.BooleanVar(value=cfg["sens"])
        selfign = tk.BooleanVar(value=cfg["selfign"])
        maxmb = tk.StringVar(value=str(cfg["maxmb"]))
        workers = tk.StringVar(value=str(cfg["workers"]))
        ctk.CTkSwitch(t2, text="Excluir o CONTEÚDO de arquivos sensíveis (.env, chaves, credenciais)", variable=sens).pack(anchor="w", padx=10, pady=8)
        ctk.CTkSwitch(t2, text="Ignorar o conteúdo desta ferramenta (o próprio script)", variable=selfign).pack(anchor="w", padx=10, pady=8)
        r = ctk.CTkFrame(t2, fg_color="transparent")
        r.pack(anchor="w", padx=10, pady=8)
        ctk.CTkLabel(r, text="Limite por arquivo em MB (0 = sem limite):").grid(row=0, column=0, sticky="w", pady=4)
        ctk.CTkEntry(r, textvariable=maxmb, width=90).grid(row=0, column=1, padx=8)
        ctk.CTkLabel(r, text="Threads de leitura (0 = automático):").grid(row=1, column=0, sticky="w", pady=4)
        ctk.CTkEntry(r, textvariable=workers, width=90).grid(row=1, column=1, padx=8)

        ctk.CTkLabel(t2, text="Pastas massivas (Muitos arquivos):", font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=10, pady=(12, 0))
        r2 = ctk.CTkFrame(t2, fg_color="transparent")
        r2.pack(anchor="w", padx=10, pady=4)
        ctk.CTkLabel(r2, text="Avisar/Ignorar se tiver mais de (arquivos):").grid(row=0, column=0, sticky="w", pady=4)
        heavy_limit = tk.StringVar(value=str(cfg.get("heavy_limit", 1000)))
        ctk.CTkEntry(r2, textvariable=heavy_limit, width=90).grid(row=0, column=1, padx=8)
        ctk.CTkLabel(r2, text="Ação ao encontrar:").grid(row=1, column=0, sticky="w", pady=4)
        heavy_action = tk.StringVar(value={"read": "Ler tudo", "ignore": "Ignorar", "ask": "Perguntar"}.get(cfg.get("heavy_action", "ask"), "Perguntar"))
        seg_action = ctk.CTkSegmentedButton(r2, values=["Ler tudo", "Ignorar", "Perguntar"], variable=heavy_action)
        seg_action.grid(row=1, column=1, padx=8)

        # -- exportação / markdown
        part = tk.StringVar(value=str(cfg["part"]))
        mv = {k: tk.BooleanVar(value=cfg[k]) for k in ("md_emoji", "md_collapse", "md_contents", "md_tree", "md_stats")}
        r = ctk.CTkFrame(t3, fg_color="transparent")
        r.pack(anchor="w", padx=10, pady=8)
        ctk.CTkLabel(r, text="Tamanho por parte na exportação .txt, em caracteres (0 = arquivo único):").grid(row=0, column=0, sticky="w")
        ctk.CTkEntry(r, textvariable=part, width=110).grid(row=0, column=1, padx=8)
        ctk.CTkLabel(t3, text="Markdown final (DOCUMENTACAO_PROJETO.md)", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=10, pady=(14, 2))
        for k, txt in (("md_emoji", "Usar emojis 😀"), ("md_collapse", "Blocos de código recolhíveis (<details>)"),
                       ("md_contents", "Incluir o conteúdo integral dos arquivos"), ("md_tree", "Incluir a TREE"),
                       ("md_stats", "Incluir estatísticas por linguagem")):
            ctk.CTkSwitch(t3, text=txt, variable=mv[k]).pack(anchor="w", padx=10, pady=5)

        # -- aparência
        app_v = tk.StringVar(value={"Light": "Claro", "Dark": "Escuro"}.get(cfg["appearance"], "Sistema"))
        scale_v = tk.DoubleVar(value=cfg["scale"])
        ctk.CTkLabel(t4, text="Tema:").pack(anchor="w", padx=10, pady=(10, 2))
        ctk.CTkSegmentedButton(t4, values=["Claro", "Escuro", "Sistema"], variable=app_v).pack(anchor="w", padx=10)
        ctk.CTkLabel(t4, text="Escala da interface (aplicada ao confirmar):").pack(anchor="w", padx=10, pady=(16, 2))
        ctk.CTkSlider(t4, from_=0.8, to=1.4, number_of_steps=12, variable=scale_v, width=300).pack(anchor="w", padx=10)

        def apply():
            try:
                mb = float(maxmb.get().replace(",", ".") or 0)
                pc = int(part.get() or 0)
                wk = int(workers.get() or 0)
                hl = int(heavy_limit.get() or 1000)
                if mb < 0 or pc < 0 or wk < 0 or wk > 64 or hl < 0:
                    raise ValueError
            except ValueError:
                return messagebox.showerror(APP_TITLE, "Os limites devem ser números não negativos (threads ≤ 64).", parent=win)
            ha = {"Ler tudo": "read", "Ignorar": "ignore", "Perguntar": "ask"}.get(seg_action.get(), "ask")
            new = dict(cfg)
            new.update(excl_checked=[p_ for p_ in PRESET_ALL if chk_vars[p_].get()],
                       rules_text="\n".join(ln.rstrip() for ln in rules_box.get("1.0", "end").splitlines()).strip(),
                       sens=sens.get(), selfign=selfign.get(), maxmb=mb, part=pc, workers=wk,
                       heavy_limit=hl, heavy_action=ha,
                       appearance={"Claro": "Light", "Escuro": "Dark"}.get(app_v.get(), "System"),
                       scale=round(scale_v.get(), 2), **{k: v.get() for k, v in mv.items()})
            scan_changed = effective_rules(new) != effective_rules(cfg)
            content_changed = (new["sens"], new["selfign"], new["maxmb"]) != (cfg["sens"], cfg["selfign"], cfg["maxmb"])
            md_changed = any(new[k] != cfg[k] for k in mv)
            self.cfg = new
            save_config(ROOT, new)
            win.destroy()
            ctk.set_appearance_mode(new["appearance"])
            ctk.set_widget_scaling(new["scale"])
            ctk.set_window_scaling(new["scale"])
            self.theme_seg.set({"Light": "Claro", "Dark": "Escuro"}.get(new["appearance"], "Sistema"))
            if scan_changed and self.pl.state[1] != "red":
                self.clear_data(1, "Invalidado: as regras de exclusão mudaram; gere a TREE novamente.")
            elif (scan_changed or content_changed) and self.pl.state[2] != "red":
                self.clear_data(2, "Invalidado: as opções de conteúdo mudaram; extraia novamente.")
            elif md_changed and self.pl.state[5] != "red":
                self.clear_md()
            self.toast("Opções salvas.", "ok")
        bar = ctk.CTkFrame(win, fg_color="transparent")
        bar.pack(pady=10)
        mk_btn(bar, "✔ APLICAR E SALVAR", apply, "success", width=180, height=36).pack(side="left", padx=6)
        mk_btn(bar, "Cancelar", win.destroy, "secondary", width=110, height=36).pack(side="left", padx=6)

    # ------------------------------------------------------------ helpers de cópia/salvamento
    def copy_text(self, text, what):
        if not text:
            return
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()
        self.status(f"{what} copiado ({len(text)} caracteres).")
        self.toast(f"{what} copiado ({len(text)} caracteres).", "ok")

    def copy_store(self, store, what, base):
        if store.total_chars > CLIPBOARD_WARN_CHARS:
            if not messagebox.askyesno(
                    APP_TITLE, f"{what} tem {store.total_chars} caracteres — grande demais para a área de "
                               f"transferência e provavelmente para o destino.\n\nSIM = copiar mesmo assim.\n"
                               f"NÃO = exportar para arquivo(s), com divisão em partes.", icon="warning"):
                return self.export_store(store, base)
        self.copy_text(store.read_all(), what)

    def save_text(self, default, text, title):
        if not text:
            return
        path = filedialog.asksaveasfilename(title=title, initialdir=str(ROOT), initialfile=default,
                                            defaultextension=".txt",
                                            filetypes=[("Texto", "*.txt"), ("Todos", "*.*")])
        if not path:
            return
        try:
            with AtomicWriter(path) as f:
                f.write(text)
            self.status(f"Salvo em {path}")
            self.toast("Arquivo salvo.", "ok")
        except OSError as exc:
            messagebox.showerror(APP_TITLE, f"Não foi possível salvar:\n{exc}")

    def export_store(self, store, base, ext=".txt"):
        part = self.cfg["part"]
        if not part and store.total_chars > 2_000_000:
            if messagebox.askyesno(APP_TITLE, f"O conteúdo tem {store.total_chars} caracteres. Dividir em partes de "
                                              f"200000 caracteres (recomendado para IAs)?\n(O tamanho pode ser ajustado em OPÇÕES.)"):
                part = 200_000
        d = filedialog.askdirectory(title="Pasta de destino", initialdir=str(ROOT))
        if not d:
            return
        if part:
            n = len(plan_parts(store.index, part))
            names = [f"{base}_PARTE_{i:03d}{ext}" for i in range(1, n + 1)]  # <-- ALTERADO
        else:
            names = [f"{base}{ext}"]  # <-- ALTERADO
        existing = [x for x in names if (Path(d) / x).exists()]
        if existing and not messagebox.askyesno(
                APP_TITLE, "Estes arquivos já existem e serão SOBRESCRITOS:\n\n" + "\n".join(existing[:15])
                           + ("\n..." if len(existing) > 15 else "") + "\n\nContinuar?"):
            return

        def fn():
            written = write_content_files(store, d, base, part, self.prog, ext)  # <-- ALTERADO
            msg = (f"{len(written)} arquivo(s) em {d}:\n" +
                   "\n".join(f"  {p.name} — {human_size(s)}" for p, s in written[:20]) +
                   ("\n  ..." if len(written) > 20 else ""))
            self.ui(lambda: (self.status(f"{len(written)} arquivo(s) gravado(s) em {d}"),
                             self.toast(f"{len(written)} arquivo(s) gravado(s).", "ok"),
                             messagebox.showinfo(APP_TITLE, msg)))
        self.cur_stage = None
        self.run_job(fn, "Gravando arquivos...")

    # ------------------------------------------------------------ Etapa 1
    def on_tree(self):
        if self.busy:
            return
        opts = Options.from_cfg(self.cfg)
        self.begin_stage(1, "Varrendo…")
        self.run_job(lambda: self.job_tree(opts), "Varrendo o projeto...")

    def job_tree(self, opts):
        def ask_heavy(rel, count):
            return self.call_ui(lambda: messagebox.askyesno(
                APP_TITLE,
                f"A pasta '{rel}' parece ser gigante (mais de {count} arquivos).\n\n"
                "Ler diretórios massivos como APIs completas ou node_modules trava a extração e infla a documentação.\n\n"
                "Deseja IGNORAR esta pasta? (Recomendado: SIM)"
            ))
        scan = scan_project(ROOT, opts, SCRIPT_PATH, self.cancel, self.prog, ask_heavy)
        self.call_ui(lambda: self.apply_tree(scan))

    def apply_tree(self, scan):
        self.scan = scan
        self.partial1 = [f"{len(scan.errors)} caminho(s) não inspecionado(s)"] if scan.errors else []
        w = [f"📁 {scan.dirs} diretórios · 📄 {scan.files} arquivos · 🔗 {scan.symlinks} links"]
        if scan.errors:
            w.append(f"⚠ {len(scan.errors)} caminho(s) não inspecionado(s) — resultado PARCIAL (registrado nos pacotes)")
        if scan.excluded_dirs:
            w.append("🚫 Excluídos por regra: " + ", ".join(scan.excluded_dirs[:6]) + (" ..." if len(scan.excluded_dirs) > 6 else ""))
        self.heavy_found = sorted({k.split("/")[-1] for k in scan.heavy})
        if scan.heavy:
            w.append("🐘 Volumosos incluídos: " + ", ".join(f"{k}/ ({v} arq.)" for k, v in sorted(scan.heavy.items())[:5])
                     + " — use «Excluir volumosos e refazer» se não forem relevantes.")
        sens = [e["rel"] for e in scan.entries if is_sensitive(e["name"])]
        if sens:
            w.append("🔐 Possivelmente sensíveis: " + ", ".join(sens[:5]) + (" ..." if len(sens) > 5 else ""))
        pane = self.panes["tree"]
        pane.info.configure(text="\n".join(w))
        text = scan.tree_text
        trunc = None
        if len(text) > PREVIEW_LIMIT:
            text, trunc = text[:PREVIEW_LIMIT], len(scan.tree_text)
        pane.set_text(text, trunc, "tree")
        self.stage(1, "green", f"{scan.files} arquivos", partial=bool(scan.errors))
        self.update_cards()
        self.status("TREE gerada.")
        if scan.heavy:
            self.toast("Há diretórios volumosos na TREE — considere excluí-los.", "warn")

    def on_copy_tree(self):
        if self.scan:
            self.copy_text(self.scan.tree_text, "TREE")

    def on_save_tree(self):
        if self.scan:
            self.save_text("TREE_PROJETO.txt", self.scan.tree_text, "Salvar TREE")

    def on_heavy(self):
        if not self.heavy_found or self.busy:
            return
        lines = self.cfg["rules_text"].splitlines()
        have = {ln.strip().lower() for ln in lines}
        for n in self.heavy_found:
            if f"{n}/".lower() not in have:
                lines.append(f"{n}/")
        self.cfg["rules_text"] = "\n".join(lines).strip()
        save_config(ROOT, self.cfg)
        self.toast("Regras adicionadas; refazendo a TREE.", "info")
        self.on_tree()

    # ------------------------------------------------------------ Etapa 2
    def on_content(self):
        if self.busy or not self.pl.green(1):
            return
        opts = Options.from_cfg(self.cfg)
        self.begin_stage(2, "Lendo…")
        self.run_job(lambda: self.job_content(opts), "Extraindo conteúdo...")

    def job_content(self, opts):
        scan = self.scan
        store, stats = extract_contents(scan, opts, self.cancel, self.prog)
        try:
            report = build_report(scan, stats, store, opts)
            self.call_ui(lambda: self.apply_content(store, stats, report))
        except BaseException:
            store.cleanup()
            raise

    def apply_content(self, store, stats, report):
        problems = []
        if stats.errors:
            problems.append(f"{len(stats.errors)} arquivo(s) com erro")
        if stats.unverified:
            problems.append(f"{len(stats.unverified)} arquivo(s) com verificação de integridade falha")
        self.store, self.stats, self.report, self.partial2 = store, stats, report, problems
        text, truncated = store.read_preview(PREVIEW_LIMIT)
        self.panes["content"].set_text(text, store.total_chars if truncated else None)
        self.panes["report"].set_text(report, None, "report")
        info = (f"📝 Texto: {len(stats.ok)} · 🖼️ Binários: {len(stats.binary)} · ⏭️ Ignorados: {len(stats.ignored)} · "
                f"🚫 Excluídos: {len(stats.excluded)} · ❌ Erros: {len(stats.errors)} · 💾 {human_size(store.total_bytes)}")
        if problems:
            info += "\n⚠ " + "; ".join(problems) + " — resultado PARCIAL (registrado nos pacotes)"
        if stats.sensitive:
            info += "\n🔐 Possivelmente sensíveis: " + ", ".join(stats.sensitive[:4]) + (" ..." if len(stats.sensitive) > 4 else "")
        self.panes["content"].info.configure(text=info)
        self.stage(2, "green", f"{len(stats.ok)} textos", partial=bool(problems))
        self.update_cards()
        self.status("Conteúdo extraído.")
        if stats.sensitive:
            self.toast("Arquivos sensíveis incluídos — revise antes de compartilhar.", "warn")

    def on_copy_content(self):
        if self.store:
            self.copy_store(self.store, "Conteúdo", "CONTEUDO_PROJETO")

    def on_save_content(self):
        if self.store:
            self.export_store(self.store, "CONTEUDO_PROJETO")

    # ------------------------------------------------------------ Etapa 3
    def on_prompt(self):
        if self.busy or not self.pl.green(1, 2):
            return
        mode = PromptModeDialog(self).result
        if not mode:
            return
        self.begin_stage(3, f"Gerando prompt ({mode})…")
        self.run_job(lambda: self.job_prompt(mode), f"Gerando prompt {mode}...")

    def job_prompt(self, mode="DOC"):
        prompt = build_prompt(mode)
        self.call_ui(lambda: self.apply_prompt(prompt, mode))

    def apply_prompt(self, prompt, mode="DOC"):
        self.prompt = prompt
        self.prompt_mode = mode  # <-- LINHA ADICIONADA
        self.panes["prompt"].set_text(prompt)
        self.stage(3, "green", f"Prompt {mode} pronto.")
        self.status(f"Prompt {mode} gerado.")

    def on_step3(self):
        if self.busy or not self.pl.green(1, 2):
            return
        mode = PromptModeDialog(self).result
        if not mode:
            return
        self.begin_stage(3, f"Gerando prompt ({mode}) e fundindo…")
        self.run_job(lambda: (self.job_prompt(mode), self.job_fuse(clear=False)), "Prompt + fusão...")

    def on_fuse(self):
        if self.busy or not self.pl.green(1, 2, 3):
            return
        self.run_job(self.job_fuse, "Fundindo etapas 1, 2 e 3...")

    def job_fuse(self, clear=True):
        if clear:
            self.call_ui(self._begin_fuse)
        pkg = build_package("fusao", self.scan, self.store, self.stats, self.report, self.prompt, None,
                            self.partial1 + self.partial2, self.cancel, self.prog)
        try:
            self.call_ui(lambda: self.apply_fuse(pkg))
        except BaseException:
            pkg.cleanup()
            raise

    def _begin_fuse(self):
        self.cur_stage = 3
        if self.pkg123:
            self.pkg123.cleanup()
            self.pkg123 = None
        self.pl.fusion_ready = False
        self.panes["pkg"].info.configure(text="")
        self.stage(3, "yellow", "Fundindo etapas 1, 2 e 3…")

    def apply_fuse(self, pkg):
        self.pkg123 = pkg
        self.pl.fusion_ready = True
        self.panes["pkg"].info.configure(
            text=f"📦 Pacote 1+2+3 pronto: {pkg.total_chars} caracteres ({human_size(pkg.total_bytes)}). "
                 f"Copie ou salve (com partes, se necessário). Nenhuma IA foi executada.")
        txt, tr = pkg.read_preview(PREVIEW_LIMIT)
        self.panes["pkg"].set_text(txt, pkg.total_chars if tr else None)
        self.stage(3, "green", "Prompt + pacote 1+2+3 prontos.", partial=bool(self.partial1 or self.partial2))
        self.status("Fusão concluída.")

    def on_copy_pkg(self):
        if self.pkg123:
            self.copy_store(self.pkg123, "Pacote 1+2+3", "PACOTE_FUSAO_1_2_3")

    def on_save_pkg(self):
        if self.pkg123:
            mode = getattr(self, 'prompt_mode', 'DOC')
            if mode == 'COD':
                # Pega o nome da pasta do projeto e a data/hora atual
                projeto = self.scan.root.name if (self.scan and self.scan.root) else "PROJETO"
                data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
                self.export_store(self.pkg123, f"{projeto}_{data_hora}", ext=".txt")
            else:
                # Se for DOC, salva como DOCUMENTACAO.md
                self.export_store(self.pkg123, "DOCUMENTACAO", ext=".md")

    # ------------------------------------------------------------ Etapa 4
    def on_attach(self):
        if self.busy:
            return
        p = filedialog.askopenfilename(title="Selecione o DOCUMENTACAO.md existente", initialdir=str(ROOT),
                                       filetypes=[("Markdown", "*.md"), ("Todos", "*.*")])
        if not p:
            return
        try:
            prev = read_previous_doc(p)
        except (OSError, ValueError) as exc:
            self.prev = None
            self.clear_data(4, "")
            self.clear_md()
            self.stage(4, "red", f"FALHA ao ler o anexo: {exc}")
            self.panes["final"].info.configure(text="Nenhum anexo carregado.")
            return
        self.prev = prev
        self.clear_data(4, "Invalidado: o anexo mudou; una novamente.")
        self.clear_md()
        self.panes["final"].info.configure(
            text=f"📎 Anexo carregado: {prev['name']} · {prev['size']} bytes · {prev['encoding']}\n"
                 f"Caminho: {prev['path']} — lido sem modificar o arquivo.")
        self.stage(4, "red", "Anexo carregado; falta UNIR TUDO.")
        self.toast("Documentação anterior anexada.", "ok")

    def on_detach(self):
        self.prev = None
        self.clear_data(4, "Invalidado: o anexo foi removido; una novamente.")
        self.clear_md()
        self.panes["final"].info.configure(text="Nenhum anexo. Sem anexo, o pacote final servirá para criar a documentação inicial.")
        self.stage(4, "red", "Anexo removido.")

    def on_final(self):
        if self.busy or not self.pl.green(1, 2, 3):
            return
        if self.prev is None and not messagebox.askyesno(
                APP_TITLE, "Nenhuma documentação anterior foi anexada.\n\nContinuar e preparar o pacote para criar a "
                           "documentação INICIAL (sem comparação com versão anterior)?"):
            return
        self.begin_stage(4, "Unindo…")
        self.run_job(self.job_final, "Unindo tudo...")

    def job_final(self):
        pkg = build_package("final", self.scan, self.store, self.stats, self.report, self.prompt, self.prev,
                            self.partial1 + self.partial2, self.cancel, self.prog)
        try:
            self.call_ui(lambda: self.apply_final(pkg))
        except BaseException:
            pkg.cleanup()
            raise

    def apply_final(self, pkg):
        self.final = pkg
        prev = self.prev
        modo = "ATUALIZAÇÃO (cenário B, com documentação anterior)" if prev else "DOCUMENTAÇÃO INICIAL (cenário A)"
        parcial = self.partial1 + self.partial2
        resumo = [
            f"PACOTE FINAL PRONTO — {modo}",
            f"Tamanho: {pkg.total_chars} caracteres ({human_size(pkg.total_bytes)})",
            f"SHA256: {pkg.sha}",
            "Integridade: " + ("COMPLETA" if not parcial else "PARCIAL — " + "; ".join(parcial)),
            "",
            "Conteúdo do pacote, nesta ordem: prompt padrão, manifesto, TREE, relatório da extração, "
            "conteúdo integral dos arquivos" + (", documentação anterior integral." if prev else "."),
            "",
            "Próximos passos: copie (ou salve em partes) e entregue à IA. A geração do DOCUMENTACAO.md "
            "pela IA é feita externamente; esta ferramenta não executa nenhuma IA.",
            "Se o pacote não couber no contexto da IA, use SALVAR com partes e envie-as em ordem.",
            "Quer uma documentação pronta SEM IA? Use a etapa 5 (Markdown final).",
        ]
        self.panes["final"].set_text("\n".join(resumo))
        self.stage(4, "green", "Pacote final pronto.", partial=bool(parcial))
        self.status("Pacote final preparado.")

    def on_copy_final(self):
        if self.final:
            self.copy_store(self.final, "Pacote final", "PACOTE_FINAL")

    def on_save_final(self):
        if self.final:
            self.export_store(self.final, "PACOTE_FINAL")

    # ------------------------------------------------------------ Etapa 5 (Markdown)
    def on_md(self):
        if self.busy or not self.pl.green(1, 2):
            return
        opts = Options.from_cfg(self.cfg)
        self.begin_stage(5, "Gerando Markdown…")
        self.run_job(lambda: self.job_md(opts), "Gerando Markdown...")

    def job_md(self, opts):
        md = build_markdown(self.scan, self.store, self.stats, opts, self.prev,
                            self.partial1 + self.partial2, self.cancel, self.prog)
        try:
            self.call_ui(lambda: self.apply_md(md))
        except BaseException:
            md.cleanup()
            raise

    def apply_md(self, md):
        self.mdstore = md
        txt, tr = md.read_preview(PREVIEW_LIMIT)
        self.panes["md"].set_text(txt, md.total_chars if tr else None, "md")
        self.panes["md"].info.configure(
            text=f"📝 DOCUMENTACAO_PROJETO.md pronto: {md.total_chars} caracteres ({human_size(md.total_bytes)})"
                 + (" · inclui a documentação anterior anexada" if self.prev else "") + ". Gerado localmente, sem IA.")
        self.stage(5, "green", f"{human_size(md.total_bytes)}", partial=bool(self.partial1 or self.partial2))
        self.status("Markdown gerado.")
        self.toast("Markdown final gerado! Salve com «💾 Salvar .md».", "ok")

    def on_copy_md(self):
        if self.mdstore:
            self.copy_store(self.mdstore, "Markdown", "DOCUMENTACAO_PROJETO")

    def on_save_md(self):
        if not self.mdstore or self.busy:
            return
        path = filedialog.asksaveasfilename(title="Salvar Markdown", initialdir=str(ROOT),
                                            initialfile="DOCUMENTACAO_PROJETO.md", defaultextension=".md",
                                            filetypes=[("Markdown", "*.md"), ("Todos", "*.*")])
        if not path:
            return
        store = self.mdstore

        def fn():
            size = write_store_file(store, path)
            self.ui(lambda: (self.status(f"Salvo em {path} ({human_size(size)})"),
                             self.toast(f"Markdown salvo ({human_size(size)}).", "ok")))
        self.cur_stage = None
        self.run_job(fn, "Gravando Markdown...")

    # ------------------------------------------------------------ GitHub / teste automatizado
    def on_github(self):
        if self.busy:
            return
        if shutil.which("git") is None:
            return messagebox.showerror(APP_TITLE, "Git não encontrado no PATH.\nInstale em https://git-scm.com/")
        with_doc = bool(self.mdstore and self.pl.green(5))
        public = True
        if not git_has_remote(ROOT):
            if shutil.which("gh") is None:
                return messagebox.showerror(
                    APP_TITLE, "Este projeto ainda não tem repositório remoto e o GitHub CLI (gh) não foi "
                               "encontrado.\nInstale em https://cli.github.com/ e rode «gh auth login».")
            ans = messagebox.askyesnocancel(
                APP_TITLE, f"Será criado o repositório «{ROOT.name}» no GitHub.\n\n"
                           f"SIM = público   ·   NÃO = privado   ·   CANCELAR = abortar")
            if ans is None:
                return
            public = ans
        curr_v = float(self.cfg.get("project_version", 1.0))
        default = DEFAULT_COMMIT_MSG + (" + documentação" if with_doc else "")
        
        dialog_text = f"Versão {curr_v:.1f}\nO que foi editado/implementado?\n(vazio = «{default}»):"
        msg = ctk.CTkInputDialog(text=dialog_text, title="Subir pro GitHub").get_input()
        if msg is None:
            return
            
        msg = msg.strip() or default
        final_msg = f"v{curr_v:.1f} - {msg}"
        
        store = self.mdstore if with_doc else None
        autotest = bool(self.cfg.get("autotest_before_push"))

        def fn():
            if autotest and run_autotest(ROOT, lambda t: self.prog(0, None, t)) is False:
                raise RuntimeError("Teste automatizado reprovou; push cancelado.")
            r = git_publish(ROOT, final_msg, store, PUSH_DOC_NAME, lambda t: self.prog(0, None, t), public)
            self.ui(lambda: self.github_done(r, curr_v))
        self.cur_stage = None
        self.run_job(fn, "Subindo para o GitHub...")

    def github_done(self, r, pushed_version=None):
        detail = "\n".join(r["log"][-25:])
        if r["ok"]:
            if pushed_version is not None:
                self.cfg["project_version"] = round(pushed_version + 0.1, 1)
                save_config(ROOT, self.cfg)
                
            extra = " (com documentação)" if r["doc_included"] else ""
            self.status("Publicado no GitHub" + extra + ".")
            self.toast("Subiu pro GitHub" + extra + "!", "ok", 5000)
            messagebox.showinfo(APP_TITLE, "Publicado com sucesso" + extra + ".\n\n" + detail)
        else:
            self.status("Falha ao subir: " + r["error"])
            self.toast("Falha ao subir pro GitHub.", "err", 6000)
            messagebox.showerror(APP_TITLE, r["error"] + "\n\n" + detail)

    def on_autotest(self):
        if self.busy:
            return
        res = run_autotest(ROOT)
        if res is None:
            self.toast("Teste automatizado: ainda não implementado.", "info")
        else:
            self.toast("Teste automatizado " + ("passou." if res else "REPROVOU."), "ok" if res else "err")

    # ------------------------------------------------------------ executar tudo
    def on_run_all(self):
        if self.busy:
            return
        mode = PromptModeDialog(self).result
        if not mode:
            return
        opts = Options.from_cfg(self.cfg)

        def fn():
            def stg(n, msg):
                self.call_ui(lambda: self.begin_stage(n, msg))
            stg(1, "Varrendo…")
            self.job_tree(opts)
            if self.cancel.is_set():
                raise Cancelled()
            stg(2, "Lendo…")
            self.job_content(opts)
            if self.cancel.is_set():
                raise Cancelled()
            stg(3, f"Prompt ({mode}) e fusão…")
            self.job_prompt(mode)
            self.job_fuse(clear=False)
            if self.cancel.is_set():
                raise Cancelled()
            stg(4, "Unindo…")
            self.job_final()
            if self.cancel.is_set():
                raise Cancelled()
            stg(5, "Gerando Markdown…")
            self.job_md(opts)
            self.ui(lambda: (self.toast("Tudo pronto! Pacotes e Markdown gerados.", "ok", 6000),
                             self.tabs.set("📝 Markdown")))
        self.cur_stage = None
        self.run_job(fn, "Executando todas as etapas...")

    # ------------------------------------------------------------ remontagem
    def on_remount(self):
        paths = filedialog.askopenfilenames(title="Selecione TODAS as partes", initialdir=str(ROOT),
                                            filetypes=[("Texto", "*.txt"), ("Todos", "*.*")])
        if not paths:
            return
        try:
            text, ok, msg = remount_parts(paths)
            with open(paths[0], "r", encoding="utf-8", newline="") as f:
                m = re.match(r"#### DOCUMENTADOR \| (.*?) \| PARTE", f.readline())
            base = m.group(1) if m else "CONTEUDO_PROJETO"
        except (ValueError, OSError) as exc:
            return messagebox.showerror(APP_TITLE, str(exc))
        messagebox.showinfo(APP_TITLE, msg)
        if ok:
            self.save_text(f"{base}_REMONTADO.txt", text, "Salvar conteúdo remontado")


# ----------------------------------------------------------------------------
# Autoteste (sem interface)
# ----------------------------------------------------------------------------

def recover_content(block):
    """Reconstrói o conteúdo original a partir de um bloco de texto (para teste)."""
    lines_sep = [m.start() for m in re.finditer(r"(?m)^={60}\n", block)]
    start = lines_sep[1] + 61
    m = re.search(r"<<< FIM DO ARQUIVO: .*? >>>\n\n$", block)
    body = block[start:m.start()]
    flag = re.search(r"TERMINA COM QUEBRA DE LINHA: (\S+)", block).group(1)
    if flag == "não":
        body = body[:-1]
    return body


def selftest():
    import shutil
    base = Path(tempfile.mkdtemp(prefix="doc_selftest_"))
    ok = True

    def check(cond, msg):
        nonlocal ok
        print(("OK   " if cond else "FALHA"), msg)
        ok = ok and cond

    try:
        proj = base / "proj"
        (proj / "sub" / "deep").mkdir(parents=True)
        (proj / "node_modules").mkdir()
        files = {
            "a.py": 'print("olá")\n'.encode("utf-8"),
            "sub/latin.txt": "ação e coração\n".encode("cp1252"),
            "sub/deep/crlf.txt": b"linha1\r\nlinha2 sem final",
            "sub/bom.txt": codecs.BOM_UTF8 + "bom ok\n".encode("utf-8"),
            "sub/u16.txt": "texto utf16 áé\n".encode("utf-16"),
            ".hidden": b"oculto\n", "semext": b"sem extensao\n", "vazio.txt": b"",
            "bin.dat": b"\x00\x01\x02\xff" * 100, "img.png": b"\x89PNG\r\n\x1a\n" + b"\x00" * 50,
            ".env": b"SEGREDO=1\n", "DOCUMENTACAO.md": b"# Doc antiga\n```py\nx\n```\nsem final",
            "TREE_PROJETO.txt": b"saida antiga", "PACOTE_FINAL_PARTE_001.txt": b"saida antiga 2",
            "DOCUMENTACAO_PROJETO.md": b"saida md antiga",
            "node_modules/x.js": b"//x\n",
            "grande.txt": ("linha grande ção\n" * 3000).encode("utf-8"),
            "crases.md": b"````\ncode\n````\n",
            "app.log": b"log\n", "sub/deep/keep.min.js": b"var a=1;\n", "package.json": b"{}\n",
        }
        for rel, data in files.items():
            (proj / rel).write_bytes(data)
        try:
            os.symlink(str(proj), str(proj / "sub" / "loop"), target_is_directory=True)
            has_link = True
        except (OSError, NotImplementedError):
            has_link = False
        cancel = threading.Event()
        outputs = {"bin.dat", "img.png", "TREE_PROJETO.txt", "PACOTE_FINAL_PARTE_001.txt", "DOCUMENTACAO_PROJETO.md"}

        # ---- regras
        rules = parse_rules("# comentário\nnode_modules/, *.log\nsub/deep/*.min.js\n.git/\n\n")
        check(len(rules) == 4, "parse_rules lê linhas, vírgulas e ignora comentários")
        check(match_rule(rules, "node_modules", "a/node_modules", True) == "node_modules/", "regra 'nome/' casa diretório em qualquer nível")
        check(match_rule(rules, "node_modules", "node_modules", False) is None, "regra 'nome/' não casa arquivo")
        check(match_rule(rules, "App.LOG", "x/App.LOG", False) == "*.log", "curinga de extensão, sem diferenciar maiúsculas")
        check(match_rule(rules, "keep.min.js", "sub/deep/keep.min.js", False) == "sub/deep/*.min.js", "regra por caminho relativo")
        check(match_rule([], "a", "a", False) is None, "sem regras nada casa")

        scan = scan_project(proj, Options(rules=[]), proj / "a.py", cancel)
        check(scan.files == len(files), f"TREE conta {scan.files} arquivos (esperado {len(files)})")
        check("[ESTA FERRAMENTA]" in scan.tree_text and "[SAÍDA GERADA PELA FERRAMENTA]" in scan.tree_text,
              "marca ferramenta e saídas na TREE")
        check(".hidden" in scan.tree_text and "semext" in scan.tree_text, "inclui ocultos e sem extensão")
        if has_link:
            check("LINK SIMBÓLICO PARA DIRETÓRIO" in scan.tree_text and scan.symlinks == 1,
                  "link simbólico identificado e não seguido (sem loop)")
        scan2 = scan_project(proj, Options(rules=rules), proj / "a.py", cancel)
        check("EXCLUÍDO POR REGRA: node_modules/" in scan2.tree_text and scan2.excluded_dirs == ["node_modules"],
              "exclusão de diretório visível e informada")
        check(any(e["name"] == "app.log" and e["status"] == "excluded" for e in scan2.entries)
              and any(e["name"] == "keep.min.js" and e["status"] == "excluded" for e in scan2.entries),
              "exclusão de arquivos por curinga e por caminho")
        for nm in ("PACOTE_FINAL.txt", "PACOTE_FUSAO_1_2_3_PARTE_002.txt", "CONTEUDO_PROJETO_REMONTADO.txt",
                   "DOCUMENTACAO_PROJETO.md"):
            check(bool(OUTPUT_RE.match(nm)), f"saída reconhecida: {nm}")
        check(not OUTPUT_RE.match("DOCUMENTACAO.md"), "DOCUMENTACAO.md do usuário NÃO é tratado como saída")

        opts = Options()
        store, stats = extract_contents(scan, opts, cancel)
        for rel, data in files.items():
            if rel in outputs or rel in ("app.log",) and False:
                continue
            idx = next(i for i, b in enumerate(store.index) if b["rel"] == rel)
            info = decode_bytes(data)
            rec = recover_content(store.read_block(idx))
            check(rec == info["text"], f"conteúdo preservado: {rel} [{info['encoding']}]")
        check({r for r, _, _ in stats.binary} == {"bin.dat", "img.png"}, "binários viram metadados")
        check(".env" in stats.sensitive, "arquivo sensível sinalizado")
        check(len(stats.ignored) == 3, "saídas antigas não contaminam a extração")
        check(not stats.errors, "sem erros de leitura")

        # paralelo == sequencial
        s1, _ = extract_contents(scan, Options(workers=1), cancel)
        s4, _ = extract_contents(scan, Options(workers=4), cancel)
        check(s1.sha == s4.sha == store.sha, "extração paralela idêntica à sequencial (mesmo SHA256)")
        s1.cleanup()
        s4.cleanup()
        store2, stats2 = extract_contents(scan2, opts, cancel)
        check(len(stats2.excluded) == 2 and not any(b["label"] == "texto" and b["rel"] == "app.log" for b in store2.index),
              "arquivos excluídos por regra não têm conteúdo incorporado")
        store2.cleanup()

        report = build_report(scan, stats, store, opts)
        check("RELATÓRIO DA EXTRAÇÃO" in report and store.sha in report, "relatório gerado")

        out = base / "out"
        out.mkdir()
        parts = write_content_files(store, out, "CONTEUDO_PROJETO", 7000)
        check(len(parts) > 3, f"exportação dividida em {len(parts)} partes")
        joined, sha_ok, msg = remount_parts([p for p, _ in parts])
        check(sha_ok and joined == store.read_all(), "remontagem idêntica (hash e conteúdo)")
        check(not list(out.glob("*.gravando_tmp")), "gravação atômica não deixa temporários")

        # ---- prompt, pipeline e pacotes
        prompt = build_prompt()
        for needle in ("DOCUMENTACAO.md", "CENÁRIO A", "CENÁRIO B", "Não invente", "COMPLETO", "PARCIAL",
                       "restante do arquivo", "partes numeradas"):
            check(needle.lower() in prompt.lower(), f"prompt contém: {needle}")

        pl = Pipeline()
        check(all(s == "red" for s in pl.state.values()) and len(pl.state) == 5, "todas as 5 etapas iniciam vermelhas")
        al = pl.allowed()
        check(al["tree"] and not al["content"] and not al["prompt"] and not al["fuse"] and not al["final"] and not al["md"],
              "pré-requisitos bloqueiam etapas posteriores")
        pl.state[1] = "green"
        check(pl.allowed()["content"] and not pl.allowed()["prompt"], "etapa 2 liberada após a 1")
        pl.state[2] = pl.state[3] = "green"
        pl.fusion_ready = True
        check(pl.allowed()["fuse"] and pl.allowed()["final"] and pl.allowed()["copy_pkg"] and pl.allowed()["md"],
              "fusão/união/markdown liberadas")
        pl.state[4] = pl.state[5] = "green"
        changed = pl.invalidate_from(2)
        check(changed == [2, 3, 4, 5] and pl.state[1] == "green" and not pl.fusion_ready
              and not pl.allowed()["final"] and not pl.allowed()["md"], "regerar etapa 2 invalida 2, 3, 4, 5 e a fusão")

        prev = dict(name="DOCUMENTACAO.md", path="x", text="# Doc antiga\n```py\nx\n```\nsem final",
                    size=10, sha="0" * 64, encoding="utf-8")
        fus = build_package("fusao", scan, store, stats, report, prompt, None, [], cancel)
        ftxt = fus.read_all()
        check(f"{SEC_BEGIN}{SEC_TREE} #####" in ftxt and scan.tree_text in ftxt and "NÃO INCLUÍDA" in ftxt,
              "pacote de fusão contém TREE e indica ausência de documentação anterior")
        check(all(store.read_block(i) in ftxt for i in range(len(store.index))), "pacote contém TODOS os blocos de conteúdo")
        fin = build_package("final", scan, store, stats, report, prompt, prev, ["1 caminho(s) não inspecionado(s)"], cancel)
        gtxt = fin.read_all()
        m = re.search(re.escape(SEC_BEGIN + SEC_PREV + " #####\n") + "(.*?)" + re.escape(SEC_END + SEC_PREV + " #####"),
                      gtxt, re.S)
        check(bool(m) and m.group(1).rstrip("\n") == prev["text"].rstrip("\n"), "documentação anterior incluída integralmente")
        check("PARCIAL" in gtxt and "Cenário B" in gtxt, "manifesto registra extração parcial e cenário B")
        fin0 = build_package("final", scan, store, stats, report, prompt, None, [], cancel)
        check("documentação inicial" in fin0.read_all() and SEC_BEGIN + SEC_PREV not in fin0.read_all().split("##### FIM: MANIFESTO")[1],
              "pacote final sem anexo cria documentação inicial")
        pparts = write_content_files(fin, out, "PACOTE_FINAL", 9000)
        pj, pok, _ = remount_parts([p for p, _ in pparts])
        check(pok and pj == gtxt, f"pacote final dividido em {len(pparts)} partes e remontado idêntico")
        rd = read_previous_doc(proj / "DOCUMENTACAO.md")
        check(rd["text"] == files["DOCUMENTACAO.md"].decode("utf-8") and rd["size"] == len(files["DOCUMENTACAO.md"]),
              "anexo lido sem alteração")

        # ---- Markdown final
        mdo = Options(md_emoji=True, md_collapse=True)
        md = build_markdown(scan, store, stats, mdo, prev, [], cancel)
        mtxt = md.read_all()
        check(mtxt.startswith("# 📚 proj") and "## 📋 Resumo executivo" in mtxt and "## 🌳 Estrutura do projeto" in mtxt,
              "markdown tem título, emojis e seções principais")
        check(scan.tree_text in mtxt, "markdown contém a TREE integral")
        check("| 🐍 Python |" in mtxt and "█" in mtxt, "markdown traz estatísticas por linguagem com barras")
        check("🟩 Node.js / npm" in mtxt, "markdown detecta tecnologia por arquivo marcador")
        check("<details>" in mtxt and '<a id="f-0"></a>' in mtxt, "markdown usa blocos recolhíveis e âncoras")
        check("`````" in mtxt and "````\ncode\n````\n" in mtxt, "cerca do markdown é mais longa que as crases do arquivo")
        check("> [!WARNING]" in mtxt and "`.env`" in mtxt, "markdown alerta sobre arquivo sensível")
        check("Documentação anterior" in mtxt and "# Doc antiga" in mtxt, "markdown inclui documentação anterior anexada")
        # conteúdo de cada arquivo de texto aparece integralmente
        miss = []
        for i, b in enumerate(store.index):
            if b["label"] == "texto":
                body = store.read_slice(i, b["meta"]["body_off"], b["meta"]["body_len"])
                if body and body not in mtxt:
                    miss.append(b["rel"])
        check(not miss, f"todos os corpos de arquivo aparecem no markdown {miss[:3]}")
        md.cleanup()
        md2 = build_markdown(scan, store, stats, Options(md_emoji=False, md_collapse=False, md_contents=False,
                                                         md_tree=False, md_stats=False), None, ["x"], cancel)
        t2 = md2.read_all()
        check("📚" not in t2 and "<details>" not in t2 and "PARCIAL" in t2 and "## Estrutura" not in t2,
              "markdown sem emojis/sem conteúdo/sem tree respeita as opções")
        md2.cleanup()

        # ---- configuração persistente
        cfgp = base / "cfg" / "config.json"
        c = dict(DEFAULT_CFG, rules_text="node_modules/\n*.log", maxmb=2.5, md_emoji=False, scale=1.2)
        check(save_config(proj, c, cfgp), "configuração gravada")
        c2 = load_config(proj, cfgp)
        check(c2["rules_text"] == c["rules_text"] and c2["maxmb"] == 2.5 and c2["md_emoji"] is False and c2["scale"] == 1.2,
              "configuração restaurada (por projeto e global)")
        check(load_config(base / "outro", cfgp)["rules_text"] == "" and load_config(base / "outro", cfgp)["scale"] == 1.2,
              "regras são por projeto; aparência é global")
        cfgp.write_text("{lixo", encoding="utf-8")
        check(load_config(proj, cfgp) == dict(DEFAULT_CFG), "configuração corrompida volta ao padrão sem erro")

        # ---- exclusões prontas (caixas de seleção)
        check(len(PRESET_ALL) >= 20 and PRESET_RECOMMENDED <= set(PRESET_ALL), f"{len(PRESET_ALL)} exclusões prontas; recomendadas são subconjunto")
        cx = dict(DEFAULT_CFG, excl_checked=["node_modules/", "*.log", "Code Cache/"], rules_text="sub/deep/*.min.js")
        er = effective_rules(cx)
        check(len(er) == 4 and Options.from_cfg(cx).rules == er, "marcadas + personalizadas viram regras efetivas")
        check(match_rule(er, "code cache", "x/Chrome/Code Cache", True) == "Code Cache/", "nome com espaço e caixa diferente casa em qualquer nível")
        scan3 = scan_project(proj, Options(rules=er), proj / "a.py", cancel)
        check("node_modules" in scan3.excluded_dirs and any(e["name"] == "app.log" and e["status"] == "excluded" for e in scan3.entries),
              "TREE aplica as exclusões marcadas")
        save_config(proj, cx, cfgp)
        check(load_config(proj, cfgp)["excl_checked"] == ["node_modules/", "*.log", "Code Cache/"], "exclusões marcadas persistem")
        check(load_config(base / "novo", base / "nao_existe.json")["excl_checked"] == [], "padrão: nada marcado")

        # ---- publicação no GitHub (git local + remoto "bare"; gh não é necessário)
        if shutil.which("git"):
            for k, v in (("GIT_AUTHOR_NAME", "t"), ("GIT_AUTHOR_EMAIL", "t@t"),
                         ("GIT_COMMITTER_NAME", "t"), ("GIT_COMMITTER_EMAIL", "t@t")):
                os.environ.setdefault(k, v)
            gp, bare = base / "gitproj", base / "remote.git"
            gp.mkdir()
            (gp / "x.py").write_text("print(1)\n", encoding="utf-8")
            git_run(["git", "init", "--bare", str(bare)], base)
            git_run(["git", "init"], gp)
            git_run(["git", "branch", "-M", "main"], gp)
            git_run(["git", "remote", "add", "origin", str(bare)], gp)
            mdt = build_markdown(scan, store, stats, Options(), None, [], cancel)
            r1 = git_publish(gp, "teste", mdt)
            mdt.cleanup()
            _, tree_out, _ = git_run(["git", "--git-dir", str(bare), "ls-tree", "-r", "--name-only", "main"], base)
            check(r1["ok"] and r1["pushed"] and r1["committed"] and r1["doc_included"],
                  "git_publish: commit + push com documentação")
            check({"x.py", ".gitignore", PUSH_DOC_NAME} <= set(tree_out.split()),
                  "remoto recebeu projeto, .gitignore e a documentação gerada")
            r2 = git_publish(gp, "nada", None)
            check(r2["ok"] and not r2["committed"] and not r2["doc_included"], "sem alterações: não cria commit, push ok")
            check(run_autotest(gp) is None, "teste automatizado é resquício (retorna None)")
        else:
            print("PULADO git não instalado: teste de publicação")

        for s in (fus, fin, fin0, store):
            s.cleanup()
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("\nRESULTADO:", "TODOS OS TESTES PASSARAM" if ok else "HÁ FALHAS")
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if ctk is None:
        msg = ("Este aplicativo usa CustomTkinter.\nInstale com:  pip install customtkinter\n"
               "(O modo --selftest funciona sem ele.)")
        print(msg)
        try:  # tenta avisar também por janela, se o Tk básico existir
            import tkinter
            from tkinter import messagebox as mb
            r = tkinter.Tk()
            r.withdraw()
            mb.showerror(APP_TITLE, msg)
        except Exception:
            pass
        sys.exit(1)
    sys.setrecursionlimit(max(sys.getrecursionlimit(), 20000))  # árvores muito profundas
    if os.name == "nt":
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass
    ctk.set_default_color_theme("blue")
    App().mainloop()


if __name__ == "__main__":
    main()
``````

</details>

<a id="f-97"></a>
<details>
<summary>🧾 <b>historico.json</b> — JSON · 319 B · 18 linhas · utf-8</summary>

```json
{
  "LIS-GIG-12/2026-BRL": {
    "soma": 293897.0,
    "quantidade": 43
  },
  "LIS-GRU-12/2026-BRL": {
    "soma": 183931.0,
    "quantidade": 33
  },
  "OPO-GIG-12/2026-BRL": {
    "soma": 436996.0,
    "quantidade": 60
  },
  "OPO-GRU-12/2026-BRL": {
    "soma": 195737.0,
    "quantidade": 35
  }
}
```

</details>

<a id="f-98"></a>
<details>
<summary>🐍 <b>historico.py</b> — Python · 2.2 KB · 64 linhas · utf-8</summary>

```python
"""
historico.py
------------
Motor de inteligência de preços do FlyScanner.
Aprende a média de cada rota com base no fluxo do buscador e calcula o score de desconto.
"""
import json
import os

ARQUIVO_HISTORICO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "historico.json")

def carregar_db():
    if not os.path.exists(ARQUIVO_HISTORICO):
        return {}
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def salvar_db(db):
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def processar_score(voo: dict) -> dict:
    """
    Recebe um voo, atualiza a média histórica daquela rota/mês
    e injeta a pontuação de desconto no dicionário do voo.
    """
    db = carregar_db()
    
    # Chave única para a média: Ex: "GIG-LIS-12-2026-BRL"
    mes_ano = voo.get("data_ida", "")[3:] if voo.get("data_ida") else "geral"
    chave = f"{voo.get('origem')}-{voo.get('destino')}-{mes_ano}-{voo.get('moeda')}"
    preco_atual = float(voo.get("valor", 0))

    if preco_atual <= 0:
        voo["score"] = 0
        return voo

    # Se a rota já existe no banco, calcula o score baseado na média histórica
    if chave in db:
        media_historica = db[chave]["soma"] / db[chave]["quantidade"]
        
        # Lógica de Pontos: (Média - Preço Atual) / Média * 100
        # Ex: Média 2500, Atual 2000 -> (500 / 2500) * 100 = 20 pontos
        if preco_atual < media_historica:
            desconto_percentual = ((media_historica - preco_atual) / media_historica) * 100
            voo["score"] = int(desconto_percentual)
        else:
            voo["score"] = 0 # Está mais caro ou igual à média
            
        # Atualiza o banco de dados com o novo preço encontrado para manter a média viva
        db[chave]["soma"] += preco_atual
        db[chave]["quantidade"] += 1
    else:
        # Primeira vez que o robô vê essa rota no mês. Não há como comparar ainda.
        voo["score"] = 0
        db[chave] = {"soma": preco_atual, "quantidade": 1}

    # Salva o aprendizado
    salvar_db(db)
    
    return voo
```

</details>

<a id="f-99"></a>
<details>
<summary>🐍 <b>interface.pyw</b> — Python · 31.0 KB · 658 linhas · utf-8</summary>

```python
"""
interface.py
------------
Ponto de entrada da aplicação (é este arquivo que você roda: `python interface.py`).
"""

import json
import os
import queue
import re

import customtkinter as ctk

import apis
import buscador
import condicoes as condicoes_mod
import log
from tkcalendar import DateEntry

ARQUIVO_CONFIG_APIS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_apis.json")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- PALETA DE CORES GLOBAL (Estilo Nubank/Fintech) ---
COR_FUNDO = "#09090B"
COR_CARD = "#18181B"
COR_DESTAQUE = "#820AD1"
COR_HOVER_DESTAQUE = "#6B08A4"
COR_TEXTO = "#E4E4E7"
COR_TEXTO_SECUNDARIO = "#A1A1AA"
COR_INPUT_BG = "#27272A"
COR_INPUT_HOVER = "#3F3F46"

FONTE_TITULO = ("Segoe UI", 16, "bold")
FONTE_LABEL = ("Segoe UI", 13)


def carregar_config_apis() -> dict:
    if not os.path.exists(ARQUIVO_CONFIG_APIS):
        return {"input": {}, "output": {}, "input_ativas": [], "output_ativas": [], "ordem_inputs": [], "ordem_outputs": []}
    try:
        with open(ARQUIVO_CONFIG_APIS, "r", encoding="utf-8") as f:
            dados = json.load(f)
        dados.setdefault("input", {})
        dados.setdefault("output", {})
        dados.setdefault("input_ativas", [])
        dados.setdefault("output_ativas", [])
        dados.setdefault("ordem_inputs", [])
        dados.setdefault("ordem_outputs", [])
        return dados
    except (json.JSONDecodeError, OSError):
        return {"input": {}, "output": {}, "input_ativas": [], "output_ativas": [], "ordem_inputs": [], "ordem_outputs": []}


def salvar_config_apis(dados: dict) -> None:
    with open(ARQUIVO_CONFIG_APIS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


class JanelaLog(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("FlyScanner - Log")
        self.geometry("800x500")
        self.protocol("WM_DELETE_WINDOW", self.withdraw)

        topo = ctk.CTkFrame(self)
        topo.pack(fill="x", padx=10, pady=(10, 0))
        ctk.CTkLabel(topo, text="Log do sistema", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left")
        ctk.CTkButton(topo, text="Limpar log", width=100, command=self._limpar).pack(side="right")

        self.caixa_log = ctk.CTkTextbox(self, wrap="word", font=("Consolas", 12))
        self.caixa_log.pack(fill="both", expand=True, padx=10, pady=10)
        self.caixa_log.configure(state="disabled")

        self._fila = log.nova_fila_de_escuta()
        self._popular_log_existente()
        self._checar_fila()

    def _popular_log_existente(self):
        conteudo = log.ler_log_completo()
        if conteudo:
            self.caixa_log.configure(state="normal")
            self.caixa_log.insert("end", conteudo)
            self.caixa_log.see("end")
            self.caixa_log.configure(state="disabled")

    def _limpar(self):
        log.limpar_log()
        self.caixa_log.configure(state="normal")
        self.caixa_log.delete("1.0", "end")
        self.caixa_log.configure(state="disabled")

    def _checar_fila(self):
        try:
            while True:
                linha = self._fila.get_nowait()
                self.caixa_log.configure(state="normal")
                self.caixa_log.insert("end", linha + "\n")
                self.caixa_log.see("end")
                self.caixa_log.configure(state="disabled")
        except queue.Empty:
            pass
        finally:
            self.after(500, self._checar_fila)


class FlyScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FlyScanner - Buscar Passagens")
        self.geometry("980x750")

        self.robo = buscador.Robo(intervalo_segundos=60)
        self.config_apis = carregar_config_apis()

        self.modulos_input = apis.listar_apis_input()
        self.modulos_output = apis.listar_apis_output()

        # Garante que novas APIs adicionadas aos arquivos apareçam na ordem
        for ch in self.modulos_input:
            if ch not in self.config_apis["ordem_inputs"]:
                self.config_apis["ordem_inputs"].append(ch)
        for ch in self.modulos_output:
            if ch not in self.config_apis["ordem_outputs"]:
                self.config_apis["ordem_outputs"].append(ch)

        self._entradas_input = {}
        self._checkbox_input = {}
        self._entradas_output = {}
        self._checkbox_output = {}

        self._montar_ui()
        self._janela_log = JanelaLog(self)
        self._janela_log.withdraw()

        log.registrar("Interface iniciada.", nivel="INFO", origem="interface")

    # ------------------------------------------------------------------ UI

    def _montar_ui(self):
        barra_topo = ctk.CTkFrame(self)
        barra_topo.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(barra_topo, text="FlyScanner", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx=5)
        ctk.CTkButton(barra_topo, text="Ver Log", width=100, command=self._abrir_janela_log).pack(side="right", padx=5)

        self.botao_robo = ctk.CTkButton(
            barra_topo, text="▶ Rodar Robô", fg_color="#2e7d32", hover_color="#1b5e20",
            width=140, command=self._alternar_robo,
        )
        self.botao_robo.pack(side="right", padx=5)

        self.abas = ctk.CTkTabview(self)
        self.abas.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.abas.add("Fila de Inputs")
        self.abas.add("Condições")
        self.abas.add("Retornos")

        self._montar_aba_inputs(self.abas.tab("Fila de Inputs"))
        self._montar_aba_condicoes(self.abas.tab("Condições"))
        self._montar_aba_retorno(self.abas.tab("Retornos"))

    # ---- Aba 1: Inputs (Reativos e Reordenáveis) ------------------------

    def _montar_aba_inputs(self, aba):
        aba.configure(fg_color=COR_FUNDO)
        self.scroll_inputs = ctk.CTkScrollableFrame(aba, fg_color="transparent")
        self.scroll_inputs.pack(fill="both", expand=True, padx=20, pady=10)

        self.container_cards_input = ctk.CTkFrame(self.scroll_inputs, fg_color="transparent")
        self.container_cards_input.pack(fill="x", expand=True)

        btn_salvar = ctk.CTkButton(
            self.scroll_inputs, text="Salvar Fila e Integrações", font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=COR_DESTAQUE, hover_color=COR_HOVER_DESTAQUE, height=50, corner_radius=10,
            command=self._salvar_inputs
        )
        btn_salvar.pack(pady=20, fill="x", padx=100)

        self._renderizar_cards_inputs()

    def _renderizar_cards_inputs(self):
        # Limpa tudo antes de redesenhar
        for widget in self.container_cards_input.winfo_children():
            widget.destroy()

        self._entradas_input.clear()
        self._checkbox_input.clear()

        ativas_salvas = set(self.config_apis.get("input_ativas", []))
        ordem = [ch for ch in self.config_apis["ordem_inputs"] if ch in self.modulos_input]

        if not ordem:
            ctk.CTkLabel(self.container_cards_input, text="Nenhuma API encontrada.", text_color=COR_TEXTO_SECUNDARIO).pack(pady=20)
            return

        for index, chave in enumerate(ordem):
            modulo = self.modulos_input[chave]
            
            card = ctk.CTkFrame(self.container_cards_input, fg_color=COR_CARD, corner_radius=12)
            card.pack(fill="x", pady=(0, 15))
            
            # --- HEADER DO CARD (Reordenação + Toggle) ---
            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=20, pady=(15, 10))
            
            frame_setas = ctk.CTkFrame(header, fg_color="transparent")
            frame_setas.pack(side="left", padx=(0, 15))
            
            # Botão Subir
            btn_up = ctk.CTkButton(frame_setas, text="▲", width=30, height=20, fg_color=COR_INPUT_BG, hover_color=COR_INPUT_HOVER, text_color=COR_TEXTO_SECUNDARIO)
            btn_up.pack(pady=(0, 2))
            if index > 0:
                btn_up.configure(command=lambda c=chave, d=-1: self._mover_card_input(c, d))
            else:
                btn_up.configure(state="disabled", fg_color="transparent")
                
            # Botão Descer
            btn_down = ctk.CTkButton(frame_setas, text="▼", width=30, height=20, fg_color=COR_INPUT_BG, hover_color=COR_INPUT_HOVER, text_color=COR_TEXTO_SECUNDARIO)
            btn_down.pack()
            if index < len(ordem) - 1:
                btn_down.configure(command=lambda c=chave, d=1: self._mover_card_input(c, d))
            else:
                btn_down.configure(state="disabled", fg_color="transparent")

            var = ctk.BooleanVar(value=(chave in ativas_salvas))
            self._checkbox_input[chave] = var
            
            chk = ctk.CTkSwitch(
                header, text=f"{index + 1}º Fila | {modulo.NOME} [{'Ativa' if var.get() else 'Inativa'}]", 
                variable=var, font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO,
                progress_color=COR_DESTAQUE, button_color="#FFFFFF", button_hover_color=COR_TEXTO
            )
            chk.configure(command=lambda v=var, c=chk, n=modulo.NOME, i=index: c.configure(text=f"{i + 1}º Fila | {n} [{'Ativa' if v.get() else 'Inativa'}]"))
            chk.pack(side="left")

            # --- CONTEÚDO DO CARD (Credenciais e Intervalo) ---
            self._entradas_input[chave] = {}
            valores_salvos = self.config_apis["input"].get(chave, {})
            
            conteudo = ctk.CTkFrame(card, fg_color="transparent")
            conteudo.pack(fill="x", padx=20, pady=(0, 15))

            # Campo Fixo: Cooldown (Intervalo)
            linha_tempo = ctk.CTkFrame(conteudo, fg_color="transparent")
            linha_tempo.pack(fill="x", pady=(0, 10))
            ctk.CTkLabel(linha_tempo, text="Repetir busca a cada (Minutos)", text_color=COR_DESTAQUE, font=ctk.CTkFont(*FONTE_LABEL, weight="bold"), width=200, anchor="w").pack(side="left", padx=(0, 10))
            
            ent_tempo = ctk.CTkEntry(linha_tempo, height=40, border_width=1, corner_radius=8, width=120)
            ent_tempo.pack(side="left")
            ent_tempo.insert(0, str(valores_salvos.get("intervalo_minutos", "60")))
            self._entradas_input[chave]["intervalo_minutos"] = ent_tempo

            for campo in getattr(modulo, "CAMPOS_CONFIG", []):
                linha = ctk.CTkFrame(conteudo, fg_color="transparent")
                linha.pack(fill="x", pady=5)
                
                ctk.CTkLabel(linha, text=campo["label"], text_color=COR_TEXTO_SECUNDARIO, font=ctk.CTkFont(*FONTE_LABEL), width=200, anchor="w").pack(side="left", padx=(0, 10))
                
                is_senha = campo.get("tipo") == "senha"
                entrada = ctk.CTkEntry(linha, height=40, border_width=1, corner_radius=8, show="*" if is_senha else "")
                entrada.pack(side="left", fill="x", expand=True)
                
                if campo["chave"] in valores_salvos:
                    entrada.insert(0, valores_salvos[campo["chave"]])
                
                self._entradas_input[chave][campo["chave"]] = entrada
                
                if is_senha:
                    def toggle_senha(e=entrada, b=None):
                        if e.cget("show") == "*":
                            e.configure(show="")
                            b.configure(text="Ocultar")
                        else:
                            e.configure(show="*")
                            b.configure(text="Mostrar")

                    btn_olho = ctk.CTkButton(
                        linha, text="Mostrar", width=70, height=40, fg_color=COR_INPUT_BG, 
                        text_color=COR_TEXTO_SECUNDARIO, hover_color=COR_INPUT_HOVER, corner_radius=8
                    )
                    btn_olho.configure(command=lambda e=entrada, b=btn_olho: toggle_senha(e, b))
                    btn_olho.pack(side="left", padx=(10, 0))

    def _mover_card_input(self, chave, direcao):
        """Salva o estado atual, move o array e redesenha a tela."""
        self._salvar_inputs(silencioso=True)
        
        ordem = self.config_apis["ordem_inputs"]
        idx = ordem.index(chave)
        novo_idx = idx + direcao
        
        # Faz o Swap
        ordem[idx], ordem[novo_idx] = ordem[novo_idx], ordem[idx]
        self._renderizar_cards_inputs()

    def _salvar_inputs(self, silencioso=False):
        for chave, campos in self._entradas_input.items():
            self.config_apis["input"][chave] = {
                campo_chave: widget.get() for campo_chave, widget in campos.items()
            }
            # Converte o intervalo pra int no JSON
            try:
                self.config_apis["input"][chave]["intervalo_minutos"] = int(self.config_apis["input"][chave].get("intervalo_minutos", 60))
            except:
                self.config_apis["input"][chave]["intervalo_minutos"] = 60
        
        ativas = [chave for chave, var in self._checkbox_input.items() if var.get()]
        self.config_apis["input_ativas"] = ativas
        
        # Mantém a ordem definida pela UI
        self.config_apis["ordem_inputs"] = [ch for ch in self.config_apis["ordem_inputs"] if ch in self.modulos_input]
        salvar_config_apis(self.config_apis)
        
        if not silencioso:
            msg_log = f"Fila de Inputs salva. APIs ativas: {len(ativas)}"
            log.registrar_sucesso(msg_log, origem="interface")

    # ---- Aba 2: Condições (Padrão Startup) -----------------------------

    def _montar_aba_condicoes(self, aba):
        aba.configure(fg_color=COR_FUNDO) 
        scroll = ctk.CTkScrollableFrame(aba, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=10)

        atuais = condicoes_mod.carregar()
        self._campos_condicoes = {}

        # CARD 1: ROTA
        card_rota = ctk.CTkFrame(scroll, fg_color=COR_CARD, corner_radius=12)
        card_rota.pack(fill="x", pady=(0, 15))
        
        ctk.CTkLabel(card_rota, text="✈️ Rota de Voo", font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO).pack(anchor="w", padx=20, pady=(15, 10))

        frame_grid_rota = ctk.CTkFrame(card_rota, fg_color="transparent")
        frame_grid_rota.pack(fill="x", padx=20, pady=(0, 15))
        frame_grid_rota.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(frame_grid_rota, text="Origem", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self._entrada_origem = ctk.CTkEntry(frame_grid_rota, height=40, border_width=1, corner_radius=8, placeholder_text="Ex: GIG, CGH, LIS")
        self._entrada_origem.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        self._entrada_origem.insert(0, str(atuais.get("origem", "")))
        self._entrada_origem.bind("<KeyRelease>", lambda e: self._sugerir_multiplos_aeroportos(e, self._entrada_origem))
        self._campos_condicoes["origem"] = self._entrada_origem

        ctk.CTkLabel(frame_grid_rota, text="Destino", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=1, sticky="w", pady=(0, 5))
        self._entrada_destino = ctk.CTkEntry(frame_grid_rota, height=40, border_width=1, corner_radius=8, placeholder_text="Ex: JFK, MCO")
        self._entrada_destino.grid(row=1, column=1, sticky="ew")
        self._entrada_destino.insert(0, str(atuais.get("destino", "")))
        self._entrada_destino.bind("<KeyRelease>", lambda e: self._sugerir_multiplos_aeroportos(e, self._entrada_destino))
        self._campos_condicoes["destino"] = self._entrada_destino

        # CARD 2: DATAS E FLEXIBILIDADE
        card_datas = ctk.CTkFrame(scroll, fg_color=COR_CARD, corner_radius=12)
        card_datas.pack(fill="x", pady=15)
        
        ctk.CTkLabel(card_datas, text="📅 Planejamento de Tempo", font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO).pack(anchor="w", padx=20, pady=(15, 10))

        frame_grid_datas = ctk.CTkFrame(card_datas, fg_color="transparent")
        frame_grid_datas.pack(fill="x", padx=20, pady=(0, 15))
        frame_grid_datas.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(frame_grid_datas, text="Modalidade", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.var_tipo_viagem = ctk.StringVar(value=atuais.get("tipo_viagem", "ida_volta"))
        btn_tipo = ctk.CTkSegmentedButton(
            frame_grid_datas, values=["ida", "ida_volta"], variable=self.var_tipo_viagem,
            command=self._alternar_datas, selected_color=COR_DESTAQUE, selected_hover_color=COR_HOVER_DESTAQUE, height=35
        )
        btn_tipo.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        self._campos_condicoes["tipo_viagem"] = btn_tipo

        ctk.CTkLabel(frame_grid_datas, text="Data de Ida (DD/MM/AAAA)", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=1, sticky="w", pady=(0, 5))
        self.entrada_ida = ctk.CTkEntry(frame_grid_datas, height=40, border_width=1, corner_radius=8, placeholder_text="Ex: 15/08/2026")
        self.entrada_ida.grid(row=1, column=1, sticky="ew", padx=(0, 10))
        self.entrada_ida.insert(0, atuais.get("data_ida", ""))
        self.entrada_ida.bind("<KeyRelease>", lambda e: self._aplicar_mascara_data(e, self.entrada_ida))

        ctk.CTkLabel(frame_grid_datas, text="Data de Volta (DD/MM/AAAA)", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=2, sticky="w", pady=(0, 5))
        self.entrada_volta = ctk.CTkEntry(frame_grid_datas, height=40, border_width=1, corner_radius=8, placeholder_text="Ex: 25/08/2026")
        self.entrada_volta.grid(row=1, column=2, sticky="ew")
        self.entrada_volta.insert(0, atuais.get("data_volta", ""))
        self.entrada_volta.bind("<KeyRelease>", lambda e: self._aplicar_mascara_data(e, self.entrada_volta))

        # CARD 3: ORÇAMENTO
        card_financas = ctk.CTkFrame(scroll, fg_color=COR_CARD, corner_radius=12)
        card_financas.pack(fill="x", pady=15)
        
        ctk.CTkLabel(card_financas, text="💰 Inteligência Financeira", font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO).pack(anchor="w", padx=20, pady=(15, 10))

        frame_grid_financas = ctk.CTkFrame(card_financas, fg_color="transparent")
        frame_grid_financas.pack(fill="x", padx=20, pady=(0, 20))
        frame_grid_financas.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(frame_grid_financas, text="Moeda Base", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.var_moeda = ctk.StringVar(value=atuais.get("moeda", "BRL - Real"))
        self.combo_moeda = ctk.CTkOptionMenu(
            frame_grid_financas, values=["BRL - Real", "USD - Dólar", "EUR - Euro", "GBP - Libra"], 
            variable=self.var_moeda, command=self._atualizar_sifrao, height=40, 
            fg_color=COR_INPUT_BG, button_color=COR_INPUT_HOVER, button_hover_color=COR_DESTAQUE
        )
        self.combo_moeda.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        self._campos_condicoes["moeda"] = self.combo_moeda

        ctk.CTkLabel(frame_grid_financas, text="Máximo Teto", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=1, sticky="w", pady=(0, 5))
        self.entrada_vmax = ctk.CTkEntry(frame_grid_financas, height=40, border_width=1, corner_radius=8, font=ctk.CTkFont(*FONTE_LABEL))
        self.entrada_vmax.grid(row=1, column=1, sticky="ew")
        self.entrada_vmax.insert(0, self._formatar_para_moeda(atuais.get("valor_maximo", ""), atuais.get("moeda", "BRL")))
        self.entrada_vmax.bind("<FocusOut>", lambda e: self._aplicar_mascara_moeda(self.entrada_vmax))
        
        self.var_menor_preco = ctk.BooleanVar(value=str(atuais.get("apenas_menor_preco", "false")).lower() == "true")
        chk_historico = ctk.CTkSwitch(
            card_financas, text="🔥 Apenas Menor Preço Histórico", variable=self.var_menor_preco,
            font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_DESTAQUE, progress_color=COR_DESTAQUE
        )
        chk_historico.pack(padx=20, pady=(0, 20), anchor="w")

        btn_salvar = ctk.CTkButton(
            scroll, text="Salvar Estratégia de Busca", font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=COR_DESTAQUE, hover_color=COR_HOVER_DESTAQUE, height=50, corner_radius=10,
            command=self._salvar_condicoes
        )
        btn_salvar.pack(pady=20, fill="x", padx=100)

        self._alternar_datas(self.var_tipo_viagem.get())

    # --- Funções Auxiliares Aba 2 ---
    def _sugerir_multiplos_aeroportos(self, event, widget):
        if event.keysym in ("BackSpace", "Shift_L", "Shift_R", "Control_L"): return
        texto_completo = widget.get().upper()
        termos = [t.strip() for t in texto_completo.split(",")]
        termo_atual = termos[-1]
        if len(termo_atual) < 3: return
        db_aeroportos = {"RIO": "GIG", "SAO": "GRU", "NOV": "JFK", "LIS": "LIS", "PAR": "CDG"}
        for chave, codigo in db_aeroportos.items():
            if termo_atual.startswith(chave):
                termos[-1] = codigo
                novo_texto = ", ".join(termos) + ", "
                widget.delete(0, "end")
                widget.insert(0, novo_texto)
                widget.icursor("end")
                break

    def _aplicar_mascara_data(self, event, widget):
        if event.keysym in ("BackSpace", "Delete", "Left", "Right"): return
        texto = re.sub(r"[^\d]", "", widget.get())
        if len(texto) > 2: texto = texto[:2] + "/" + texto[2:]
        if len(texto) > 5: texto = texto[:5] + "/" + texto[5:9]
        widget.delete(0, "end")
        widget.insert(0, texto[:10])

    def _alternar_datas(self, valor_selecionado):
        if valor_selecionado == "ida":
            self.entrada_volta.configure(state="disabled", fg_color=COR_INPUT_BG, text_color="#52525B")
        else:
            self.entrada_volta.configure(state="normal", fg_color=["#F9F9FA", "#343638"], text_color=["gray10", "#DCE4EE"])

    def _atualizar_sifrao(self, valor_selecionado):
        self._aplicar_mascara_moeda(self.entrada_vmax, valor_selecionado)

    def _obter_sifrao(self, moeda_str):
        mapa = {"BRL": "R$ ", "USD": "$ ", "EUR": "€ ", "GBP": "£ "}
        return mapa.get(moeda_str[:3], "$ ")

    def _formatar_para_moeda(self, valor_bruto, moeda_str):
        if not valor_bruto: return ""
        try:
            valor_float = float(str(valor_bruto).replace(",", ".").replace(self._obter_sifrao(moeda_str), "").strip())
            sifrao = self._obter_sifrao(moeda_str)
            return f"{sifrao}{valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except ValueError:
            return str(valor_bruto)

    def _aplicar_mascara_moeda(self, widget, moeda_forca=None):
        moeda_str = moeda_forca if moeda_forca else self.var_moeda.get()
        texto_limpo = re.sub(r"[^\d,.-]", "", widget.get())
        texto_formatado = self._formatar_para_moeda(texto_limpo, moeda_str)
        widget.delete(0, "end")
        widget.insert(0, texto_formatado)

    def _limpar_moeda_para_salvar(self, texto_formatado):
        if not texto_formatado: return ""
        limpo = re.sub(r"[^\d,.-]", "", texto_formatado)
        return limpo.replace(".", "").replace(",", ".")

    def _salvar_condicoes(self):
        novas = {
            "origem": self._campos_condicoes["origem"].get(),
            "destino": self._campos_condicoes["destino"].get(),
            "tipo_viagem": self.var_tipo_viagem.get(),
            "data_ida": self.entrada_ida.get(),
            "data_volta": self.entrada_volta.get() if self.var_tipo_viagem.get() == "ida_volta" else "",
            "valor_maximo": self._limpar_moeda_para_salvar(self.entrada_vmax.get()),
            "moeda": self.var_moeda.get()[:3],
            "apenas_menor_preco": self.var_menor_preco.get()
        }
        condicoes_mod.salvar(novas)
        log.registrar_sucesso("Estratégia de busca salva.", origem="interface")


    # ---- Aba 3: Retorno (UX Premium Reordenável) ------------------------

    def _montar_aba_retorno(self, aba):
        aba.configure(fg_color=COR_FUNDO)
        self.scroll_outputs = ctk.CTkScrollableFrame(aba, fg_color="transparent")
        self.scroll_outputs.pack(fill="both", expand=True, padx=20, pady=10)

        self.container_cards_output = ctk.CTkFrame(self.scroll_outputs, fg_color="transparent")
        self.container_cards_output.pack(fill="x", expand=True)

        btn_salvar = ctk.CTkButton(
            self.scroll_outputs, text="Salvar Destinos de Retorno", font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=COR_DESTAQUE, hover_color=COR_HOVER_DESTAQUE, height=50, corner_radius=10,
            command=self._salvar_retorno
        )
        btn_salvar.pack(pady=20, fill="x", padx=100)

        self._renderizar_cards_outputs()

    def _renderizar_cards_outputs(self):
        for widget in self.container_cards_output.winfo_children():
            widget.destroy()

        self._entradas_output.clear()
        self._checkbox_output.clear()

        ativas_salvas = set(self.config_apis.get("output_ativas", []))
        ordem = [ch for ch in self.config_apis["ordem_outputs"] if ch in self.modulos_output]

        if not ordem:
            ctk.CTkLabel(self.container_cards_output, text="Nenhuma API de saída encontrada.", text_color=COR_TEXTO_SECUNDARIO).pack(pady=20)
            return

        for index, chave in enumerate(ordem):
            modulo = self.modulos_output[chave]
            
            card = ctk.CTkFrame(self.container_cards_output, fg_color=COR_CARD, corner_radius=12)
            card.pack(fill="x", pady=(0, 15))
            
            # --- HEADER ---
            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=20, pady=(15, 10))
            
            frame_setas = ctk.CTkFrame(header, fg_color="transparent")
            frame_setas.pack(side="left", padx=(0, 15))
            
            btn_up = ctk.CTkButton(frame_setas, text="▲", width=30, height=20, fg_color=COR_INPUT_BG, hover_color=COR_INPUT_HOVER, text_color=COR_TEXTO_SECUNDARIO)
            btn_up.pack(pady=(0, 2))
            if index > 0: btn_up.configure(command=lambda c=chave, d=-1: self._mover_card_output(c, d))
            else: btn_up.configure(state="disabled", fg_color="transparent")
                
            btn_down = ctk.CTkButton(frame_setas, text="▼", width=30, height=20, fg_color=COR_INPUT_BG, hover_color=COR_INPUT_HOVER, text_color=COR_TEXTO_SECUNDARIO)
            btn_down.pack()
            if index < len(ordem) - 1: btn_down.configure(command=lambda c=chave, d=1: self._mover_card_output(c, d))
            else: btn_down.configure(state="disabled", fg_color="transparent")

            var = ctk.BooleanVar(value=(chave in ativas_salvas))
            self._checkbox_output[chave] = var
            
            chk = ctk.CTkSwitch(
                header, text=f"{modulo.NOME} [{'Ativa' if var.get() else 'Inativa'}]", 
                variable=var, font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO,
                progress_color=COR_DESTAQUE, button_color="#FFFFFF"
            )
            chk.configure(command=lambda v=var, c=chk, n=modulo.NOME: c.configure(text=f"{n} [{'Ativa' if v.get() else 'Inativa'}]"))
            chk.pack(side="left")

            # --- CONTEÚDO ---
            self._entradas_output[chave] = {}
            valores_salvos = self.config_apis["output"].get(chave, {})
            
            conteudo = ctk.CTkFrame(card, fg_color="transparent")
            conteudo.pack(fill="x", padx=20, pady=(0, 15))

            if not getattr(modulo, "CAMPOS_CONFIG", []):
                ctk.CTkLabel(conteudo, text="Pronto para uso (Sem configuração adicional).", text_color=COR_TEXTO_SECUNDARIO, font=ctk.CTkFont(*FONTE_LABEL)).pack(anchor="w", pady=(0, 5))
                continue

            for campo in modulo.CAMPOS_CONFIG:
                linha = ctk.CTkFrame(conteudo, fg_color="transparent")
                linha.pack(fill="x", pady=5)
                
                ctk.CTkLabel(linha, text=campo["label"], text_color=COR_TEXTO_SECUNDARIO, font=ctk.CTkFont(*FONTE_LABEL), width=200, anchor="w").pack(side="left", padx=(0, 10))
                
                is_senha = campo.get("tipo") == "senha"
                entrada = ctk.CTkEntry(linha, height=40, border_width=1, corner_radius=8, show="*" if is_senha else "")
                entrada.pack(side="left", fill="x", expand=True)
                
                if campo["chave"] in valores_salvos:
                    entrada.insert(0, valores_salvos[campo["chave"]])
                
                self._entradas_output[chave][campo["chave"]] = entrada

    def _mover_card_output(self, chave, direcao):
        self._salvar_retorno(silencioso=True)
        ordem = self.config_apis["ordem_outputs"]
        idx = ordem.index(chave)
        novo_idx = idx + direcao
        ordem[idx], ordem[novo_idx] = ordem[novo_idx], ordem[idx]
        self._renderizar_cards_outputs()

    def _salvar_retorno(self, silencioso=False):
        for chave, campos in self._entradas_output.items():
            self.config_apis["output"][chave] = {campo_chave: widget.get() for campo_chave, widget in campos.items()}
            
        ativas = [chave for chave, var in self._checkbox_output.items() if var.get()]
        self.config_apis["output_ativas"] = ativas
        self.config_apis["ordem_outputs"] = [ch for ch in self.config_apis["ordem_outputs"] if ch in self.modulos_output]
        
        salvar_config_apis(self.config_apis)
        
        if not silencioso:
            log.registrar_sucesso(f"Saídas salvas. Ativas: {len(ativas)}", origem="interface")

    # ---- Robô -------------------------------------------------------

    def _alternar_robo(self):
        if self.robo.rodando:
            self.robo.stop()
            self.botao_robo.configure(text="▶ Rodar Robô", fg_color="#2e7d32", hover_color="#1b5e20")
            return

        self._salvar_inputs(silencioso=True)
        self._salvar_condicoes()
        self._salvar_retorno(silencioso=True)

        # Respeita a ordem definida na UI
        apis_input_selecionadas = {}
        for chave in self.config_apis.get("ordem_inputs", []):
            if chave in self.config_apis.get("input_ativas", []):
                apis_input_selecionadas[chave] = self.config_apis["input"].get(chave, {})
            
        apis_output_selecionadas = {}
        for chave in self.config_apis.get("ordem_outputs", []):
            if chave in self.config_apis.get("output_ativas", []):
                apis_output_selecionadas[chave] = self.config_apis["output"].get(chave, {})

        if not apis_input_selecionadas:
            log.registrar_erro("Nenhuma Fila de Input ATIVA.", origem="interface")
            return
        if not apis_output_selecionadas:
            log.registrar_erro("Nenhum Retorno ATIVO.", origem="interface")
            return

        self.robo.configurar(apis_input_selecionadas, apis_output_selecionadas)
        self.robo.start()
        self.botao_robo.configure(text="■ Parar Robô", fg_color="#c62828", hover_color="#8e0000")

    def _abrir_janela_log(self):
        self._janela_log.deiconify()
        self._janela_log.lift()


if __name__ == "__main__":
    app = FlyScannerApp()
    app.mainloop()
```

</details>

<a id="f-100"></a>
<details>
<summary>🐍 <b>log.py</b> — Python · 3.0 KB · 101 linhas · utf-8</summary>

```python
"""
log.py
------
Sistema central de logs do FlyScanner.

Qualquer parte do sistema (interface, buscador, apis_input, apis_output)
manda mensagens pra cá através da função `registrar()`. O log.py guarda
tudo em arquivo (log/flyscanner.log) e também distribui as mensagens pra
quem estiver "ouvindo" (a janela de Log da interface), via uma fila
thread-safe (queue.Queue).

Não depende do customtkinter, só de bibliotecas padrão, pra poder ser
chamado de qualquer script (inclusive os que rodam em thread separada).
"""

import os
import queue
import threading
from datetime import datetime

_LOCK = threading.Lock()
_LISTENERS = []  # lista de queue.Queue que recebem cada nova linha de log

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log")
LOG_FILE = os.path.join(LOG_DIR, "flyscanner.log")

NIVEIS = ("INFO", "SUCESSO", "AVISO", "ERRO")


def _garantir_pasta():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)


def registrar(mensagem: str, nivel: str = "INFO", origem: str = "sistema"):
    """
    Registra uma mensagem de log.

    nivel: INFO, SUCESSO, AVISO ou ERRO
    origem: de onde veio (ex: 'google_flight', 'terminal', 'buscador', 'interface')
    """
    nivel = nivel.upper() if nivel.upper() in NIVEIS else "INFO"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{timestamp}] [{nivel}] [{origem}] {mensagem}"

    with _LOCK:
        _garantir_pasta()
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(linha + "\n")
        except OSError:
            pass  # se não conseguir gravar em disco, ao menos os listeners recebem

        for fila in list(_LISTENERS):
            try:
                fila.put_nowait(linha)
            except Exception:
                pass

    return linha


def registrar_erro(mensagem: str, origem: str = "sistema"):
    return registrar(mensagem, nivel="ERRO", origem=origem)


def registrar_sucesso(mensagem: str, origem: str = "sistema"):
    return registrar(mensagem, nivel="SUCESSO", origem=origem)


def registrar_aviso(mensagem: str, origem: str = "sistema"):
    return registrar(mensagem, nivel="AVISO", origem=origem)


def nova_fila_de_escuta() -> queue.Queue:
    """
    A janela de Log da interface chama isso pra ganhar uma fila própria.
    Toda nova mensagem registrada também cai nessa fila, e a interface
    fica dando `fila.get_nowait()` periodicamente (via `after()` do Tkinter)
    pra jogar na tela sem travar a UI.
    """
    fila = queue.Queue()
    _LISTENERS.append(fila)
    return fila


def ler_log_completo() -> str:
    """Lê o arquivo de log inteiro (útil pra popular a janela ao abrir)."""
    _garantir_pasta()
    if not os.path.exists(LOG_FILE):
        return ""
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read()


def limpar_log():
    _garantir_pasta()
    with _LOCK:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("")
    registrar("Log limpo pelo usuário.", nivel="INFO", origem="log")
```

</details>

<a id="f-101"></a>
<details>
<summary>📝 <b>ofertas.md</b> — Markdown · 14.6 KB · 407 linhas · utf-8</summary>

```markdown
### ✈️ LIS ➔ GIG `🔥🔥🔥🔥 SCORE: 30% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Azul
- **Preço:** **BRL 4.806,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GIG
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 7.503,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GIG `🔥🔥🔥🔥 SCORE: 30% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 4.740,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GIG `🔥🔥 SCORE: 12% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 5.970,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GIG `🔥🔥 SCORE: 11% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 5.995,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GIG `🔥 SCORE: 5% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 6.396,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GIG `🔥 SCORE: 2% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 6.568,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GIG `🔥 SCORE: 1% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Air Europa
- **Preço:** **BRL 6.659,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GIG
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** LATAM
- **Preço:** **BRL 7.793,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GRU `🔥🔥🔥🔥 SCORE: 38% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 3.593,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GRU `🔥🔥 SCORE: 15% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 4.764,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GRU `🔥🔥 SCORE: 18% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Royal Air Maroc
- **Preço:** **BRL 4.573,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GRU `🔥🔥 SCORE: 10% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 5.004,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GRU `🔥 SCORE: 5% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Iberia
- **Preço:** **BRL 5.227,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27)
---

### ✈️ LIS ➔ GRU
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** LATAM
- **Preço:** **BRL 6.137,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20LIS%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥 SCORE: 2% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** KLM
- **Preço:** **BRL 7.226,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥 SCORE: 2% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Air France
- **Preço:** **BRL 7.259,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 7.596,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Iberia
- **Preço:** **BRL 7.607,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥🔥 SCORE: 18% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 6.063,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥🔥 SCORE: 12% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 6.489,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥🔥 SCORE: 11% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Air Europa
- **Preço:** **BRL 6.499,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥 SCORE: 9% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 6.661,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥 SCORE: 7% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Iberia
- **Preço:** **BRL 6.785,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥 SCORE: 7% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** KLM
- **Preço:** **BRL 6.789,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GIG `🔥 SCORE: 7% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Air France
- **Preço:** **BRL 6.789,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GIG%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GRU `🔥🔥🔥 SCORE: 25% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Air Europa
- **Preço:** **BRL 4.318,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GRU `🔥🔥 SCORE: 19% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Iberia
- **Preço:** **BRL 4.596,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GRU `🔥🔥 SCORE: 19% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Tap Air Portugal
- **Preço:** **BRL 4.608,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GRU `🔥🔥🔥 SCORE: 24% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Royal Air Maroc
- **Preço:** **BRL 4.274,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GRU `🔥 SCORE: 3% ABAIXO DA MÉDIA`
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Lufthansa
- **Preço:** **BRL 5.344,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GRU
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Lufthansa
- **Preço:** **BRL 6.349,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27)
---

### ✈️ OPO ➔ GRU
- **Capturado em:** 17/09/2026 15:11:15
- **Ida:** 27/12/2026
- **Companhia:** Lufthansa
- **Preço:** **BRL 6.390,00**
- **Ação:** [Ver Passagem no Google Flights](https://www.google.com/travel/flights?q=Flights%20to%20GRU%20from%20OPO%20on%202026-12-27)
---

## ✈️ OPO ➔ GIG  `SCORE 1%` 🔥

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 7.208,00** | KLM | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG  `SCORE 1%` 🔥

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 7.246,00** | Air France | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG 

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 7.576,00** | Tap Air Portugal | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG 

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 7.587,00** | Iberia | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG  `SCORE 17%` 🔥🔥

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 6.048,00** | Tap Air Portugal | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG  `SCORE 15%` 🔥🔥

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 6.213,00** | Air Europa | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG  `SCORE 11%` 🔥🔥

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 6.472,00** | Tap Air Portugal | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG  `SCORE 7%` 🔥

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 6.767,00** | Iberia | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG  `SCORE 6%` 🔥

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 6.771,00** | KLM | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG  `SCORE 6%` 🔥

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 6.801,00** | Air France | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

## ✈️ OPO ➔ GIG 

![Foto de GIG](https://loremflickr.com/800/250/rio+de+janeiro,city/all)

**BRL 8.780,00** | Tap Air Portugal | Apenas Ida

- **Ida:** 27/12/2026
- **Capturado:** 17/09 16:36

🔗 **[Finalizar Compra no Google Flights](https://www.google.com/travel/flights?q=One%20way%20flights%20to%20GIG%20from%20OPO%20on%202026-12-27)**
---
<br>

```

</details>

<a id="sec-noinc"></a>

## 🚫 Itens não incorporados

### 🖼️ Binários (49)

| Arquivo | Tipo | Tamanho |
|---|---|--:|
| `.git/objects/02/c2a58090da1bcc7edda05bbed354cd4e2959fe` | Binário não identificado | 1.7 KB |
| `.git/objects/0a/21cadb7db0d5a0b6d525641c58adc983260e58` | Binário não identificado | 722 B |
| `.git/objects/15/f361958c53ce09aed9c6f63917ce96e5e1aabd` | Binário não identificado | 174 B |
| `.git/objects/26/7184ae95e6d559acb11f4cd3b2e27a0275fd18` | Binário não identificado | 1002 B |
| `.git/objects/34/90333be399b1034574d8f42984af1370c1b0a2` | Binário não identificado | 15.2 KB |
| `.git/objects/3c/b5ab6a4a922cdf86a82cd9f1f74baf436cad4f` | Binário não identificado | 137 B |
| `.git/objects/3d/4f613f5ebf806773bdc2c250719fdf46cf6b08` | Binário não identificado | 613 B |
| `.git/objects/3e/e1babfd8b29475a4f04894ac5fb258a7919e12` | Binário não identificado | 55.4 KB |
| `.git/objects/48/08ab758e0ad4df48354f3f920aa9f615c819a3` | Binário não identificado | 1.4 KB |
| `.git/objects/4a/eeb8b59d501eb6080ed23164da6be1e0079850` | Binário não identificado | 2.3 KB |
| `.git/objects/4c/b59194d9990da0f832c6741a6ff84ecb7ac219` | Binário não identificado | 2.1 KB |
| `.git/objects/4f/2906b4e572fd76d207ed0a667539b34cc63611` | Binário não identificado | 136 B |
| `.git/objects/79/85c21c3289843651cc22490b40ca745e415603` | Binário não identificado | 2.3 KB |
| `.git/objects/86/175dcb48ee1954a58d9f14c2eae3acbdd36269` | Binário não identificado | 329 B |
| `.git/objects/86/6a9cb297c595d94cd771ef2938a2a260385ffb` | Binário não identificado | 161 B |
| `.git/objects/86/95f65cb76456c198cb86201a8fdda1cac4e63e` | Binário não identificado | 59 B |
| `.git/objects/92/e006d60645684a7376aa0ded27fe185a5af8fc` | Binário não identificado | 233 B |
| `.git/objects/9b/ad42b8faf6b22b607983cf9b1ab7786b0471af` | Binário não identificado | 1.6 KB |
| `.git/objects/a0/7c5b90093009e059e18ab5e49b34b15e7b53d9` | Binário não identificado | 189 B |
| `.git/objects/a1/13afef0488a9e43608c66f42ea94bbe596f482` | Binário não identificado | 2.3 KB |
| `.git/objects/a7/00f8beea4e15ebe2af6cd99f1f6cd181afaf73` | Binário não identificado | 1.4 KB |
| `.git/objects/b3/e05071d81501d67b3a780c907807b7801dfb95` | Binário não identificado | 1.0 KB |
| `.git/objects/b3/fd2e138a904ac1fc9c2561077ae06958a87abb` | Binário não identificado | 1.2 KB |
| `.git/objects/c2/4fac19c1f670939c0ddec004b2db9cd1bd8642` | Binário não identificado | 8.1 KB |
| `.git/objects/c7/35132f8a2b16c20041a96c481e069af2e5ac88` | Binário não identificado | 911 B |
| `.git/objects/cf/1f721644db5a90e5490ef86b95a81240c95c71` | Binário não identificado | 2.3 KB |
| `.git/objects/d2/7a1862a680c4199a941d73d0b8c017d092d392` | Binário não identificado | 1.1 KB |
| `.git/objects/d4/f2040909ea94981a7dd4de75597fbb00f486d4` | Binário não identificado | 492 B |
| `.git/objects/e0/44a12d30164e2feb5e07e156a15496bd9eb6e9` | Binário não identificado | 2.2 KB |
| `.git/objects/e3/6c5104418c79a8e480a47abf1042a6113d6392` | Binário não identificado | 1.3 KB |
| `.git/objects/e9/9cc6f5dc2db7a489e31270a93ca5d9178dc16f` | Binário não identificado | 311 B |
| `.git/objects/ec/7bc51918ab31e5999fcb0959988af8656572bf` | Binário não identificado | 106.6 KB |
| `.git/objects/f4/97e5a7ad10065df025ab639a8e39338099c354` | Binário não identificado | 433 B |
| `.git/index` | Binário não identificado | 2.6 KB |
| `__pycache__/apis.cpython-314.pyc` | Bytecode Python | 7.0 KB |
| `__pycache__/buscador.cpython-314.pyc` | Bytecode Python | 8.6 KB |
| `__pycache__/condicoes.cpython-314.pyc` | Bytecode Python | 7.6 KB |
| `__pycache__/historico.cpython-314.pyc` | Bytecode Python | 3.1 KB |
| `__pycache__/log.cpython-314.pyc` | Bytecode Python | 6.1 KB |
| `apis_input/__pycache__/aviasales.cpython-314.pyc` | Bytecode Python | 4.0 KB |
| `apis_input/__pycache__/decolar.cpython-314.pyc` | Bytecode Python | 862 B |
| `apis_input/__pycache__/google_flight.cpython-314.pyc` | Bytecode Python | 763 B |
| `apis_input/__pycache__/kiwi_tequila.cpython-314.pyc` | Bytecode Python | 2.6 KB |
| `apis_input/__pycache__/serpapi_flights.cpython-314.pyc` | Bytecode Python | 5.0 KB |
| `apis_input/__pycache__/skyscanner.cpython-314.pyc` | Bytecode Python | 1015 B |
| `apis_output/__pycache__/markdown_export.cpython-314.pyc` | Bytecode Python | 4.5 KB |
| `apis_output/__pycache__/telegram.cpython-314.pyc` | Bytecode Python | 7.9 KB |
| `apis_output/__pycache__/terminal.cpython-314.pyc` | Bytecode Python | 2.4 KB |
| `apis_output/__pycache__/whatsapp.cpython-314.pyc` | Bytecode Python | 1.3 KB |

### 🚫 Excluídos por regra (1)

| Caminho | Regra |
|---|---|
| `evolution-api/` | `Pasta Massiva (> 1000 arquivos)` |

### ⏭️ Ignorados (1)

| Arquivo | Motivo |
|---|---|
| `DOCUMENTACAO_PROJETO.md` | saída gerada pela própria ferramenta (evita contaminar execuções seguintes) |

### 🔗 Links simbólicos (0)

_Nenhum._

### ❌ Erros (0)

_Nenhum._

<a id="sec-integ"></a>

## ✅ Integridade da extração

| Verificação | Resultado |
|---|---|
| 🔑 SHA256 do conteúdo extraído | `d30eb1427c9c1f8c53f8efc84152d2bf00e2a210c16c235f6cfa8cd4e470e1eb` |
| 🌳 SHA256 da TREE | `17a8d4d752ab28a9b3035309a43e2b04896e848a882f91022fd1975da7234e72` |
| 🛡️ Situação | ✅ completa |
| 📏 Regras de exclusão | nenhuma |
| 🔤 Arquivos fora de UTF-8 | 1 — `.git/objects/71/01e22178f7038e1154467a94fc20b8e4d87bdd` |
| 🧪 Falhas de verificação de bytes | 0 |

---

<sub>📚 Gerado por documentador.pyw v1.0 · 2026-11-03 11:09:47</sub>
