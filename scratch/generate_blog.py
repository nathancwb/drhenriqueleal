# -*- coding: utf-8 -*-
import os, json

POSTS = [
    # 1. Harmonização Facial
    {
        "slug": "harmonizacao-facial-mitos-e-verdades-curitiba",
        "title": "Harmonização Facial em Curitiba: 7 Mitos e Verdades que Você Precisa Saber",
        "category": "Harmonização Facial",
        "excerpt": "Descubra o que é verdade e o que é mito sobre a harmonização facial. Entenda como o procedimento preserva a naturalidade e valoriza seus traços em Curitiba.",
        "cover": "assets/img/harmonizacao-facial-nova.webp",
        "date": "2026-08-15",
        "readingMinutes": 5,
        "tags": ["Harmonização Facial", "Curitiba", "Ácido Hialurônico", "Naturalidade"],
        "content_html": """
        <p class="lead">A busca por procedimentos estéticos que valorizam a beleza natural sem exageros tem crescido expressivamente em Curitiba. No entanto, muitas dúvidas e desinformações ainda cercam a harmonização facial.</p>
        
        <h2>1. A harmonização facial deixa o rosto artificial?</h2>
        <p><strong>Mito.</strong> O objetivo da harmonização bem executada é justamente o oposto: realçar a beleza e devolver proporções anatômicas equilibradas de forma sutil. Quando realizada com planejamento minucioso e respeito às distâncias faciais, ninguém percebe que você fez um procedimento, apenas que está com a aparência mais descansada e jovem.</p>
        
        <h2>2. O procedimento é definitivo ou reversível?</h2>
        <p><strong>Verdade.</strong> A maioria dos preenchedores modernos utilizados no consultório, como o ácido hialurônico, é temporária e biocompatível, sendo absorvida naturalmente pelo organismo em um período de 12 a 18 meses. Além disso, caso necessário, o ácido hialurônico pode ser completamente revertido com a aplicação da enzima hialuronidase.</p>
        
        <h2>3. Qualquer pessoa pode fazer harmonização?</h2>
        <p><strong>Verdade, desde que haja indicação clínica.</strong> O procedimento é recomendado a partir dos 20 a 25 anos para prevenção ou estruturação, e em pacientes maduros para sustentação e combate à flacidez. A consulta de avaliação individualizada no consultório em Curitiba é fundamental para definir as reais necessidades anatômicas de cada paciente.</p>
        
        <h2>4. Harmonização facial estica a pele como cirurgia?</h2>
        <p><strong>Mito.</strong> A harmonização não estica a pele; ela atua repondo coxins de gordura perdidos, estruturando pontos de suporte ósseo (como queixo e mandíbula) e estimulando o colágeno.</p>
        
        <div class="article-highlight-box">
            <h4>Dica do Dr. Henrique Leal</h4>
            <p>Em Curitiba, priorize profissionais que realizam o estudo detalhado das proporções áureas da sua face em repouso e em movimento, garantindo que sua mímica e expressividade continuem 100% autênticas.</p>
        </div>
        """
    },
    {
        "slug": "harmonizacao-facial-masculina-guia-curitiba",
        "title": "Harmonização Facial Masculina: Como Definir Mandíbula e Queixo sem Perder a Naturalidade",
        "category": "Harmonização Facial",
        "excerpt": "Guia completo sobre a estruturação mandibular e do mento masculino. Linhas firmes, ângulo reto e sofisticação no consultório do Dr. Henrique Leal em Curitiba.",
        "cover": "assets/img/resultados/slider-caso-masculino-depois.webp",
        "date": "2026-08-10",
        "readingMinutes": 6,
        "tags": ["Harmonização Masculina", "Mandíbula", "Mento", "Curitiba"],
        "content_html": """
        <p class="lead">Cada vez mais homens em Curitiba buscam a harmonização facial para valorizar traços marcantes, conferir autoridade à fisionomia e definir o contorno do terço inferior do rosto.</p>
        
        <h2>Diferenças entre a Harmonização Masculina e Feminina</h2>
        <p>Enquanto o planejamento feminino busca ângulos suaves, formatos de coração e queixo mais afilado, a harmonização masculina foca em:</p>
        <ul>
            <li><strong>Mandíbula bem delineada:</strong> Ângulo mandibular mais reto e demarcado, separando claramente o rosto do pescoço.</li>
            <li><strong>Mento (queixo) quadrado e projetado:</strong> Alinhado com a largura dos lábios para conferir firmeza e equilíbrio ao perfil.</li>
            <li><strong>Malar discreto:</strong> Evita-se a projeção excessiva das maçãs do rosto para não feminilizar a expressão.</li>
        </ul>
        
        <h2>Como é feito o procedimento no consultório</h2>
        <p>Utilizamos microcânulas e ácido hialurônico de alta viscosidade e sustentação, com anestesia local prévia. O paciente retorna às suas atividades profissionais imediatamente, sem necessidade de repouso prolongado.</p>
        
        <h2>Durabilidade dos resultados</h2>
        <p>Os resultados da estruturação mandibular masculina duram em média de 14 a 18 meses, com aspecto natural e viril desde o primeiro dia.</p>
        """
    },
    # 2. Botox / Toxina Botulínica
    {
        "slug": "botox-preventivo-quando-comecar-curitiba",
        "title": "Botox Preventivo em Curitiba: Qual a Idade Certa para Começar?",
        "category": "Toxina Botulínica",
        "excerpt": "Entenda o conceito de toxina botulínica preventiva, como evitar que rugas de expressão se tornem marcas profundas na pele e os cuidados essenciais.",
        "cover": "assets/img/botox-nova.webp",
        "date": "2026-08-04",
        "readingMinutes": 4,
        "tags": ["Botox", "Prevenção", "Rugas de Expressão", "Curitiba"],
        "content_html": """
        <p class="lead">A aplicação preventiva de toxina botulínica tornou-se um dos cuidados dermatológicos e estéticos mais procurados por jovens adultos em Curitiba que desejam envelhecer com viço e elegância.</p>
        
        <h2>O que é o Botox Preventivo?</h2>
        <p>Diferente do tratamento corretivo (aplicado quando as rugas já estão estáticas e marcadas mesmo em repouso), o Botox preventivo relaxa suavemente a musculatura hipercinética antes que a fratura dérmica aconteça.</p>
        
        <h2>Qual a idade ideal para iniciar?</h2>
        <p>Geralmente entre os 25 e 30 anos, quando as primeiras linhas de expressão começam a aparecer ao sorrir ou franzir a testa. Cada organismo é único, e a indicação depende da força muscular, mímica facial e exposição solar.</p>
        
        <h2>Vantagens do protocolo preventivo</h2>
        <ul>
            <li>Doses menores e aspecto ultra natural;</li>
            <li>Previne a formação de vincos permanentes entre as sobrancelhas (glabela) e na testa;</li>
            <li>Preserva a elasticidade e jovialidade da pele a longo prazo.</li>
        </ul>
        """
    },
    {
        "slug": "quanto-tempo-dura-o-botox-curitiba",
        "title": "Quanto Tempo Dura o Botox na Testa e Olhos? Dicas para Prolongar o Efeito",
        "category": "Toxina Botulínica",
        "excerpt": "Descubra fatores que influenciam na durabilidade da toxina botulínica e como manter seu rosto descansado e sem rugas por mais tempo em Curitiba.",
        "cover": "assets/img/resultados/botox-testa-depois.webp",
        "date": "2026-07-28",
        "readingMinutes": 5,
        "tags": ["Botox", "Durabilidade", "Testa e Olhos", "Cuidados"],
        "content_html": """
        <p class="lead">Uma das perguntas mais frequentes no consultório em Curitiba é: afinal, quantos meses dura o efeito do Botox e como fazer para que ele dure o máximo possível?</p>
        
        <h2>Tempo médio de durabilidade</h2>
        <p>A toxina botulínica atinge seu efeito máximo por volta de 14 a 15 dias após a aplicação e mantém sua ação clínica por um período médio de <strong>4 a 6 meses</strong>. Em homens ou praticantes intensos de atividade física com metabolismo acelerado, esse período pode ser de 3 a 5 meses.</p>
        
        <h2>Fatores que afetam a duração</h2>
        <ul>
            <li><strong>Metabolismo individual e exercícios:</strong> Atletas de alta intensidade tendem a absorver a toxina mais rapidamente.</li>
            <li><strong>Expressividade:</strong> Pessoas com mímica facial muito ativa movimentam os músculos com maior frequência.</li>
            <li><strong>Qualidade da toxina e técnica de dosagem:</strong> O uso de produtos de padrão ouro e a aplicação precisa nos pontos anatômicos corretos garantem fixação superior.</li>
        </ul>
        
        <h2>Como prolongar os resultados</h2>
        <p>Evite esfregar a região nas primeiras 24 horas, utilize protetor solar diariamente e mantenha a pele bem hidratada com acompanhamento regular.</p>
        """
    },
    # 3. Fios de Sustentação (PDO)
    {
        "slug": "fios-de-pdo-lifting-sem-cirurgia-curitiba",
        "title": "Fios de PDO em Curitiba: Como Funciona o Lifting Facial sem Cortes",
        "category": "Fios de PDO",
        "excerpt": "Conheça a tecnologia dos fios de polidioxanona (PDO), técnica internacional aprendida na Coreia do Sul para reposicionar tecidos e estimular colágeno.",
        "cover": "assets/img/foto-fios-nova.webp",
        "date": "2026-07-20",
        "readingMinutes": 6,
        "tags": ["Fios de PDO", "Lifting Facial", "Coreia do Sul", "Curitiba"],
        "content_html": """
        <p class="lead">Os fios de sustentação de PDO (Polidioxanona) representam uma das maiores inovações da estética regenerativa mundial, proporcionando tração e estímulo de colágeno sem cortes ou cicatrizes.</p>
        
        <h2>Como os fios atuam no rosto?</h2>
        <p>Os fios espiculados possuem pequenas garras microscópicas que se ancoram nas camadas profundas da pele, tracionando bochechas caídas (efeito 'buldogue'), melhorando o sulco nasogeniano ('bigode chinês') e redefinindo a linha da mandíbula.</p>
        
        <h2>Fios de Tração vs Fios de Estímulo</h2>
        <ul>
            <li><strong>Fios de Tração (Espiculados/Canulados):</strong> Reposicionam os tecidos imediatamente, criando efeito lifting visível na hora.</li>
            <li><strong>Fios Lisos (Mono e Matrix):</strong> Criam uma malha dérmica para redensificar a pele fina, tratar rugas em código de barras e olheiras.</li>
        </ul>
        
        <h2>Segurança e Absorção</h2>
        <p>A polidioxanona é um material 100% biocompatível e seguro, utilizado há décadas em cirurgias cardíacas. O fio é absorvido em cerca de 6 a 8 meses, mas o novo colágeno formado permanece sustentando a pele por até 2 anos.</p>
        """
    },
    {
        "slug": "fios-de-pdo-ou-bioestimulador-qual-escolher",
        "title": "Fios de PDO ou Bioestimulador de Colágeno: Qual o Ideal para o Seu Rosto?",
        "category": "Fios de PDO",
        "excerpt": "Comparativo completo entre fios de tração e bioestimuladores injetáveis para tratar flacidez e perda de contorno facial em Curitiba.",
        "cover": "assets/img/bioestimulador-de-colageno.webp",
        "date": "2026-07-14",
        "readingMinutes": 5,
        "tags": ["Fios de PDO", "Bioestimuladores", "Flacidez", "Comparativo"],
        "content_html": """
        <p class="lead">Tanto os Fios de PDO quanto os Bioestimuladores de Colágeno são excelentes para combater o envelhecimento, mas possuem mecanismos e indicações primárias distintas.</p>
        
        <h2>Quando escolher Fios de PDO?</h2>
        <p>Os fios são a primeira escolha quando o paciente apresenta queda tecidual leve a moderada e busca reposicionamento imediato do contorno do rosto, sem adicionar volume.</p>
        
        <h2>Quando escolher Bioestimuladores Injetáveis?</h2>
        <p>Os bioestimuladores (como ácido poli-L-láctico e hidroxiapatita) são ideais para tratar a qualidade global da pele, aumentando a espessura dérmica, firmeza e viço progressivamente.</p>
        
        <h2>A combinação perfeita</h2>
        <p>No consultório em Curitiba, frequentemente associamos os dois métodos: os fios estruturam e erguem os tecidos, enquanto o bioestimulador fortalece a derme, garantindo um resultado muito mais duradouro e harmônico.</p>
        """
    },
    # 4. Bioestimuladores de Colágeno
    {
        "slug": "sculptra-radiesse-elleva-comparativo-curitiba",
        "title": "Sculptra, Radiesse e Elleva: Diferenças entre os Melhores Bioestimuladores de Colágeno",
        "category": "Bioestimuladores",
        "excerpt": "Análise comparativa das principais marcas de bioestimuladores de colágeno do mercado. Saiba como escolher o melhor tratamento em Curitiba.",
        "cover": "assets/img/bioestimulador.webp",
        "date": "2026-07-05",
        "readingMinutes": 6,
        "tags": ["Sculptra", "Radiesse", "Elleva", "Bioestimuladores", "Curitiba"],
        "content_html": """
        <p class="lead">A partir dos 25 anos, nosso corpo perde cerca de 1% de colágeno ao ano. Os bioestimuladores injetáveis são a tecnologia mais eficaz para reverter esse processo de forma biológica.</p>
        
        <h2>1. Sculptra e Elleva (Ácido Poli-L-Láctico - PLLA)</h2>
        <p>Estimulam intensamente a produção de colágeno tipo I. São perfeitos para quem sofre com perda de espessura da pele e flacidez difusa no rosto, pescoço e glúteos.</p>
        
        <h2>2. Radiesse (Hidroxiapatita de Cálcio)</h2>
        <p>Além de estimular colágeno e elastina, oferece um leve efeito de ancoragem e firmeza tecidual imediata, sendo excelente para contorno mandibular e rejuvenescimento das mãos.</p>
        
        <h2>Como o Dr. Henrique Leal define o protocolo ideal</h2>
        <p>A escolha entre PLLA ou Hidroxiapatita depende do grau de flacidez, espessura cutânea e das áreas a serem tratadas, avaliadas minuciosamente durante a consulta presencial no Água Verde em Curitiba.</p>
        """
    },
    {
        "slug": "como-tratar-flacidez-facial-pescoco-curitiba",
        "title": "Como Tratar Flacidez no Rosto e Pescoço com Bioestimuladores em Curitiba",
        "category": "Bioestimuladores",
        "excerpt": "Dicas clínicas e protocolos modernos para recuperar a firmeza do pescoço, papada e contorno facial sem cirurgia.",
        "cover": "assets/img/resultados/slider-caso-rejuvenescimento-depois.webp",
        "date": "2026-06-28",
        "readingMinutes": 5,
        "tags": ["Pescoço", "Flacidez", "Rejuvenescimento", "Bioestimuladores"],
        "content_html": """
        <p class="lead">O pescoço e o contorno da mandíbula são regiões que frequentemente denunciam o envelhecimento antes do restante do rosto devido à pele fina e à constante movimentação.</p>
        
        <h2>Por que a pele do pescoço perde firmeza?</h2>
        <p>A baixa concentração de glândulas sebáceas e a perda contínua de elastina fazem com que o pescoço desenvolva linhas horizontais e flacidez precoce.</p>
        
        <h2>O protocolo de tratamento com bioestimuladores</h2>
        <p>A aplicação de microdoses vetorizadas de bioestimulador distribui partículas estimuladoras ao longo dos vetores de tração do pescoço e mandíbula, promovendo o espessamento gradual da derme e melhorando o tônus tecidual.</p>
        """
    },
    # 5. Preenchimento Labial
    {
        "slug": "preenchimento-labial-natural-lips-curitiba",
        "title": "Preenchimento Labial Natural Lips em Curitiba: Lábios Hidratados e sem Exageros",
        "category": "Preenchimento Labial",
        "excerpt": "Descubra a técnica Natural Lips do Dr. Henrique Leal: contorno sutil, hidratação profunda e respeito à anatomia da sua boca.",
        "cover": "assets/img/preenchimento-labial-depois-clean.webp",
        "date": "2026-06-20",
        "readingMinutes": 4,
        "tags": ["Preenchimento Labial", "Natural Lips", "Ácido Hialurônico", "Curitiba"],
        "content_html": """
        <p class="lead">O medo do resultado exagerado ou do aspecto artificial ('bico de pato') ainda afasta muitas pessoas do preenchimento labial. A técnica Natural Lips foi desenvolvida para quebrar esse paradigma.</p>
        
        <h2>O que é o conceito Natural Lips?</h2>
        <p>Trata-se de um protocolo que prioriza a definição dos contornos naturais (arco do cupido e filtro labial), hidratação profunda e reposição de volume milimetricamente dosada, respeitando a proporção entre lábio superior e inferior.</p>
        
        <h2>Como é a sessão?</h2>
        <p>Com aplicação de anestésico odontológico para conforto total do paciente, o procedimento leva cerca de 30 a 40 minutos. O paciente vê o resultado na hora e pode acompanhar cada detalhe no espelho.</p>
        """
    },
    {
        "slug": "cuidados-pos-preenchimento-labial-guia",
        "title": "Cuidados Pós-Preenchimento Labial: Recuperação, Inchaço e Duração",
        "category": "Preenchimento Labial",
        "excerpt": "O que fazer e o que evitar nos primeiros dias após o preenchimento labial para garantir uma cicatrização perfeita.",
        "cover": "assets/img/resultados/labio-resultado-4.webp",
        "date": "2026-06-12",
        "readingMinutes": 4,
        "tags": ["Pós-Procedimento", "Preenchimento Labial", "Cuidados", "Inchaço"],
        "content_html": """
        <p class="lead">O sucesso do preenchimento labial depende tanto da perícia técnica do profissional quanto dos cuidados simples adotados pelo paciente nos primeiros dias.</p>
        
        <h2>O que esperar nos primeiros 3 dias</h2>
        <p>É perfeitamente normal que os lábios apresentem leve inchaço (edema) e sensibilidade nas primeiras 48 a 72 horas. O resultado final se consolida entre 15 e 20 dias.</p>
        
        <h2>Recomendações importantes:</h2>
        <ul>
            <li>Aplique compressas frias delicadamente nas primeiras 24 horas;</li>
            <li>Evite bebidas e alimentos muito quentes no primeiro dia;</li>
            <li>Não pressione ou massageie os lábios sem orientação profissional;</li>
            <li>Evite atividade física intensa nas primeiras 24 a 48 horas.</li>
        </ul>
        """
    },
    # 6. Rinomodelação
    {
        "slug": "rinomodelacao-com-acido-hialuronico-curitiba",
        "title": "Rinomodelação em Curitiba: Como Empinar e Alinhar o Nariz sem Cirurgia",
        "category": "Rinomodelação",
        "excerpt": "Procedimento rápido e seguro para corrigir pequenas imperfeições no dorso nasal e levantar a ponta caída em Curitiba.",
        "cover": "assets/img/resultados/upnose-depois.webp",
        "date": "2026-06-04",
        "readingMinutes": 5,
        "tags": ["Rinomodelação", "Up Nose", "Nariz", "Curitiba"],
        "content_html": """
        <p class="lead">A rinomodelação não cirúrgica é uma excelente alternativa à rinoplastia tradicional para pacientes que desejam harmonizar o perfil nasal sem cortes, anestesia geral ou pós-operatório complexo.</p>
        
        <h2>O que é possível corrigir com a Rinomodelação?</h2>
        <ul>
            <li>Disfarçar a 'giba' nasal (ossinho saliente no dorso);</li>
            <li>Elevar a ponta caída (Método Up Nose);</li>
            <li>Corrigir assimetrias leves e afinar visualmente o nariz de frente.</li>
        </ul>
        
        <h2>Segurança e Precisão Anatômica</h2>
        <p>O nariz é uma região de alta complexidade vascular. Por isso, no consultório do Dr. Henrique Leal em Curitiba, o procedimento é realizado com cânulas de ponta romba e microdoses precisas de ácido hialurônico de padrão médico rigoroso.</p>
        """
    },
    {
        "slug": "rinomodelacao-doi-cuidados-e-duracao",
        "title": "Rinomodelação Dói? Riscos, Tempo de Recuperação e Durabilidade",
        "category": "Rinomodelação",
        "excerpt": "Tudo sobre o nível de dor, anestesia local, cuidados essenciais e tempo de durabilidade da rinomodelação.",
        "cover": "assets/img/resultados/caso-rinomodelacao-perfil-1-depois.webp",
        "date": "2026-05-28",
        "readingMinutes": 4,
        "tags": ["Rinomodelação", "Dúvidas", "Segurança", "Durabilidade"],
        "content_html": """
        <p class="lead">Descubra como o uso de anestésicos modernos torna a experiência da rinomodelação muito confortável e tranquila.</p>
        
        <h2>A rinomodelação dói?</h2>
        <p>Não. Utilizamos anestesia local odontológica precisa no ponto de entrada da cânula. A sensação durante a aplicação é de leve pressão passageira, sem dor aguda.</p>
        
        <h2>Tempo de recuperação</h2>
        <p>A recuperação é praticamente imediata. O paciente pode retornar ao trabalho no mesmo dia, devendo apenas evitar apoiar óculos pesados sobre o dorso nasal nas primeiras duas semanas.</p>
        """
    },
    # 7. Estética Íntima
    {
        "slug": "estetica-intima-preenchimento-acido-hialuronico-curitiba",
        "title": "Preenchimento Íntimo Feminino em Curitiba: Como o Ácido Hialurônico Devolve Firmeza e Conforto",
        "category": "Estética Íntima",
        "excerpt": "Procedimento médico-estético delicado para recuperação de volume, hidratação e firmeza dos grandes lábios com total sigilo e conforto.",
        "cover": "assets/img/intimos-nova.webp",
        "date": "2026-05-20",
        "readingMinutes": 5,
        "tags": ["Estética Íntima", "Preenchimento Íntimo", "Curitiba", "Autoestima"],
        "content_html": """
        <p class="lead">Com o passar dos anos, oscilações de peso ou alterações hormonais (como na menopausa), a região íntima feminina sofre perda de gordura subcutânea e tônus dérmico.</p>
        
        <h2>Como funciona o preenchimento íntimo?</h2>
        <p>A aplicação de ácido hialurônico específico para a área genital devolve o volume e o turgor aos grandes lábios, protegendo as estruturas internas, reduzindo atritos desconfortáveis e melhorando a estética e a autoconfiança.</p>
        
        <h2>Privacidade e Acolhimento</h2>
        <p>No consultório em Curitiba, o atendimento é realizado em ambiente privativo, seguro e acolhedor, com protocolos anestésicos que garantem uma sessão indolor e tranquila.</p>
        """
    },
    {
        "slug": "rejuvenescimento-intimo-beneficios-e-autoestima",
        "title": "Rejuvenescimento Íntimo: Procedimentos Modernos para Saúde e Autoestima da Mulher",
        "category": "Estética Íntima",
        "excerpt": "Bioestimuladores, hidratação e fios na estética íntima: conheça os tratamentos que unem bem-estar, função e beleza.",
        "cover": "assets/img/intimos.webp",
        "date": "2026-05-12",
        "readingMinutes": 5,
        "tags": ["Rejuvenescimento Íntimo", "Saúde Feminina", "Bioestimulador"],
        "content_html": """
        <p class="lead">O autocuidado íntimo vai muito além da estética: trata-se de conforto diário, liberdade no uso de roupas e reconexão com a própria autoestima.</p>
        
        <h2>Principais opções de tratamentos íntimos:</h2>
        <ul>
            <li><strong>Preenchimento com Ácido Hialurônico:</strong> Para reposição volumétrica e hidratação profunda.</li>
            <li><strong>Bioestimuladores de Colágeno:</strong> Para combate à flacidez e fortalecimento dérmico.</li>
            <li><strong>Clareamento Íntimo:</strong> Para uniformização do tom da pele em áreas com hiperpigmentação por atrito.</li>
        </ul>
        """
    },
    # 8. Protocolo Bioforce
    {
        "slug": "protocolo-bioforce-regeneracao-celular-curitiba",
        "title": "Protocolo Bioforce: O Tratamento Assinatura para Regeneração Facial Profunda",
        "category": "Protocolo Bioforce",
        "excerpt": "Associação exclusiva de bioestimuladores de última geração e peptídeos bioativos desenvolvida pelo Dr. Henrique Leal em Curitiba.",
        "cover": "assets/img/7G1A9991.webp",
        "date": "2026-05-04",
        "readingMinutes": 5,
        "tags": ["Protocolo Bioforce", "Regeneração", "Assinatura", "Curitiba"],
        "content_html": """
        <p class="lead">O Protocolo Bioforce é o tratamento de assinatura da clínica, concebido para pacientes que buscam rejuvenescimento biológico profundo sem efeito 'inflado'.</p>
        
        <h2>O que compõe o Protocolo Bioforce?</h2>
        <p>Trata-se de uma sinergia avançada que combina bioestimuladores particulados importados, fatores de crescimento celular e peptídeos sinalizadores, estimulando a neocolagênese e a angiogênese dérmica de forma acelerada.</p>
        
        <h2>Resultados esperados</h2>
        <p>Melhora visível da densidade da pele, redução de poros dilatados, atenuação de linhas finas e recuperação do viço juvenil em poucas semanas.</p>
        """
    },
    {
        "slug": "peptideos-bioativos-e-antiaging-avancado",
        "title": "Peptídeos Bioativos na Estética Avançada: Como Estimular a Juventude da Pele",
        "category": "Protocolo Bioforce",
        "excerpt": "A ciência por trás dos peptídeos sinalizadores e como eles reprogramam a síntese de colágeno nas células da pele.",
        "cover": "assets/img/henrique-portrait.webp",
        "date": "2026-04-26",
        "readingMinutes": 4,
        "tags": ["Peptídeos", "Ciência", "Antiaging", "Regeneração"],
        "content_html": """
        <p class="lead">Compreenda como a biologia molecular e a estética avançada se unem para promover tratamentos de rejuvenescimento celular altamente eficazes.</p>
        
        <h2>Como os peptídeos atuam?</h2>
        <p>Os peptídeos bioativos funcionam como 'mensageiros' biológicos que comunicam aos fibroblastos a necessidade de sintetizar novas fibras de colágeno e elastina, restaurando a matriz extracelular da pele.</p>
        """
    },
    # 9. Ozonioterapia
    {
        "slug": "ozonioterapia-beneficios-estetica-saude-curitiba",
        "title": "Ozonioterapia em Curitiba: Benefícios do Ozônio Medicinal para Pele e Inflamação",
        "category": "Ozonioterapia",
        "excerpt": "Como o gás ozônio atua na oxigenação celular, combate a radicais livres e potencialização de resultados estéticos em Curitiba.",
        "cover": "assets/img/henrique-clinic.webp",
        "date": "2026-04-18",
        "readingMinutes": 5,
        "tags": ["Ozonioterapia", "Ozônio Medicinal", "Saúde", "Curitiba"],
        "content_html": """
        <p class="lead">A ozonioterapia medicinal é uma terapia biológica reconhecida por suas propriedades anti-inflamatórias, germicidas e de otimização da oxigenação tecidual.</p>
        
        <h2>Aplicações na estética e bem-estar</h2>
        <ul>
            <li>Tratamento complementar de acne e dermatites;</li>
            <li>Melhora da microcirculação sanguínea e oxigenação cutânea;</li>
            <li>Ação antioxidante sistêmica e estímulo ao metabolismo celular.</li>
        </ul>
        """
    },
    {
        "slug": "ozonioterapia-para-rejuvenescimento-e-cicatrizacao",
        "title": "Ozonioterapia no Pós-Procedimento: Aceleração da Cicatrização e Oxigenação Tecidual",
        "category": "Ozonioterapia",
        "excerpt": "Entenda por que o ozônio medicinal é utilizado para acelerar a recuperação de procedimentos estéticos e reduzir edemas.",
        "cover": "assets/img/henrique-faq-new.webp",
        "date": "2026-04-10",
        "readingMinutes": 4,
        "tags": ["Cicatrização", "Pós-Operatório", "Ozonioterapia"],
        "content_html": """
        <p class="lead">A utilização do ozônio medicinal no pós-procedimento imediato reduz expressivamente o tempo de recuperação e o risco de intercorrências.</p>
        
        <h2>Principais benefícios na cicatrização:</h2>
        <p>O ozônio estimula a liberação de óxido nítrico e fatores de crescimento endotelial, acelerando o fechamento tecidual e diminuindo hematomas e edemas com rapidez.</p>
        """
    },
    # 10. Terapia Capilar
    {
        "slug": "terapia-capilar-para-queda-de-cabelo-curitiba",
        "title": "Terapia Capilar em Curitiba: Como Tratar Queda de Cabelo e Calvície com Tecnologia",
        "category": "Terapia Capilar",
        "excerpt": "Protocolos integrados de estímulo folicular, nutrição capilar e combate à calvície masculina e feminina no Água Verde.",
        "cover": "assets/img/resultados/IMG_6808.webp",
        "date": "2026-04-02",
        "readingMinutes": 5,
        "tags": ["Terapia Capilar", "Queda de Cabelo", "Calvície", "Curitiba"],
        "content_html": """
        <p class="lead">A queda de cabelo (eflúvio telógeno e alopecia androgenética) afeta diretamente a autoestima de homens e mulheres. O diagnóstico precoce e o tratamento clínico integrado são a chave para a recuperação capilar.</p>
        
        <h2>Como funciona a Terapia Capilar Avançada?</h2>
        <p>Associamos ativos antiqueda injetáveis, bioestimuladores foliculares, microinfusão de medicamentos e ozonioterapia para desinflamar o couro cabeludo e estimular o crescimento de fios mais grossos e resistentes.</p>
        """
    },
    {
        "slug": "microinfusao-capilar-e-fortalecimento-dos-fios",
        "title": "Microinfusão e Fatores de Crescimento Capilar: Fortalecimento desde a Raiz",
        "category": "Terapia Capilar",
        "excerpt": "Entenda como a entrega direta de nutrientes no bulbo capilar desacelera o afinamento e estimula novos fios.",
        "cover": "assets/img/resultados/caso-harmonizacao-masculina-2.webp",
        "date": "2026-03-24",
        "readingMinutes": 4,
        "tags": ["Microinfusão", "Fatores de Crescimento", "Bulbo Capilar"],
        "content_html": """
        <p class="lead">A aplicação direta de substâncias terapêuticas na derme do couro cabeludo garante absorção infinitamente superior aos tratamentos orais ou tópicos convencionais.</p>
        
        <h2>Indicações do procedimento:</h2>
        <ul>
            <li>Calvície em estágio inicial ou intermediário;</li>
            <li>Afinamento progressivo dos fios;</li>
            <li>Queda capilar pós-estresse ou pós-parto.</li>
        </ul>
        """
    }
]

