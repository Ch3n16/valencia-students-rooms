# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static HTML/CSS/JavaScript marketing website for student housing rentals in Valencia, Spain. **No build system, no framework, no package.json.** Files are served directly as static HTML.

## Development Commands

```bash
# Serve locally (any of these work)
python3 -m http.server 8000
npx serve .
open index.html   # direct browser open (some features may differ)
```

No build, lint, or test commands exist — this is a zero-toolchain project.

## Architecture

### File Layout
- **8 HTML pages** — each is a standalone page (index, habitaciones, ubicacion, zonas-comunes, contacto, faqs, vivir-valencia, verano)
- **`styles.css`** — single monolithic stylesheet for all pages
- **`script.js`** — all JavaScript shared across pages

### Internationalization System
- Dual-language (ES/EN) via a client-side translation object in `script.js` (lines 1–294)
- Language persisted in `localStorage`
- HTML elements use `id` attributes that map to translation keys (kebab-case IDs → camelCase JS keys, e.g. `id="hero-title"` → `heroTitle`)
- `changeLanguage()` function (line 448+) applies translations by selecting DOM elements by ID

### CSS Design System
CSS custom properties defined at the top of `styles.css`:
- Brand accent: `--accent: #FF6600` (Valencia orange)
- Fonts: `Space Grotesk` (headings), `Inter` (body)
- Border radius: `24px` primary, `12px` secondary
- Responsive breakpoint: `1024px`

### Interactive Features in `script.js`
- **CAPTCHA** — visual emoji grid (3×3) verification before form submission
- **Mobile nav** — hamburger menu toggle
- **Language toggle** — switches all translatable elements
- **Room gallery** — modal with thumbnails on `habitaciones.html`
- **WhatsApp float button** — IIFE al final de `script.js`; se posiciona dinámicamente bajo el navbar; en `contacto.html` usa `IntersectionObserver` para animar el botón hasta el número de teléfono (`id="wa-phone-wrapper"`) cuando entra en viewport

## Key Conventions

- All pages share `styles.css` and `script.js` via relative paths
- The navigation dropdown for "Ubicación" uses a CSS hover + JS click pattern defined in `styles.css` lines 243–310
- Images are PNG/JPEG at high resolution; no lazy loading is implemented
- The `fix_arrows.py` script is a one-off development utility, not part of the site
- `faqs.html` carga Bootstrap 5 CDN (CSS en `<head>`, JS bundle antes de `</body>`); el resto de páginas no usan Bootstrap
- Los overrides Bootstrap (acordeón con tema naranja) están al final de `styles.css`
- El botón WhatsApp (`#wa-float-btn`, clase `.wa-float-btn`) está presente en los 8 HTML; el número de destino es `wa.me/34000000000` (placeholder)
