from Seq0 import Seq

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


"""La funcion que tenemos que realizar está relacionada con la lista de secuencias,
Por tanto, ¿Crearemos la función dentro de la class? ¿En este main programm? 
¿O fuera de la class pero inside the module?

Dentro de la class si trabajamos con los attributes de la sequencia itself
Como stathic method si el ejercicio estuviera relacionado con la class itself, pero
en este caso no lo está, porque esa función sólo la vamos a usar en este ejercicio en concreto
Por tanto, lo mejor sería, sacarla fuera de la class pero dentro del module o en el main programm.
La va a hacer como staticmethod esta vez, pero NO es lo suyo"""

Seq.print_seqs(seq_list)