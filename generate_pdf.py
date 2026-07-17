import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

# Colors based on the custom palette
COLOR_PRIMARY = colors.HexColor('#2d8259')     # Forest Green
COLOR_SECONDARY = colors.HexColor('#d97706')   # Amber Gold
COLOR_DARK = colors.HexColor('#1f2937')        # Deep Charcoal
COLOR_LIGHT = colors.HexColor('#4b5563')       # Medium Grey
COLOR_MUTED = colors.HexColor('#9ca3af')       # Light Grey
COLOR_BG_SIDEBAR = colors.HexColor('#f8fafc')  # Very light grey

def build_pdf(filename, lang='es'):
    # Create document
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=0.4 * inch,
        rightMargin=0.4 * inch,
        topMargin=0.4 * inch,
        bottomMargin=0.4 * inch
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    style_name = ParagraphStyle(
        'CVName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=COLOR_DARK
    )
    
    style_title = ParagraphStyle(
        'CVTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=COLOR_PRIMARY,
        spaceAfter=12
    )
    
    style_h1 = ParagraphStyle(
        'CVH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=COLOR_DARK,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )
    
    style_body = ParagraphStyle(
        'CVBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=COLOR_LIGHT,
        spaceAfter=8
    )
    
    style_job_title = ParagraphStyle(
        'CVJobTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=COLOR_DARK
    )
    
    style_job_meta = ParagraphStyle(
        'CVJobMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=COLOR_PRIMARY
    )
    
    style_job_date = ParagraphStyle(
        'CVJobDate',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        textColor=COLOR_LIGHT
    )
    
    style_bullet = ParagraphStyle(
        'CVBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=COLOR_LIGHT,
        leftIndent=10,
        firstLineIndent=-8,
        spaceAfter=3
    )
    
    style_tech = ParagraphStyle(
        'CVTech',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=COLOR_LIGHT,
        spaceAfter=8
    )
    
    style_sidebar_label = ParagraphStyle(
        'CVSidebarLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=COLOR_DARK
    )
    
    style_sidebar_val = ParagraphStyle(
        'CVSidebarVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=COLOR_LIGHT,
        spaceAfter=6
    )

    story = []
    
    # -------------------------------------------------------------------------
    # HEADER (Full Width)
    # -------------------------------------------------------------------------
    header_data = [
        [
            Paragraph("Adriel Avila", style_name),
            Paragraph(
                "<b>Web CV:</b> <font color='#2d8259'><u>thexpert507.github.io/cv</u></font>" if lang == 'es' else "<b>Web CV:</b> <font color='#2d8259'><u>thexpert507.github.io/cv</u></font>",
                ParagraphStyle('CVWebLink', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=11, alignment=2, textColor=COLOR_LIGHT)
            )
        ],
        [
            Paragraph("Desarrollador Fullstack Senior" if lang == 'es' else "Senior Fullstack Developer", style_title),
            Paragraph(
                "adrielarnel00@gmail.com | +507 64970936",
                ParagraphStyle('CVContactTop', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, alignment=2, textColor=COLOR_LIGHT)
            )
        ]
    ]
    
    header_table = Table(header_data, colWidths=[4.2 * inch, 3.5 * inch])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_PRIMARY, spaceAfter=8, spaceBefore=4))
    
    # -------------------------------------------------------------------------
    # COLUMNS LAYOUT
    # -------------------------------------------------------------------------
    left_flowables = []
    right_flowables = []
    
    # --- LEFT COLUMN: ABOUT & EXPERIENCE ---
    # About
    about_title = "Sobre Mí" if lang == 'es' else "About Me"
    left_flowables.append(Paragraph(about_title.upper(), style_h1))
    left_flowables.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_MUTED, spaceAfter=6, spaceBefore=2))
    
    about_text = (
        "Desarrollador Fullstack Senior autodidacta con más de 8 años de experiencia práctica en el diseño, "
        "construcción y mantenimiento de aplicaciones web robustas en producción. Especializado en TypeScript, "
        "architecturas backend escalables e integraciones reales de IA y Web3. Enfocado en aportar criterio técnico "
        "autónomo, ownership y calidad de código en entornos remotos."
        if lang == 'es' else
        "Self-taught Senior Fullstack Developer with 8+ years of hands-on experience designing, building, "
        "and maintaining robust web applications in production. Specialized in TypeScript, scalable backend "
        "architectures, and real-world AI & Web3 integrations. Focused on delivering technical autonomy, "
        "high code quality, and strong ownership in remote environments."
    )
    left_flowables.append(Paragraph(about_text, style_body))
    
    # Experience
    exp_title = "Experiencia Laboral" if lang == 'es' else "Work Experience"
    left_flowables.append(Paragraph(exp_title.upper(), style_h1))
    left_flowables.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_MUTED, spaceAfter=8, spaceBefore=2))
    
    # Jobs data
    jobs = [
        {
            'title': 'Desarrollador Fullstack Senior' if lang == 'es' else 'Senior Fullstack Developer',
            'company': 'Alfa - Trustful Technology for Tomorrow',
            'date': 'Mar. 2022 - Presente' if lang == 'es' else 'Mar. 2022 - Present',
            'bullets': [
                "Desarrollo integral (backend, frontend e infraestructura) de <b>Talent AI</b>, la plataforma SaaS B2B de reclutamiento impulsada por inteligencia artificial.",
                "Integración de modelos de lenguaje (LLMs) y flujos de IA para la automatización y procesamiento inteligente en la selección de candidatos.",
                "Desarrollo de servicios backend altamente concurrentes con Node.js, NestJS y PostgreSQL, integrando caché con Redis.",
                "Implementación de interfaces de usuario dinámicas y adaptables utilizando React y TypeScript.",
                "Creación de integraciones Web3 para proyectos fintech y de inversiones, facilitando la conexión con contratos inteligentes y wallets.",
                "Aplicación de programación funcional en TypeScript para crear librerías internas que estandarizan el manejo de errores."
            ] if lang == 'es' else [
                "Full-stack development (backend, frontend, and infrastructure) of <b>Talent AI</b>, the company's core AI-powered B2B recruiting SaaS platform.",
                "Integrated large language models (LLMs) and AI workflows to automate and streamline applicant screening processes.",
                "Developed highly concurrent backend services using Node.js, NestJS, and PostgreSQL, utilizing Redis caching.",
                "Implemented dynamic and responsive user interfaces using React and TypeScript.",
                "Created Web3 integrations for fintech and investment projects, enabling smart contract and wallet connectivity.",
                "Applied functional programming principles in TypeScript to standardize error handling in internal libraries."
            ],
            'tech': 'TypeScript, Node.js, NestJS, React, PostgreSQL, Redis, Docker, Web3.js'
        },
        {
            'title': 'Desarrollador Fullstack (Contractor Independiente)' if lang == 'es' else 'Fullstack Developer (Independent Contractor)',
            'company': 'Profesional Independiente' if lang == 'es' else 'Independent Contractor',
            'date': 'Ago. 2021 - Ene. 2026' if lang == 'es' else 'Aug. 2021 - Jan. 2026',
            'bullets': [
                "Diseño y desarrollo a medida de soluciones web completas (Frontend y Backend) para diversos clientes.",
                "Implementación de plataformas de comercio electrónico y sistemas de gestión de contenidos (CMS) adaptables.",
                "Gestión directa del ciclo de vida del proyecto: desde requerimientos hasta el despliegue final en producción."
            ] if lang == 'es' else [
                "Designed and developed tailor-made full-stack web solutions for multiple clients.",
                "Implemented responsive e-commerce platforms and content management systems (CMS).",
                "Managed the full project life cycle from initial client requirements to final production deployment."
            ],
            'tech': 'React, Node.js, TypeScript, E-commerce, CMS, CSS Grid/Flexbox'
        },
        {
            'title': 'Desarrollador Web' if lang == 'es' else 'Web Developer',
            'company': 'Tecnitech Solutions',
            'date': 'Ene. 2018 - Ene. 2022' if lang == 'es' else 'Jan. 2018 - Jan. 2022',
            'bullets': [
                "Construcción y mantenimiento de aplicaciones web interactivas.",
                "Desarrollo de interfaces dinámicas utilizando AngularJS y JavaScript (ES6+).",
                "Diseño y optimización de esquemas de bases de datos relacionales.",
                "Aseguramiento del diseño responsivo y la compatibilidad entre navegadores."
            ] if lang == 'es' else [
                "Built and maintained robust, interactive web applications.",
                "Developed dynamic user interfaces using AngularJS and JavaScript (ES6+).",
                "Designed and optimized relational database schemas.",
                "Ensured responsive layouts and cross-browser compatibility across modern browsers."
            ],
            'tech': 'AngularJS, JavaScript, HTML5/CSS3, Relational Databases'
        },
        {
            'title': 'Desarrollador Fullstack' if lang == 'es' else 'Fullstack Developer',
            'company': 'Dilio',
            'date': 'Jul. 2021 - Sept. 2021' if lang == 'es' else 'Jul. 2021 - Sep. 2021',
            'bullets': [
                "Desarrollo de nuevas funcionalidades frontend utilizando React y TypeScript.",
                "Integración y consulta de datos analíticos masivos con Google BigQuery y Firebase."
            ] if lang == 'es' else [
                "Developed new frontend features for web applications using React and TypeScript.",
                "Integrated and queried large analytical datasets using Google BigQuery and Firebase."
            ],
            'tech': 'React, TypeScript, Google BigQuery, Firebase'
        }
    ]
    
    for job in jobs:
        left_flowables.append(Paragraph(job['title'], style_job_title))
        
        # Job Meta (Company & Date side-by-side)
        meta_table = Table(
            [[Paragraph(job['company'], style_job_meta), Paragraph(job['date'], style_job_date)]],
            colWidths=[3.0 * inch, 1.8 * inch]
        )
        meta_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('TOPPADDING', (0,0), (-1,-1), 1),
        ]))
        left_flowables.append(meta_table)
        
        for bullet in job['bullets']:
            left_flowables.append(Paragraph(f"&bull; {bullet}", style_bullet))
        
        left_flowables.append(Spacer(1, 2))
        tech_label = "<b>Tecnologías:</b>" if lang == 'es' else "<b>Tech:</b>"
        left_flowables.append(Paragraph(f"{tech_label} {job['tech']}", style_tech))
        left_flowables.append(Spacer(1, 3))

    # --- RIGHT COLUMN: CONTACT, SKILLS, EDUCATION ---
    # Profile Image
    if os.path.exists('profile.jpeg'):
        from reportlab.platypus import Image
        # Using 1.3 inches for a perfect circular-like ratio or square
        img = Image('profile.jpeg', width=1.3 * inch, height=1.3 * inch)
        img_table = Table([[img]], colWidths=[2.3 * inch])
        img_table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 12),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ]))
        right_flowables.append(img_table)

    # Contact Title
    contact_title = "Contacto" if lang == 'es' else "Contact"
    right_flowables.append(Paragraph(contact_title.upper(), style_h1))
    right_flowables.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_MUTED, spaceAfter=8, spaceBefore=2))
    
    contacts = [
        ("Email", "adrielarnel00@gmail.com"),
        ("Teléfono" if lang == 'es' else "Phone", "+507 64970936"),
        ("GitHub", "github.com/thexpert507"),
        ("LinkedIn", "linkedin.com/in/adriel-avila"),
        ("Web CV", "thexpert507.github.io/cv"),
        ("Ubicación" if lang == 'es' else "Location", "Panamá (Remoto)" if lang == 'es' else "Panama (Remote)")
    ]
    for label, val in contacts:
        right_flowables.append(Paragraph(label, style_sidebar_label))
        right_flowables.append(Paragraph(val, style_sidebar_val))
        
    # Skills Title
    skills_title = "Aptitudes" if lang == 'es' else "Skills"
    right_flowables.append(Paragraph(skills_title.upper(), style_h1))
    right_flowables.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_MUTED, spaceAfter=8, spaceBefore=2))
    
    skills = [
        ("Backend", "Node.js, NestJS, PostgreSQL, Redis, Arquitectura de Software" if lang == 'es' else "Node.js, NestJS, PostgreSQL, Redis, Software Architecture"),
        ("Frontend & Design", "TypeScript, React.js, AngularJS, JavaScript, HTML5/CSS3, Diseño Adaptable" if lang == 'es' else "TypeScript, React.js, AngularJS, JavaScript, HTML5/CSS3, Responsive Design"),
        ("Web3 & Cloud", "web3.js, Docker, Google BigQuery, Firebase"),
        ("Enfoques" if lang == 'es' else "Focus", "Prog. Funcional, POO, E-commerce, CMS" if lang == 'es' else "Functional Prog., OOP, E-commerce, CMS")
    ]
    for cat, items in skills:
        right_flowables.append(Paragraph(cat, style_sidebar_label))
        right_flowables.append(Paragraph(items, style_sidebar_val))

    # Education Title
    edu_title = "Educación" if lang == 'es' else "Education"
    right_flowables.append(Paragraph(edu_title.upper(), style_h1))
    right_flowables.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_MUTED, spaceAfter=8, spaceBefore=2))
    
    edu_headline = "Autodidacta e Independiente" if lang == 'es' else "Self-Taught & Continuous Learning"
    edu_body = (
        "Enfoque continuo en desarrollo de software, arquitectura de sistemas y nuevas tecnologías a través de la práctica."
        if lang == 'es' else
        "Continuous focus on software development, systems architecture, and emerging technologies through practice."
    )
    right_flowables.append(Paragraph(edu_headline, style_sidebar_label))
    right_flowables.append(Paragraph(edu_body, style_sidebar_val))

    # Languages Title
    lang_title = "Idiomas" if lang == 'es' else "Languages"
    right_flowables.append(Paragraph(lang_title.upper(), style_h1))
    right_flowables.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_MUTED, spaceAfter=8, spaceBefore=2))
    
    right_flowables.append(Paragraph("Inglés" if lang == 'es' else "English", style_sidebar_label))
    right_flowables.append(Paragraph(
        "Técnico / Intermedio (Lectura y comunicación escrita fluida)" if lang == 'es' else "Professional Working Proficiency (Fluent in written & technical communication)", 
        style_sidebar_val
    ))
    
    right_flowables.append(Paragraph("Español" if lang == 'es' else "Spanish", style_sidebar_label))
    right_flowables.append(Paragraph("Nativo" if lang == 'es' else "Native speaker", style_sidebar_val))

    # --- MASTER TABLE ---
    # Constructing a table to put left and right side-by-side with a nice divider
    # Left column width: 4.8 inches, right column width: 2.7 inches
    # Spacing between columns: 0.2 inches
    master_data = [[left_flowables, "", right_flowables]]
    
    master_table = Table(
        master_data,
        colWidths=[4.8 * inch, 0.2 * inch, 2.7 * inch]
    )
    
    master_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        # Light grey background for the sidebar (right cell)
        ('BACKGROUND', (2,0), (2,0), COLOR_BG_SIDEBAR),
        ('LEFTPADDING', (2,0), (2,0), 12),
        ('RIGHTPADDING', (2,0), (2,0), 12),
        ('TOPPADDING', (2,0), (2,0), 10),
        ('BOTTOMPADDING', (2,0), (2,0), 10),
        # Right border for the sidebar as a neat divider
        ('LINEBEFORE', (2,0), (2,0), 1, COLOR_MUTED),
    ]))
    
    story.append(master_table)
    
    # Build Document
    doc.build(story)

if __name__ == '__main__':
    print("Generando PDFs...")
    build_pdf("cv_es.pdf", lang='es')
    build_pdf("cv_en.pdf", lang='en')
    print("PDFs generados con éxito: cv_es.pdf y cv_en.pdf")
