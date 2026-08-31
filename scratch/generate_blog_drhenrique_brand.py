# -*- coding: utf-8 -*-
import os, json

POSTS = [
    # 1. Harmonização Facial
    {
        "slug": "harmonizacao-facial-mitos-e-verdades-curitiba",
        "title": "Harmonização Facial em Curitiba: 7 Mitos e Verdades que Você Precisa Saber",
        "category": "Harmonização Facial",
        "excerpt": "Descubra o que é verdade e o que é mito sobre a harmonização facial. Entenda como o procedimento preserva a naturalidade e valoriza seus traços em Curitiba.",
        "cover": "assets/img/resultados/caso-harmonizacao-feminina-1.webp",
        "coverAlt": "Antes e depois de harmonização facial feminina com naturalidade em Curitiba",
        "date": "2026-08-15",
        "readingMinutes": 5,
        "tags": ["Harmonização Facial", "Curitiba", "Ácido Hialurônico", "Naturalidade"],
        "lead": "A busca por procedimentos estéticos que valorizam a beleza natural sem exageros tem crescido expressivamente em Curitiba. No entanto, muitas dúvidas e desinformações ainda cercam a harmonização facial.",
        "sections": [
            {
                "id": "secao-artificial",
                "navTitle": "A harmonização deixa o rosto artificial?",
                "title": "1. A harmonização facial deixa o rosto artificial?",
                "p1": "<strong>Mito.</strong> O objetivo da harmonização bem executada pelo Dr. Henrique Leal é exatamente o oposto: realçar a beleza anatômica e devolver proporções equilibradas de forma discreta e elegante.",
                "p2": "Quando realizada com planejamento milimétrico e respeito aos ângulos da face, as pessoas ao seu redor percebem apenas que você está com uma fisionomia mais jovem, descansada e iluminada, sem identificar que houve intervenção.",
                "figure": {
                    "src": "assets/img/harmonizacao-facial-nova.webp",
                    "alt": "Avaliação clínica de proporção áurea com Dr. Henrique Leal",
                    "caption": "Planejamento individualizado respeitando a proporção áurea e a mímica facial no Água Verde."
                }
            },
            {
                "id": "secao-reversivel",
                "navTitle": "O procedimento é definitivo ou reversível?",
                "title": "2. O procedimento é definitivo ou reversível?",
                "p1": "<strong>Verdade.</strong> Os preenchedores modernos utilizados no consultório, como o ácido hialurônico de padrão ouro, são biocompatíveis e absorvidos de forma natural pelo organismo em um período de 12 a 18 meses.",
                "p2": "Além disso, uma das maiores vantagens do ácido hialurônico é a sua total reversibilidade: caso o paciente deseje ajustes imediatos, é possível aplicar a enzima hialuronidase para dissolver o produto de forma rápida e segura.",
                "list": [
                    "Ácido hialurônico de alta pureza e biocompatibilidade",
                    "Absorção gradual e estímulo secundário de hidratação",
                    "Possibilidade de reversão rápida com hialuronidase se necessário",
                    "Manutenção programada sem sobrecarregar a estrutura facial"
                ]
            },
            {
                "id": "secao-estica-pele",
                "navTitle": "Harmonização estica a pele como cirurgia?",
                "title": "3. Harmonização facial estica a pele como cirurgia plástica?",
                "p1": "<strong>Mito.</strong> A harmonização não estica nem puxa a pele cirurgicamente. Ela atua repondo coxins de gordura reabsorvidos com o envelhecimento, estruturando o suporte ósseo (mandíbula e queixo) e bioestimulando colágeno.",
                "p2": "O efeito de rejuvenescimento surge da reestruturação volumétrica dos pontos de sustentação, devolvendo o formato de triângulo invertido típico da juventude.",
                "quote": {
                    "text": "A verdadeira harmonização não transforma quem você é, mas restaura proporções e sustentações perdidas, preservando 100% da sua essência.",
                    "author": "Dr. Henrique Leal Rosa"
                }
            },
            {
                "id": "secao-avaliacao",
                "navTitle": "Como escolher o profissional em Curitiba",
                "title": "4. Como escolher o profissional certo em Curitiba",
                "p1": "Em Curitiba, priorize profissionais com dupla formação e profundo domínio anatômico. O Dr. Henrique Leal une a precisão cirúrgica da Odontologia (CRO-PR) ao conhecimento de biologia tecidual da Biomedicina (CRBM-PR).",
                "p2": "Durante a consulta no Edifício Today's Office (Água Verde), realizamos a análise facial completa em repouso, fala e sorriso, garantindo que o resultado seja impecável sob qualquer ângulo."
            }
        ]
    },
    # 2. Harmonização Masculina
    {
        "slug": "harmonizacao-facial-masculina-guia-curitiba",
        "title": "Harmonização Facial Masculina: Como Definir Mandíbula e Queixo sem Perder a Naturalidade",
        "category": "Harmonização Facial",
        "excerpt": "Guia completo sobre a estruturação mandibular e do mento masculino. Linhas firmes, ângulo reto e sofisticação no consultório do Dr. Henrique Leal em Curitiba.",
        "cover": "assets/img/resultados/slider-caso-masculino-depois.webp",
        "coverAlt": "Perfil e contorno mandibular masculino após harmonização facial em Curitiba",
        "date": "2026-08-10",
        "readingMinutes": 6,
        "tags": ["Harmonização Masculina", "Mandíbula", "Mento", "Curitiba"],
        "lead": "Cada vez mais homens em Curitiba buscam a harmonização facial para valorizar traços marcantes, conferir autoridade à fisionomia e definir o contorno do terço inferior do rosto sem parecerem operados.",
        "sections": [
            {
                "id": "secao-diferencas",
                "navTitle": "Diferenças da harmonização masculina",
                "title": "O que diferencia a harmonização masculina da feminina?",
                "p1": "A face masculina possui características anatômicas únicas: formato mais quadrado, ângulo mandibular próximo a 90 graus e queixo reto e projetado na mesma largura dos lábios.",
                "p2": "O planejamento do Dr. Henrique Leal foca exclusivamente em reforçar essas linhas de força sem projetar maçãs do rosto ou estreitar o queixo, preservando a virilidade e elegância natural.",
                "figure": {
                    "src": "assets/img/resultados/caso-contorno-mandibular-1.webp",
                    "alt": "Antes e depois de contorno mandibular masculino em Curitiba",
                    "caption": "Definição do ângulo da mandíbula e mento com ácido hialurônico de alta sustentação."
                }
            },
            {
                "id": "secao-procedimento",
                "navTitle": "Como é realizado o procedimento",
                "title": "Como é a sessão no consultório",
                "p1": "O procedimento é minimamente invasivo, realizado com microcânulas de ponta romba que não cortam vasos sanguíneos, minimizando o risco de hematomas.",
                "p2": "Utilizamos anestesia local odontológica para proporcionar conforto absoluto. A sessão dura cerca de 45 minutos e o paciente pode retornar ao trabalho no mesmo dia.",
                "list": [
                    "Anestesia local sem dor",
                    "Aplicação com microcânula segura",
                    "Sem cortes ou cicatrizes",
                    "Retorno imediato às atividades profissionais"
                ]
            },
            {
                "id": "secao-durabilidade",
                "navTitle": "Durabilidade e manutenção",
                "title": "Quanto tempo dura o resultado no homem?",
                "p1": "Devido à densidade do produto utilizado para estruturação óssea, os resultados costumam durar de 14 a 18 meses.",
                "p2": "Homens que praticam esportes de alta intensidade podem realizar manutenções leves a cada 12 meses para manter o contorno sempre afiado e definido.",
                "quote": {
                    "text": "O objetivo na face masculina é conferir autoridade, definição e firmeza, sem transformar os traços que fazem de você quem você é.",
                    "author": "Dr. Henrique Leal Rosa"
                }
            }
        ]
    },
    # 3. Botox Preventivo
    {
        "slug": "botox-preventivo-quando-comecar-curitiba",
        "title": "Botox Preventivo em Curitiba: Qual a Idade Certa para Começar?",
        "category": "Toxina Botulínica",
        "excerpt": "Entenda o conceito de toxina botulínica preventiva, como evitar que rugas de expressão se tornem marcas profundas na pele e os cuidados essenciais.",
        "cover": "assets/img/botox-nova.webp",
        "coverAlt": "Dr. Henrique Leal aplicando toxina botulínica em consultório em Curitiba",
        "date": "2026-08-04",
        "readingMinutes": 4,
        "tags": ["Botox", "Prevenção", "Rugas de Expressão", "Curitiba"],
        "lead": "A aplicação preventiva de toxina botulínica tornou-se um dos cuidados dermatológicos e estéticos mais procurados por jovens adultos em Curitiba que desejam envelhecer com viço e elegância.",
        "sections": [
            {
                "id": "secao-conceito",
                "navTitle": "O que é o Botox Preventivo?",
                "title": "O que é e como funciona o Botox Preventivo?",
                "p1": "Diferente da aplicação corretiva (feita quando as rugas já estão estáticas e visíveis mesmo com o rosto relaxado), o Botox preventivo relaxa suavemente os músculos hiperativos antes que a pele sofra fratura dérmica.",
                "p2": "Com microdoses personalizadas, evitamos que o ato de franzir a testa ao sol ou sorrir fortemente forme vincos permanentes no futuro.",
                "figure": {
                    "src": "assets/img/resultados/slider-caso-botox-depois.webp",
                    "alt": "Resultado natural de botox preventivo na testa e olhos",
                    "caption": "Testa lisa, sobrancelhas arqueadas com leveza e expressão totalmente preservada."
                }
            },
            {
                "id": "secao-idade",
                "navTitle": "Idade ideal para iniciar",
                "title": "Qual a idade certa para começar?",
                "p1": "Em média, a partir dos 25 aos 28 anos, momento em que a produção natural de colágeno desacelera e as primeiras linhas dinâmicas começam a marcar.",
                "p2": "No entanto, pessoas muito expressivas ou com pele clara exposta frequentemente à luz solar podem iniciar a avaliação preventiva mais cedo.",
                "list": [
                    "Previne a fixação de rugas na glabela (entre as sobrancelhas)",
                    "Suaviza linhas de 'pés de galinha' sem congelar o sorriso",
                    "Mantém o arqueamento elegante e natural do olhar",
                    "Economiza procedimentos invasivos no futuro"
                ]
            }
        ]
    },
    # 4. Durabilidade do Botox
    {
        "slug": "quanto-tempo-dura-o-botox-curitiba",
        "title": "Quanto Tempo Dura o Botox na Testa e Olhos? Dicas para Prolongar o Efeito",
        "category": "Toxina Botulínica",
        "excerpt": "Descubra fatores que influenciam na durabilidade da toxina botulínica e como manter seu rosto descansado e sem rugas por mais tempo em Curitiba.",
        "cover": "assets/img/resultados/botox-testa-depois.webp",
        "coverAlt": "Antes e depois de toxina botulínica na testa e glabela em Curitiba",
        "date": "2026-07-28",
        "readingMinutes": 5,
        "tags": ["Botox", "Durabilidade", "Testa e Olhos", "Cuidados"],
        "lead": "Uma das perguntas mais frequentes no consultório em Curitiba é: afinal, quantos meses dura o efeito do Botox e como fazer para que ele dure o máximo possível?",
        "sections": [
            {
                "id": "secao-duracao-media",
                "navTitle": "Tempo médio de durabilidade",
                "title": "Qual o tempo médio de duração da toxina botulínica?",
                "p1": "O efeito da toxina começa a ser notado em 48 a 72 horas, atinge o ápice por volta do 15º dia e se mantém estável por um período de 4 a 6 meses.",
                "p2": "Após esse período, as terminações nervosas voltam a se conectar gradativamente com o músculo, restaurando a mímica original de forma gradual e segura.",
                "figure": {
                    "src": "assets/img/resultados/botox-glabela-depois.webp",
                    "alt": "Suavização das rugas da glabela com toxina botulínica",
                    "caption": "Efeito de relaxamento muscular sem perda da expressividade no consultório do Água Verde."
                }
            },
            {
                "id": "secao-fatores",
                "navTitle": "Fatores que afetam a duração",
                "title": "O que faz o Botox durar mais ou menos tempo?",
                "p1": "Atletas de alto rendimento e praticantes de musculação intensa possuem metabolismo acelerado, o que pode reduzir a durabilidade para 3 a 4 meses.",
                "p2": "Por outro lado, o uso de marcas padrão ouro (como Dysport e Botox Allergan) com diluição e dosagem corretas garante a máxima fixação biológica possível.",
                "list": [
                    "Evitar massagear ou deitar nas primeiras 4 horas após aplicação",
                    "Usar protetor solar com alto fator de proteção diariamente",
                    "Manter suplementação de zinco e hidratação cutânea em dia",
                    "Evitar calor excessivo (sauna intensa) nos primeiros dias"
                ]
            }
        ]
    },
    # 5. Fios de PDO
    {
        "slug": "fios-de-pdo-lifting-sem-cirurgia-curitiba",
        "title": "Fios de PDO em Curitiba: Como Funciona o Lifting Facial sem Cortes",
        "category": "Fios de PDO",
        "excerpt": "Conheça a tecnologia dos fios de polidioxanona (PDO), técnica internacional aprendida na Coreia do Sul para reposicionar tecidos e estimular colágeno.",
        "cover": "assets/img/foto-fios-nova.webp",
        "coverAlt": "Dr. Henrique Leal aplicando fios de sustentação PDO em Curitiba",
        "date": "2026-07-20",
        "readingMinutes": 6,
        "tags": ["Fios de PDO", "Lifting Facial", "Coreia do Sul", "Curitiba"],
        "lead": "Os fios de sustentação de PDO (Polidioxanona) representam uma das maiores inovações da estética regenerativa mundial, proporcionando tração tecidual imediata e estímulo biológico contínuo de colágeno sem a necessidade de cirurgias ou internações.",
        "sections": [
            {
                "id": "secao-como-funciona",
                "navTitle": "Como os fios atuam no rosto",
                "title": "Como os Fios de PDO agem na pele?",
                "p1": "Fabricados com polidioxanona (material biocompatível e absorvível), os fios são inseridos na camada subcutânea por meio de microcânulas especiais.",
                "p2": "Os fios de tração (espiculados) possuem microgarras que ancoram a derme caída, tracionando o terço médio (bochechas), sulco nasogeniano ('bigode chinês') e linha da mandíbula.",
                "figure": {
                    "src": "assets/img/foto-fios.webp",
                    "alt": "Aplicação precisa de fios de PDO no consultório",
                    "caption": "Procedimento realizado sob anestesia local em ambiente seguro e confortável."
                }
            },
            {
                "id": "secao-tipos-fios",
                "navTitle": "Fios de Tração vs Fios de Estímulo",
                "title": "Qual a diferença entre fios espiculados e fios lisos?",
                "p1": "Os <strong>fios espiculados</strong> são destinados ao efeito lifting mecânico imediato, reposicionando a gordura facial que cedeu com o tempo.",
                "p2": "Já os <strong>fios lisos</strong> formam uma malha dérmica que não traciona, mas estimula uma produção massiva de colágeno em áreas de pele fina, como olheiras e código de barras.",
                "list": [
                    "Lifting não cirúrgico imediato",
                    "Estímulo prolongado de colágeno tipo I e III por até 2 anos",
                    "Absorção completa do fio em 6 a 8 meses",
                    "Sem cortes, pontos ou cicatrizes visíveis"
                ]
            }
        ]
    },
    # 6. Fios vs Bioestimulador
    {
        "slug": "fios-de-pdo-ou-bioestimulador-qual-escolher",
        "title": "Fios de PDO ou Bioestimulador de Colágeno: Qual o Ideal para o Seu Rosto?",
        "category": "Fios de PDO",
        "excerpt": "Comparativo completo entre fios de tração e bioestimuladores injetáveis para tratar flacidez e perda de contorno facial em Curitiba.",
        "cover": "assets/img/resultados/caso-rejuvenescimento-facial-1.webp",
        "coverAlt": "Caso de rejuvenescimento facial completo com fios de PDO e bioestimulador",
        "date": "2026-07-14",
        "readingMinutes": 5,
        "tags": ["Fios de PDO", "Bioestimuladores", "Flacidez", "Comparativo"],
        "lead": "Tanto os Fios de PDO quanto os Bioestimuladores de Colágeno são tecnologias consagradas no combate ao envelhecimento, mas cada uma atua em uma camada e com propósitos biomecânicos diferentes.",
        "sections": [
            {
                "id": "secao-comparativo",
                "navTitle": "Lifting mecânico vs Qualidade da pele",
                "title": "Lifting mecânico imediato vs Estímulo gradual de firmeza",
                "p1": "Se a sua principal queixa for a sensação de 'rosto derretendo', bochecha caída e perda da linha mandibular, os <strong>Fios de PDO</strong> proporcionam tração física instantânea.",
                "p2": "Se a sua queixa for a perda de espessura da pele, textura fina, 'craquelado' e flacidez difusa, os <strong>Bioestimuladores Injetáveis</strong> (Sculptra, Radiesse, Elleva) promovem o espessamento celular progressivo.",
                "figure": {
                    "src": "assets/img/bioestimulador-de-colageno.webp",
                    "alt": "Bioestimulador de colágeno injetável",
                    "caption": "Aplicação vetorizada de bioestimuladores para redensificação dérmica profunda."
                }
            },
            {
                "id": "secao-associacao",
                "navTitle": "A associação dos tratamentos",
                "title": "Por que associar Fios de PDO e Bioestimuladores?",
                "p1": "Na clínica do Dr. Henrique Leal em Curitiba, a combinação das duas técnicas é o padrão ouro: os fios reposicionam as estruturas caídas e o bioestimulador ancora a pele no novo lugar com firmeza biológica duradoura."
            }
        ]
    },
    # 7. Sculptra, Radiesse, Elleva
    {
        "slug": "sculptra-radiesse-elleva-comparativo-curitiba",
        "title": "Sculptra, Radiesse e Elleva: Diferenças entre os Melhores Bioestimuladores de Colágeno",
        "category": "Bioestimuladores",
        "excerpt": "Análise comparativa das principais marcas de bioestimuladores de colágeno do mercado. Saiba como escolher o melhor tratamento em Curitiba.",
        "cover": "assets/img/bioestimulador-de-colageno.webp",
        "coverAlt": "Frascos e tecnologia de bioestimuladores de colágeno em Curitiba",
        "date": "2026-07-05",
        "readingMinutes": 6,
        "tags": ["Sculptra", "Radiesse", "Elleva", "Bioestimuladores", "Curitiba"],
        "lead": "A partir dos 25 anos, perdemos aproximadamente 1% de colágeno anualmente. Os bioestimuladores injetáveis são a ferramenta médica mais potente para reverter essa perda de maneira biológica e duradoura.",
        "sections": [
            {
                "id": "secao-sculptra-elleva",
                "navTitle": "Sculptra e Elleva (PLLA)",
                "title": "1. Sculptra e Elleva (Ácido Poli-L-Láctico)",
                "p1": "Compostos por micropartículas biocompatíveis de PLLA, agem como potentes indutores biológicos que ativam os fibroblastos a sintetizarem colágeno tipo I novo ao longo de 90 dias.",
                "p2": "São indicados para tratar flacidez generalizada no rosto, pescoço, colo e glúteos, com durabilidade clínica que pode ultrapassar 24 meses.",
                "figure": {
                    "src": "assets/img/resultados/slider-caso-rejuvenescimento-depois.webp",
                    "alt": "Pele firme e rejuvenescida com bioestimuladores de colágeno",
                    "caption": "Rejuvenescimento natural com melhora evidente da elasticidade e firmeza facial."
                }
            },
            {
                "id": "secao-radiesse",
                "navTitle": "Radiesse (Hidroxiapatita de Cálcio)",
                "title": "2. Radiesse (Hidroxiapatita de Cálcio)",
                "p1": "Composto por microesferas de CaHA suspensas em gel carreador. Além do estímulo biológico potente de colágeno e elastina, oferece um efeito imediato de firmeza e ancoragem.",
                "p2": "Excelente para contorno mandibular, melhora da papada e rejuvenescimento do dorso das mãos com veias aparentes."
            }
        ]
    },
    # 8. Flacidez Rosto e Pescoço
    {
        "slug": "como-tratar-flacidez-facial-pescoco-curitiba",
        "title": "Como Tratar Flacidez no Rosto e Pescoço com Bioestimuladores em Curitiba",
        "category": "Bioestimuladores",
        "excerpt": "Dicas clínicas e protocolos modernos para recuperar a firmeza do pescoço, papada e contorno facial sem cirurgia.",
        "cover": "assets/img/resultados/caso-rejuvenescimento-facial-1-depois.webp",
        "coverAlt": "Contorno facial e pescoço rejuvenescidos com bioestimuladores",
        "date": "2026-06-28",
        "readingMinutes": 5,
        "tags": ["Pescoço", "Flacidez", "Rejuvenescimento", "Bioestimuladores"],
        "lead": "O pescoço e a linha da mandíbula frequentemente denunciam o envelhecimento antes do restante da face, pois possuem pele fina e baixa densidade de glândulas sebáceas.",
        "sections": [
            {
                "id": "secao-causas",
                "navTitle": "Por que o pescoço perde firmeza?",
                "title": "Por que a pele do pescoço perde sustentação?",
                "p1": "Além da degradação biológica do colágeno, o hábito moderno de olhar constantemente para telas (o chamado 'tech neck') acelera o surgimento de colares horizontais e flacidez na papada.",
                "p2": "O tratamento com bioestimuladores injetáveis vetorizados devolve a espessura dérmica, criando um 'efeito espartilho' natural que firma a pele frouxa.",
                "figure": {
                    "src": "assets/img/resultados/facial-completo.webp",
                    "alt": "Perfil facial rejuvenescido no consultório do Dr. Henrique Leal",
                    "caption": "Reestruturação anatômica integrada no bairro Água Verde em Curitiba."
                }
            }
        ]
    },
    # 9. Natural Lips
    {
        "slug": "preenchimento-labial-natural-lips-curitiba",
        "title": "Preenchimento Labial Natural Lips em Curitiba: Lábios Hidratados e sem Exageros",
        "category": "Preenchimento Labial",
        "excerpt": "Descubra a técnica Natural Lips do Dr. Henrique Leal: contorno sutil, hidratação profunda e respeito à anatomia da sua boca.",
        "cover": "assets/img/resultados/labio-antes-depois-3.webp",
        "coverAlt": "Antes e depois de preenchimento labial natural lips em Curitiba",
        "date": "2026-06-20",
        "readingMinutes": 4,
        "tags": ["Preenchimento Labial", "Natural Lips", "Ácido Hialurônico", "Curitiba"],
        "lead": "O receio de ficar com lábios exagerados ou artificiais ('efeito bico de pato') ainda afasta muitas mulheres do preenchimento. O conceito Natural Lips foi desenvolvido pelo Dr. Henrique Leal exatamente para superar esse medo.",
        "sections": [
            {
                "id": "secao-metodo",
                "navTitle": "O método Natural Lips",
                "title": "O que caracteriza o método Natural Lips?",
                "p1": "O foco não é injetar grandes volumes, mas sim desenhar com precisão o contorno do arco do cupido, evertir sutilmente a mucosa e hidratar as camadas internas com ácido hialurônico fluido de alta maleabilidade.",
                "p2": "Respeitamos a proporção áurea clássica (1 parte de volume no lábio superior para 1,6 partes no lábio inferior), garantindo harmonia no repouso e no sorriso.",
                "figure": {
                    "src": "assets/img/resultados/labio-resultado-4.webp",
                    "alt": "Lábios naturais, hidratados e sem excesso de volume",
                    "caption": "Resultado suave com contorno definido e brilho natural."
                }
            }
        ]
    },
    # 10. Cuidados Pós Preenchimento Labial
    {
        "slug": "cuidados-pos-preenchimento-labial-guia",
        "title": "Cuidados Pós-Preenchimento Labial: Recuperação, Inchaço e Duração",
        "category": "Preenchimento Labial",
        "excerpt": "O que fazer e o que evitar nos primeiros dias após o preenchimento labial para garantir uma cicatrização perfeita.",
        "cover": "assets/img/preenchimento-labial-depois-clean.webp",
        "coverAlt": "Lábios após preenchimento labial no consultório em Curitiba",
        "date": "2026-06-12",
        "readingMinutes": 4,
        "tags": ["Pós-Procedimento", "Preenchimento Labial", "Cuidados", "Inchaço"],
        "lead": "Os primeiros dias após o preenchimento labial exigem cuidados simples para que o ácido hialurônico se acomode perfeitamente nos tecidos e o edema inicial diminua com rapidez.",
        "sections": [
            {
                "id": "secao-linha-do-tempo",
                "navTitle": "Linha do tempo do inchaço",
                "title": "O que acontece nos primeiros dias?",
                "p1": "Nas primeiras 48 horas, é totalmente normal haver inchaço e leve sensibilidade ao toque. O resultado que você vê no primeiro dia ainda não é o definitivo.",
                "p2": "A partir do 5º ao 7º dia o edema regride cerca de 70%, e o formato final consolidado se estabelece entre 15 e 20 dias.",
                "list": [
                    "Fazer compressas frias leves nas primeiras 24 horas",
                    "Evitar alimentos excessivamente quentes ou condimentados no dia do procedimento",
                    "Não pressionar os lábios ou usar canudos nas primeiras 48 horas",
                    "Evitar atividade física pesada nas primeiras 24 a 48 horas"
                ],
                "figure": {
                    "src": "assets/img/resultados/labio-resultado-5.webp",
                    "alt": "Lábios cicatrizados com formato harmônico",
                    "caption": "Resultado consolidado após 15 dias de cicatrização."
                }
            }
        ]
    },
    # 11. Rinomodelação
    {
        "slug": "rinomodelacao-com-acido-hialuronico-curitiba",
        "title": "Rinomodelação em Curitiba: Como Empinar e Alinhar o Nariz sem Cirurgia",
        "category": "Rinomodelação",
        "excerpt": "Procedimento rápido e seguro para corrigir pequenas imperfeições no dorso nasal e levantar a ponta caída em Curitiba.",
        "cover": "assets/img/resultados/upnose-depois.webp",
        "coverAlt": "Antes e depois de rinomodelação up nose em Curitiba",
        "date": "2026-06-04",
        "readingMinutes": 5,
        "tags": ["Rinomodelação", "Up Nose", "Nariz", "Curitiba"],
        "lead": "A rinomodelação não cirúrgica é uma excelente alternativa à rinoplastia tradicional para pacientes que desejam empinar a ponta do nariz e disfarçar o ossinho saliente (giba) sem cortes ou anestesia geral.",
        "sections": [
            {
                "id": "secao-indicacoes",
                "navTitle": "O que a rinomodelação corrige",
                "title": "Quais queixas a rinomodelação consegue resolver?",
                "p1": "Com microdoses de ácido hialurônico de alta sustentação, conseguimos retificar o dorso nasal, camuflando a curvatura do osso e criando a ilusão óptica de um nariz mais reto e afilado.",
                "p2": "Além disso, através do protocolo Up Nose, estruturamos a base da columela para erguer a ponta caída ao sorrir.",
                "figure": {
                    "src": "assets/img/resultados/caso-rinomodelacao-perfil-1.webp",
                    "alt": "Perfil nasal alinhado com rinomodelação não cirúrgica",
                    "caption": "Correção de giba nasal e sustentação da ponta em sessão única de 30 minutos."
                }
            }
        ]
    },
    # 12. Rinomodelação Dúvidas
    {
        "slug": "rinomodelacao-doi-cuidados-e-duracao",
        "title": "Rinomodelação Dói? Riscos, Tempo de Recuperação e Durabilidade",
        "category": "Rinomodelação",
        "excerpt": "Tudo sobre o nível de dor, anestesia local, cuidados essenciais e tempo de durabilidade da rinomodelação.",
        "cover": "assets/img/resultados/caso-rinomodelacao-perfil-1-depois.webp",
        "coverAlt": "Nariz empinado e alinhado após rinomodelação",
        "date": "2026-05-28",
        "readingMinutes": 4,
        "tags": ["Rinomodelação", "Dúvidas", "Segurança", "Durabilidade"],
        "lead": "A rinomodelação é um dos procedimentos com maior impacto visual imediato, mas exige rigor técnico e segurança anatômica máxima por parte do profissional.",
        "sections": [
            {
                "id": "secao-seguranca",
                "navTitle": "Segurança e anestesia",
                "title": "A rinomodelação dói e é segura?",
                "p1": "Não dói: aplicamos anestésico local no ponto de entrada. Utilizamos microcânula flexível e sem ponta cortante, o que protege os vasos sanguíneos da região nasal.",
                "p2": "A durabilidade média é de 12 a 18 meses, pois o nariz é uma área de pouca mobilidade muscular, preservando o produto por mais tempo.",
                "figure": {
                    "src": "assets/img/resultados/upnose-antes.webp",
                    "alt": "Avaliação de perfil nasal no consultório",
                    "caption": "Estudo anatômico das proporções do dorso e ângulo nasolabial."
                }
            }
        ]
    },
    # 13. Estética Íntima Preenchimento
    {
        "slug": "estetica-intima-preenchimento-acido-hialuronico-curitiba",
        "title": "Preenchimento Íntimo Feminino em Curitiba: Como o Ácido Hialurônico Devolve Firmeza e Conforto",
        "category": "Estética Íntima",
        "excerpt": "Procedimento médico-estético delicado para recuperação de volume, hidratação e firmeza dos grandes lábios com total sigilo e conforto.",
        "cover": "assets/img/intimos-nova.webp",
        "coverAlt": "Estética íntima feminina no consultório do Dr. Henrique Leal em Curitiba",
        "date": "2026-05-20",
        "readingMinutes": 5,
        "tags": ["Estética Íntima", "Preenchimento Íntimo", "Curitiba", "Autoestima"],
        "lead": "Com o passar dos anos, emagrecimento severo ou oscilações hormonais na menopausa, a região genital feminina perde volume nos grandes lábios, gerando flacidez, atrito desconfortável com roupas e queda da autoestima.",
        "sections": [
            {
                "id": "secao-procedimento-intimo",
                "navTitle": "Como funciona o preenchimento íntimo",
                "title": "Como o ácido hialurônico atua na estética íntima?",
                "p1": "A aplicação de ácido hialurônico específico na derme dos grandes lábios restaura o turgor, protege as estruturas internas e rejuvenesce o aspecto visual da região íntima.",
                "p2": "No consultório em Curitiba, o procedimento é realizado com anestesia local, em ambiente estéril e com total sigilo e respeito ao conforto da paciente.",
                "figure": {
                    "src": "assets/img/intimos.webp",
                    "alt": "Cuidado e bem-estar na estética íntima feminina",
                    "caption": "Tratamento seguro e acolhedor para a saúde e autoestima da mulher."
                }
            }
        ]
    },
    # 14. Rejuvenescimento Íntimo
    {
        "slug": "rejuvenescimento-intimo-beneficios-e-autoestima",
        "title": "Rejuvenescimento Íntimo: Procedimentos Modernos para Saúde e Autoestima da Mulher",
        "category": "Estética Íntima",
        "excerpt": "Bioestimuladores, hidratação e fios na estética íntima: conheça os tratamentos que unem bem-estar, função e beleza.",
        "cover": "assets/img/intimos.webp",
        "coverAlt": "Procedimentos modernos de rejuvenescimento íntimo em Curitiba",
        "date": "2026-05-12",
        "readingMinutes": 5,
        "tags": ["Rejuvenescimento Íntimo", "Saúde Feminina", "Bioestimulador"],
        "lead": "O autocuidado íntimo moderno une tratamentos avançados de bioestímulo, preenchimento e clareamento para devolver conforto funcional e autoconfiança plena à mulher.",
        "sections": [
            {
                "id": "secao-opcoes-intimas",
                "navTitle": "Opções de tratamentos íntimos",
                "title": "Quais tratamentos podem ser associados?",
                "p1": "Além do ácido hialurônico para volume, podemos utilizar bioestimuladores de colágeno para combater a flacidez cutânea da vulva e clareamento para manchas decorrentes de depilação ou atrito.",
                "p2": "A avaliação presencial é o momento de tirar todas as dúvidas com tranquilidade e definir o plano de cuidados mais adequado.",
                "figure": {
                    "src": "assets/img/intimos-nova.webp",
                    "alt": "Consultório acolhedor e seguro em Curitiba",
                    "caption": "Atendimento humanizado com foco na sua saúde e bem-estar."
                }
            }
        ]
    },
    # 15. Protocolo Bioforce
    {
        "slug": "protocolo-bioforce-regeneracao-celular-curitiba",
        "title": "Protocolo Bioforce: O Tratamento Assinatura para Regeneração Facial Profunda",
        "category": "Protocolo Bioforce",
        "excerpt": "Associação exclusiva de bioestimuladores de última geração e peptídeos bioativos desenvolvida pelo Dr. Henrique Leal em Curitiba.",
        "cover": "assets/img/7G1A9991.webp",
        "coverAlt": "Dr. Henrique Leal Rosa no consultório em Curitiba",
        "date": "2026-05-04",
        "readingMinutes": 5,
        "tags": ["Protocolo Bioforce", "Regeneração", "Assinatura", "Curitiba"],
        "lead": "O Protocolo Bioforce é a assinatura clínica do Dr. Henrique Leal em Curitiba, desenvolvido para quem busca rejuvenescimento biológico profundo, viço incomparável e firmeza dérmica sem nenhum aspecto volumizado artificial.",
        "sections": [
            {
                "id": "secao-sinergia",
                "navTitle": "A ciência do Protocolo Bioforce",
                "title": "A sinergia entre Bioestimulação e Fatores Regenerativos",
                "p1": "O protocolo associa bioestimuladores importados de última geração com fatores de crescimento e peptídeos sinalizadores celulares.",
                "p2": "Essa combinação reprograma a atividade dos fibroblastos, promovendo uma neocolagênese acelerada que melhora poros, linhas finas e o tônus da pele em poucas semanas.",
                "figure": {
                    "src": "assets/img/henrique-portrait.webp",
                    "alt": "Dr. Henrique Leal Rosa - Cirurgião Dentista e Biomédico",
                    "caption": "Atendimento exclusivo no Edifício Today's Office, bairro Água Verde em Curitiba."
                }
            }
        ]
    },
    # 16. Peptídeos Bioativos
    {
        "slug": "peptideos-bioativos-e-antiaging-avancado",
        "title": "Peptídeos Bioativos na Estética Avançada: Como Estimular a Juventude da Pele",
        "category": "Protocolo Bioforce",
        "excerpt": "A ciência por trás dos peptídeos sinalizadores e como eles reprogramam a síntese de colágeno nas células da pele.",
        "cover": "assets/img/henrique-portrait.webp",
        "coverAlt": "Dr. Henrique Leal explicando a ciência dos peptídeos bioativos",
        "date": "2026-04-26",
        "readingMinutes": 4,
        "tags": ["Peptídeos", "Ciência", "Antiaging", "Regeneração"],
        "lead": "A estética moderna evoluiu da simples reposição volumétrica para a reprogramação celular inteligente através de biomoléculas sinalizadoras.",
        "sections": [
            {
                "id": "secao-peptideos",
                "navTitle": "Como os peptídeos funcionam",
                "title": "O papel dos peptídeos na matriz extracelular",
                "p1": "Os peptídeos bioativos atuam como 'chaves' químicas que ligam os receptores de membrana das células da pele, estimulando a síntese autóloga de ácido hialurônico, colágeno e elastina.",
                "p2": "O resultado é uma pele biologicamente mais jovem, densa e luminosa, com textura sedosa e viço saudável.",
                "figure": {
                    "src": "assets/img/dr-henrique.webp",
                    "alt": "Consulta estética com base em evidências científicas",
                    "caption": "Biotecnologia aplicada ao rejuvenescimento natural da face."
                }
            }
        ]
    },
    # 17. Ozonioterapia Benefícios
    {
        "slug": "ozonioterapia-beneficios-estetica-saude-curitiba",
        "title": "Ozonioterapia em Curitiba: Benefícios do Ozônio Medicinal para Pele e Inflamação",
        "category": "Ozonioterapia",
        "excerpt": "Como o gás ozônio atua na oxigenação celular, combate a radicais livres e potencialização de resultados estéticos em Curitiba.",
        "cover": "assets/img/henrique-clinic.webp",
        "coverAlt": "Sala de atendimento e consultório de ozonioterapia em Curitiba",
        "date": "2026-04-18",
        "readingMinutes": 5,
        "tags": ["Ozonioterapia", "Ozônio Medicinal", "Saúde", "Curitiba"],
        "lead": "A ozonioterapia medicinal é uma das práticas integrativas mais consagradas para melhora da microcirculação tecidual, combate a processos inflamatórios e revitalização da pele.",
        "sections": [
            {
                "id": "secao-ozonio-beneficios",
                "navTitle": "Aplicações do ozônio medicinal",
                "title": "Como o ozônio atua no organismo?",
                "p1": "A mistura de oxigênio-ozônio medicinal estimula as enzimas antioxidantes endógenas, combate bactérias e fungos, e melhora a liberação de oxigênio pelos glóbulos vermelhos nos tecidos periféricos.",
                "p2": "Na estética, é excelente para controle da acne ativa, revitalização cutânea e tratamento de celulite e gordura localizada.",
                "figure": {
                    "src": "assets/img/henrique-faq-new.webp",
                    "alt": "Avaliação e esclarecimento de dúvidas com Dr. Henrique Leal",
                    "caption": "Protocolos personalizados de ozonioterapia no consultório em Curitiba."
                }
            }
        ]
    },
    # 18. Ozonioterapia Pós Procedimento
    {
        "slug": "ozonioterapia-para-rejuvenescimento-e-cicatrizacao",
        "title": "Ozonioterapia no Pós-Procedimento: Aceleração da Cicatrização e Oxigenação Tecidual",
        "category": "Ozonioterapia",
        "excerpt": "Entenda por que o ozônio medicinal é utilizado para acelerar a recuperação de procedimentos estéticos e reduzir edemas.",
        "cover": "assets/img/henrique-faq-new.webp",
        "coverAlt": "Dr. Henrique Leal orientando paciente sobre pós-procedimento",
        "date": "2026-04-10",
        "readingMinutes": 4,
        "tags": ["Cicatrização", "Pós-Operatório", "Ozonioterapia"],
        "lead": "A aplicação do ozônio medicinal após procedimentos estéticos reduz expressivamente o tempo de edema, equimoses (roxos) e acelera a regeneração tecidual.",
        "sections": [
            {
                "id": "secao-cicatrizacao",
                "navTitle": "Aceleração da cicatrização",
                "title": "Por que o ozônio acelera a recuperação pós-estética?",
                "p1": "O ozônio promove a liberação imediata de óxido nítrico e fatores de crescimento endotelial, acelerando a vascularização e desinflamando a área tratada rapidamente.",
                "p2": "Isso proporciona ao paciente um pós-procedimento muito mais confortável, seguro e com retorno antecipado às suas atividades cotidianas.",
                "figure": {
                    "src": "assets/img/henrique-clinic.webp",
                    "alt": "Ambiente clínico seguro e esterilizado",
                    "caption": "Segurança e conforto para uma recuperação tranquila e rápida."
                }
            }
        ]
    },
    # 19. Terapia Capilar
    {
        "slug": "terapia-capilar-para-queda-de-cabelo-curitiba",
        "title": "Terapia Capilar em Curitiba: Como Tratar Queda de Cabelo e Calvície com Tecnologia",
        "category": "Terapia Capilar",
        "excerpt": "Protocolos integrados de estímulo folicular, nutrição capilar e combate à calvície masculina e feminina no Água Verde.",
        "cover": "assets/img/resultados/IMG_6808.webp",
        "coverAlt": "Tratamento de terapia capilar e recuperação dos fios em Curitiba",
        "date": "2026-04-02",
        "readingMinutes": 5,
        "tags": ["Terapia Capilar", "Queda de Cabelo", "Calvície", "Curitiba"],
        "lead": "A queda excessiva de cabelo (eflúvio telógeno) e a calvície genética (alopecia androgenética) afetam diretamente a autoestima. O tratamento precoce no consultório é decisivo para salvar os folículos pilosos antes que atrofiem definitivamente.",
        "sections": [
            {
                "id": "secao-protocolo-capilar",
                "navTitle": "Protocolo capilar integrado",
                "title": "Como funciona o tratamento capilar clínico?",
                "p1": "O protocolo do Dr. Henrique Leal em Curitiba combina microinfusão de medicamentos antiqueda (MMP), fatores de crescimento peptídicos e bioestimulação folicular.",
                "p2": "Esse combo desinflama a raiz do cabelo, bloqueia os efeitos locais da DHT e estimula a transição dos fios da fase de repouso (telógena) para a fase de crescimento ativo (anágena).",
                "figure": {
                    "src": "assets/img/resultados/IMG_4637.webp",
                    "alt": "Densidade capilar recuperada com estímulo folicular",
                    "caption": "Aumento significativo da densidade e calibre dos fios no consultório."
                }
            }
        ]
    },
    # 20. Microinfusão Capilar
    {
        "slug": "microinfusao-capilar-e-fortalecimento-dos-fios",
        "title": "Microinfusão e Fatores de Crescimento Capilar: Fortalecimento desde a Raiz",
        "category": "Terapia Capilar",
        "excerpt": "Entenda como a entrega direta de nutrientes no bulbo capilar desacelera o afinamento e estimula novos fios.",
        "cover": "assets/img/resultados/IMG_9716.webp",
        "coverAlt": "Microinfusão capilar no couro cabeludo com ativos antiqueda",
        "date": "2026-03-24",
        "readingMinutes": 4,
        "tags": ["Microinfusão", "Fatores de Crescimento", "Bulbo Capilar"],
        "lead": "A entrega direta de nutrientes e substâncias vasodilatadoras no bulbo capilar garante uma absorção centenas de vezes superior à de loções tópicas ou comprimidos orais.",
        "sections": [
            {
                "id": "secao-microinfusao",
                "navTitle": "Vantagens da microinfusão",
                "title": "Por que a microinfusão capilar é tão eficiente?",
                "p1": "Através de microagulhas precisas, os ativos antiqueda e aminoácidos são depositados exatamente onde a matriz do fio é produzida.",
                "p2": "O procedimento é rápido, confortável e promove o espessamento progressivo dos fios ralos, devolvendo volume e vitalidade ao couro cabeludo.",
                "figure": {
                    "src": "assets/img/resultados/caso-harmonizacao-masculina-2.webp",
                    "alt": "Paciente masculino com cabelo e contorno facial restaurados",
                    "caption": "Rejuvenescimento capilar e facial integrado no Água Verde."
                }
            }
        ]
    }
]

MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
def format_date_pt(d_str):
    y, m, d = d_str.split("-")
    return f"{int(d)} de {MONTHS[int(m)-1]} de {y}"

# Shared CSS for Article Pages using DR HENRIQUE LEAL IDENTITY (Navy #1B3A5C, Blue #2A7DE1, Gold #2A7DE1, Playfair Display & Inter)
DR_HENRIQUE_ARTICLE_CSS = """
        /* Typography & Variables */
        :root {
            --color-primary: #1B3A5C;
            --color-primary-dark: #0F2847;
            --color-accent: #2A7DE1;
            --color-accent-hover: #1E6BC9;
            --color-accent: #2A7DE1;
            --font-heading: 'Playfair Display', Georgia, serif;
            --font-body: 'Inter', -apple-system, sans-serif;
        }

        body {
            font-family: var(--font-body);
            color: #334155;
            background-color: #FFFFFF;
            margin: 0;
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
        }

        /* Header integration with style.css */
        .article-page-header {
            padding-top: 150px;
            padding-bottom: 50px;
            background: #FAFBFD;
            border-bottom: 1px solid rgba(27, 58, 92, 0.08);
        }

        .article-breadcrumbs {
            font-size: 0.85rem;
            color: #64748B;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .article-breadcrumbs a {
            color: var(--color-primary);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s ease;
        }
        .article-breadcrumbs a:hover {
            color: var(--color-accent);
        }

        .author-box-top {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 24px;
        }
        .author-img-circle {
            width: 58px;
            height: 58px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid var(--color-accent);
            box-shadow: 0 4px 14px rgba(27, 58, 92, 0.12);
        }
        .author-name-title {
            font-family: var(--font-heading);
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--color-primary);
            margin: 0 0 2px 0;
        }
        .author-role-sub {
            font-size: 0.84rem;
            color: #64748B;
            margin: 0;
        }

        .article-cat-pill {
            display: inline-block;
            background: rgba(42, 125, 225, 0.08);
            color: var(--color-primary);
            font-size: 0.80rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            padding: 6px 14px;
            border-radius: 30px;
            border: 1px solid rgba(42, 125, 225, 0.18);
        }
        .article-tag-item {
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--color-accent);
        }

        .article-main-h1 {
            font-family: var(--font-heading);
            font-size: clamp(2.2rem, 4vw, 3.2rem);
            color: var(--color-primary);
            line-height: 1.25;
            margin: 20px 0 24px 0;
            font-weight: 700;
        }

        .human-badge-drhenrique {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--color-primary);
            color: #FFFFFF;
            font-size: 0.80rem;
            font-weight: 600;
            padding: 6px 16px;
            border-radius: 30px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(27, 58, 92, 0.15);
        }

        .article-meta-info {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 20px;
            font-size: 0.88rem;
            color: #64748B;
            font-weight: 500;
        }
        .article-meta-info span {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* 2-Column Article Layout */
        .article-layout-grid {
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 50px;
            padding: 60px 0 90px 0;
        }

        /* Sticky Sidebar */
        .article-sidebar {
            position: sticky;
            top: 110px;
            align-self: flex-start;
        }
        .sidebar-index-title {
            font-family: var(--font-heading);
            font-size: 1.35rem;
            color: var(--color-primary);
            margin: 0 0 16px 0;
            padding-bottom: 12px;
            border-bottom: 2px solid rgba(27, 58, 92, 0.08);
        }
        .sidebar-nav-list {
            display: flex;
            flex-direction: column;
            gap: 0;
        }
        .sidebar-nav-link {
            padding: 12px 0;
            font-size: 0.90rem;
            font-weight: 500;
            color: #475569;
            text-decoration: none;
            border-bottom: 1px solid rgba(27, 58, 92, 0.06);
            transition: all 0.2s ease;
            line-height: 1.4;
        }
        .sidebar-nav-link:hover {
            color: var(--color-accent);
            padding-left: 6px;
        }

        .sidebar-clinic-box {
            margin-top: 30px;
            background: #F8FAFC;
            border: 1px solid rgba(27, 58, 92, 0.08);
            border-radius: 16px;
            padding: 24px;
        }
        .sidebar-clinic-box h4 {
            font-family: var(--font-heading);
            font-size: 1.05rem;
            color: var(--color-primary);
            margin: 0 0 8px 0;
        }
        .sidebar-clinic-box p {
            font-size: 0.82rem;
            color: #64748B;
            line-height: 1.6;
            margin: 0 0 14px 0;
        }
        .sidebar-clinic-btn {
            display: inline-block;
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--color-accent);
            text-decoration: none;
            transition: transform 0.2s ease;
        }
        .sidebar-clinic-btn:hover {
            transform: translateX(3px);
        }

        /* Article Content Column */
        .article-main-col {
            min-width: 0;
        }

        .article-lead-text {
            border-left: 4px solid var(--color-accent);
            padding-left: 20px;
            font-size: 1.18rem;
            line-height: 1.8;
            color: var(--color-primary);
            font-weight: 500;
            margin-bottom: 35px;
            background: rgba(42, 125, 225, 0.02);
            padding-top: 6px;
            padding-bottom: 6px;
            border-radius: 0 8px 8px 0;
        }

        .article-cover-wrap {
            width: 100%;
            max-width: 680px;
            height: 280px;
            border-radius: 16px;
            overflow: hidden;
            margin: 0 auto 35px auto;
            box-shadow: 0 8px 24px rgba(27, 58, 92, 0.07);
        }
        .article-cover-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .article-h2-title {
            font-family: var(--font-heading);
            font-size: 1.85rem;
            color: var(--color-primary);
            margin: 45px 0 18px 0;
            line-height: 1.3;
            scroll-margin-top: 110px;
        }
        .article-p-text {
            font-size: 1.05rem;
            color: #475569;
            line-height: 1.85;
            margin-bottom: 20px;
        }
        .article-figure-box {
            margin: 35px 0;
        }
        .article-figure-img-wrap {
            width: 100%;
            max-width: 680px;
            height: 260px;
            border-radius: 14px;
            overflow: hidden;
            margin: 0 auto;
            box-shadow: 0 6px 20px rgba(27, 58, 92, 0.06);
        }
        .article-figure-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .article-figure-caption {
            text-align: center;
            font-size: 0.84rem;
            color: #64748B;
            margin-top: 10px;
            font-style: italic;
        }

        .article-ol-list {
            padding-left: 24px;
            margin-bottom: 25px;
        }
        .article-ol-list li {
            font-size: 1.02rem;
            color: #475569;
            margin-bottom: 10px;
            line-height: 1.7;
        }

        /* Luxury Dark Card Mid-Article CTA */
        .mid-article-dark-cta {
            margin: 45px 0;
            background: linear-gradient(135deg, #0F2847 0%, #1B3A5C 100%);
            border-radius: 24px;
            padding: 40px;
            color: #FFFFFF;
            box-shadow: 0 16px 40px rgba(15, 40, 71, 0.25);
            display: grid;
            grid-template-columns: 1fr auto;
            align-items: center;
            gap: 35px;
        }
        .dark-cta-eyebrow {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.76rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: var(--color-accent);
            margin-bottom: 12px;
        }
        .dark-cta-eyebrow-bar {
            width: 16px;
            height: 2px;
            background: var(--color-accent);
        }
        .dark-cta-h3 {
            font-family: var(--font-heading);
            font-size: clamp(1.6rem, 2.5vw, 2.2rem);
            color: #FFFFFF;
            line-height: 1.25;
            margin: 0 0 12px 0;
        }
        .dark-cta-h3 span {
            color: var(--color-accent);
        }
        .dark-cta-desc {
            font-size: 0.95rem;
            color: rgba(255, 255, 255, 0.85);
            line-height: 1.65;
            margin-bottom: 22px;
            max-width: 520px;
        }
        .dark-cta-features-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
            padding-top: 18px;
            border-top: 1px solid rgba(255, 255, 255, 0.12);
            margin-bottom: 24px;
        }
        .dark-feature-title {
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #FFFFFF;
            margin: 0 0 2px 0;
        }
        .dark-feature-sub {
            font-size: 0.70rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: rgba(255, 255, 255, 0.6);
            margin: 0;
        }
        .dark-cta-portrait-wrap {
            width: 220px;
            height: 260px;
            border-radius: 16px;
            overflow: hidden;
            border: 3px solid rgba(255, 255, 255, 0.9);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .dark-cta-portrait {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .article-blockquote {
            margin: 35px 0;
            border-left: 4px solid var(--color-accent);
            background: #FAFBFD;
            border-radius: 0 16px 16px 0;
            padding: 24px 28px;
        }
        .article-blockquote p {
            font-family: var(--font-heading);
            font-size: 1.22rem;
            font-style: italic;
            color: var(--color-primary);
            line-height: 1.7;
            margin: 0 0 10px 0;
        }
        .article-blockquote cite {
            font-size: 0.88rem;
            color: #64748B;
            font-style: normal;
            font-weight: 600;
            display: block;
        }

        /* Pre-Footer Luxury Navy CTA */
        .article-prefooter-cta {
            background: linear-gradient(135deg, #1B3A5C 0%, #0F2847 100%);
            padding: 70px 0;
            color: #FFFFFF;
            text-align: center;
        }
        .article-prefooter-title {
            font-family: var(--font-heading);
            font-size: clamp(2rem, 3.5vw, 2.8rem);
            color: #FFFFFF;
            margin-bottom: 14px;
        }
        .article-prefooter-desc {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.85);
            max-width: 620px;
            margin: 0 auto 30px auto;
            line-height: 1.7;
        }

        @media (max-width: 992px) {
            .article-layout-grid {
                grid-template-columns: 1fr;
                gap: 30px;
            }
            .article-sidebar {
                position: static;
            }
            .mid-article-dark-cta {
                grid-template-columns: 1fr;
            }
            .dark-cta-portrait-wrap {
                width: 100%;
                height: 220px;
            }
            .dark-cta-features-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (max-width: 640px) {
            .article-page-header {
                padding-top: 120px;
            }
            .article-cover-wrap {
                height: 240px;
            }
            .article-figure-img-wrap {
                height: 220px;
            }
            .mid-article-dark-cta {
                padding: 24px 20px;
            }
        }
"""