# Write blog-data.js for client-side search/filtering
with open("assets/js/blog-data.js", "w", encoding="utf-8") as f:
    f.write("window.BLOG_POSTS = " + json.dumps(POSTS, ensure_ascii=False, indent=2) + ";\n")
print("Saved assets/js/blog-data.js")

# Format date helper
MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
def format_date_pt(d_str):
    y, m, d = d_str.split("-")
    return f"{int(d)} de {MONTHS[int(m)-1]} de {y}"

# 1. GENERATE blog.html (Index page)
featured = POSTS[0]
rest_posts = POSTS[1:]

categories = sorted(list(set(p["category"] for p in POSTS)))

blog_index_html = f"""<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/style.css?v=11.0">
    <link rel="icon" type="image/png" href="assets/img/favicon.png?v=3">
    <link rel="apple-touch-icon" href="assets/img/favicon.png?v=3">
    <title>Blog & Artigos Clínicos | Dr. Henrique Leal Rosa em Curitiba</title>
    <meta name="description" content="Artigos educativos sobre Harmonização Facial, Botox, Fios de PDO, Bioestimuladores e Estética Avançada em Curitiba com o Dr. Henrique Leal Rosa.">
    <link rel="canonical" href="https://drhenriqueleal.com.br/blog.html">
    
    <style>
        .blog-hero {{ padding: 160px 0 40px; background: #FAFBFD; text-align: center; border-bottom: 1px solid rgba(27, 58, 92, 0.06); }}
        .blog-hero-label {{ font-size: 0.82rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: var(--color-primary); display: block; margin-bottom: 12px; }}
        .blog-hero-title {{ font-family: var(--font-heading); font-size: clamp(2.2rem, 4vw, 3.4rem); color: var(--color-primary); margin-bottom: 16px; }}
        .blog-hero-desc {{ font-size: 1.1rem; color: var(--color-text-light); max-width: 680px; margin: 0 auto 30px; line-height: 1.7; }}
        
        .blog-filter-bar {{ display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 40px; padding: 0 10px; }}
        .blog-filter-btn {{ background: #FFFFFF; color: #475569; border: 1px solid rgba(27, 58, 92, 0.12); padding: 8px 18px; border-radius: 30px; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: all 0.25s ease; }}
        .blog-filter-btn:hover, .blog-filter-btn.active {{ background: var(--color-primary); color: #FFFFFF; border-color: var(--color-primary); box-shadow: 0 4px 14px rgba(27, 58, 92, 0.15); }}
        
        .featured-post-card {{ background: #FFFFFF; border-radius: 24px; border: 1px solid rgba(27, 58, 92, 0.08); overflow: hidden; display: grid; grid-template-columns: 1.1fr 1fr; margin-bottom: 50px; box-shadow: 0 10px 35px rgba(27, 58, 92, 0.05); transition: transform 0.3s ease, box-shadow 0.3s ease; text-decoration: none; color: inherit; }}
        .featured-post-card:hover {{ transform: translateY(-4px); box-shadow: 0 20px 45px rgba(27, 58, 92, 0.1); }}
        .featured-post-img-wrap {{ width: 100%; height: 100%; min-height: 340px; position: relative; overflow: hidden; }}
        .featured-post-img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }}
        .featured-post-card:hover .featured-post-img {{ transform: scale(1.04); }}
        .featured-post-body {{ padding: 40px 36px; display: flex; flex-direction: column; justify-content: center; }}
        .post-cat-badge {{ display: inline-block; background: rgba(27, 58, 92, 0.08); color: var(--color-primary); font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 4px 12px; border-radius: 20px; margin-bottom: 14px; width: fit-content; }}
        .featured-post-title {{ font-family: var(--font-heading); font-size: 1.85rem; color: var(--color-primary); line-height: 1.25; margin-bottom: 14px; }}
        .featured-post-excerpt {{ font-size: 0.98rem; color: #64748b; line-height: 1.65; margin-bottom: 24px; }}
        .post-meta-row {{ display: flex; align-items: center; gap: 18px; font-size: 0.84rem; color: #94a3b8; font-weight: 500; }}
        .post-meta-item {{ display: flex; align-items: center; gap: 6px; }}
        
        .blog-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-bottom: 70px; }}
        .blog-card {{ background: #FFFFFF; border-radius: 20px; border: 1px solid rgba(27, 58, 92, 0.08); overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 6px 24px rgba(27, 58, 92, 0.04); text-decoration: none; color: inherit; transition: transform 0.3s ease, box-shadow 0.3s ease; }}
        .blog-card:hover {{ transform: translateY(-5px); box-shadow: 0 16px 36px rgba(27, 58, 92, 0.09); }}
        .blog-card-img-wrap {{ width: 100%; height: 210px; overflow: hidden; position: relative; }}
        .blog-card-img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }}
        .blog-card:hover .blog-card-img {{ transform: scale(1.06); }}
        .blog-card-body {{ padding: 26px 24px; display: flex; flex-direction: column; flex-grow: 1; }}
        .blog-card-title {{ font-family: var(--font-heading); font-size: 1.25rem; color: var(--color-primary); line-height: 1.35; margin-bottom: 10px; }}
        .blog-card-excerpt {{ font-size: 0.90rem; color: #64748b; line-height: 1.6; margin-bottom: 18px; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}
        .blog-card-footer {{ margin-top: auto; padding-top: 14px; border-top: 1px solid rgba(27, 58, 92, 0.06); display: flex; justify-content: space-between; align-items: center; font-size: 0.80rem; color: #94a3b8; }}
        .read-more-link {{ font-weight: 700; color: var(--color-primary); display: inline-flex; align-items: center; gap: 4px; transition: transform 0.2s ease; }}
        .blog-card:hover .read-more-link {{ transform: translateX(3px); }}
        
        .blog-cta-box {{ background: linear-gradient(135deg, #1B3A5C 0%, #11253E 100%); border-radius: 24px; padding: 50px 40px; text-align: center; color: #FFFFFF; margin-bottom: 70px; }}
        .blog-cta-title {{ font-family: var(--font-heading); font-size: clamp(1.8rem, 3vw, 2.4rem); margin-bottom: 14px; color: #FFFFFF; }}
        .blog-cta-text {{ font-size: 1.05rem; color: rgba(255, 255, 255, 0.88); max-width: 600px; margin: 0 auto 28px; line-height: 1.6; }}
        
        @media (max-width: 992px) {{
            .featured-post-card {{ grid-template-columns: 1fr; }}
            .featured-post-img-wrap {{ min-height: 240px; height: 260px; }}
            .blog-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}
        @media (max-width: 640px) {{
            .blog-grid {{ grid-template-columns: 1fr; }}
            .blog-hero {{ padding: 130px 0 30px; }}
            .featured-post-body {{ padding: 24px 20px; }}
        }}
    </style>
</head>

<body>

    <!-- ==================== HEADER ==================== -->
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
                <a href="blog.html" style="color: #ffffff; font-weight: 700;">Blog</a>
                <a href="index.html#localizacao">Consultório</a>
                <a href="index.html#faq">Dúvidas</a>
            </nav>
            <button class="menu-toggle" id="menuToggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <!-- ==================== HERO BLOG ==================== -->
    <section class="blog-hero">
        <div class="container">
            <span class="blog-hero-label">Blog & Artigos Clínicos</span>
            <h1 class="blog-hero-title">Ciência, Estética e Cuidados em Curitiba</h1>
            <p class="blog-hero-desc">
                Orientações práticas, dúvidas frequentes e artigos sobre tratamentos faciais e corporais, com foco em segurança e naturalidade.
            </p>
            
            <!-- Category Filter Bar -->
            <div class="blog-filter-bar" id="categoryFilterBar">
                <button class="blog-filter-btn active" data-category="ALL">Todos os Artigos ({len(POSTS)})</button>
"""

