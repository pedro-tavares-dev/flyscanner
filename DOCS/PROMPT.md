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





