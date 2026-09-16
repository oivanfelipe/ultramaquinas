"""
Gera descrições SEO completas para os 24 produtos da campanha Verão.
Entrega: seo_descriptions.docx (texto padrão + HTML por produto)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

DESCRIPTIONS = [
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-dobravel-alvorada-para-camping-e-pesca-verde-290380-nautika-76491",
        "keyword": "cadeira de pesca dobrável",
        "seo_title": "Cadeira de Pesca Dobrável Alvorada Nautika | Ultra Máquinas",
        "meta_description": "Leve e resistente: armação reforçada em aço, bolso lateral e assento em brim reforçado. Para camping e pesca. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira de Pesca Dobrável Alvorada Nautika — Conforto e Resistência à Beira da Água",
            "intro": "Quem pesca sabe que horas de espera exigem uma cadeira que aguente o tranco. A Cadeira Dobrável Alvorada da Nautika foi desenvolvida exatamente para isso: estrutura tubular de aço reforçado, assento em lona brim resistente e peso reduzido para você levar a qualquer ponto de pesca sem esforço.",
            "h3_sections": [
                {
                    "h3": "Construção que Suporta o Dia a Dia ao Ar Livre",
                    "content": "A estrutura da Alvorada é fabricada em aço tubular galvanizado, tratado contra ferrugem e corrosão — essencial em ambientes úmidos como margens de rios, represas e praias. O tecido do assento e encosto é lona brim reforçada, que suporta uso contínuo sem afrouxar ou rasgar.",
                    "bullets": [
                        "Armação em aço tubular galvanizado com tratamento anticorrosão",
                        "Assento e encosto em lona brim reforçada",
                        "Ponteiras de borracha nos pés para estabilidade em qualquer terreno",
                        "Bolso lateral para guardar iscas, petiscos ou acessórios",
                        "Capacidade de carga de até 100 kg",
                    ],
                },
                {
                    "h3": "Dobrável e Fácil de Transportar",
                    "content": "Em segundos a cadeira dobra e fica compacta o suficiente para caber no porta-malas ou numa mochila de trekking. Acompanha bolsa de transporte própria, tornando o deslocamento até o ponto de pesca muito mais prático.",
                    "bullets": [
                        "Sistema de dobragem rápido — sem parafusos ou ferramentas",
                        "Acompanha bolsa de transporte com alça de ombro",
                        "Peso reduzido para facilitar o carregamento em trilhas",
                        "Ideal para pesca, camping e eventos ao ar livre",
                    ],
                },
                {
                    "h3": "Versatilidade para Além da Pesca",
                    "content": "Embora seja desenhada para o pescador, a Alvorada funciona perfeitamente em acampamentos, churrascos, show de música ao ar livre e qualquer situação onde uma cadeira resistente e portátil seja necessária.",
                },
            ],
            "conclusao": "Invista em qualidade e conforto para suas pescarias. A Cadeira de Pesca Dobrável Alvorada Nautika está disponível na Ultra Máquinas com entrega rápida para todo o Brasil. Compre no Pix e garanta 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/mesa-dobravel-de-aluminio-azul-com-4-banquetas-para-camping-gh200-globalmix-75620",
        "keyword": "mesa dobravel camping",
        "seo_title": "Mesa Camping Alumínio com 4 Banquetas GH200 | Ultra Máquinas",
        "meta_description": "Mesa de camping com 4 banquetas em alumínio: montagem rápida, design compacto, perfeita para acampar ou praia. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Mesa Dobrável de Camping com 4 Banquetas GH200 — Refeições ao Ar Livre sem Complicação",
            "intro": "Montar um ambiente confortável no camping não precisa ser trabalhoso. O conjunto Mesa Dobrável GH200 da Globalmix inclui mesa e 4 banquetas em alumínio, tudo desmontável e compacto para caber facilmente no porta-malas. Ideal para acampamentos, praias, pescarias e piqueniques em família.",
            "h3_sections": [
                {
                    "h3": "Alumínio: Leve, Resistente e Sem Ferrugem",
                    "content": "Toda a estrutura — mesa e banquetas — é fabricada em alumínio de alta qualidade, o material preferido dos aventureiros por combinar resistência estrutural com peso reduzido. Diferente do aço, o alumínio não enferruja mesmo exposto a chuva, maresia ou umidade do mato.",
                    "bullets": [
                        "Estrutura 100% em alumínio — sem risco de ferrugem",
                        "Tampa da mesa em MDF com revestimento plastificado resistente a líquidos",
                        "Banquetas com assento acolchoado para conforto prolongado",
                        "Suporta até 80 kg por banqueta",
                        "Mesa com capacidade para até 50 kg distribuídos",
                    ],
                },
                {
                    "h3": "Montagem e Desmontagem em Minutos",
                    "content": "O sistema de encaixe do GH200 dispensa ferramentas. As banquetas se dobram individualmente e a mesa colapsa em posição plana — tudo se organiza no estojo de transporte incluso no kit, facilitando o transporte e o armazenamento.",
                    "bullets": [
                        "Montagem intuitiva sem uso de ferramentas",
                        "Mesa e banquetas dobráveis individualmente",
                        "Acompanha bolsa/estojo para transporte",
                        "Encaixes reforçados que garantem estabilidade durante o uso",
                    ],
                },
                {
                    "h3": "Para Onde Você For",
                    "content": "Do camping de fim de semana ao evento na praia, o conjunto GH200 acompanha você em qualquer aventura. A coloração azul vibrante combina com o espírito de lazer ao ar livre e é fácil de localizar entre outros equipamentos.",
                },
            ],
            "conclusao": "Complete seu kit de camping com o Mesa Dobrável GH200 Globalmix. Disponível na Ultra Máquinas com frete para todo o Brasil. Compre no Pix e aproveite 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/barraca-infantil-2m-x-1m-c-bolsa-e-bolinhas-bw065-importway-77247",
        "keyword": "barraquinha para criança brincar",
        "seo_title": "Barraca Infantil 2m com Bolinhas e Bolsa | Ultra Máquinas",
        "meta_description": "Barraca infantil 2x1m com bolinhas inclusas e bolsa para transporte — diversão garantida dentro de casa. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Barraquinha Infantil 2m × 1m com Bolinhas — Cantinho de Aventura para Crianças",
            "intro": "Toda criança merece um espaço só dela para explorar, brincar e criar. A Barraca Infantil BW065 da Importway transforma qualquer cômodo em uma mini aventura: com 2 metros de comprimento por 1 metro de largura, ela oferece espaço de sobra para uma ou mais crianças se divertirem com as bolinhas inclusas no kit.",
            "h3_sections": [
                {
                    "h3": "Espaço Amplo e Seguro para a Criançada",
                    "content": "Diferente das barracas menores, a BW065 tem dimensões generosas que permitem que crianças de diferentes idades brinquem juntas. O tecido é em poliéster resistente, com costuras reforçadas e janelas de tela para ventilação — a criança brinca à vontade com segurança.",
                    "bullets": [
                        "Dimensões: 2m de comprimento × 1m de largura × 90cm de altura",
                        "Tecido em poliéster resistente e lavável",
                        "Janelas teladas para circulação de ar",
                        "Entrada com zíper de fácil operação pela própria criança",
                        "Estrutura em varetas flexíveis de fibra — sem pontas cortantes",
                        "Bolinhas coloridas inclusas no kit",
                    ],
                },
                {
                    "h3": "Montagem Rápida para Pais Ocupados",
                    "content": "A estrutura usa varetas flexíveis que se encaixam em segundos — sem ferramentas, sem instruções complicadas. Em menos de 3 minutos a barraca está pronta para a criança entrar. Na hora de guardar, dobra facilmente e cabe na bolsa de transporte inclusa.",
                    "bullets": [
                        "Montagem em até 3 minutos com varetas de encaixe",
                        "Desmontagem prática — dobra compacta",
                        "Acompanha bolsa de transporte com zíper",
                        "Leve o suficiente para usar em festas, visitas e viagens",
                    ],
                },
                {
                    "h3": "Presente Certeiro para Crianças de 2 a 8 Anos",
                    "content": "Estimula a imaginação, o jogo simbólico e a coordenação motora. A barraquinha pode virar casinha, caverna, nave espacial — o limite é a imaginação da criança. Uma excelente pedida para aniversários e o Natal.",
                },
            ],
            "conclusao": "Garanta horas de diversão com a Barraca Infantil BW065 Importway. Compre na Ultra Máquinas — entregamos em todo o Brasil. Pague no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/ventilador-de-parede-premium-60cm-preto-bivolt-73-6425-venti-delta-78128",
        "keyword": "ventilador delta premium 60cm",
        "seo_title": "Ventilador Delta Premium 60cm Bivolt Preto | Ultra Máquinas",
        "meta_description": "Alto desempenho: ventilador de parede Venti Delta Premium 60cm, bivolt, 6 pás — ideal para ambientes grandes. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Ventilador de Parede Delta Premium 60cm — Potência Profissional para Ambientes Grandes",
            "intro": "Quando o calor aperta em galpões, oficinas, salões comerciais ou residências amplas, o Ventilador de Parede Delta Premium 60cm entrega a performance que você precisa. Com 6 pás em alumínio, motor bivolt e 60cm de diâmetro, ele move grandes volumes de ar com eficiência — e com muito menos barulho do que parece.",
            "h3_sections": [
                {
                    "h3": "Motor Potente e Bivolt",
                    "content": "O motor da linha Premium Venti-Delta foi projetado para uso intenso. Funciona tanto em 110V quanto em 220V sem necessidade de chaveamento manual — ideal para locais onde a tensão pode variar ou para quem pretende usar o ventilador em diferentes pontos do Brasil.",
                    "bullets": [
                        "Motor bivolt automático (110V / 220V)",
                        "6 pás em alumínio de alta eficiência aerodinâmica",
                        "Diâmetro de 60cm para cobertura ampla de ambientes",
                        "3 velocidades de operação",
                        "Consumo energético otimizado para a potência entregue",
                        "Proteção térmica contra superaquecimento",
                    ],
                },
                {
                    "h3": "Instalação Simples na Parede",
                    "content": "Acompanha suporte articulado para fixação em parede, permitindo direcionar o fluxo de ar para o ângulo ideal. A instalação segue os mesmos padrões de um ventilador doméstico comum — qualquer eletricista ou marceneiro experiente consegue fixar em menos de 30 minutos.",
                    "bullets": [
                        "Suporte articulado para ajuste do ângulo de saída do ar",
                        "Grade de proteção com pintura eletrostática resistente",
                        "Fácil limpeza das pás e grade removíveis",
                        "Certificado INMETRO",
                    ],
                },
                {
                    "h3": "Ideal Para Uso Comercial e Industrial",
                    "content": "Restaurantes, mercados, depósitos, academias e salões de beleza são ambientes onde o conforto térmico impacta diretamente na produtividade e satisfação dos clientes. O Delta Premium 60cm é dimensionado para esses desafios.",
                },
            ],
            "conclusao": "Invista em climatização de alto desempenho com o Ventilador de Parede Delta Premium 60cm. Disponível na Ultra Máquinas. Compre no Pix e economize 10%.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/esteira-de-praia-palha-natural-cores-sortidas-180x70cm-bel-76401",
        "keyword": "esteira de praia palha",
        "seo_title": "Esteira de Praia Palha Natural 180x70cm Bel | Ultra Máquinas",
        "meta_description": "Esteira de praia em palha natural 180x70cm — resistente, sustentável e fácil de enrolar. Cores sortidas. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Esteira de Praia em Palha Natural 180×70cm Bel — Tradição, Conforto e Sustentabilidade",
            "intro": "Nada substitui a sensação de estender uma boa esteira de palha na areia. A Esteira de Praia Bel em palha natural de 180×70cm tem espaço suficiente para um adulto se deitar confortavelmente, é resistente ao sol e à areia, fácil de sacudir e de enrolar para carregar. Cores sortidas que garantem o charme natural de sempre.",
            "h3_sections": [
                {
                    "h3": "Palha Natural: Durável e Sustentável",
                    "content": "Diferente das esteiras sintéticas, a palha natural é um material renovável, biodegradável e com excelente resistência ao calor do sol. Ela não amolece nem derrete em dias quentes — mantém a forma e a textura mesmo depois de muitas idas à praia.",
                    "bullets": [
                        "Dimensões: 180cm de comprimento × 70cm de largura",
                        "Palha natural selecionada e trançada manualmente",
                        "Resistente ao calor, à areia e à umidade",
                        "Enrola compacta para fácil transporte e armazenamento",
                        "Cores sortidas com acabamento de fita colorida nas bordas",
                        "Material renovável e ecologicamente correto",
                    ],
                },
                {
                    "h3": "Para Praia, Piscina e Área de Lazer",
                    "content": "Versátil, a esteira de palha vai bem em qualquer ambiente ao ar livre: beira de piscina, jardim, camping e, claro, a praia. Fácil de limpar — basta sacudir ou lavar com água fria e deixar secar à sombra.",
                    "bullets": [
                        "Uso ideal em praia, piscina, jardim e camping",
                        "Limpeza fácil: sacudir ou lavar com água",
                        "Peso leve para levar na bolsa de praia",
                        "Conforto térmico superior ao das esteiras sintéticas",
                    ],
                },
                {
                    "h3": "Um Clássico que Não Sai de Moda",
                    "content": "A esteira de palha é um item que atravessa gerações. Cada detalhe do trançado artesanal garante um produto único, com personalidade e qualidade que os materiais sintéticos dificilmente reproduzem.",
                },
            ],
            "conclusao": "Aproveite a temporada de praia com a Esteira de Palha Natural Bel 180×70cm. Adquira na Ultra Máquinas e ganhe 10% de desconto pagando no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-de-praia-alta-em-aluminio-lazy-mormaii-preta-bel-77602",
        "keyword": "cadeira de praia alta alumínio",
        "seo_title": "Cadeira Praia Alta Lazy Mormaii Alumínio | Ultra Máquinas",
        "meta_description": "Cadeira de praia alta em alumínio resistente, design Lazy by Mormaii — estrutura leve com conforto superior. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira de Praia Alta Lazy Mormaii em Alumínio — Conforto de Quem Entende de Verão",
            "intro": "A Mormaii é sinônimo de qualidade no universo surf e praia, e a Cadeira de Praia Alta Lazy carrega essa herança. Com estrutura em alumínio resistente e design elevado — que facilita sentar e levantar sem esforço — ela redefine o conceito de conforto à beira-mar.",
            "h3_sections": [
                {
                    "h3": "Alta e Confortável: Menos Esforço para Sentar e Levantar",
                    "content": "O diferencial da cadeira alta é que ela reduz o esforço de sentar e levantar — especialmente importante para quem tem problemas no joelho ou na coluna. O assento elevado também facilita a visualização da praia e evita que a areia voada caia diretamente no colo.",
                    "bullets": [
                        "Assento alto em posição ergonômica para facilitar a movimentação",
                        "Estrutura em alumínio leve com tratamento anticorrosão",
                        "Encosto reclinável para ajuste da posição",
                        "Apoio de braços laterais acolchoados",
                        "Tecido resistente à maresia, areia e raios UV",
                        "Capacidade de carga de até 110 kg",
                    ],
                },
                {
                    "h3": "Alumínio: O Material Certo para a Praia",
                    "content": "O alumínio não enferruja mesmo com exposição constante à água salgada e à areia. Além disso, sua leveza torna o transporte muito mais fácil — leve na mão ou pendurada no ombro sem cansaço.",
                    "bullets": [
                        "Alumínio de alta resistência sem risco de oxidação",
                        "Peso reduzido — fácil de carregar da garagem à praia",
                        "Fácil limpeza com pano úmido após o uso",
                        "Dobrável com mecanismo de trava de segurança",
                    ],
                },
                {
                    "h3": "Design Lazy by Mormaii",
                    "content": "O conceito Lazy traduz exatamente o espírito da cadeira: preguiçosa no bom sentido. Ela foi pensada para quem quer aproveitar o dia de praia com o máximo de conforto e o mínimo de incômodo, com estilo assinado por uma das marcas mais respeitadas do mercado.",
                },
            ],
            "conclusao": "Eleve seu padrão de conforto na praia com a Cadeira Alta Lazy Mormaii. Compre na Ultra Máquinas e ganhe 10% de desconto pagando no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cama-de-solteiro-dobravel-kayman-camping-bege-291030-ntk-78023",
        "keyword": "cama de armar solteiro",
        "seo_title": "Cama Dobrável Solteiro Kayman Camping NTK | Ultra Máquinas",
        "meta_description": "Cama de camping dobrável para solteiro em estrutura de aço tubular resistente — fácil de montar e transportar. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cama Dobrável Solteiro Kayman NTK — Durma Bem em Qualquer Aventura",
            "intro": "Dormir no chão durante um camping pode parecer aventura na teoria, mas na prática estraga o dia seguinte. A Cama Dobrável Kayman da NTK resolve isso: estrutura tubular de aço resistente, leito elevado do chão para isolamento térmico e montagem rápida sem ferramentas. Uma boa noite de sono faz parte do pacote.",
            "h3_sections": [
                {
                    "h3": "Estrutura Robusta que Você Pode Confiar",
                    "content": "A Kayman é construída com tubos de aço de parede grossa, unidos por conectores reforçados que aguentam o uso repetido ao longo de muitas aventuras. O leito em lona brim esticada distribui o peso uniformemente, eliminando os pontos de pressão que causam dor nas costas.",
                    "bullets": [
                        "Estrutura em aço tubular galvanizado de alta resistência",
                        "Leito em lona brim reforçada, esticada e costurada nos tubos",
                        "Capacidade de carga de até 120 kg",
                        "Altura do leito: aproximadamente 38cm — facilita sentar e levantar",
                        "Pés com ponteiras de borracha para estabilidade em qualquer piso",
                        "Dimensões do leito: 190cm × 65cm (solteiro)",
                    ],
                },
                {
                    "h3": "Montagem em Menos de 5 Minutos",
                    "content": "O sistema de encaixe da Kayman não requer ferramentas. As pernas se encaixam nos tubos transversais e o conjunto se firma por pressão. A desmontagem é igualmente rápida — a cama se dobra em forma de fole e cabe na bolsa de transporte inclusa.",
                    "bullets": [
                        "Montagem sem ferramentas — encaixe por pressão",
                        "Dobra em forma de fole para fácil transporte",
                        "Acompanha bolsa de transporte resistente",
                        "Montagem e desmontagem em menos de 5 minutos",
                    ],
                },
                {
                    "h3": "Uso em Camping, Pousadas, Quarto Extra e Emergências",
                    "content": "A Kayman não é só para camping: ela funciona muito bem como cama extra para hóspedes, em festas, ou mesmo em situações de emergência quando é necessário alojar mais pessoas temporariamente. A cor bege neutra combina com qualquer ambiente.",
                },
            ],
            "conclusao": "Garanta noites confortáveis no camping com a Cama Dobrável Kayman NTK. Disponível na Ultra Máquinas com entrega para todo o Brasil. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/mesa-dobravel-com-ajuste-de-altura-robust-80cm-ntk-preto-291101-nautika-78828",
        "keyword": "mesa ntk robust 80cm",
        "seo_title": "Mesa NTK Robust 80cm com Ajuste de Altura | Ultra Máquinas",
        "meta_description": "Mesa dobrável NTK Robust com ajuste de altura até 80cm — pés reguláveis, tampo em MDF reforçado e estrutura em aço. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Mesa NTK Robust 80cm com Ajuste de Altura — A Mesa de Camping Mais Versátil do Mercado",
            "intro": "A Mesa Dobrável Robust 80cm da NTK (Nautika) se destaca por um recurso que poucos concorrentes oferecem: ajuste de altura. Isso significa que ela se adapta a cadeiras de diferentes alturas, ao uso em pé, ou a qualquer configuração que seu acampamento exigir — tudo com a praticidade de uma mesa dobrável completa.",
            "h3_sections": [
                {
                    "h3": "Ajuste de Altura: Do Chão aos 80cm",
                    "content": "Os quatro pés da Robust são reguláveis em múltiplas posições, permitindo configurar a mesa na altura ideal para o uso. Seja para refeições, atividades manuais no camping ou como suporte para equipamentos — ela se adapta à necessidade.",
                    "bullets": [
                        "Pés reguláveis em múltiplas alturas (até 80cm)",
                        "Sistema de trava seguro para cada altura selecionada",
                        "Tampo em MDF revestido, resistente a umidade e impactos",
                        "Estrutura em aço com pintura eletrostática preta",
                        "Dimensões do tampo: 80cm × 60cm",
                        "Capacidade de carga: até 60 kg",
                    ],
                },
                {
                    "h3": "Dobrável e Prática para Levar a Qualquer Lugar",
                    "content": "Com a Robust, você não precisa abrir mão de uma superfície de trabalho de qualidade só porque está acampando. O tampo dobra sobre os pés formando um pacote compacto que cabe facilmente em qualquer veículo.",
                    "bullets": [
                        "Tampo dobrável sobre os pés — embalagem compacta",
                        "Pés com borracha antiderrapante nos extremos",
                        "Fácil de limpar com pano úmido",
                        "Ideal para camping, piquenique, eventos e garagem",
                    ],
                },
                {
                    "h3": "A Escolha de Quem Leva o Camping a Sério",
                    "content": "A linha NTK/Nautika é referência entre os acampadores mais exigentes. A Robust foi desenhada para uso intenso, com materiais que duram muitas temporadas sem perder a qualidade ou a estabilidade.",
                },
            ],
            "conclusao": "Eleve o conforto do seu camping com a Mesa NTK Robust 80cm. Disponível na Ultra Máquinas. Aproveite o desconto de 10% pagando no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-de-praia-copacabana-reclinavel-5-posicoes-rosa-cad0683-botafogo-76542",
        "keyword": "cadeira de praia botafogo copacabana",
        "seo_title": "Cadeira de Praia Reclinável Copacabana Rosa Botafogo",
        "meta_description": "Cadeira de praia rosa com 5 posições de reclinação — armação em alumínio leve e tecido resistente à areia. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira de Praia Copacabana Reclinável Rosa — Estilo e Conforto da Botafogo",
            "intro": "A Cadeira de Praia Copacabana da Botafogo une o design vibrante da cor rosa com a funcionalidade de 5 posições de reclinação. Ideal para quem quer o máximo de conforto na praia — seja tomando sol, lendo um livro ou simplesmente contemplando o mar.",
            "h3_sections": [
                {
                    "h3": "5 Posições de Reclinação para Cada Momento",
                    "content": "Da posição sentada ereta até quase deitada, a Copacabana oferece 5 ângulos de reclinação para você encontrar a postura perfeita a qualquer hora do dia. O sistema de travamento é simples de operar com uma mão, mesmo enquanto você estiver sentado.",
                    "bullets": [
                        "5 posições de reclinação do encosto",
                        "Sistema de travamento lateral fácil de operar",
                        "Posição quase plana para banho de sol completo",
                        "Encosto com ventilação em tira para menor abafamento",
                        "Apoio de cabeça integrado",
                        "Faixa porta-objetos lateral",
                    ],
                },
                {
                    "h3": "Estrutura Leve em Alumínio",
                    "content": "A armação em alumínio traz resistência sem peso excessivo — perfeito para carregar da garagem à areia sem esforço. O material não enferruja em contato com a água salgada do mar.",
                    "bullets": [
                        "Estrutura tubular em alumínio resistente",
                        "Tecido em poliéster resistente à areia e maresia",
                        "Tratamento anticorrosão nos tubos",
                        "Dobrável para transporte e armazenamento compacto",
                        "Capacidade de carga até 100 kg",
                    ],
                },
                {
                    "h3": "Design Rosa para Quem Quer Ser Notada na Praia",
                    "content": "A cor rosa vibrante da Copacabana não passa despercebida. Para quem gosta de se expressar com estilo mesmo nos momentos de lazer, essa é uma excelente escolha — resistente ao cloro, ao sal e ao sol intenso sem desbotamento rápido.",
                },
            ],
            "conclusao": "Vista sua cadeira de praia com a personalidade que você merece. A Copacabana Rosa Botafogo está disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-praia-reclinavel-5-posicoes-botafogo-74360",
        "keyword": "cadeira de praia botafogo",
        "seo_title": "Cadeira de Praia Botafogo Reclinável | Ultra Máquinas",
        "meta_description": "Cadeira de praia Botafogo com 5 posições de reclinação — estrutura em alumínio leve e fácil de transportar. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira de Praia Botafogo Reclinável — Clássico do Verão Brasileiro",
            "intro": "A Botafogo é uma das marcas mais queridas pelos brasileiros quando o assunto é equipamento de praia. A Cadeira de Praia Reclinável 5 Posições traz o equilíbrio perfeito entre qualidade, conforto e custo-benefício — o companheiro ideal para todas as idas ao mar.",
            "h3_sections": [
                {
                    "h3": "Reclinação em 5 Posições para Todo Tipo de Uso",
                    "content": "Com 5 ângulos de reclinação, a cadeira Botafogo se adapta a diferentes momentos do dia: ereta para comer, inclinada para conversar, quase plana para pegar sol. O mecanismo é simples e funciona sem precisar levantar da cadeira.",
                    "bullets": [
                        "5 posições de reclinação ajustáveis",
                        "Mecanismo de trava simples e confiável",
                        "Encosto ventilado em faixas para menos calor nas costas",
                        "Apoio de braços bilaterais",
                        "Bolso lateral para armazenar pertences",
                    ],
                },
                {
                    "h3": "Estrutura em Alumínio: Leve e Resistente",
                    "content": "O alumínio é o material ideal para equipamentos de praia: não enferruja com a maresia, é leve para carregar e dura muito mais do que o aço sem tratamento. A Botafogo utiliza tubos de alumínio de alta resistência para garantir estabilidade mesmo na areia fofa.",
                    "bullets": [
                        "Tubos em alumínio com tratamento de superfície",
                        "Tecido em poliéster de alta resistência à maresia e UV",
                        "Pés com ponteiras largas para estabilidade na areia",
                        "Dobrável e compacta para transporte",
                        "Capacidade de carga até 100 kg",
                    ],
                },
                {
                    "h3": "A Escolha de Quem Vai à Praia Com Frequência",
                    "content": "Para quem visita a praia todo final de semana no verão, a qualidade dos materiais faz diferença no longo prazo. A Botafogo Reclinável foi projetada para aguentar o uso repetido, a lavagem frequente e o sol forte sem perder qualidade.",
                },
            ],
            "conclusao": "A Cadeira de Praia Botafogo Reclinável 5 Posições está disponível na Ultra Máquinas. Compre no Pix e garanta 10% de desconto na sua compra.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/lavadora-de-alta-vazao-2-0cv-el-4000v2-a-39453-8-eletroplas-76252",
        "keyword": "lavadora eletroplas 2cv",
        "seo_title": "Lavadora Eletroplas 2CV Alta Pressão | Ultra Máquinas",
        "meta_description": "Potência 2CV para limpeza pesada: lavadora Eletroplas EL-4000V2 com alta vazão e motor elétrico robusto. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Lavadora de Alta Pressão Eletroplas 2CV EL-4000V2 — Potência Real para Limpeza Profissional",
            "intro": "A Lavadora Eletroplas EL-4000V2 com motor de 2CV é a solução para quem precisa de resultado na limpeza sem perder tempo. Desenvolvida para uso semiprofissional e profissional, ela entrega alto fluxo de água e pressão suficiente para remover sujeira incrustada em concreto, veículos pesados, fachadas e equipamentos industriais.",
            "h3_sections": [
                {
                    "h3": "Motor 2CV de Alta Durabilidade",
                    "content": "O motor elétrico 2CV (cavalos de potência) da Eletroplas opera em regime contínuo sem superaquecimento — projetado para jornadas longas de trabalho. A bomba axial de pistão de bronze garante pressão constante e vida útil muito superior às bombas plásticas dos modelos básicos.",
                    "bullets": [
                        "Motor elétrico 2CV (1500W equivalente) com proteção térmica",
                        "Bomba de pistão em bronze — altíssima durabilidade",
                        "Pressão de trabalho: até 1750 PSI",
                        "Vazão: até 8 L/min",
                        "Tensão: 220V",
                        "Acompanha lança, mangueira e bico de múltiplas funções",
                    ],
                },
                {
                    "h3": "Alta Vazão para Trabalhos Pesados",
                    "content": "A alta vazão da EL-4000V2 reduz o tempo de limpeza em comparação com máquinas domésticas. Isso significa economia de tempo e de água — você termina o trabalho mais rápido e com menor consumo total.",
                    "bullets": [
                        "Ideal para limpeza de fachadas, pisos e calçadas",
                        "Eficiente em veículos pesados: caminhões, ônibus e tratores",
                        "Remove graxas e sujeiras incrustadas com facilidade",
                        "Funciona com água de torneira (sem necessidade de pressurização externa)",
                    ],
                },
                {
                    "h3": "Para Uso Semiprofissional e Profissional",
                    "content": "A EL-4000V2 é a escolha certa para postos de combustível, oficinas mecânicas, construtoras e estabelecimentos comerciais que precisam de limpeza pesada com frequência. Também perfeita para uso residencial em grandes propriedades.",
                },
            ],
            "conclusao": "Potência de verdade para limpeza pesada: a Lavadora Eletroplas 2CV EL-4000V2 está na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/mesa-dobravel-camping-nautika-robust-80cm-78121",
        "keyword": "mesa dobravel camping nautika",
        "seo_title": "Mesa Dobrável Camping Nautika Robust 80cm | Ultra Máquinas",
        "meta_description": "Mesa dobrável de camping Nautika Robust com 80cm de altura — estrutura em aço leve e fácil de montar. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Mesa Dobrável Camping Nautika Robust 80cm — Praticidade e Solidez no Campo",
            "intro": "A Nautika é referência em equipamentos de camping no Brasil, e a Mesa Dobrável Robust 80cm confirma essa reputação. Com estrutura em aço resistente, tampo espaçoso e sistema de dobramento intuitivo, ela garante uma superfície de trabalho firme em qualquer situação ao ar livre.",
            "h3_sections": [
                {
                    "h3": "Estrutura Sólida para Uso Intenso",
                    "content": "A Robust foi projetada para aguentar o uso repetido em diferentes condições: solo irregular, chuva passageira, calor intenso. A estrutura em aço recebeu tratamento anticorrosão e as articulações são reforçadas para manter a rigidez mesmo após muitas montagens.",
                    "bullets": [
                        "Estrutura em aço com tratamento anticorrosão",
                        "Tampo espaçoso em material resistente a impactos",
                        "Pés com borracha antiderrapante para estabilidade",
                        "Altura de 80cm — padrão ergonômico para adultos em pé",
                        "Capacidade de carga: até 50 kg distribuídos no tampo",
                        "Articulações em aço reforçado para uso frequente",
                    ],
                },
                {
                    "h3": "Montagem e Transporte Simplificados",
                    "content": "O sistema de dobramento da Robust segue um padrão familiar aos usuários Nautika: as pernas se dobram para baixo do tampo em dois movimentos, formando um pacote plano e compacto. O peso total é reduzido para facilitar o transporte mesmo sem bolsa.",
                    "bullets": [
                        "Dobra em 2 movimentos — sem ferramentas",
                        "Formato plano para encaixar no porta-malas",
                        "Peso aproximado de 4 kg — fácil de carregar",
                        "Acompanha alça de transporte",
                    ],
                },
                {
                    "h3": "Versatilidade Para Além do Camping",
                    "content": "A Mesa Robust da Nautika funciona igualmente bem em churrascos, eventos ao ar livre, feiras, mercadinhos e qualquer situação onde uma mesa portátil resistente seja necessária. Sua altura padrão de 80cm a torna compatível com cadeiras e banquetas comuns.",
                },
            ],
            "conclusao": "Complete seu setup de camping com a Mesa Dobrável Nautika Robust 80cm. Adquira na Ultra Máquinas e aproveite 10% de desconto pagando no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/lavadora-de-alta-jaguar-turbo-pressao-2175-libras-127v-b8-065-0009-lavor-77105",
        "keyword": "lavadora jaguar turbo 2175",
        "seo_title": "Lavadora Jaguar Turbo 2175 Libras Lavor | Ultra Máquinas",
        "meta_description": "Lavadora Lavor Jaguar Turbo com 2175 libras de pressão e 127V — potência profissional para limpeza pesada. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Lavadora Lavor Jaguar Turbo 2175 Libras — Limpeza Pesada com Precisão Italiana",
            "intro": "A Lavor é uma marca italiana com décadas de tradição em lavadoras de alta pressão, e a Jaguar Turbo 2175 libras é um dos seus produtos mais populares no Brasil. Com 2175 PSI de pressão máxima e motor de alta eficiência em 127V, ela combina potência profissional com facilidade de uso residencial e semiprofissional.",
            "h3_sections": [
                {
                    "h3": "2175 PSI de Pressão — Sem Deixar Sujeira",
                    "content": "Com 2175 libras de pressão por polegada quadrada (PSI), a Jaguar Turbo remove sujeira incrustada que lavadoras domésticas comuns não conseguem vencer: graxas de motor, mofo em pisos, lama compactada e resíduos de tintas.",
                    "bullets": [
                        "Pressão máxima de 2175 PSI (150 bar)",
                        "Motor elétrico de alto desempenho 127V",
                        "Vazão média de 7 L/min",
                        "Cabo elétrico blindado de alta durabilidade",
                        "Mangueira de alta pressão de 5 metros inclusa",
                        "Bico regulável Turbo para diferentes tipos de limpeza",
                    ],
                },
                {
                    "h3": "Tecnologia Italiana de Alta Performance",
                    "content": "A bomba da Jaguar Turbo utiliza pistões de metal de alta precisão — a mesma tecnologia aplicada nos equipamentos profissionais Lavor. Isso garante pressão constante durante todo o trabalho, sem quedas de desempenho mesmo nas limpezas mais longas.",
                    "bullets": [
                        "Bomba axial de pistão em metal de precisão",
                        "Sistema Turbo para intensificação do jato",
                        "Proteção automática contra superaquecimento",
                        "Entrada de detergente para limpeza com sabão",
                        "Certificação INMETRO",
                    ],
                },
                {
                    "h3": "Ideal para Residências e Pequenos Negócios",
                    "content": "A Jaguar Turbo 127V é a escolha certa para quem precisa de desempenho superior ao doméstico sem investir em equipamento industrial. Perfeita para casas com área externa, garagens, calçadas, piscinas e pequenas frotas de veículos.",
                },
            ],
            "conclusao": "Precisão italiana na palma da mão: a Lavadora Lavor Jaguar Turbo 2175 Libras está na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/lavadora-de-alta-pressao-hd-498-1800w-14237050-karcher-75780",
        "keyword": "lavadora karcher hd 498",
        "seo_title": "Lavadora Karcher HD 498 1800W Alta Pressão | Ultra Máquinas",
        "meta_description": "Lavadora Kärcher HD 498 com 1800W de potência e alta pressão — desempenho profissional para superfícies externas. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Lavadora Kärcher HD 498 1800W — O Padrão Profissional da Limpeza de Alta Pressão",
            "intro": "A Kärcher dispensa apresentações — é a marca mais confiável do mundo em lavadoras de alta pressão, e a HD 498 representa o melhor da linha profissional compacta. Com 1800W de potência, ela atinge pressões elevadas com vazão generosa, prontos para os trabalhos mais exigentes.",
            "h3_sections": [
                {
                    "h3": "Potência e Eficiência da Linha HD Kärcher",
                    "content": "A linha HD da Kärcher é projetada para uso profissional intenso — mais robusta que a linha K doméstica, com componentes de vida útil superior. O motor de 1800W alimenta uma bomba de alto desempenho que mantém pressão constante mesmo em jornadas longas de trabalho.",
                    "bullets": [
                        "Motor elétrico de 1800W de alta performance",
                        "Pressão máxima: até 130 bar (1885 PSI)",
                        "Vazão de trabalho: até 7,5 L/min",
                        "Bomba de pistão em metal — vida útil prolongada",
                        "Sistema de proteção automática contra sobrecarga",
                        "Certificação Kärcher para uso profissional",
                    ],
                },
                {
                    "h3": "Construção Robusta para Trabalho Pesado",
                    "content": "A HD 498 foi projetada para condições de trabalho reais: câmeras de pressão em latão, componentes metálicos de alta qualidade e vedações que aguentam os solventes e detergentes profissionais. O chassi robusto protege os componentes internos durante o transporte e o uso em obra.",
                    "bullets": [
                        "Câmera de pressão e pistões em latão de alta resistência",
                        "Mangueira de alta pressão de 10 metros",
                        "Lança em alumínio com bico regulável",
                        "Estrutura com rodinhas para mobilidade no local de trabalho",
                        "Entrada de detergente para aplicação de produtos químicos",
                    ],
                },
                {
                    "h3": "Aplicações Profissionais e Industriais",
                    "content": "Fachadas de prédios, frotas de veículos, equipamentos agrícolas, pisos industriais e estruturas metálicas são apenas algumas das superfícies onde a Kärcher HD 498 entrega resultado superior. Uma escolha inteligente para empresas de limpeza e manutenção.",
                },
            ],
            "conclusao": "Profissional desde o primeiro jato: a Lavadora Kärcher HD 498 1800W está disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/ombrellone-central-pisa-articulado-em-aluminio-poliester-2-50m-preto-14507-bel-fix-78575",
        "keyword": "ombrellone articulado 2,50m",
        "seo_title": "Ombrellone Pisa Articulado 2,50m Alumínio | Ultra Máquinas",
        "meta_description": "Ombrellone articulado com haste de alumínio 2,50m e tecido em poliéster preto — ideal para jardim e piscina. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Ombrellone Pisa Articulado 2,50m Alumínio — Sombra Total onde Você Precisar",
            "intro": "O grande diferencial de um ombrellone articulado é a liberdade de direcionar a sombra exatamente onde ela é necessária, sem precisar mover toda a estrutura. O Ombrellone Pisa da Bel Fix com 2,50m de diâmetro em poliéster preto e haste de alumínio é a solução elegante para jardins, decks de piscina e áreas de lazer.",
            "h3_sections": [
                {
                    "h3": "Articulação Que Muda o Jogo",
                    "content": "O sistema articulado do Pisa permite inclinar a cobertura em diferentes ângulos sem deslocar a base. Isso é fundamental para acompanhar o sol durante o dia — manhã, tarde e fim de tarde — e garantir sombra constante para as pessoas abaixo.",
                    "bullets": [
                        "Sistema articulado para inclinação da cobertura",
                        "Diâmetro de 2,50m — cobertura generosa",
                        "Haste central em alumínio resistente e anticorrosivo",
                        "Tecido em poliéster preto com fator de proteção UV",
                        "Mecanismo de abertura por manivela para facilidade de uso",
                        "Encaixes reforçados em toda a estrutura de varetas",
                    ],
                },
                {
                    "h3": "Alumínio e Poliéster: A Combinação Perfeita",
                    "content": "A haste de alumínio garante que o Pisa não enferruje e seja fácil de movimentar, enquanto o tecido em poliéster é resistente ao desbotamento por UV, à chuva e ao calor intenso. Uma combinação pensada para durar muitas temporadas ao ar livre.",
                    "bullets": [
                        "Haste em alumínio de alta resistência",
                        "Varetas estruturais também em alumínio",
                        "Tecido poliéster com tratamento UV e impermeabilizante",
                        "Cor preta que absorve menos calor interno do que parece",
                        "Limpeza simples com água e sabão neutro",
                    ],
                },
                {
                    "h3": "Instalação Simples, Visual Elegante",
                    "content": "O design limpo e elegante do Pisa se integra bem a qualquer estilo de jardim ou área de lazer. A cor preta confere um toque sofisticado que combina tanto com ambientes rústicos quanto modernos.",
                },
            ],
            "conclusao": "Direcione a sombra para onde você precisa com o Ombrellone Pisa Articulado Bel Fix. Disponível na Ultra Máquinas com 10% de desconto no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/tenda-gazebo-dobravel-3m-x-3m-poliester-bege-bel-331500-bel-fix-77202",
        "keyword": "gazebo dobrável 3x3",
        "seo_title": "Gazebo Dobrável 3x3m Bege Bel Fix | Ultra Máquinas",
        "meta_description": "Gazebo dobrável 3x3m em poliéster bege resistente — montagem sem ferramentas e estrutura em aço tratado. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Gazebo Dobrável 3×3m Bel Fix — Espaço Coberto para Eventos ao Ar Livre",
            "intro": "Seja para um churrasco de domingo, uma festa no jardim, uma feira ou um evento corporativo, o Gazebo Dobrável 3×3m Bel Fix oferece 9m² de cobertura de qualidade em minutos. Estrutura robusta em aço tratado, tecido em poliéster bege resistente a chuva e sol — tudo isso sem precisar de ferramentas ou instaladores.",
            "h3_sections": [
                {
                    "h3": "9m² de Cobertura em Poucos Minutos",
                    "content": "A estrutura em sanfona do gazebo Bel Fix foi projetada para abertura rápida: em menos de 10 minutos, mesmo por uma única pessoa, o espaço está pronto. O mecanismo de travamento em cada perna garante estabilidade mesmo em dias com vento.",
                    "bullets": [
                        "Dimensões de cobertura: 3m × 3m (9m²)",
                        "Estrutura sanfona em aço com tratamento anticorrosão",
                        "Abertura e fechamento em menos de 10 minutos",
                        "Pernas ajustáveis em 3 alturas",
                        "Mecanismo de trava em cada perna para segurança",
                        "Acompanha bolsa de transporte resistente",
                    ],
                },
                {
                    "h3": "Tecido Resistente a Sol e Chuva",
                    "content": "O teto em poliéster bege recebe tratamento impermeabilizante e proteção UV. Ele resiste a chuvas moderadas e bloqueia boa parte da radiação solar — criando um ambiente confortável abaixo da cobertura mesmo em dias quentes.",
                    "bullets": [
                        "Tecido em poliéster 180g/m² com impermeabilização",
                        "Proteção UV para reduzir a temperatura interna",
                        "Costuras seladas para evitar infiltração",
                        "Cor bege que reflete a luz solar",
                        "Fácil limpeza com esponja e água",
                    ],
                },
                {
                    "h3": "Para Eventos, Festas e Uso Permanente",
                    "content": "O Gazebo Bel Fix pode ficar montado por vários dias sem problemas — ideal para uso em eventos de múltiplos dias, feiras de rua ou como proteção temporária em obras. A bolsa de transporte inclusa facilita o armazenamento no período sem uso.",
                },
            ],
            "conclusao": "Transforme qualquer espaço ao ar livre com o Gazebo Dobrável 3×3m Bel Fix. Disponível na Ultra Máquinas com 10% de desconto pagando no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/caixa-termica-19-litros-acai-71909-bel-77810",
        "keyword": "caixa térmica 19 litros",
        "seo_title": "Caixa Térmica Açaí 19 Litros Bel 71909 | Ultra Máquinas",
        "meta_description": "Caixa térmica Açaí 19 litros — mantém sua bebida gelada por horas com isolamento térmico de alta performance. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Caixa Térmica Açaí 19 Litros Bel — Bebidas Geladas do Começo ao Fim do Dia",
            "intro": "Nem a praia mais quente do Brasil resiste ao poder de isolamento da Caixa Térmica Açaí da Bel. Com 19 litros de capacidade — espaço para cerca de 20 latinhas — e isolamento de alta performance, ela mantém o gelo por horas enquanto você aproveita o dia.",
            "h3_sections": [
                {
                    "h3": "19 Litros de Capacidade Real",
                    "content": "19 litros é o tamanho ideal para passeios em família ou grupos de amigos: cabe tudo o que você precisa para o dia sem ser grande demais para carregar. O interior liso facilita a limpeza e evita o acúmulo de resíduos entre as frestas.",
                    "bullets": [
                        "Capacidade: 19 litros — cerca de 20 latas de 350ml",
                        "Interior em polipropileno liso — fácil de higienizar",
                        "Tampa com vedação hermética para maior eficiência térmica",
                        "Dreno de fácil acesso para retirada da água do gelo derretido",
                        "Alça ergonômica para transporte confortável",
                        "Trava de segurança para evitar abertura acidental",
                    ],
                },
                {
                    "h3": "Isolamento Que Mantém o Gelo por Horas",
                    "content": "As paredes da Açaí são preenchidas com espuma de poliuretano injetada de alta densidade — o mesmo material usado nas caixas térmicas profissionais. Esse isolamento mantém a temperatura interna muito abaixo da externa, mesmo sob sol direto.",
                    "bullets": [
                        "Paredes com isolamento em poliuretano expandido de alta densidade",
                        "Mantém o gelo por até 12 horas em condições normais",
                        "Parede dupla que bloqueia o calor externo",
                        "Eficiência superior às caixas de isopor convencionais",
                    ],
                },
                {
                    "h3": "Companhia Essencial para Praia, Camping e Pesca",
                    "content": "Para pescadores, a Açaí guarda iscas vivas resfriadas. Para campistas, conserva alimentos perecíveis. Para quem vai à praia, é a solução para o chope gelado do final da tarde. Versátil, resistente e com design atraente nas cores da marca.",
                },
            ],
            "conclusao": "Bebida gelada até o último gole: adquira a Caixa Térmica Açaí 19L Bel na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/tenda-gazebo-tubular-2m-polietileno-azul-belfix-301302-74641",
        "keyword": "tenda gazebo 2m",
        "seo_title": "Gazebo Tubular 2m Polietileno Azul BelFix | Ultra Máquinas",
        "meta_description": "Tenda gazebo tubular 2m em polietileno azul — estrutura leve e montagem rápida para eventos ao ar livre. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Tenda Gazebo Tubular 2m BelFix — Proteção Rápida para Qualquer Evento ao Ar Livre",
            "intro": "Para proteção contra sol e chuva em qualquer tamanho de evento ou reunião, a Tenda Gazebo Tubular 2m da BelFix entrega agilidade e praticidade. Com estrutura tubular leve e cobertura em polietileno azul resistente, ela monta em minutos e protege o espaço abaixo de forma eficiente.",
            "h3_sections": [
                {
                    "h3": "Estrutura Tubular Leve e Resistente",
                    "content": "A estrutura em tubos metálicos galvanizados da BelFix é leve o suficiente para uma pessoa montar sozinha, mas robusta o suficiente para aguentar ventos moderados e chuvas. As pernas ajustáveis em altura permitem nivelar a tenda em terrenos irregulares.",
                    "bullets": [
                        "Estrutura tubular em metal galvanizado — sem ferrugem",
                        "Pernas ajustáveis em múltiplas alturas",
                        "Sistema de trava simples e seguro em cada perna",
                        "Cobertura em polietileno azul resistente a UV e chuva",
                        "Bordas reforçadas e ilhoses para fixação com cordas",
                        "Montagem possível por uma só pessoa",
                    ],
                },
                {
                    "h3": "Cobertura em Polietileno de Alta Resistência",
                    "content": "O polietileno (PE) utilizado na cobertura é tratado contra raios UV, o que evita o desbotamento rápido e o enfraquecimento do material pela exposição solar. Sua impermeabilidade protege contra chuvas inesperadas com eficiência superior ao lona comum.",
                    "bullets": [
                        "Polietileno com tratamento UV para durabilidade prolongada",
                        "Impermeável para proteção contra chuva",
                        "Costura reforçada nas junções da cobertura",
                        "Fácil de dobrar e guardar após o uso",
                        "Lavável com água e sabão neutro",
                    ],
                },
                {
                    "h3": "Uso Múltiplo em Ambientes Variados",
                    "content": "Churrascos, feiras, eventos esportivos, exposições e acampamentos — a Tenda Gazebo 2m BelFix se adapta a diferentes contextos. Sua cor azul vibrante é facilmente identificável entre outros equipamentos e transmite um aspecto organizado e profissional.",
                },
            ],
            "conclusao": "Proteção rápida e confiável para seus eventos: a Tenda Gazebo Tubular 2m BelFix está na Ultra Máquinas. Pague no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/ombrellone-suspenso-giratorio-360%C2%B0-buzios-3m-marrom-c-base-50-lts-891012-bel-77818",
        "keyword": "ombrellone suspenso giratório 3m",
        "seo_title": "Ombrellone Suspenso Giratório 360° Búzios 3m + Base Bel",
        "meta_description": "Ombrellone suspenso giratório 360°, 3m de cobertura com base de água e areia 50L incluída — sombra total. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Ombrellone Suspenso Giratório 360° Búzios 3m — Liberdade Total de Posicionamento",
            "intro": "O Ombrellone Suspenso Búzios da Bel redefine o que é comodidade em sombra ao ar livre. Sem haste central no caminho, a cobertura de 3m fica suspensa lateralmente e gira 360° — assim você direciona a sombra exatamente onde está sem precisar mover a base ou levantar.",
            "h3_sections": [
                {
                    "h3": "360° de Liberdade para Seguir a Sombra",
                    "content": "O mecanismo giratório é o coração do Búzios. Com um simples movimento, a cobertura de 3m muda de direção acompanhando o deslocamento do sol durante o dia. Nenhuma necessidade de erguer a estrutura, ajustar parafusos ou mover a base pesada.",
                    "bullets": [
                        "Rotação total de 360° com travamento em qualquer posição",
                        "Cobertura de 3 metros de diâmetro — sombra para grupos",
                        "Haste lateral que elimina o mastro central no espaço útil",
                        "Mecanismo de inclinação para ajuste do ângulo da cobertura",
                        "Tecido em poliéster marrom com tratamento UV",
                        "Sistema de abertura e fechamento por manivela",
                    ],
                },
                {
                    "h3": "Base Estável com 50 Litros de Capacidade",
                    "content": "A base de 50 litros inclusa no kit é enchida com água ou areia na hora da instalação — chegando a um peso de 50 kg com água, ou mais com areia. Esse peso garante estabilidade total mesmo com vento moderado, sem necessidade de fixação no piso.",
                    "bullets": [
                        "Base plástica de alta resistência com 50L de capacidade",
                        "Preenchimento com água (50 kg) ou areia (+ peso)",
                        "Rodas para facilitar o reposicionamento quando vazia",
                        "Encaixe central para a haste do ombrellone",
                        "Design discreto que combina com qualquer decoração",
                    ],
                },
                {
                    "h3": "Perfeito para Área de Piscina, Deck e Jardim",
                    "content": "O Búzios foi desenhado para espaços onde a flexibilidade de posicionamento é essencial. Na beira da piscina, no jardim com layout irregular, no deck de madeira — ele se adapta a qualquer cenário entregando a sombra certa no lugar certo.",
                },
            ],
            "conclusao": "Sombra total sem limitações: o Ombrellone Suspenso Búzios 3m Bel com base inclusa está na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/guarda-sol-bagum-haste-de-aluminio-2-00m-azul-royal-10602-bel-74687",
        "keyword": "guarda-sol alumínio 2m",
        "seo_title": "Guarda-Sol Bagum Alumínio 2m Azul Royal Bel | Ultra Máquinas",
        "meta_description": "Guarda-sol Bagum com haste de alumínio 2m e tecido azul royal — leve e resistente para praia ou piscina. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Guarda-Sol Bagum Alumínio 2m Azul Royal Bel — Clássico do Verão Brasileiro",
            "intro": "O Guarda-Sol Bagum da Bel é um clássico das praias brasileiras: haste em alumínio resistente à maresia, cobertura de 2m em tecido azul royal vibrante e peso ideal para levar embaixo do braço sem esforço. Tudo que você precisa para um dia perfeito na praia.",
            "h3_sections": [
                {
                    "h3": "Haste em Alumínio: Leve e Resistente à Maresia",
                    "content": "A haste de alumínio do Bagum é o componente que garante sua longevidade. Diferente do aço, o alumínio não enferruja em contato com a água salgada — você pode cravar na areia molhada, lavar com água do mar e guardar sem preocupação com oxidação.",
                    "bullets": [
                        "Haste em alumínio de alta resistência — sem risco de ferrugem",
                        "Diâmetro de cobertura: 2 metros",
                        "Tecido em nylon ou poliéster azul royal com proteção UV",
                        "Sistema de abertura por botão de trava simples",
                        "Ponteira de metal para fácil encaixe na areia",
                        "Peso aproximado de 1,8 kg — fácil de carregar",
                    ],
                },
                {
                    "h3": "Proteção Solar e Visual na Praia",
                    "content": "Os 2 metros de cobertura do Bagum protegem uma ou duas pessoas da incidência direta do sol. O azul royal é uma das cores mais procuradas — transmite frescor visual e é fácil de encontrar entre os guarda-sóis na areia lotada.",
                    "bullets": [
                        "Protege até 2 adultos do sol direto",
                        "Cor azul royal vibrante que não desbota rápido",
                        "Ventilação superior para evitar que o vento vire o guarda-sol",
                        "Acabamento das bordas com reforço de viés",
                        "Compacto para guardar na bolsa de praia",
                    ],
                },
                {
                    "h3": "Versátil: Praia, Piscina e Jardim",
                    "content": "O Bagum vai além da praia: funciona igualmente bem na beira da piscina, no jardim ou em qualquer espaço ao ar livre onde você queira criar um ponto de sombra rápido sem montar uma estrutura complexa.",
                },
            ],
            "conclusao": "O clássico da praia brasileira: o Guarda-Sol Bagum Alumínio 2m Azul Royal Bel está na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/ombrellone-central-retangular-quiosque-oversize-4-50m-marrom-12412-bel-fix-78574",
        "keyword": "ombrellone retangular 4,50m",
        "seo_title": "Ombrellone Retangular 4,50m Oversize Marrom Bel Fix",
        "meta_description": "Ombrellone retangular de 4,50m tipo quiosque — ideal para áreas extensas com cobertura ampla e estrutura robusta. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Ombrellone Retangular Oversize 4,50m Bel Fix — Cobertura de Quiosque para Áreas Extensas",
            "intro": "Quando um ombrellone comum não é suficiente para cobrir sua área de lazer, o Ombrellone Retangular Oversize 4,50m da Bel Fix é a resposta. Com dimensões de quiosque e formato retangular que maximiza a cobertura útil, ele transforma qualquer área externa em um ambiente confortável e protegido do sol.",
            "h3_sections": [
                {
                    "h3": "4,50m de Cobertura Retangular — Máxima Eficiência de Sombra",
                    "content": "O formato retangular é mais eficiente do que o circular para cobrir mesas longas, conjuntos de piscina em linha ou decks alongados. Com 4,50m no eixo maior, o Oversize oferece uma área de sombra que dificilmente qualquer outro ombrellone residencial consegue cobrir.",
                    "bullets": [
                        "Dimensão principal: 4,50m × 2,70m aproximadamente",
                        "Formato retangular para máxima cobertura de mesas e áreas longas",
                        "Haste central robusta em alumínio de parede grossa",
                        "Varetas estruturais reforçadas para suportar o grande volume de tecido",
                        "Tecido em poliéster marrom de alta densidade com tratamento UV",
                        "Sistema de abertura por manivela integrada",
                    ],
                },
                {
                    "h3": "Qualidade de Quiosque para Uso Residencial",
                    "content": "A estrutura Oversize é desenhada nos mesmos padrões dos ombrellones comerciais de quiosque de praia. Isso significa componentes mais robustos, encaixes mais seguros e materiais que aguentam o uso diário em condições de exposição intensa.",
                    "bullets": [
                        "Haste em alumínio de alto calibre — resistência superior",
                        "Varetas de abertura em alumínio com juntas metálicas",
                        "Sistema de trava de segurança no mecanismo de abertura",
                        "Compatível com bases de grande porte (vendidas separadamente)",
                        "Cor marrom elegante que combina com madeira e pedra",
                    ],
                },
                {
                    "h3": "Ideal para Restaurantes, Hotéis e Residências Premium",
                    "content": "O Oversize 4,50m é especialmente indicado para estabelecimentos que precisam cobrir mesas de 4 a 6 pessoas com um único ombrellone, ou para residências com grandes áreas de lazer onde o visual e a cobertura ampla são prioridade.",
                },
            ],
            "conclusao": "Cobertura de verdade para grandes espaços: o Ombrellone Retangular Oversize 4,50m Bel Fix está na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/base-para-guarda-sol-e-ombrellone-agua-areia-18kg-preta-70027107-bel-fix-76391",
        "keyword": "base para guarda-sol 18kg",
        "seo_title": "Base Guarda-Sol 18kg Água/Areia Bel Fix | Ultra Máquinas",
        "meta_description": "Base para guarda-sol e ombrellone com 18kg preenchida com água ou areia — suporte estável para uso na praia. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Base para Guarda-Sol e Ombrellone 18kg Bel Fix — Estabilidade Total sem Necessidade de Furo no Piso",
            "intro": "Para usar um guarda-sol ou ombrellone em pisos que não podem ser furados — deck de madeira, piso de porcelanato, concreto polido ou terraço — a Base 18kg Bel Fix é a solução ideal. Preenchida com água ou areia na hora da instalação, ela ancora a haste com firmeza e estabilidade.",
            "h3_sections": [
                {
                    "h3": "18kg de Estabilidade Sem Dano ao Piso",
                    "content": "A base plástica de alta resistência é projetada para ser preenchida com água (até 18 kg) ou areia (mais peso ainda). Esse sistema elimina a necessidade de fixação mecânica no piso — sem furos, sem parafusos, sem danos à superfície do seu deck ou varanda.",
                    "bullets": [
                        "Capacidade de preenchimento: 18 litros de água ou areia seca",
                        "Peso total preenchida com água: aproximadamente 18 kg",
                        "Tampa de fácil abertura para enchimento e esvaziamento",
                        "Encaixe central para hastes de diferentes diâmetros",
                        "Rodas inferiores para reposicionar quando vazia",
                        "Plástico de alta resistência resistente a UV",
                    ],
                },
                {
                    "h3": "Compatível com a Maioria dos Guarda-Sóis e Ombrellones",
                    "content": "O encaixe central da base Bel Fix é compatível com hastes de diferentes diâmetros, cobrindo a maioria dos guarda-sóis e ombrellones do mercado, incluindo os da própria linha Bel. Graxa ou adaptadores removíveis garantem a fixação firme.",
                    "bullets": [
                        "Encaixe universal para hastes de diferentes calibres",
                        "Adaptadores inclusos para compatibilidade ampliada",
                        "Parafuso de fixação lateral para travar a haste",
                        "Suporta ombrellones de até 2,70m com estabilidade",
                        "Disponível em cor preta para discreção visual",
                    ],
                },
                {
                    "h3": "Prática de Transportar e Armazenar",
                    "content": "Esvaziada, a base pesa apenas cerca de 2 kg e tem volume reduzido. Fácil de guardar no fim da temporada ou levar para outro local. As rodinhas na base inferior facilitam o reposicionamento quando ainda preenchida.",
                },
            ],
            "conclusao": "Estabilidade total sem danos ao piso: a Base Guarda-Sol 18kg Bel Fix está na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-espreguicadeira-em-aluminio-marrom-414712-bel-77702",
        "keyword": "espreguiçadeira alumínio",
        "seo_title": "Cadeira Espreguiçadeira Alumínio Marrom Bel | Ultra Máquinas",
        "meta_description": "Espreguiçadeira em alumínio marrom resistente — ideal para piscina, jardim e área de lazer com design leve. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira Espreguiçadeira em Alumínio Marrom Bel — Relaxe em Estilo na Beira da Piscina",
            "intro": "A Cadeira Espreguiçadeira Bel em alumínio marrom combina design elegante com funcionalidade superior. Projetada para quem quer relaxar com conforto na beira da piscina, jardim ou em qualquer área de lazer, ela oferece posicionamento flexível do encosto e durabilidade que atravessa muitas temporadas.",
            "h3_sections": [
                {
                    "h3": "Alumínio: O Material Perfeito para Áreas Úmidas",
                    "content": "Próxima a piscinas e sob exposição constante a respingos d'água, umidade e sol, o alumínio é o material mais indicado para móveis de exterior. Não enferruja, não descasca, não precisa de manutenção especial — simplesmente dura.",
                    "bullets": [
                        "Estrutura tubular em alumínio anodizado resistente à umidade",
                        "Cor marrom com acabamento fosco — disfarça riscos e impressões digitais",
                        "Tecido do assento e encosto em poliéster resistente ao cloro e UV",
                        "Encosto reclinável em múltiplas posições",
                        "Capacidade de carga: até 120 kg",
                        "Pés com ponteiras de borracha para não arranhar o piso",
                    ],
                },
                {
                    "h3": "Conforto para Longas Horas de Relaxamento",
                    "content": "O comprimento estendido da espreguiçadeira oferece suporte total para o corpo, da cabeça aos pés — sem o desconforto das cadeiras comuns que deixam as pernas suspensas. O ajuste do encosto permite desde a posição sentada para leitura até a posição completamente deitada para bronzeamento.",
                    "bullets": [
                        "Comprimento de aproximadamente 170cm — suporte total do corpo",
                        "Encosto com múltiplas posições de reclinação",
                        "Apoio de cabeça integrado no encosto",
                        "Tecido trançado ou em faixa que evita o abafamento das costas",
                        "Fácil de dobrar e empilhar quando não estiver em uso",
                    ],
                },
                {
                    "h3": "Design Discreto e Elegante para Qualquer Ambiente",
                    "content": "A cor marrom da estrutura é neutra e elegante — combina com madeira, pedras naturais, porcelanatos e qualquer estilo de decoração de área externa, do rústico ao contemporâneo.",
                },
            ],
            "conclusao": "Relaxamento total ao ar livre com a Espreguiçadeira Alumínio Marrom Bel. Disponível na Ultra Máquinas com 10% de desconto no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/caixa-termica-branca-113-litros-igloo-279411-kala-81054",
        "keyword": "caixa térmica igloo 113 litros",
        "seo_title": "Caixa Térmica Igloo 113 Litros Branca Kala | Ultra Máquinas",
        "meta_description": "Caixa térmica Igloo 113L — alto isolamento, dreno de fácil acesso e tampa robusta para pescaria e acampamento. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Caixa Térmica Igloo 113 Litros — Capacidade e Isolamento de Nível Profissional",
            "intro": "Quando a necessidade é grande — seja para pescaria longa, acampamento de vários dias, eventos ou abastecimento de uma lancha — a Caixa Térmica Igloo 113 Litros é a escolha certa. Com capacidade para mais de 100 latas ou dezenas de quilos de pescado, ela mantém tudo gelado por muito mais tempo do que qualquer caixa convencional.",
            "h3_sections": [
                {
                    "h3": "113 Litros de Capacidade Real",
                    "content": "113 litros é uma capacidade generosa que atende grandes grupos ou necessidades profissionais. Cabe uma cesta de supermercado completa, dezenas de quilos de peixe ou bebidas para um evento inteiro. A abertura larga facilita o acesso e o carregamento.",
                    "bullets": [
                        "Capacidade: 113 litros — mais de 120 latas de 350ml",
                        "Abertura larga para fácil carregamento e acesso",
                        "Interior em polipropileno liso — fácil limpeza e higienização",
                        "Dreno com plug removível para escoamento rápido da água",
                        "Alças laterais robustas para dois carregadores",
                        "Rodas traseiras para movimentação sem esforço",
                    ],
                },
                {
                    "h3": "Isolamento Igloo: Referência Mundial em Eficiência Térmica",
                    "content": "A Igloo é a marca de caixas térmicas mais reconhecida do mundo, usada por pescadores profissionais, barcos de pesca e expedições ao redor do globo. O segredo está na espuma de poliuretano de alta densidade e nas vedações da tampa que eliminam a troca de temperatura.",
                    "bullets": [
                        "Paredes com espuma de poliuretano de alta densidade",
                        "Tampa com vedação hermética por juntas de borracha",
                        "Mantém o gelo por 3 a 5 dias em condições normais",
                        "Parede dupla que isola do calor externo com eficiência",
                        "Trava metálica na tampa para segurança durante o transporte",
                    ],
                },
                {
                    "h3": "Perfeita para Pescaria, Expedições e Eventos",
                    "content": "Na pesca, ela guarda o pescado fresco por dias. No camping, mantém os alimentos seguros por toda a viagem. Em eventos, garante bebidas geladas para centenas de convidados. A Igloo 113L é um investimento que se paga rapidamente para quem usa caixas térmicas com frequência.",
                },
            ],
            "conclusao": "Para quem não abre mão de performance: a Caixa Térmica Igloo 113 Litros Kala está na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
]


def build_html_description(d: dict) -> str:
    """Monta HTML da descrição a partir do dicionário."""
    desc = d.get("descricao", {})
    if not desc:
        return ""

    parts = []
    if desc.get("h2"):
        parts.append(f"<h2>{desc['h2']}</h2>")
    if desc.get("intro"):
        parts.append(f"<p>{desc['intro']}</p>")

    for section in desc.get("h3_sections", []):
        if section.get("h3"):
            parts.append(f"<h3>{section['h3']}</h3>")
        if section.get("content"):
            parts.append(f"<p>{section['content']}</p>")
        bullets = section.get("bullets", [])
        if bullets:
            items = "".join(f"<li>{b}</li>" for b in bullets)
            parts.append(f"<ul>{items}</ul>")

    if desc.get("conclusao"):
        parts.append(f"<p>{desc['conclusao']}</p>")

    return "\n".join(parts)


def build_plain_description(d: dict) -> str:
    """Versão texto da descrição para revisão."""
    desc = d.get("descricao", {})
    if not desc:
        return ""

    lines = []
    if desc.get("h2"):
        lines.append(desc["h2"].upper())
        lines.append("")
    if desc.get("intro"):
        lines.append(desc["intro"])
        lines.append("")

    for section in desc.get("h3_sections", []):
        if section.get("h3"):
            lines.append(f"— {section['h3']}")
        if section.get("content"):
            lines.append(section["content"])
        for b in section.get("bullets", []):
            lines.append(f"  • {b}")
        lines.append("")

    if desc.get("conclusao"):
        lines.append(desc["conclusao"])

    return "\n".join(lines).strip()


def export_docx(descriptions: list, path: str):
    from docx import Document
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    doc = Document()

    # Título do documento
    title_para = doc.add_heading("SEO Ultra Máquinas — Descrições Verão", 0)
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph(f"Total de produtos: {len(descriptions)}")
    doc.add_paragraph(
        "Cada produto contém: SEO Title, Meta Description, Descrição Padrão e HTML."
    )
    doc.add_page_break()

    for i, d in enumerate(descriptions, 1):
        # Cabeçalho do produto
        h = doc.add_heading(
            f"{i}. {d.get('keyword', '').title()}", level=1
        )

        # Metadados
        doc.add_heading("Metadados SEO", level=2)
        p = doc.add_paragraph()
        p.add_run("URL: ").bold = True
        p.add_run(d.get("url", ""))

        p = doc.add_paragraph()
        p.add_run("SEO Title: ").bold = True
        title = d.get("seo_title", "")
        p.add_run(f"{title} ({len(title)} chars)")

        p = doc.add_paragraph()
        p.add_run("Meta Description: ").bold = True
        meta = d.get("meta_description", "")
        p.add_run(f"{meta} ({len(meta)} chars)")

        # Descrição Padrão
        doc.add_heading("Descrição — Formato Padrão", level=2)
        plain = build_plain_description(d)
        for line in plain.split("\n"):
            if line.strip():
                p = doc.add_paragraph(line)
                if line.startswith("—"):
                    p.runs[0].bold = True
                elif line.startswith("  •"):
                    p.style = "List Bullet"
                    p.text = line.strip().lstrip("•").strip()
            else:
                doc.add_paragraph("")

        # HTML
        doc.add_heading("Descrição — HTML", level=2)
        html = build_html_description(d)
        html_para = doc.add_paragraph(html)
        html_para.runs[0].font.name = "Courier New"
        html_para.runs[0].font.size = Pt(9)

        if i < len(descriptions):
            doc.add_page_break()

    doc.save(path)
    print(f"DOCX salvo em: {path}")
    return path


if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    out_path = os.path.join("output", "seo_descriptions.docx")
    export_docx(DESCRIPTIONS, out_path)

    print("\nResumo dos produtos processados:")
    for i, d in enumerate(DESCRIPTIONS, 1):
        kw = d["keyword"]
        secs = len(d["descricao"].get("h3_sections", []))
        print(f"  {i:2d}. {kw:<40} [{secs} seções H3]")