for cat in categories:
    count = sum(1 for p in POSTS if p["category"] == cat)
    blog_index_html += f'                <button class="blog-filter-btn" data-category="{cat}">{cat} ({count})</button>\n'

blog_index_html += f"""            </div>
        </div>
    </section>

    <!-- ==================== BLOG POSTS CONTAINER ==================== -->
    <section style="padding: 50px 0 80px; background: #FFFFFF;">
        <div class="container">
            
            <!-- Featured Post -->
            <a href="{featured['slug']}.html" class="featured-post-card" data-category="{featured['category']}">
                <div class="featured-post-img-wrap">
                    <img src="{featured['cover']}" alt="{featured['title']}" class="featured-post-img">
                </div>
                <div class="featured-post-body">
                    <span class="post-cat-badge">{featured['category']}</span>
                    <h2 class="featured-post-title">{featured['title']}</h2>
                    <p class="featured-post-excerpt">{featured['excerpt']}</p>
                    <div class="post-meta-row">
                        <span class="post-meta-item">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="4" rx="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
                            {format_date_pt(featured['date'])}
                        </span>
                        <span class="post-meta-item">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                            {featured['readingMinutes']} min de leitura
                        </span>
                    </div>
                </div>
            </a>

            <!-- Posts Grid -->
            <div class="blog-grid" id="blogGrid">
"""

