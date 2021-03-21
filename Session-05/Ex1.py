 # MANERA 1

"""import seq01
s1 = seq01.Seq("ACCTGC")
s2 = seq01.Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")"""

#MANERA 2

from seq01 import Seq
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")