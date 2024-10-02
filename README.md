# ColloquiumSlides
In deze repository staat de sourcecode van de slides die met gebruik van Manim worden gemaakt voor de presentaties voor het vak AM3000 Bachelorcolloquium door Sander Dietz, 2023/2024 Q3.

# Manim environment
Installeer het anaconda environment met `conda env create -f environment.yml`, dit kan even duren. Voor meer informatie over het gebruik van Manim, ga naar [Manim Documentation](https://docs.manim.community/en/stable/) of [Manim Quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html).

# LaTeX
Zorg ervoor dat je $\LaTeX$ hebt geïnstalleerd. Voor windows wordt [MikTeX](https://miktex.org/download) aanbevolen door Manim.

# Render slides
Om snel een enkele slide te renderen, gebruik `manim -pql Script.py SceneX`. Om alle slides in één keer op hoge kwaliteit te renderen, gebruik `manim -qh Script.py Scene1 Scene2 ... SceneN`.
