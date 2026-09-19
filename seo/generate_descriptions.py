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
            "h2": "Cadeira de Pesca Dobrável Alvorada Nautika",
            "intro": "Horas de espera à beira d'água exigem uma cadeira que aguente o tranco. A Alvorada da Nautika tem estrutura tubular de aço galvanizado, assento em lona brim e peso reduzido para levar a qualquer ponto de pesca sem esforço.",
            "h3_sections": [
                {
                    "h3": "Estrutura em Aço para Uso Contínuo ao Ar Livre",
                    "content": "O aço tubular galvanizado resiste à ferrugem em margens de rios, represas e praias. O tecido do assento e encosto é lona brim, que não afrouxa nem rasga com uso repetido.",
                    "bullets": [
                        "Armação em aço tubular galvanizado com tratamento anticorrosão",
                        "Assento e encosto em lona brim reforçada",
                        "Ponteiras de borracha nos pés para estabilidade em qualquer terreno",
                        "Bolso lateral para guardar iscas, petiscos ou acessórios",
                        "Capacidade de carga de até 100 kg",
                    ],
                },
                {
                    "h3": "Dobra em Segundos, Cabe no Porta-Malas",
                    "content": "A cadeira dobra compacta o suficiente para o porta-malas ou mochila de trekking. Acompanha bolsa de transporte com alça de ombro.",
                    "bullets": [
                        "Sistema de dobragem rápido — sem parafusos ou ferramentas",
                        "Acompanha bolsa de transporte com alça de ombro",
                        "Peso reduzido para trilhas e deslocamentos longos",
                        "Ideal para pesca, camping e eventos ao ar livre",
                    ],
                },
                {
                    "h3": "Além da Pesca",
                    "content": "Funciona em acampamentos, churrascos e shows ao ar livre. Em qualquer lugar onde uma cadeira resistente e portátil seja necessária.",
                },
            ],
            "conclusao": "A Cadeira de Pesca Dobrável Alvorada Nautika está disponível na Ultra Máquinas com entrega para todo o Brasil. Compre no Pix e garanta 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/mesa-dobravel-de-aluminio-azul-com-4-banquetas-para-camping-gh200-globalmix-75620",
        "keyword": "mesa dobravel camping",
        "seo_title": "Mesa Camping Alumínio com 4 Banquetas GH200 | Ultra Máquinas",
        "meta_description": "Mesa de camping com 4 banquetas em alumínio: montagem rápida, design compacto, perfeita para acampar ou praia. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Mesa Dobrável de Camping com 4 Banquetas GH200",
            "intro": "O conjunto Mesa Dobrável GH200 da Globalmix inclui mesa e 4 banquetas em alumínio, tudo desmontável e compacto para caber no porta-malas. Funciona em acampamentos, praias, pescarias e piqueniques.",
            "h3_sections": [
                {
                    "h3": "Alumínio em Toda a Estrutura — Sem Risco de Ferrugem",
                    "content": "Mesa e banquetas em alumínio: não enferruja mesmo exposto a chuva, maresia ou umidade do mato. Mais leve do que aço e com vida útil comparável.",
                    "bullets": [
                        "Estrutura 100% em alumínio — sem risco de ferrugem",
                        "Tampa da mesa em MDF com revestimento plastificado resistente a líquidos",
                        "Banquetas com assento acolchoado para uso prolongado",
                        "Suporta até 80 kg por banqueta",
                        "Mesa com capacidade para até 50 kg distribuídos",
                    ],
                },
                {
                    "h3": "Montagem sem Ferramentas",
                    "content": "O sistema de encaixe dispensa ferramentas. As banquetas dobram individualmente e a mesa colapsa em posição plana — tudo no estojo de transporte incluso.",
                    "bullets": [
                        "Montagem intuitiva sem uso de ferramentas",
                        "Mesa e banquetas dobráveis individualmente",
                        "Acompanha bolsa/estojo para transporte",
                        "Encaixes reforçados que mantêm estabilidade no uso",
                    ],
                },
                {
                    "h3": "Do Camping ao Evento na Praia",
                    "content": "A coloração azul é fácil de localizar entre outros equipamentos. O kit completo — mesa mais quatro banquetas — no mesmo volume de transporte.",
                },
            ],
            "conclusao": "Mesa Dobrável GH200 Globalmix disponível na Ultra Máquinas com frete para todo o Brasil. Compre no Pix e aproveite 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/barraca-infantil-2m-x-1m-c-bolsa-e-bolinhas-bw065-importway-77247",
        "keyword": "barraquinha para criança brincar",
        "seo_title": "Barraca Infantil 2m com Bolinhas e Bolsa | Ultra Máquinas",
        "meta_description": "Barraca infantil 2x1m com bolinhas inclusas e bolsa para transporte — diversão garantida dentro de casa. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Barraquinha Infantil 2m × 1m com Bolinhas",
            "intro": "A Barraca Infantil BW065 da Importway tem 2 metros de comprimento por 1 metro de largura: espaço para uma ou mais crianças brincarem com as bolinhas inclusas. O tecido é poliéster com costuras reforçadas e janelas teladas para ventilação.",
            "h3_sections": [
                {
                    "h3": "Dimensões Maiores que o Padrão",
                    "content": "Diferente das barracas menores do mercado, a BW065 permite que crianças de diferentes idades brinquem juntas. A entrada tem zíper que a própria criança consegue operar.",
                    "bullets": [
                        "Dimensões: 2m × 1m × 90cm de altura",
                        "Tecido em poliéster resistente e lavável",
                        "Janelas teladas para circulação de ar",
                        "Entrada com zíper de fácil operação",
                        "Varetas flexíveis de fibra — sem pontas cortantes",
                        "Bolinhas coloridas inclusas no kit",
                    ],
                },
                {
                    "h3": "Montagem em até 3 Minutos",
                    "content": "Varetas de encaixe sem ferramentas. Em menos de 3 minutos a barraca está pronta. Dobra compacta e cabe na bolsa de transporte inclusa.",
                    "bullets": [
                        "Montagem em até 3 minutos com varetas de encaixe",
                        "Desmontagem prática — dobra compacta",
                        "Acompanha bolsa de transporte com zíper",
                        "Leve o suficiente para festas, visitas e viagens",
                    ],
                },
                {
                    "h3": "Para Crianças de 2 a 8 Anos",
                    "content": "A barraquinha pode virar casinha, caverna, nave espacial. Estimula imaginação, jogo simbólico e coordenação motora. Boa pedida para aniversários e Natal.",
                },
            ],
            "conclusao": "Barraca Infantil BW065 Importway disponível na Ultra Máquinas com entrega em todo o Brasil. Pague no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/ventilador-de-parede-premium-60cm-preto-bivolt-73-6425-venti-delta-78128",
        "keyword": "ventilador delta premium 60cm",
        "seo_title": "Ventilador Delta Premium 60cm Bivolt Preto | Ultra Máquinas",
        "meta_description": "Alto desempenho: ventilador de parede Venti Delta Premium 60cm, bivolt, 6 pás — ideal para ambientes grandes. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Ventilador de Parede Delta Premium 60cm",
            "intro": "Com 6 pás em alumínio, motor bivolt e 60cm de diâmetro, o Ventilador de Parede Delta Premium move grandes volumes de ar em galpões, oficinas, salões comerciais e residências amplas — com menos barulho do que o tamanho sugere.",
            "h3_sections": [
                {
                    "h3": "Motor Bivolt Automático",
                    "content": "Funciona em 110V e 220V sem chaveamento manual — útil para locais com tensão variável ou para quem usa o ventilador em diferentes estados.",
                    "bullets": [
                        "Motor bivolt automático (110V / 220V)",
                        "6 pás em alumínio com perfil aerodinâmico",
                        "Diâmetro de 60cm para cobertura ampla",
                        "3 velocidades de operação",
                        "Consumo otimizado para a potência entregue",
                        "Proteção térmica contra superaquecimento",
                    ],
                },
                {
                    "h3": "Instalação em Parede com Suporte Articulado",
                    "content": "Acompanha suporte articulado para fixar na parede e direcionar o fluxo de ar. Um eletricista instala em menos de 30 minutos seguindo o mesmo processo de qualquer ventilador doméstico.",
                    "bullets": [
                        "Suporte articulado para ajuste do ângulo de saída do ar",
                        "Grade de proteção com pintura eletrostática",
                        "Pás e grade removíveis para limpeza fácil",
                        "Certificado INMETRO",
                    ],
                },
                {
                    "h3": "Onde o Calor é Problema Real",
                    "content": "Restaurantes, mercados, depósitos, academias e salões de beleza. Ambientes onde o conforto térmico afeta diretamente a produtividade e a satisfação dos clientes.",
                },
            ],
            "conclusao": "Ventilador de Parede Delta Premium 60cm disponível na Ultra Máquinas. Compre no Pix e economize 10%.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/esteira-de-praia-palha-natural-cores-sortidas-180x70cm-bel-76401",
        "keyword": "esteira de praia palha",
        "seo_title": "Esteira de Praia Palha Natural 180x70cm Bel | Ultra Máquinas",
        "meta_description": "Esteira de praia em palha natural 180x70cm — resistente, sustentável e fácil de enrolar. Cores sortidas. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Esteira de Praia em Palha Natural 180×70cm Bel",
            "intro": "A Esteira de Praia Bel em palha natural tem 180×70cm — espaço para um adulto se deitar com folga. Resiste ao sol e à areia, fácil de sacudir e de enrolar para carregar. Cores sortidas.",
            "h3_sections": [
                {
                    "h3": "Palha Natural: Durável e Renovável",
                    "content": "A palha natural não amolece nem derrete em dias quentes. Mantém a forma e a textura depois de muitas idas à praia. Material renovável e biodegradável.",
                    "bullets": [
                        "Dimensões: 180cm × 70cm",
                        "Palha natural selecionada e trançada manualmente",
                        "Resistente ao calor, à areia e à umidade",
                        "Enrola compacta para transporte",
                        "Cores sortidas com fita colorida nas bordas",
                        "Material renovável e ecologicamente correto",
                    ],
                },
                {
                    "h3": "Praia, Piscina, Jardim e Camping",
                    "content": "Vai bem em qualquer ambiente ao ar livre. Para limpar: sacudir ou lavar com água fria e deixar secar à sombra.",
                    "bullets": [
                        "Uso em praia, piscina, jardim e camping",
                        "Limpeza fácil: sacudir ou lavar com água",
                        "Peso leve para caber na bolsa de praia",
                        "Conforto térmico superior ao das esteiras sintéticas",
                    ],
                },
                {
                    "h3": "Artesanal por Natureza",
                    "content": "O trançado manual garante que cada esteira seja ligeiramente diferente. Os materiais sintéticos copiam o visual, mas a sensação na pele não é a mesma.",
                },
            ],
            "conclusao": "Esteira de Palha Natural Bel 180×70cm disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-de-praia-alta-em-aluminio-lazy-mormaii-preta-bel-77602",
        "keyword": "cadeira de praia alta alumínio",
        "seo_title": "Cadeira Praia Alta Lazy Mormaii Alumínio | Ultra Máquinas",
        "meta_description": "Cadeira de praia alta em alumínio resistente, design Lazy by Mormaii — estrutura leve com conforto superior. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira de Praia Alta Lazy Mormaii em Alumínio",
            "intro": "A Cadeira de Praia Alta Lazy by Mormaii tem assento elevado: sentar e levantar exige menos esforço, a areia voada fica mais longe e a visibilidade da praia melhora. Estrutura em alumínio resistente à maresia.",
            "h3_sections": [
                {
                    "h3": "Assento Elevado — Menos Esforço para Sentar e Levantar",
                    "content": "O assento alto é especialmente útil para quem tem problemas no joelho ou na coluna. A posição também evita areia no colo em dias de vento.",
                    "bullets": [
                        "Assento alto em posição ergonômica",
                        "Estrutura em alumínio com tratamento anticorrosão",
                        "Encosto reclinável",
                        "Apoio de braços laterais acolchoados",
                        "Tecido resistente à maresia, areia e raios UV",
                        "Capacidade de carga de até 110 kg",
                    ],
                },
                {
                    "h3": "Alumínio não Enferruja na Areia",
                    "content": "Mesmo com exposição constante à água salgada e à areia, o alumínio não oxida. Mais leve do que aço para carregar da garagem à praia.",
                    "bullets": [
                        "Alumínio de alta resistência sem risco de oxidação",
                        "Limpeza com pano úmido após o uso",
                        "Dobrável com mecanismo de trava de segurança",
                    ],
                },
                {
                    "h3": "Conceito Lazy",
                    "content": "O nome diz o que é: uma cadeira pensada para quem quer o máximo de conforto com o mínimo de incômodo. Assinatura Mormaii.",
                },
            ],
            "conclusao": "Cadeira Alta Lazy Mormaii disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cama-de-solteiro-dobravel-kayman-camping-bege-291030-ntk-78023",
        "keyword": "cama de armar solteiro",
        "seo_title": "Cama Dobrável Solteiro Kayman Camping NTK | Ultra Máquinas",
        "meta_description": "Cama de camping dobrável para solteiro em estrutura de aço tubular resistente — fácil de montar e transportar. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cama Dobrável Solteiro Kayman NTK",
            "intro": "Dormir no chão no camping tem um custo no dia seguinte. A Cama Dobrável Kayman da NTK tem estrutura tubular de aço, leito elevado do chão e montagem sem ferramentas.",
            "h3_sections": [
                {
                    "h3": "Aço Tubular que Aguenta Uso Repetido",
                    "content": "Tubos de parede grossa unidos por conectores reforçados. O leito em lona brim esticada distribui o peso, sem ponto de pressão nas costas.",
                    "bullets": [
                        "Estrutura em aço tubular galvanizado",
                        "Leito em lona brim reforçada costurada nos tubos",
                        "Capacidade de carga de até 120 kg",
                        "Altura do leito: aproximadamente 38cm",
                        "Pés com ponteiras de borracha para estabilidade",
                        "Dimensões do leito: 190cm × 65cm (solteiro)",
                    ],
                },
                {
                    "h3": "Montagem em Menos de 5 Minutos",
                    "content": "As pernas encaixam nos tubos transversais por pressão, sem ferramentas. Desmonta em forma de fole e cabe na bolsa de transporte inclusa.",
                    "bullets": [
                        "Montagem sem ferramentas — encaixe por pressão",
                        "Dobra em forma de fole para transporte",
                        "Acompanha bolsa de transporte resistente",
                        "Montagem e desmontagem em menos de 5 minutos",
                    ],
                },
                {
                    "h3": "Camping, Hóspede Inesperado ou Emergência",
                    "content": "A Kayman serve como cama extra para hóspedes, em festas ou em situações temporárias. A cor bege combina com qualquer ambiente.",
                },
            ],
            "conclusao": "Cama Dobrável Kayman NTK disponível na Ultra Máquinas com entrega para todo o Brasil. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/mesa-dobravel-com-ajuste-de-altura-robust-80cm-ntk-preto-291101-nautika-78828",
        "keyword": "mesa ntk robust 80cm",
        "seo_title": "Mesa NTK Robust 80cm com Ajuste de Altura | Ultra Máquinas",
        "meta_description": "Mesa dobrável NTK Robust com ajuste de altura até 80cm — pés reguláveis, tampo em MDF reforçado e estrutura em aço. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Mesa NTK Robust 80cm com Ajuste de Altura",
            "intro": "Os quatro pés da Mesa Robust 80cm da NTK são reguláveis em múltiplas posições. Ela se adapta a cadeiras de diferentes alturas, ao uso em pé ou a qualquer configuração que o acampamento exigir.",
            "h3_sections": [
                {
                    "h3": "Pés Reguláveis até 80cm",
                    "content": "Configure a altura para refeições, atividades manuais no camping ou como suporte para equipamentos. Cada pé trava de forma independente.",
                    "bullets": [
                        "Pés reguláveis em múltiplas alturas (até 80cm)",
                        "Sistema de trava seguro por pé",
                        "Tampo em MDF revestido, resistente a umidade e impactos",
                        "Estrutura em aço com pintura eletrostática preta",
                        "Dimensões do tampo: 80cm × 60cm",
                        "Capacidade de carga: até 60 kg",
                    ],
                },
                {
                    "h3": "Dobra em Pacote Plano",
                    "content": "O tampo dobra sobre os pés. O conjunto formado cabe facilmente no porta-malas. Pés com borracha antiderrapante nos extremos.",
                    "bullets": [
                        "Tampo dobrável sobre os pés",
                        "Pés com borracha antiderrapante",
                        "Fácil de limpar com pano úmido",
                        "Útil em camping, piquenique, eventos e garagem",
                    ],
                },
                {
                    "h3": "A Linha NTK é Conhecida Entre Campistas",
                    "content": "A Robust foi projetada para uso repetido, com materiais que aguentam várias temporadas sem perder rigidez.",
                },
            ],
            "conclusao": "Mesa NTK Robust 80cm disponível na Ultra Máquinas. Compre no Pix e aproveite 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-de-praia-copacabana-reclinavel-5-posicoes-rosa-cad0683-botafogo-76542",
        "keyword": "cadeira de praia botafogo copacabana",
        "seo_title": "Cadeira de Praia Reclinável Copacabana Rosa Botafogo",
        "meta_description": "Cadeira de praia rosa com 5 posições de reclinação — armação em alumínio leve e tecido resistente à areia. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira de Praia Copacabana Reclinável Rosa",
            "intro": "A Cadeira de Praia Copacabana da Botafogo tem 5 posições de reclinação e cor rosa. Boa para tomar sol, ler ou contemplar o mar — o mecanismo de trava lateral opera com uma só mão.",
            "h3_sections": [
                {
                    "h3": "5 Posições de Reclinação",
                    "content": "Da posição sentada ereta até quase deitada. O travamento é simples de operar mesmo sentado, sem precisar levantar.",
                    "bullets": [
                        "5 posições de reclinação do encosto",
                        "Sistema de travamento lateral de operação fácil",
                        "Posição quase plana para banho de sol",
                        "Encosto com ventilação em tira",
                        "Apoio de cabeça integrado",
                        "Faixa porta-objetos lateral",
                    ],
                },
                {
                    "h3": "Alumínio Leve e sem Ferrugem",
                    "content": "A armação em alumínio não enferruja em contato com água salgada. Fácil de carregar da garagem à areia.",
                    "bullets": [
                        "Estrutura tubular em alumínio resistente",
                        "Tecido em poliéster resistente à areia e maresia",
                        "Tratamento anticorrosão nos tubos",
                        "Dobrável para transporte compacto",
                        "Capacidade de carga até 100 kg",
                    ],
                },
                {
                    "h3": "Cor Rosa Resistente ao Sol",
                    "content": "O tecido rosa aguenta cloro, sal e sol intenso sem desbotar rápido. Para quem quer estilo mesmo nos dias de lazer.",
                },
            ],
            "conclusao": "Cadeira Copacabana Rosa Botafogo disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-praia-reclinavel-5-posicoes-botafogo-74360",
        "keyword": "cadeira de praia botafogo",
        "seo_title": "Cadeira de Praia Botafogo Reclinável | Ultra Máquinas",
        "meta_description": "Cadeira de praia Botafogo com 5 posições de reclinação — estrutura em alumínio leve e fácil de transportar. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira de Praia Botafogo Reclinável",
            "intro": "A Cadeira de Praia Reclinável 5 Posições da Botafogo tem alumínio na estrutura, tecido resistente à maresia e custo-benefício que justifica a fidelidade de quem vai à praia todo fim de semana.",
            "h3_sections": [
                {
                    "h3": "5 Posições para Cada Momento do Dia",
                    "content": "Ereta para comer, inclinada para conversar, quase plana para pegar sol. O mecanismo funciona sem precisar levantar da cadeira.",
                    "bullets": [
                        "5 posições de reclinação ajustáveis",
                        "Mecanismo de trava simples e confiável",
                        "Encosto ventilado em faixas — menos calor nas costas",
                        "Apoio de braços bilateral",
                        "Bolso lateral para pertences",
                    ],
                },
                {
                    "h3": "Alumínio que Aguenta Temporada Inteira",
                    "content": "O alumínio não enferruja com maresia, é leve para carregar e dura mais do que aço sem tratamento. Os tubos da Botafogo têm tratamento de superfície.",
                    "bullets": [
                        "Tubos em alumínio com tratamento de superfície",
                        "Tecido em poliéster resistente à maresia e UV",
                        "Pés com ponteiras largas para estabilidade na areia",
                        "Dobrável e compacta para transporte",
                        "Capacidade de carga até 100 kg",
                    ],
                },
                {
                    "h3": "Para Quem Vai à Praia Com Frequência",
                    "content": "A qualidade dos materiais faz diferença depois de 20 ou 30 lavagens e de um verão inteiro de sol forte. A Botafogo Reclinável aguentam esse ritmo.",
                },
            ],
            "conclusao": "Cadeira de Praia Botafogo Reclinável 5 Posições disponível na Ultra Máquinas. Compre no Pix e garanta 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/lavadora-de-alta-vazao-2-0cv-el-4000v2-a-39453-8-eletroplas-76252",
        "keyword": "lavadora eletroplas 2cv",
        "seo_title": "Lavadora Eletroplas 2CV Alta Pressão | Ultra Máquinas",
        "meta_description": "Potência 2CV para limpeza pesada: lavadora Eletroplas EL-4000V2 com alta vazão e motor elétrico robusto. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Lavadora de Alta Pressão Eletroplas 2CV EL-4000V2",
            "intro": "A Lavadora Eletroplas EL-4000V2 com motor de 2CV trabalha em regime contínuo sem superaquecimento. Desenvolvida para uso semiprofissional e profissional, remove sujeira incrustada em concreto, veículos pesados, fachadas e equipamentos industriais.",
            "h3_sections": [
                {
                    "h3": "Motor 2CV com Bomba de Bronze",
                    "content": "A bomba axial de pistão de bronze entrega pressão constante e tem vida útil muito superior às bombas plásticas dos modelos básicos.",
                    "bullets": [
                        "Motor elétrico 2CV com proteção térmica",
                        "Bomba de pistão em bronze",
                        "Pressão de trabalho: até 1750 PSI",
                        "Vazão: até 8 L/min",
                        "Tensão: 220V",
                        "Acompanha lança, mangueira e bico multifuncional",
                    ],
                },
                {
                    "h3": "Alta Vazão para Trabalhos Pesados",
                    "content": "A vazão de 8 L/min reduz o tempo de limpeza em relação às máquinas domésticas, com menor consumo total de água.",
                    "bullets": [
                        "Fachadas, pisos e calçadas",
                        "Veículos pesados: caminhões, ônibus e tratores",
                        "Remove graxas e resíduos incrustados",
                        "Opera com água de torneira, sem pressurização externa",
                    ],
                },
                {
                    "h3": "Postos, Oficinas e Grandes Propriedades",
                    "content": "A EL-4000V2 é usada em postos de combustível, oficinas mecânicas, construtoras e propriedades rurais que precisam de limpeza pesada com frequência.",
                },
            ],
            "conclusao": "Lavadora Eletroplas 2CV EL-4000V2 disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/mesa-dobravel-camping-nautika-robust-80cm-78121",
        "keyword": "mesa dobravel camping nautika",
        "seo_title": "Mesa Dobrável Camping Nautika Robust 80cm | Ultra Máquinas",
        "meta_description": "Mesa dobrável de camping Nautika Robust com 80cm de altura — estrutura em aço leve e fácil de montar. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Mesa Dobrável Camping Nautika Robust 80cm",
            "intro": "A Mesa Dobrável Robust 80cm da Nautika tem estrutura em aço tratado, tampo espaçoso e articulações reforçadas. Solo irregular, chuva passageira ou calor intenso — ela mantém a rigidez.",
            "h3_sections": [
                {
                    "h3": "Aço com Tratamento Anticorrosão",
                    "content": "As articulações em aço reforçado mantêm a rigidez mesmo depois de muitas montagens. Os pés têm borracha antiderrapante.",
                    "bullets": [
                        "Estrutura em aço com tratamento anticorrosão",
                        "Tampo em material resistente a impactos",
                        "Pés com borracha antiderrapante",
                        "Altura de 80cm — ergonômica para adultos em pé",
                        "Capacidade de carga: até 50 kg no tampo",
                        "Articulações em aço reforçado",
                    ],
                },
                {
                    "h3": "Duas Dobras, Zero Ferramentas",
                    "content": "As pernas se dobram para baixo do tampo em dois movimentos. O conjunto fica plano e encaixa no porta-malas. Peso aproximado de 4 kg.",
                    "bullets": [
                        "Dobra em 2 movimentos — sem ferramentas",
                        "Formato plano para o porta-malas",
                        "Peso aproximado de 4 kg",
                        "Acompanha alça de transporte",
                    ],
                },
                {
                    "h3": "Além do Camping",
                    "content": "Churrascos, feiras, eventos ao ar livre. A altura padrão de 80cm é compatível com cadeiras e banquetas comuns.",
                },
            ],
            "conclusao": "Mesa Dobrável Nautika Robust 80cm disponível na Ultra Máquinas. Compre no Pix e aproveite 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/lavadora-de-alta-jaguar-turbo-pressao-2175-libras-127v-b8-065-0009-lavor-77105",
        "keyword": "lavadora jaguar turbo 2175",
        "seo_title": "Lavadora Jaguar Turbo 2175 Libras Lavor | Ultra Máquinas",
        "meta_description": "Lavadora Lavor Jaguar Turbo com 2175 libras de pressão e 127V — potência profissional para limpeza pesada. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Lavadora Lavor Jaguar Turbo 2175 Libras",
            "intro": "A Lavor Jaguar Turbo chega a 2175 PSI de pressão máxima com motor de alta eficiência em 127V. Remove graxas de motor, mofo em pisos, lama compactada e resíduos de tintas que lavadoras domésticas comuns não alcançam.",
            "h3_sections": [
                {
                    "h3": "2175 PSI com Bico Turbo",
                    "content": "O bico regulável Turbo intensifica o jato para superfícies mais resistentes. A mangueira de alta pressão de 5 metros acompanha o kit.",
                    "bullets": [
                        "Pressão máxima de 2175 PSI (150 bar)",
                        "Motor elétrico 127V",
                        "Vazão média de 7 L/min",
                        "Cabo elétrico blindado",
                        "Mangueira de alta pressão de 5 metros",
                        "Bico regulável Turbo",
                    ],
                },
                {
                    "h3": "Bomba de Pistão em Metal de Precisão",
                    "content": "Pistões em metal mantêm pressão constante do início ao fim do trabalho, sem queda de desempenho em limpezas longas.",
                    "bullets": [
                        "Bomba axial de pistão em metal",
                        "Sistema Turbo para intensificação do jato",
                        "Proteção automática contra superaquecimento",
                        "Entrada de detergente",
                        "Certificação INMETRO",
                    ],
                },
                {
                    "h3": "Para Casa e Pequenos Negócios",
                    "content": "Casas com área externa, garagens, calçadas, piscinas e pequenas frotas de veículos. Desempenho acima do doméstico sem o custo do industrial.",
                },
            ],
            "conclusao": "Lavadora Lavor Jaguar Turbo 2175 Libras disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/lavadora-de-alta-pressao-hd-498-1800w-14237050-karcher-75780",
        "keyword": "lavadora karcher hd 498",
        "seo_title": "Lavadora Karcher HD 498 1800W Alta Pressão | Ultra Máquinas",
        "meta_description": "Lavadora Kärcher HD 498 com 1800W de potência e alta pressão — desempenho profissional para superfícies externas. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Lavadora Kärcher HD 498 1800W",
            "intro": "A Kärcher HD 498 tem 1800W de potência e pertence à linha HD — projetada para uso profissional intenso, com componentes de vida útil superior à linha K doméstica.",
            "h3_sections": [
                {
                    "h3": "1800W e Pressão Constante em Jornadas Longas",
                    "content": "O motor de 1800W alimenta uma bomba que mantém pressão constante mesmo em horas contínuas de trabalho. Câmeras de pressão em latão.",
                    "bullets": [
                        "Motor elétrico de 1800W",
                        "Pressão máxima: até 130 bar (1885 PSI)",
                        "Vazão de trabalho: até 7,5 L/min",
                        "Bomba de pistão em metal",
                        "Proteção automática contra sobrecarga",
                        "Certificação Kärcher para uso profissional",
                    ],
                },
                {
                    "h3": "Construção para Condições de Obra",
                    "content": "Câmeras de pressão em latão, vedações que aguentam solventes e detergentes profissionais. O chassi tem rodinhas para mobilidade no local de trabalho.",
                    "bullets": [
                        "Câmera de pressão e pistões em latão",
                        "Mangueira de alta pressão de 10 metros",
                        "Lança em alumínio com bico regulável",
                        "Estrutura com rodinhas",
                        "Entrada de detergente",
                    ],
                },
                {
                    "h3": "Fachadas, Frotas e Pisos Industriais",
                    "content": "Prédios, frotas de veículos, equipamentos agrícolas e pisos industriais. A HD 498 é usada por empresas de limpeza e equipes de manutenção.",
                },
            ],
            "conclusao": "Lavadora Kärcher HD 498 1800W disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/ombrellone-central-pisa-articulado-em-aluminio-poliester-2-50m-preto-14507-bel-fix-78575",
        "keyword": "ombrellone articulado 2,50m",
        "seo_title": "Ombrellone Pisa Articulado 2,50m Alumínio | Ultra Máquinas",
        "meta_description": "Ombrellone articulado com haste de alumínio 2,50m e tecido em poliéster preto — ideal para jardim e piscina. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Ombrellone Pisa Articulado 2,50m Alumínio",
            "intro": "O Ombrellone Pisa da Bel Fix tem articulação que inclina a cobertura sem mover a base. Com 2,50m de diâmetro em poliéster preto e haste de alumínio, cobre jardins, decks de piscina e áreas de lazer.",
            "h3_sections": [
                {
                    "h3": "Articula sem Mover a Base",
                    "content": "O sistema articulado inclina a cobertura em diferentes ângulos para acompanhar o sol durante o dia — manhã, tarde e fim de tarde — sem deslocar nada.",
                    "bullets": [
                        "Sistema articulado para inclinação da cobertura",
                        "Diâmetro de 2,50m",
                        "Haste central em alumínio anticorrosivo",
                        "Tecido em poliéster preto com fator de proteção UV",
                        "Abertura por manivela",
                        "Encaixes reforçados nas varetas",
                    ],
                },
                {
                    "h3": "Alumínio e Poliéster: Sem Manutenção Especial",
                    "content": "A haste de alumínio não enferruja. O tecido em poliéster resiste ao desbotamento por UV, à chuva e ao calor. Limpeza com água e sabão neutro.",
                    "bullets": [
                        "Haste em alumínio de alta resistência",
                        "Varetas estruturais em alumínio",
                        "Tecido poliéster com tratamento UV e impermeabilizante",
                        "Limpeza simples com água e sabão neutro",
                    ],
                },
                {
                    "h3": "Visual que Combina com Qualquer Jardim",
                    "content": "O design limpo e a cor preta se integram a ambientes rústicos ou modernos sem pedir atenção.",
                },
            ],
            "conclusao": "Ombrellone Pisa Articulado Bel Fix disponível na Ultra Máquinas com 10% de desconto no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/tenda-gazebo-dobravel-3m-x-3m-poliester-bege-bel-331500-bel-fix-77202",
        "keyword": "gazebo dobrável 3x3",
        "seo_title": "Gazebo Dobrável 3x3m Bege Bel Fix | Ultra Máquinas",
        "meta_description": "Gazebo dobrável 3x3m em poliéster bege resistente — montagem sem ferramentas e estrutura em aço tratado. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Gazebo Dobrável 3×3m Bel Fix",
            "intro": "O Gazebo Dobrável 3×3m Bel Fix tem estrutura sanfona em aço tratado e teto em poliéster bege impermeabilizado. Uma pessoa monta em menos de 10 minutos, sem ferramentas.",
            "h3_sections": [
                {
                    "h3": "Estrutura Sanfona com Trava por Perna",
                    "content": "O mecanismo de travamento em cada perna garante estabilidade mesmo com vento. As pernas são ajustáveis em 3 alturas.",
                    "bullets": [
                        "Cobertura: 3m × 3m (9m²)",
                        "Estrutura sanfona em aço anticorrosão",
                        "Abertura e fechamento em menos de 10 minutos",
                        "Pernas ajustáveis em 3 alturas",
                        "Trava de segurança por perna",
                        "Acompanha bolsa de transporte",
                    ],
                },
                {
                    "h3": "Teto que Aguenta Chuva e Sol",
                    "content": "Poliéster 180g/m² com impermeabilização e proteção UV. Costuras seladas para evitar infiltração. A cor bege reflete a luz solar.",
                    "bullets": [
                        "Tecido em poliéster 180g/m² impermeabilizado",
                        "Proteção UV",
                        "Costuras seladas",
                        "Cor bege que reflete o sol",
                        "Limpeza com esponja e água",
                    ],
                },
                {
                    "h3": "Para Eventos de Um ou Vários Dias",
                    "content": "Fica montado por vários dias sem problemas. Bom para feiras de rua, eventos corporativos e proteção temporária em obras.",
                },
            ],
            "conclusao": "Gazebo Dobrável 3×3m Bel Fix disponível na Ultra Máquinas com 10% de desconto pagando no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/caixa-termica-19-litros-acai-71909-bel-77810",
        "keyword": "caixa térmica 19 litros",
        "seo_title": "Caixa Térmica Açaí 19 Litros Bel 71909 | Ultra Máquinas",
        "meta_description": "Caixa térmica Açaí 19 litros — mantém sua bebida gelada por horas com isolamento térmico de alta performance. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Caixa Térmica Açaí 19 Litros Bel",
            "intro": "A Caixa Térmica Açaí da Bel tem 19 litros — espaço para cerca de 20 latinhas — e paredes de poliuretano expandido de alta densidade. Gelo que dura horas mesmo sob sol direto.",
            "h3_sections": [
                {
                    "h3": "19 Litros: Tamanho Certo para o Dia",
                    "content": "Cabe tudo para o dia sem ser grande demais para carregar. O interior liso em polipropileno facilita a limpeza.",
                    "bullets": [
                        "Capacidade: 19 litros — cerca de 20 latas de 350ml",
                        "Interior em polipropileno liso",
                        "Tampa com vedação hermética",
                        "Dreno de acesso rápido para escoar a água do gelo",
                        "Alça ergonômica",
                        "Trava de segurança na tampa",
                    ],
                },
                {
                    "h3": "Paredes de Poliuretano de Alta Densidade",
                    "content": "O mesmo material das caixas profissionais. Mantém a temperatura interna muito abaixo da externa, mesmo exposta ao sol direto por horas.",
                    "bullets": [
                        "Paredes com isolamento em poliuretano de alta densidade",
                        "Mantém gelo por até 12 horas em condições normais",
                        "Parede dupla",
                        "Mais eficiente do que caixas de isopor convencional",
                    ],
                },
                {
                    "h3": "Pesca, Camping e Praia",
                    "content": "Para o pescador guarda iscas resfriadas. No camping conserva alimentos perecíveis. Na praia, é o chope gelado do fim da tarde.",
                },
            ],
            "conclusao": "Caixa Térmica Açaí 19L Bel disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/tenda-gazebo-tubular-2m-polietileno-azul-belfix-301302-74641",
        "keyword": "tenda gazebo 2m",
        "seo_title": "Gazebo Tubular 2m Polietileno Azul BelFix | Ultra Máquinas",
        "meta_description": "Tenda gazebo tubular 2m em polietileno azul — estrutura leve e montagem rápida para eventos ao ar livre. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Tenda Gazebo Tubular 2m BelFix",
            "intro": "A Tenda Gazebo Tubular 2m da BelFix tem estrutura tubular metálica galvanizada e cobertura em polietileno azul. Uma pessoa monta, pernas ajustáveis para terrenos irregulares.",
            "h3_sections": [
                {
                    "h3": "Estrutura Galvanizada, Pernas Ajustáveis",
                    "content": "Leve o suficiente para uma pessoa montar sozinha, com travas simples em cada perna e ilhoses nas bordas para fixação com cordas.",
                    "bullets": [
                        "Estrutura tubular em metal galvanizado",
                        "Pernas ajustáveis em múltiplas alturas",
                        "Trava simples por perna",
                        "Cobertura em polietileno azul resistente a UV e chuva",
                        "Bordas com ilhoses para cordas",
                        "Montagem por uma pessoa",
                    ],
                },
                {
                    "h3": "Polietileno com Tratamento UV",
                    "content": "Resiste ao desbotamento e ao enfraquecimento causado pela exposição solar. Impermeável para chuvas inesperadas. Lava com água e sabão neutro.",
                    "bullets": [
                        "Polietileno com tratamento UV",
                        "Impermeável",
                        "Costura reforçada nas junções",
                        "Fácil de dobrar e guardar",
                        "Lavável com água e sabão",
                    ],
                },
                {
                    "h3": "Churrascos, Feiras e Eventos Esportivos",
                    "content": "A cor azul é fácil de localizar entre outros equipamentos. Transmite aspecto organizado em feiras e exposições.",
                },
            ],
            "conclusao": "Tenda Gazebo Tubular 2m BelFix disponível na Ultra Máquinas. Pague no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/ombrellone-suspenso-giratorio-360%C2%B0-buzios-3m-marrom-c-base-50-lts-891012-bel-77818",
        "keyword": "ombrellone suspenso giratório 3m",
        "seo_title": "Ombrellone Suspenso Giratório 360° Búzios 3m + Base Bel",
        "meta_description": "Ombrellone suspenso giratório 360°, 3m de cobertura com base de água e areia 50L incluída — sombra total. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Ombrellone Suspenso Giratório 360° Búzios 3m",
            "intro": "O Ombrellone Suspenso Búzios da Bel tem haste lateral e cobertura de 3m que gira 360°. Você direciona a sombra sem mover a base nem se levantar. Acompanha base de 50 litros.",
            "h3_sections": [
                {
                    "h3": "Gira 360°, Trava em Qualquer Posição",
                    "content": "Com um simples movimento a cobertura muda de direção para acompanhar o sol. Nenhum parafuso para ajustar, nenhuma base para arrastar.",
                    "bullets": [
                        "Rotação total de 360° com travamento em qualquer posição",
                        "Cobertura de 3 metros de diâmetro",
                        "Haste lateral — sem mastro central no espaço útil",
                        "Mecanismo de inclinação para ajuste do ângulo",
                        "Tecido em poliéster marrom com tratamento UV",
                        "Abertura e fechamento por manivela",
                    ],
                },
                {
                    "h3": "Base de 50 Litros Inclusa",
                    "content": "Preencha com água (50 kg) ou areia (mais peso). Estabilidade total com vento moderado, sem fixação no piso. Rodas para reposicionar quando vazia.",
                    "bullets": [
                        "Base plástica com 50L de capacidade",
                        "Preenchimento com água (50 kg) ou areia",
                        "Rodas para reposicionar quando vazia",
                        "Encaixe central para a haste",
                    ],
                },
                {
                    "h3": "Piscina, Deck e Jardim com Layout Irregular",
                    "content": "Onde a haste central de um ombrellone comum atrapalharia o espaço, o Búzios não ocupa. A sombra vai onde está a pessoa.",
                },
            ],
            "conclusao": "Ombrellone Suspenso Búzios 3m Bel com base inclusa disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/guarda-sol-bagum-haste-de-aluminio-2-00m-azul-royal-10602-bel-74687",
        "keyword": "guarda-sol alumínio 2m",
        "seo_title": "Guarda-Sol Bagum Alumínio 2m Azul Royal Bel | Ultra Máquinas",
        "meta_description": "Guarda-sol Bagum com haste de alumínio 2m e tecido azul royal — leve e resistente para praia ou piscina. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Guarda-Sol Bagum Alumínio 2m Azul Royal Bel",
            "intro": "O Guarda-Sol Bagum da Bel tem haste em alumínio resistente à maresia, cobertura de 2m em azul royal e cerca de 1,8 kg — fácil de carregar embaixo do braço.",
            "h3_sections": [
                {
                    "h3": "Alumínio não Enferruja na Areia Molhada",
                    "content": "Crave na areia molhada, lave com água do mar e guarde sem se preocupar com oxidação. A abertura é por botão de trava simples.",
                    "bullets": [
                        "Haste em alumínio — sem risco de ferrugem",
                        "Diâmetro de cobertura: 2 metros",
                        "Tecido em poliéster azul royal com proteção UV",
                        "Abertura por botão de trava",
                        "Ponteira de metal para encaixe na areia",
                        "Peso aproximado de 1,8 kg",
                    ],
                },
                {
                    "h3": "2m de Sombra para Uma ou Duas Pessoas",
                    "content": "A ventilação superior evita que o vento vire o guarda-sol. O azul royal não desbota rápido e é fácil de encontrar entre dezenas de outros na areia.",
                    "bullets": [
                        "Protege até 2 adultos do sol direto",
                        "Ventilação superior contra viradas pelo vento",
                        "Acabamento das bordas com reforço de viés",
                        "Compacto para a bolsa de praia",
                    ],
                },
                {
                    "h3": "Praia, Piscina ou Jardim",
                    "content": "Cria um ponto de sombra rápido sem montar uma estrutura complexa. Funciona bem em qualquer espaço ao ar livre.",
                },
            ],
            "conclusao": "Guarda-Sol Bagum Alumínio 2m Azul Royal Bel disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/ombrellone-central-retangular-quiosque-oversize-4-50m-marrom-12412-bel-fix-78574",
        "keyword": "ombrellone retangular 4,50m",
        "seo_title": "Ombrellone Retangular 4,50m Oversize Marrom Bel Fix",
        "meta_description": "Ombrellone retangular de 4,50m tipo quiosque — ideal para áreas extensas com cobertura ampla e estrutura robusta. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Ombrellone Retangular Oversize 4,50m Bel Fix",
            "intro": "O Ombrellone Retangular Oversize 4,50m da Bel Fix cobre mesas longas, conjuntos de piscina em linha ou decks alongados onde um ombrellone circular deixaria espaços descobertos.",
            "h3_sections": [
                {
                    "h3": "4,50m no Eixo Principal — Formato Retangular",
                    "content": "O retangular maximiza a área coberta em relação à base usada. Com 4,50m × 2,70m aproximadamente, cobre mesas de 4 a 6 pessoas com folga.",
                    "bullets": [
                        "Dimensão principal: 4,50m × 2,70m aprox.",
                        "Haste central em alumínio de parede grossa",
                        "Varetas estruturais reforçadas",
                        "Tecido em poliéster marrom de alta densidade com tratamento UV",
                        "Abertura por manivela integrada",
                    ],
                },
                {
                    "h3": "Componentes no Padrão dos Ombrellones Comerciais",
                    "content": "Encaixes metálicos nas juntas, haste de alto calibre e sistema de trava de segurança no mecanismo de abertura.",
                    "bullets": [
                        "Haste em alumínio de alto calibre",
                        "Varetas de abertura com juntas metálicas",
                        "Sistema de trava de segurança",
                        "Compatível com bases de grande porte (vendidas separadamente)",
                        "Cor marrom que combina com madeira e pedra",
                    ],
                },
                {
                    "h3": "Restaurantes, Hotéis e Residências com Área Grande",
                    "content": "Um ombrellone 4,50m no lugar de dois ou três menores. Menos estrutura no espaço, mais cobertura.",
                },
            ],
            "conclusao": "Ombrellone Retangular Oversize 4,50m Bel Fix disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/base-para-guarda-sol-e-ombrellone-agua-areia-18kg-preta-70027107-bel-fix-76391",
        "keyword": "base para guarda-sol 18kg",
        "seo_title": "Base Guarda-Sol 18kg Água/Areia Bel Fix | Ultra Máquinas",
        "meta_description": "Base para guarda-sol e ombrellone com 18kg preenchida com água ou areia — suporte estável para uso na praia. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Base para Guarda-Sol e Ombrellone 18kg Bel Fix",
            "intro": "Para usar guarda-sol em deck de madeira, porcelanato, concreto polido ou terraço, a Base 18kg Bel Fix preenche com água ou areia e ancora a haste com firmeza — sem parafusos, sem danos à superfície.",
            "h3_sections": [
                {
                    "h3": "18 Litros de Água ou Areia — Sem Ferramentas",
                    "content": "Preenchida com água chega a 18 kg. Com areia, mais ainda. A tampa abre fácil para encher e esvaziar. Rodas na base para reposicionar quando vazia.",
                    "bullets": [
                        "Capacidade: 18 litros de água ou areia seca",
                        "Peso total com água: aproximadamente 18 kg",
                        "Tampa de fácil abertura",
                        "Encaixe central para hastes de diferentes diâmetros",
                        "Rodas inferiores para reposicionar vazia",
                        "Plástico resistente a UV",
                    ],
                },
                {
                    "h3": "Encaixe Universal com Adaptadores",
                    "content": "Compatível com a maioria dos guarda-sóis e ombrellones do mercado. Parafuso lateral trava a haste na posição.",
                    "bullets": [
                        "Encaixe universal para hastes de diferentes calibres",
                        "Adaptadores inclusos",
                        "Parafuso de fixação lateral",
                        "Suporta ombrellones de até 2,70m",
                        "Cor preta discreta",
                    ],
                },
                {
                    "h3": "Esvaziada Pesa Cerca de 2 kg",
                    "content": "Compacta para guardar no fim da temporada ou levar para outro local. As rodinhas facilitam o reposicionamento quando ainda preenchida.",
                },
            ],
            "conclusao": "Base Guarda-Sol 18kg Bel Fix disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/cadeira-espreguicadeira-em-aluminio-marrom-414712-bel-77702",
        "keyword": "espreguiçadeira alumínio",
        "seo_title": "Cadeira Espreguiçadeira Alumínio Marrom Bel | Ultra Máquinas",
        "meta_description": "Espreguiçadeira em alumínio marrom resistente — ideal para piscina, jardim e área de lazer com design leve. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Cadeira Espreguiçadeira em Alumínio Marrom Bel",
            "intro": "A Espreguiçadeira Bel em alumínio marrom tem comprimento estendido com suporte do corpo da cabeça aos pés, encosto reclinável em múltiplas posições e estrutura que não enferruja próxima a piscinas.",
            "h3_sections": [
                {
                    "h3": "Alumínio Anodizado em Área Úmida",
                    "content": "Próxima a piscinas com respingos constantes e sol direto, o alumínio não enferruja, não descasca e não precisa de manutenção especial. O acabamento fosco marrom disfarça riscos.",
                    "bullets": [
                        "Estrutura tubular em alumínio anodizado",
                        "Tecido do assento em poliéster resistente ao cloro e UV",
                        "Encosto reclinável em múltiplas posições",
                        "Capacidade de carga: até 120 kg",
                        "Pés com ponteiras de borracha para não arranhar o piso",
                    ],
                },
                {
                    "h3": "Suporte Total do Corpo para Horas de Relaxamento",
                    "content": "Comprimento de aproximadamente 170cm. Do encosto ereto para leitura até completamente deitado para bronzeamento — sem as pernas suspensas no ar.",
                    "bullets": [
                        "Comprimento de aproximadamente 170cm",
                        "Encosto com múltiplas posições de reclinação",
                        "Apoio de cabeça integrado",
                        "Tecido trançado que evita abafamento nas costas",
                        "Dobra e empilha quando não está em uso",
                    ],
                },
                {
                    "h3": "Marrom: Neutro para Qualquer Estilo de Área Externa",
                    "content": "Combina com madeira, pedras naturais, porcelanatos e qualquer decoração de área externa — do rústico ao contemporâneo.",
                },
            ],
            "conclusao": "Espreguiçadeira Alumínio Marrom Bel disponível na Ultra Máquinas com 10% de desconto no Pix.",
        },
    },
    {
        "url": "https://www.ultramaquinas.com.br/produto/caixa-termica-branca-113-litros-igloo-279411-kala-81054",
        "keyword": "caixa térmica igloo 113 litros",
        "seo_title": "Caixa Térmica Igloo 113 Litros Branca Kala | Ultra Máquinas",
        "meta_description": "Caixa térmica Igloo 113L — alto isolamento, dreno de fácil acesso e tampa robusta para pescaria e acampamento. Compre no Pix e ganhe 10% de desconto.",
        "descricao": {
            "h2": "Caixa Térmica Igloo 113 Litros",
            "intro": "A Caixa Térmica Igloo 113 Litros tem espaço para mais de 120 latas ou dezenas de quilos de pescado. O gelo dura de 3 a 5 dias em condições normais graças à espuma de poliuretano de alta densidade nas paredes.",
            "h3_sections": [
                {
                    "h3": "113 Litros: Para Grupos Grandes ou Uso Profissional",
                    "content": "Abertura larga para carregar e acessar com facilidade. Dreno com plug removível para escoar a água rápido. Alças laterais robustas para dois carregadores.",
                    "bullets": [
                        "Capacidade: 113 litros — mais de 120 latas de 350ml",
                        "Abertura larga",
                        "Interior em polipropileno liso",
                        "Dreno com plug removível",
                        "Alças laterais para dois carregadores",
                        "Rodas traseiras para movimentação",
                    ],
                },
                {
                    "h3": "Gelo por 3 a 5 Dias",
                    "content": "Paredes com poliuretano de alta densidade e tampa com vedação de borracha. Trava metálica na tampa para o transporte.",
                    "bullets": [
                        "Paredes com poliuretano expandido de alta densidade",
                        "Tampa com vedação hermética de borracha",
                        "Mantém gelo de 3 a 5 dias em condições normais",
                        "Parede dupla de isolamento",
                        "Trava metálica na tampa",
                    ],
                },
                {
                    "h3": "Pesca, Camping e Eventos",
                    "content": "Na pesca guarda o pescado fresco por dias. No camping conserva alimentos por toda a viagem. Em eventos, bebidas geladas para um grupo grande.",
                },
            ],
            "conclusao": "Caixa Térmica Igloo 113 Litros Kala disponível na Ultra Máquinas. Compre no Pix e ganhe 10% de desconto.",
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
