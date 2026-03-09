import os

base_dir = "/Users/alejandrobou/Desktop/LUIS WEB/valencia_students_rooms_final_v7"

up_arrow_html = """
    <!-- Scroll Up Arrow -->
    <div class="scroll-arrow-up" id="scrollArrowUp" onclick="scrollToPrev()" style="display: none;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M12 8l6 6H6z" />
        </svg>
    </div>
"""

up_arrow_css = """
        .scroll-arrow-up {
            position: fixed;
            bottom: 7rem;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            width: 50px;
            height: 50px;
            background: var(--accent);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(255, 102, 0, 0.3);
            transition: all 0.3s ease;
        }

        .scroll-arrow-up:hover {
            transform: translateX(-50%) scale(1.1);
            box-shadow: 0 6px 30px rgba(255, 102, 0, 0.5);
        }

        .scroll-arrow-up svg {
            width: 24px;
            height: 24px;
            fill: white;
        }
"""

js_replace_1 = """        window.addEventListener('scroll', () => {
            const scrollArrow = document.getElementById('scrollArrow');
            const scrollPosition = window.scrollY + window.innerHeight;
            const documentHeight = document.documentElement.scrollHeight;
            scrollArrow.style.display = scrollPosition >= documentHeight - 100 ? 'none' : 'flex';
        });"""

js_replace_2 = """        window.addEventListener('scroll', () => {
            const scrollArrow = document.getElementById('scrollArrow');
            const scrollArrowUp = document.getElementById('scrollArrowUp');
            const scrollPosition = window.scrollY + window.innerHeight;
            const documentHeight = document.documentElement.scrollHeight;
            if(scrollArrow) scrollArrow.style.display = scrollPosition >= documentHeight - 100 ? 'none' : 'flex';
            if(scrollArrowUp) scrollArrowUp.style.display = window.scrollY > 300 ? 'flex' : 'none';
        });"""

js_func_prev = """        function scrollToPrev() {
            const sections = document.querySelectorAll('.section, section');
            // Encuentra la sección anterior a la actual
            let target = null;
            for (let i = sections.length - 1; i >= 0; i--) {
                if (sections[i].offsetTop < window.scrollY - 100) {
                    target = sections[i];
                    break;
                }
            }
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            } else {
                window.scrollTo({top: 0, behavior: 'smooth'});
            }
        }

        function scrollToNext() {"""

for file in os.listdir(base_dir):
    if not file.endswith('.html'):
        continue
    filepath = os.path.join(base_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Eliminar la rotación de 180 grados para que TODOS apunten hacia abajo
    content = content.replace(' transform="rotate(180 12 12)"', '')

    # 2. En habitaciones.html, añadir el botón de subida
    if file == 'habitaciones.html':
        if 'id="scrollArrowUp"' not in content:
            # HTML
            content = content.replace('<!-- Scroll Down Arrow -->', up_arrow_html + '\n    <!-- Scroll Down Arrow -->')
            # CSS
            content = content.replace('</style>', up_arrow_css + '\n    </style>')
            # Listener
            content = content.replace(js_replace_1, js_replace_2)
            # Function
            content = content.replace('function scrollToNext() {', js_func_prev)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Actualización completada en todos los archivos HTML.")