for p in POSTS:
    tags_html = "".join([f'<span class="article-tag-item">#{t}</span>' for t in p["tags"]])
    
    # Generate left sidebar index links
    sidebar_links_html = ""
    for sec in p["sections"]:
        sidebar_links_html += f'<a href="#{sec["id"]}" class="sidebar-nav-link">{sec["navTitle"]}</a>\n'
    
    # Generate main article sections
    sections_html = ""
    for i, sec in enumerate(p["sections"]):
        p2_text = f'<p class="article-p-text">{sec["p2"]}</p>' if "p2" in sec else ""
        sec_content = f"""
        <h2 id="{sec['id']}" class="article-h2-title">{sec['title']}</h2>
        <p class="article-p-text">{sec['p1']}</p>
        {p2_text}
        """
        
        if "figure" in sec:
            fig = sec["figure"]
            sec_content += f"""
            <figure class="article-figure-box">
                <div class="article-figure-img-wrap">
                    <img alt="{fig['alt']}" loading="lazy" class="article-figure-img" src="{fig['src']}">
                </div>
                <figcaption class="article-figure-caption">{fig['caption']}</figcaption>
            </figure>
            """
            
        if "list" in sec:
            list_items = "".join([f'<li>{item}</li>' for item in sec["list"]])
            sec_content += f"""
            <ol class="article-ol-list">
                {list_items}
            </ol>
            """
            
        if "quote" in sec:
            q = sec["quote"]
            sec_content += f"""
            <blockquote class="article-blockquote">
                <p>“{q['text']}”</p>
                <cite>— {q['author']}</cite>
            </blockquote>
            """
            
        # Insert Dark Card CTA in the middle
        if i == 1 or (len(p["sections"]) == 1 and i == 0):
            sec_content += f"""
            <div class="mid-article-dark-cta">
                <div>
                    <div class="dark-cta-eyebrow">
                        <span class="dark-cta-eyebrow-bar"></span>
                        <span>Dr. Henrique Leal Rosa</span>
                    </div>
                    <h3 class="dark-cta-h3">
                        Deseja avaliar o seu caso <span>em Curitiba?</span>
                    </h3>
                    <p class="dark-cta-desc">
                        Planejamento anatômico individualizado com foco em discrição, sofisticação e segurança clínica no Edifício Today's Office, Água Verde.
                    </p>
                    <div class="dark-cta-features-grid">
                        <div>
                            <p class="dark-feature-title">Avaliação</p>
                            <p class="dark-feature-sub">Personalizada</p>
                        </div>
                        <div>
                            <p class="dark-feature-title">Local</p>
                            <p class="dark-feature-sub">Água Verde</p>
                        </div>
                        <div>
                            <p class="dark-feature-title">Segurança</p>
                            <p class="dark-feature-sub">Padrão Ouro</p>
                        </div>
                        <div>
                            <p class="dark-feature-title">Resultados</p>
                            <p class="dark-feature-sub">Naturais</p>
                        </div>
                    </div>
                    <div>
                        <a class="btn btn-primary" 
                           style="padding: 14px 28px; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 8px;"
                           href="https://wa.me/5541988577430?text=Ol%C3%A1%2C%20li%20o%20artigo%20sobre%20{p['slug']}%20e%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o." target="_blank" rel="noopener">
                            Agendar no WhatsApp ↗
                        </a>
                    </div>
                </div>
                <div class="dark-cta-portrait-wrap">
                    <img alt="Dr. Henrique Leal Rosa" loading="lazy" class="dark-cta-portrait" src="assets/img/henrique-portrait.webp">
                </div>
            </div>
            """
            
        sections_html += sec_content

    full_page_html = f"""<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="assets/css/style.css?v=11.0">
    <link rel="icon" type="image/png" href="assets/img/favicon.png?v=3">
    <link rel="apple-touch-icon" href="assets/img/favicon.png?v=3">
    <title>{p['title']} | Dr. Henrique Leal Rosa</title>
    <meta name="description" content="{p['excerpt']}">
    <meta name="author" content="Dr. Henrique Leal Rosa">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://drhenriqueleal.com.br/{p['slug']}.html">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{p['title']} | Dr. Henrique Leal Rosa">
    <meta property="og:description" content="{p['excerpt']}">
    <meta property="og:url" content="https://drhenriqueleal.com.br/{p['slug']}.html">
    <meta property="og:image" content="https://drhenriqueleal.com.br/{p['cover']}">
    <meta property="og:type" content="article">
    <meta property="article:published_time" content="{p['date']}">
    <meta property="article:author" content="Dr. Henrique Leal Rosa">
    
    <!-- Structured Data JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "{p['title']}",
      "description": "{p['excerpt']}",
      "image": "https://drhenriqueleal.com.br/{p['cover']}",
      "datePublished": "{p['date']}",
      "author": {{
        "@type": "Person",
        "name": "Dr. Henrique Leal Rosa",
        "jobTitle": "Cirurgião Dentista (CRO-PR) & Biomédico (CRBM-PR)"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Dr. Henrique Leal Rosa",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://drhenriqueleal.com.br/assets/img/logo-sub-colorida.webp"
        }}
      }},
      "mainEntityOfPage": "https://drhenriqueleal.com.br/{p['slug']}.html"
    }}
    </script>
    
    <style>
{DR_HENRIQUE_ARTICLE_CSS}
    </style>
</head>

<body>
    <!-- ==================== HEADER PADRÃO DR. HENRIQUE LEAL ==================== -->
    <header class="header" id="header">
        <div class="container">
            <a href="index.html" class="header-logo">
                <img src="assets/img/logo-simbolo.webp" alt="Símbolo Dr. Henrique Leal" class="logo-symbol" id="header-logo-img">
                <img src="assets/img/logo-texto.webp" alt="Dr. Henrique Leal Rosa" class="logo-text">
            </a>
            <nav class="nav-links" id="navLinks">
                <a href="index.html#resultados">Resultados</a>
                <a href="procedimentos.html">Procedimentos</a>
                <a href="sobre.html">Dr. Henrique</a>
                <a href="index.html#localizacao">Consultório</a>
                <a href="index.html#faq">Dúvidas</a>
                <a href="blog.html" style="color: #ffffff; font-weight: 700;">Blog</a>
            </nav>
            <button class="menu-toggle" id="menuToggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <!-- ==================== ARTICLE HERO ==================== -->
    <section class="article-page-header">
        <div class="container" style="max-width: 980px;">
            
            <div class="article-breadcrumbs">
                <a href="index.html">Início</a> › <a href="blog.html">Blog</a> › <span>{p['category']}</span>
            </div>

            <!-- Author Header -->
            <div class="author-box-top">
                <img alt="Dr. Henrique Leal Rosa" class="author-img-circle" src="assets/img/henrique-portrait.webp">
                <div>
                    <h3 class="author-name-title">Dr. Henrique Leal Rosa</h3>
                    <p class="author-role-sub">Cirurgião Dentista (CRO-PR 31739) & Biomédico (CRBM-PR 8966)</p>
                </div>
            </div>

            <!-- Category & Tags -->
            <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 15px;">
                <span class="article-cat-pill">{p['category']}</span>
                <div style="display: flex; gap: 10px;">{tags_html}</div>
            </div>

            <!-- Article Title -->
            <h1 class="article-main-h1">
                {p['title']}
            </h1>

            <!-- Human Reviewed Badge -->
            <div class="human-badge-drhenrique">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2A7DE1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"></path><path d="m9 12 2 2 4-4"></path></svg>
                Conteúdo médico revisado · Curitiba, PR
            </div>

            <!-- Meta Date & Time -->
            <div class="article-meta-info">
                <span>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 2v4"></path><path d="M16 2v4"></path><rect width="18" height="18" x="3" y="4" rx="2"></rect><path d="M3 10h18"></path><path d="M8 14h.01"></path><path d="M12 14h.01"></path><path d="M16 14h.01"></path><path d="M8 18h.01"></path><path d="M12 18h.01"></path><path d="M16 18h.01"></path></svg>
                    {format_date_pt(p['date'])}
                </span>
                <span>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    {p['readingMinutes']} min de leitura
                </span>
            </div>

        </div>
    </section>

    <!-- ==================== BODY (2-COLUMN GRID) ==================== -->
    <section style="background: #FFFFFF;">
        <div class="container" style="max-width: 1040px;">
            <div class="article-layout-grid">
                
                <!-- Left Sticky Sidebar Index -->
                <aside class="article-sidebar">
                    <h3 class="sidebar-index-title">Índice do Artigo</h3>
                    <nav class="sidebar-nav-list">
                        {sidebar_links_html}
                    </nav>
                    
                    <div class="sidebar-clinic-box">
                        <h4>Consultório Água Verde</h4>
                        <p>
                            Av. Rep. Argentina, 1237 - Sala 518 · Edifício Today's Office, Curitiba - PR.
                        </p>
                        <a href="https://wa.me/5541988577430" target="_blank" rel="noopener" class="sidebar-clinic-btn">
                            Agendar Consulta ↗
                        </a>
                    </div>
                </aside>

                <!-- Right Main Article Body -->
                <article class="article-main-col">
                    
                    <!-- Lead Quote with Accent Left Border -->
                    <div class="article-lead-text">
                        {p['lead']}
                    </div>

                    <!-- Main Featured Article Cover Image -->
                    <div class="article-cover-wrap">
                        <img alt="{p['coverAlt']}" fetchpriority="high" class="article-cover-img" src="{p['cover']}">
                    </div>

                    <!-- Dynamic Section Content -->
                    {sections_html}

                </article>
            </div>
        </div>
    </section>

    <!-- ==================== PRE-FOOTER CTA ==================== -->
    <section class="article-prefooter-cta">
        <div class="container" style="max-width: 820px;">
            <h2 class="article-prefooter-title">Pronto para transformar sua autoestima?</h2>
            <p class="article-prefooter-desc">
                Agende sua avaliação com o Dr. Henrique Leal no Edifício Today's Office (Água Verde) e receba um plano de tratamento exclusivo para suas necessidades.
            </p>
            <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                <a href="https://wa.me/5541988577430?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o%20com%20o%20Dr.%20Henrique." 
                   class="btn btn-primary" target="_blank" rel="noopener" style="padding: 16px 36px; font-size: 1rem;">
                    Agendar Avaliação no WhatsApp ↗
                </a>
                <a href="procedimentos.html" class="btn btn-secondary" style="padding: 16px 36px; font-size: 1rem; color: #FFFFFF; border-color: rgba(255, 255, 255, 0.4);">
                    Conhecer Procedimentos
                </a>
            </div>
        </div>
    </section>

    <!-- ==================== FOOTER PADRÃO DR. HENRIQUE LEAL ==================== -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="index.html">
                        <img src="assets/img/logo-sub-colorida.webp" alt="Dr. Henrique Leal Rosa" class="footer-logo" loading="lazy">
                    </a>
                    <p>Harmonização Facial com naturalidade e sofisticação. Curitiba, PR.</p>
                </div>
                <div class="footer-col">
                    <h4>Navegação</h4>
                    <a href="index.html">Início</a>
                    <a href="procedimentos.html">Procedimentos</a>
                    <a href="sobre.html">Dr. Henrique</a>
                    <a href="blog.html">Blog</a>
                    <a href="index.html#localizacao">Consultório</a>
                    <a href="index.html#faq">Dúvidas</a>
                </div>
                <div class="footer-col">
                    <h4>Procedimentos</h4>
                    <a href="fios-de-pdo-curitiba.html">Fios de PDO</a>
                    <a href="botox-curitiba.html">Toxina Botulínica</a>
                    <a href="preenchimento-labial-curitiba.html">Preenchimento</a>
                    <a href="bioestimuladores-de-colageno-curitiba.html">Bioestimuladores</a>
                </div>
                <div class="footer-col">
                    <h4>Contato</h4>
                    <a href="https://wa.me/5541988577430" target="_blank" rel="noopener">WhatsApp</a>
                    <a href="https://maps.google.com/?q=Av.+Rep.+Argentina,+1237+-+Sala+518+-+%C3%81gua+Verde,+Curitiba+-+PR" target="_blank" rel="noopener">Edifício Today's Office · Água Verde</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Dr. Henrique Leal Rosa. Todos os direitos reservados. CRO-PR 31739 · CRBM-PR 8966.</p>
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js?v=5.0"></script>
</body>
</html>
"""
    with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
        f.write(full_page_html)

print("Generated all 20 individual article pages with 100% Dr. Henrique Leal visual identity!")
