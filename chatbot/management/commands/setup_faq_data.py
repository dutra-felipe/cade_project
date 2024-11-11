# chatbot/management/commands/setup_faq_data.py
from django.core.management.base import BaseCommand
from chatbot.models import FAQCategory, FAQ, SearchKeyword

class Command(BaseCommand):
    help = 'Popula o banco de dados com FAQs iniciais e palavras-chave'

    def handle(self, *args, **options):
        # Criar ou obter categorias
        cat_geral, _ = FAQCategory.objects.get_or_create(name='Geral')
        cat_pesquisa, _ = FAQCategory.objects.get_or_create(name='Pesquisa')
        cat_processos, _ = FAQCategory.objects.get_or_create(name='Processos')
        
        # FAQs em Português
        faqs_pt = [
            # Categoria Geral
            {
                'question': 'O que é o CADE?',
                'answer': 'O CADE (Conselho Administrativo de Defesa Econômica) é uma autarquia federal brasileira responsável por defender a livre concorrência no mercado. Sua missão é prevenir e reprimir infrações contra a ordem econômica.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 1
            },
            {
                'question': 'Como entrar em contato com o CADE?',
                'answer': 'Você pode entrar em contato com o CADE através do formulário de contato em nosso site, pelo telefone (61) XXXX-XXXX ou pelo e-mail contato@cade.gov.br.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 2
            },
            {
                'question': 'Qual a estrutura organizacional do CADE?',
                'answer': 'O CADE é composto pelo Tribunal Administrativo, Superintendência-Geral e Departamento de Estudos Econômicos. O Tribunal é formado por um presidente e seis conselheiros.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 3
            },
            
            # Categoria Pesquisa
            {
                'question': 'Como pesquisar processos?',
                'answer': 'Para pesquisar processos, use a barra de busca no topo da página. Você pode filtrar por número do processo, partes envolvidas, data, tipo de processo e relator.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 4
            },
            {
                'question': 'Como encontrar jurisprudência específica?',
                'answer': 'Para encontrar jurisprudência específica, utilize a seção de pesquisa avançada, onde você pode filtrar por tema, data, tipo de decisão e palavras-chave. Os resultados podem ser ordenados por relevância ou data.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 5
            },
            {
                'question': 'Como fazer download de documentos?',
                'answer': 'Para fazer download de documentos, primeiro localize o processo desejado. Em seguida, clique no ícone de download ao lado do documento. Documentos públicos estão disponíveis para download imediato.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 6
            },
            
            # Categoria Processos
            {
                'question': 'O que é um Ato de Concentração?',
                'answer': 'Ato de Concentração é uma operação que envolve a fusão, aquisição ou união de duas ou mais empresas. Quando atinge certos critérios estabelecidos em lei, precisa ser submetido à análise prévia do CADE.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 7
            },
            {
                'question': 'O que é um Processo Administrativo?',
                'answer': 'O Processo Administrativo é um procedimento que investiga possíveis infrações à ordem econômica, como formação de cartel, práticas anticompetitivas, entre outras condutas.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 8
            },
            {
                'question': 'Quais são os prazos processuais?',
                'answer': 'Os prazos variam conforme o tipo de processo. Atos de Concentração têm prazo legal de 240 dias, prorrogáveis por até 90 dias. Para recursos e manifestações em processos administrativos, o prazo comum é de 30 dias.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 9
            },
            {
                'question': 'Como protocolar documentos?',
                'answer': 'Documentos podem ser protocolados eletronicamente através do Sistema SEI. É necessário ter cadastro prévio e certificado digital. Em casos excepcionais, o protocolo físico pode ser realizado na sede do CADE.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 10
            },
            {
                'question': 'Como solicitar vista dos autos?',
                'answer': 'A vista dos autos pode ser solicitada por partes e advogados habilitados através do Sistema SEI. Para processos públicos, a consulta é livre. Processos restritos requerem habilitação prévia.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 11
            },
            {
                'question': 'Como apresentar uma denúncia ao CADE?',
                'answer': 'Denúncias podem ser apresentadas através do formulário eletrônico disponível no site, por e-mail ou presencialmente. É importante incluir o máximo de informações e evidências possíveis.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 12
            }
        ]

        # FAQs em Inglês
        faqs_en = [
            # General Category (already provided above)
            {
                'question': 'What is CADE?',
                'answer': 'CADE (Administrative Council for Economic Defense) is a Brazilian federal autarchy responsible for protecting free competition in the market. Its mission is to prevent and suppress violations against the economic order.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 1
            },
            {
                'question': 'How to contact CADE?',
                'answer': 'You can contact CADE through the contact form on our website, by phone at (61) XXXX-XXXX, or by email at contact@cade.gov.br.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 2
            },
            {
                'question': 'What is CADE\'s organizational structure?',
                'answer': 'CADE consists of the Administrative Tribunal, General Superintendence, and Department of Economic Studies. The Tribunal is composed of a president and six commissioners.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 3
            },
            
            # Search Category
            {
                'question': 'How to search for cases?',
                'answer': 'To search for cases, use the search bar at the top of the page. You can filter by case number, involved parties, date, case type, and rapporteur. The system accepts operators like AND and OR for more precise searches.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 4
            },
            {
                'question': 'How to find specific jurisprudence?',
                'answer': 'To find specific jurisprudence, use the advanced search section where you can filter by topic, date, decision type, and keywords. Results can be sorted by relevance or date.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 5
            },
            {
                'question': 'How to download documents?',
                'answer': 'To download documents, first locate the desired case. Then click the download icon next to the document. Public documents are available for immediate download.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 6
            },
            
            # Processes Category
            {
                'question': 'What is a Merger Review?',
                'answer': 'A Merger Review is an operation involving the merger, acquisition, or union of two or more companies. When it meets certain criteria established by law, it must be submitted for CADE\'s prior analysis.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 7
            },
            {
                'question': 'What is an Administrative Proceeding?',
                'answer': 'An Administrative Proceeding is a procedure that investigates possible violations of the economic order, such as cartel formation, anticompetitive practices, and other conducts.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 8
            },
            {
                'question': 'What are the procedural deadlines?',
                'answer': 'Deadlines vary according to the type of process. Merger Reviews have a legal deadline of 240 days, extendable for up to 90 days. For appeals and manifestations in administrative proceedings, the common deadline is 30 days.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 9
            },
            {
                'question': 'How to file documents?',
                'answer': 'Documents can be filed electronically through the SEI System. Prior registration and digital certificate are required. In exceptional cases, physical filing can be done at CADE\'s headquarters.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 10
            },
            {
                'question': 'How to request access to case files?',
                'answer': 'Access to case files can be requested by qualified parties and lawyers through the SEI System. For public cases, consultation is free. Restricted cases require prior qualification.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 11
            },
            {
                'question': 'How to file a complaint with CADE?',
                'answer': 'Complaints can be submitted through the electronic form available on the website, by email, or in person. It is important to include as much information and evidence as possible.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 12
            }
        ]

        # FAQs em Espanhol
        faqs_es = [
            # Categoría General (already provided above)
            {
                'question': '¿Qué es CADE?',
                'answer': 'CADE (Consejo Administrativo de Defensa Económica) es una autarquía federal brasileña responsable de proteger la libre competencia en el mercado. Su misión es prevenir y reprimir las violaciones contra el orden económico.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 1
            },
            {
                'question': '¿Cómo contactar a CADE?',
                'answer': 'Puede contactar a CADE a través del formulario de contacto en nuestro sitio web, por teléfono al (61) XXXX-XXXX o por correo electrónico a contacto@cade.gov.br.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 2
            },
            {
                'question': '¿Cuál es la estructura organizativa de CADE?',
                'answer': 'CADE está compuesto por el Tribunal Administrativo, la Superintendencia General y el Departamento de Estudios Económicos. El Tribunal está formado por un presidente y seis consejeros.',
                'category': cat_geral,
                'is_predefined': True,
                'order': 3
            },
            
            # Categoría de Búsqueda
            {
                'question': '¿Cómo buscar procesos?',
                'answer': 'Para buscar procesos, utilice la barra de búsqueda en la parte superior de la página. Puede filtrar por número de proceso, partes involucradas, fecha, tipo de proceso y relator. El sistema acepta operadores como AND y OR para búsquedas más precisas.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 4
            },
            {
                'question': '¿Cómo encontrar jurisprudencia específica?',
                'answer': 'Para encontrar jurisprudencia específica, utilice la sección de búsqueda avanzada, donde puede filtrar por tema, fecha, tipo de decisión y palabras clave. Los resultados se pueden ordenar por relevancia o fecha.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 5
            },
            {
                'question': '¿Cómo descargar documentos?',
                'answer': 'Para descargar documentos, primero localice el proceso deseado. Luego haga clic en el icono de descarga junto al documento. Los documentos públicos están disponibles para descarga inmediata.',
                'category': cat_pesquisa,
                'is_predefined': True,
                'order': 6
            },
            
            # Categoría de Procesos
            {
                'question': '¿Qué es un Acto de Concentración?',
                'answer': 'Un Acto de Concentración es una operación que involucra la fusión, adquisición o unión de dos o más empresas. Cuando alcanza ciertos criterios establecidos por ley, debe ser sometido al análisis previo de CADE.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 7
            },
            {
                'question': '¿Qué es un Proceso Administrativo?',
                'answer': 'Un Proceso Administrativo es un procedimiento que investiga posibles infracciones al orden económico, como formación de cárteles, prácticas anticompetitivas y otras conductas.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 8
            },
            {
                'question': '¿Cuáles son los plazos procesales?',
                'answer': 'Los plazos varían según el tipo de proceso. Los Actos de Concentración tienen un plazo legal de 240 días, prorrogable hasta 90 días. Para recursos y manifestaciones en procesos administrativos, el plazo común es de 30 días.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 9
            },
            {
                'question': '¿Cómo presentar documentos?',
                'answer': 'Los documentos se pueden presentar electrónicamente a través del Sistema SEI. Se requiere registro previo y certificado digital. En casos excepcionales, la presentación física se puede realizar en la sede de CADE.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 10
            },
            {
                'question': '¿Cómo solicitar vista de los autos?',
                'answer': 'La vista de los autos puede ser solicitada por partes y abogados habilitados a través del Sistema SEI. Para procesos públicos, la consulta es libre. Los procesos restringidos requieren habilitación previa.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 11
            },
            {
                'question': '¿Cómo presentar una denuncia ante CADE?',
                'answer': 'Las denuncias se pueden presentar a través del formulario electrónico disponible en el sitio web, por correo electrónico o presencialmente. Es importante incluir la mayor cantidad de información y evidencia posible.',
                'category': cat_processos,
                'is_predefined': True,
                'order': 12
            }
        ]
        # Criar FAQs
        for faq_data in faqs_pt + faqs_en + faqs_es:
            FAQ.objects.get_or_create(
                category=faq_data['category'],
                question=faq_data['question'],
                answer=faq_data['answer'],
                language='pt' if faq_data in faqs_pt else 'en' if faq_data in faqs_en else 'es',
                is_predefined=faq_data.get('is_predefined', False),
                order=faq_data.get('order', 0)
            )

       # Palavras-chave para busca
        keywords_data = {
            'pt': [
                ('cade', 'cade'),
                ('processo', 'processo'),
                ('pesquisar', 'pesquisar'),
                ('contato', 'contato'),
                ('jurisprudência', 'jurisprudencia'),
                ('ato de concentração', 'ato concentracao'),
                ('processo administrativo', 'processo administrativo'),
                ('denúncia', 'denuncia'),
                ('protocolo', 'protocolo'),
                ('vista', 'vista'),
                ('prazo', 'prazo'),
                ('sei', 'sei'),
                ('tribunal', 'tribunal'),
                ('superintendência', 'superintendencia'),
                ('conselheiro', 'conselheiro')
            ],
            'en': [
                ('cade', 'cade'),
                ('case', 'case'),
                ('search', 'search'),
                ('contact', 'contact'),
                ('jurisprudence', 'jurisprudence'),
                ('merger', 'merger'),
                ('administrative process', 'administrative process'),
                ('complaint', 'complaint'),
                ('protocol', 'protocol'),
                ('access', 'access'),
                ('deadline', 'deadline'),
                ('sei', 'sei'),
                ('tribunal', 'tribunal'),
                ('superintendence', 'superintendence'),
                ('commissioner', 'commissioner')
            ],
            'es': [
                ('cade', 'cade'),
                ('proceso', 'proceso'),
                ('buscar', 'buscar'),
                ('contacto', 'contacto'),
                ('jurisprudencia', 'jurisprudencia'),
                ('fusión', 'fusion'),
                ('proceso administrativo', 'proceso administrativo'),
                ('denuncia', 'denuncia'),
                ('protocolo', 'protocolo'),
                ('vista', 'vista'),
                ('plazo', 'plazo'),
                ('sei', 'sei'),
                ('tribunal', 'tribunal'),
                ('superintendencia', 'superintendencia'),
                ('consejero', 'consejero')
            ]
        }

        # Criar palavras-chave
        for language, keywords in keywords_data.items():
            for keyword, normalized in keywords:
                SearchKeyword.objects.get_or_create(
                    keyword=keyword,
                    normalized_term=normalized,
                    language=language
                )

        self.stdout.write(
            self.style.SUCCESS('FAQs e palavras-chave criadas com sucesso!')
        )