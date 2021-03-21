import Seq0
from Seq0 import Seq

seq_list1 = Seq0.generate_seqs("A", 3)
print(seq_list1)
seq_list2 = Seq0.generate_seqs("AC", 5)
print(seq_list2)
print("List 1:")
Seq.print_seqs(seq_list1) #Esta función está dentro de la class por eso Seq.print()
print()
print("List 2:")
Seq.print_seqs(seq_list2) #Esta función está dentro de la class por eso Seq.print()

