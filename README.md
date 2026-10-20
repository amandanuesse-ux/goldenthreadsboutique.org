# goldenthreadsboutique.org

Website for Golden Threads Boutique, a nonprofit traveling clothing boutique for seniors.

- Pages are plain HTML. Shared header/footer live in `_head.html` / `_foot.html`; page bodies in `_*.html`.
- Run `python3 _build.py` to rebuild `request.html`, `give.html`, `contact.html`, `thanks.html` (edit `index.html` directly).
- Files starting with `_` are not published (GitHub Pages / Jekyll skips them).
- Forms post to FormSubmit, which emails info@goldenthreadsboutique.org.