for p in rest_posts:
    blog_index_html += f"""                <a href="{p['slug']}.html" class="blog-card" data-category="{p['category']}">
                    <div class="blog-card-img-wrap">
                        <img src="{p['cover']}" alt="{p['title']}" class="blog-card-img" loading="lazy">
                    </div>
                    <div class="blog-card-body">
                        <span class="post-cat-badge">{p['category']}</span>
                        <h3 class="blog-card-title">{p['title']}</h3>
                        <p class="blog-card-excerpt">{p['excerpt']}</p>
                        <div class="blog-card-footer">
                            <span>{format_date_pt(p['date'])}</span>
                            <span class="read-more-link">Ler artigo ↗</span>
                        </div>
                    </div>
                </a>
"""

blog_index_html += """            </div>

            <!-- Blog CTA Box -->
            <div class="blog-cta-box">
                <h2 class="blog-cta-title">Tire suas Dúvidas Diretamente no Consultório</h2>
                <p class="blog-cta-text">
                    Agende uma avaliação com o Dr. Henrique Leal no Edifício Today's Office, bairro Água Verde em Curitiba, e receba um planejamento personalizado para o seu rosto.
                </p>
                <a href="https://wa.me/5541988577430?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o%20com%20o%20Dr.%20Henrique." 
                   class="btn btn-primary" target="_blank" rel="noopener" style="padding: 16px 36px; font-size: 1rem; background: #2A7DE1; color: #1B3A5C; font-weight: 700; border: none;">
                    Conversar pelo WhatsApp
                </a>
            </div>

        </div>
    </section>

    <!-- ==================== FOOTER ==================== -->
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
                <p>&copy; 2026 Dr. Henrique Leal Rosa. Todos os direitos reservados. CRO-PR · CRBM-PR.</p>
            </div>
        </div>
    </footer>

    <!-- Filter JS Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const filterBtns = document.querySelectorAll('.blog-filter-btn');
            const cards = document.querySelectorAll('.blog-card, .featured-post-card');
            
            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    
                    const cat = btn.getAttribute('data-category');
                    cards.forEach(card => {
                        if (cat === 'ALL' || card.getAttribute('data-category') === cat) {
                            card.style.display = card.classList.contains('featured-post-card') ? 'grid' : 'flex';
                        } else {
                            card.style.display = 'none';
                        }
                    });
                });
            });
        });
    </script>
    <script src="assets/js/main.js?v=5.0"></script>
</body>
</html>
"""

