# manim -qh Definitions.py Sind Lind Dim

from manim import *

class Sind(Scene):
    def construct(self):
        self.add(MathTex(r"""\text{Laat }X&\text{ een reguliere ruimte en }n\text{ een niet-negatief geheel getal zijn.}
                           \\\text{(MU1) }&\text{ind }X=-1\text{ dan en slechts dan als }X=\varnothing.
                           \\\text{(MU2) }&\text{ind }X\leq n\text{ als er voor elk punt }x\in X\text{ en elke omgeving }V\text{ van het}
                                        \\&\text{punt }x\text{ een open verzameling}U\subseteq X\text{ bestaat zó dat }x\in U\subseteq V\text{ en}
                                        \\&\text{ind Fr }U\leq n-1.
                           \\\text{(MU3) }&\text{ind }X=n\text{ als ind }X\leq n\text{ en de ongelijkheid ind }X\leq n-1\text{ geldt niet.}
                           \\\text{(MU4) }&\text{ind }X=\infty\text{ als de ongelijkheid ind }X\leq n-1\text{ voor geen elke }n\text{ geldt.}""").scale(.75))

class Lind(Scene):
    def construct(self):
        self.add(MathTex(r"""\text{Laat }X&\text{ een normale ruimte en }n\text{ een niet-negatief geheel getal zijn.}
                           \\\text{(BČ1) }&\text{Ind }X=-1\text{ dan en slechts dan als }X=\varnothing.
                           \\\text{(BČ2) }&\text{Ind }X\leq n\text{ als er voor elke gesloten verzameling }A\subseteq X\text{ en elke}
                                        \\&\text{open verzameling }V\subseteq X\text{ die }A\text{ bevat een open verzameling }U\subseteq X
                                        \\&\text{bestaat zó dat }A\subseteq U\subseteq V\text{ en Ind Fr }U\leq n-1.
                           \\\text{(BČ3) }&\text{Ind }X=n\text{ als Ind }X\leq n\text{ en de ongelijkheid Ind }X\leq n-1\text{ geldt niet.}
                           \\\text{(BČ4) }&\text{Ind }X=\infty\text{ als de ongelijkheid Ind }X\leq n-1\text{ voor geen elke }n\text{ geldt.}""").scale(.75))

class Dim(Scene):
    def construct(self):
        self.add(MathTex(r"""\text{Laat }X&\text{ een Tychonoff ruimte en }n\text{ een geheel getal groter of gelijk aan }-1\text{ zijn.}
                           \\\text{(ČL1) }&\text{dim }X\leq n\text{ als elke eindige cozero-overdekking van }X\text{ een eindige}
                                        \\&\text{cozero-verfijning heeft van orde kleiner of gelijk aan }n.
                           \\\text{(BČ3) }&\text{dim }X=n\text{ als dim }X\leq n\text{ en de ongelijkheid dim }X\leq n-1\text{ geldt niet.}
                           \\\text{(BČ4) }&\text{dim }X=\infty\text{ als de ongelijkheid dim }X\leq n-1\text{ voor geen elke }n\text{ geldt.}""").scale(.75))