with open("blog.html", "w", encoding="utf-8") as f:
    f.write(blog_index_html)
print("Generated blog.html")

# 2. GENERATE INDIVIDUAL ARTICLE PAGES
for p in POSTS:
    tags_html = "".join([f'<span class="article-tag">{t}</span>' for t in p["tags"]])
    
    # Related posts (pick 2 other posts)
    related = [other for other in POSTS if other["slug"] != p["slug"]][:3]
    related_html = ""
    for r in related:
        related_html += f"""
        <a href="{r['slug']}.html" class="related-post-card">
            <img src="{r['cover']}" alt="{r['title']}" class="related-post-img">
            <div class="related-post-body">
                <span class="post-cat-badge">{r['category']}</span>
                <h4>{r['title']}</h4>
                <span class="related-read-more">Ler artigo ↗</span>
            </div>
        </a>
        """

    article_html = f"""<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/style.css?v=11.0">
    <link rel="icon" type="image/png" href="assets/img/favicon.png?v=3">
    <link rel="apple-touch-icon" href="assets/img/favicon.png?v=3">
    <title>{p['title']} | Dr. Henrique Leal Rosa</title>
    <meta name="description" content="{p['excerpt']}">
    <link rel="canonical" href="https://drhenriqueleal.com.br/{p['slug']}.html">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{p['title']}">
    <meta property="og:description" content="{p['excerpt']}">
    <meta property="og:image" content="https://drhenriqueleal.com.br/{p['cover']}">
    <meta property="og:type" content="article">
    
    <!-- Schema.org Article -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "MedicalWebPage",
      "headline": "{p['title']}",
      "description": "{p['excerpt']}",
      "image": "https://drhenriqueleal.com.br/{p['cover']}",
      "datePublished": "{p['date']}",
      "author": {{
        "@type": "Person",
        "name": "Dr. Henrique Leal Rosa",
        "jobTitle": "Cirurgião Dentista & Biomédico"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Dr. Henrique Leal Rosa",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://drhenriqueleal.com.br/assets/img/logo-sub-colorida.webp"
        }}
      }}
    }}
    </script>

    <style>
        .article-header {{ padding: 160px 0 40px; background: #FAFBFD; border-bottom: 1px solid rgba(27, 58, 92, 0.06); }}
        .article-breadcrumbs {{ font-size: 0.85rem; color: #94a3b8; margin-bottom: 20px; }}
        .article-breadcrumbs a {{ color: var(--color-primary); text-decoration: none; }}
        .article-main-title {{ font-family: var(--font-heading); font-size: clamp(2rem, 4vw, 3.2rem); color: var(--color-primary); line-height: 1.2; margin-bottom: 24px; }}
        
        .article-author-badge {{ display: flex; align-items: center; gap: 16px; margin-bottom: 24px; }}
        .author-avatar {{ width: 56px; height: 56px; border-radius: 50%; object-fit: cover; border: 2px solid var(--color-primary); }}
        .author-info-name {{ font-weight: 700; color: var(--color-primary); font-size: 1.05rem; }}
        .author-info-role {{ font-size: 0.82rem; color: #64748b; }}
        
        .article-meta-row {{ display: flex; flex-wrap: wrap; align-items: center; gap: 20px; font-size: 0.88rem; color: #64748b; margin-top: 16px; padding-top: 16px; border-top: 1px solid rgba(27, 58, 92, 0.08); }}
        .article-tag {{ background: rgba(27, 58, 92, 0.06); color: var(--color-primary); font-size: 0.78rem; font-weight: 600; padding: 4px 12px; border-radius: 20px; }}
        
        .article-body-wrapper {{ max-width: 820px; margin: 50px auto 80px; padding: 0 20px; }}
        .article-featured-img-wrap {{ width: 100%; max-height: 480px; border-radius: 20px; overflow: hidden; margin-bottom: 40px; box-shadow: 0 10px 30px rgba(27, 58, 92, 0.08); }}
        .article-featured-img {{ width: 100%; height: 100%; object-fit: cover; }}
        
        .article-content {{ font-size: 1.08rem; color: #334155; line-height: 1.85; }}
        .article-content p.lead {{ font-size: 1.25rem; font-weight: 500; color: var(--color-primary); line-height: 1.7; margin-bottom: 28px; }}
        .article-content h2 {{ font-family: var(--font-heading); font-size: 1.75rem; color: var(--color-primary); margin: 38px 0 16px; line-height: 1.3; }}
        .article-content p {{ margin-bottom: 20px; }}
        .article-content ul {{ margin-bottom: 24px; padding-left: 20px; }}
        .article-content li {{ margin-bottom: 10px; }}
        
        .article-highlight-box {{ background: #F8FAFC; border-left: 4px solid #2A7DE1; border-radius: 0 16px 16px 0; padding: 24px 28px; margin: 34px 0; }}
        .article-highlight-box h4 {{ font-family: var(--font-heading); color: var(--color-primary); margin-bottom: 8px; font-size: 1.15rem; }}
        .article-highlight-box p {{ margin: 0; font-size: 0.98rem; color: #475569; }}
        
        .related-posts-section {{ background: #FAFBFD; padding: 60px 0 80px; border-top: 1px solid rgba(27, 58, 92, 0.06); }}
        .related-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 30px; }}
        .related-post-card {{ background: #FFFFFF; border-radius: 16px; border: 1px solid rgba(27, 58, 92, 0.08); overflow: hidden; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: transform 0.3s ease; }}
        .related-post-card:hover {{ transform: translateY(-4px); }}
        .related-post-img {{ width: 100%; height: 160px; object-fit: cover; }}
        .related-post-body {{ padding: 20px; display: flex; flex-direction: column; flex-grow: 1; }}
        .related-post-body h4 {{ font-family: var(--font-heading); font-size: 1.05rem; color: var(--color-primary); margin-bottom: 12px; line-height: 1.35; }}
        .related-read-more {{ font-size: 0.82rem; font-weight: 700; color: var(--color-primary); margin-top: auto; }}
        
        @media (max-width: 768px) {{
            .article-header {{ padding: 130px 0 30px; }}
            .related-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>

<body>

    <!-- ==================== HEADER ==================== -->
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
                <a href="blog.html" style="color: #ffffff; font-weight: 700;">Blog</a>
                <a href="index.html#localizacao">Consultório</a>
                <a href="index.html#faq">Dúvidas</a>
            </nav>
            <button class="menu-toggle" id="menuToggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <!-- ==================== ARTICLE HEADER ==================== -->
    <section class="article-header">
        <div class="container" style="max-width: 860px;">
            <div class="article-breadcrumbs">
                <a href="index.html">Início</a> › <a href="blog.html">Blog</a> › <span>{p['category']}</span>
            </div>
            
            <span class="post-cat-badge">{p['category']}</span>
            <h1 class="article-main-title">{p['title']}</h1>
            
            <div class="article-author-badge">
                <img src="assets/img/henrique-portrait.webp" alt="Dr. Henrique Leal Rosa" class="author-avatar">
                <div>
                    <div class="author-info-name">Dr. Henrique Leal Rosa</div>
                    <div class="author-info-role">Cirurgião Dentista (CRO-PR) & Biomédico (CRBM-PR) · Curitiba</div>
                </div>
            </div>
            
            <div class="article-meta-row">
                <span>Publicado em {format_date_pt(p['date'])}</span>
                <span>Tempo de leitura: {p['readingMinutes']} minutos</span>
                <div style="display: flex; gap: 6px; flex-wrap: wrap;">{tags_html}</div>
            </div>
        </div>
    </section>

    <!-- ==================== ARTICLE BODY ==================== -->
    <article class="article-body-wrapper">
        <div class="article-featured-img-wrap">
            <img src="{p['cover']}" alt="{p['title']}" class="article-featured-img">
        </div>
        
        <div class="article-content">
            {p['content_html']}
        </div>
        
        <!-- CTA Banner within Article -->
        <div class="blog-cta-box" style="margin-top: 50px;">
            <h3 class="blog-cta-title" style="font-size: 1.8rem;">Deseja Avaliar o Seu Caso?</h3>
            <p class="blog-cta-text">
                Agende uma consulta individualizada com o Dr. Henrique Leal no bairro Água Verde em Curitiba.
            </p>
            <a href="https://wa.me/5541988577430?text=Ol%C3%A1%2C%20li%20o%20artigo%20sobre%20{p['slug']}%20e%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o." 
               class="btn btn-primary" target="_blank" rel="noopener" style="background: #2A7DE1; color: #1B3A5C; font-weight: 700; border: none; padding: 14px 30px;">
                Agendar Avaliação no WhatsApp ↗
            </a>
        </div>
    </article>

    <!-- ==================== RELATED POSTS ==================== -->
    <section class="related-posts-section">
        <div class="container" style="max-width: 860px;">
            <h3 style="font-family: var(--font-heading); color: var(--color-primary); font-size: 1.5rem;">Artigos Relacionados</h3>
            <div class="related-grid">
                {related_html}
            </div>
        </div>
    </section>

    <!-- ==================== FOOTER ==================== -->
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
                <p>&copy; 2026 Dr. Henrique Leal Rosa. Todos os direitos reservados. CRO-PR · CRBM-PR.</p>
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js?v=5.0"></script>
</body>
</html>
"""
    with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
        f.write(article_html)

print("Generated all 20 individual article pages!")
