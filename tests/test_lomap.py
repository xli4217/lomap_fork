from lomap.classes import Fsa
import os

'''
G = Always
F = Eventually
! = not
U = Until
-> = Imply
X = Next
&& = And
|| = Or
'''


spec = "(F r1 || F r2) && F r3 && ((!r2 && !r1) U r3)"
aut = Fsa()
aut.from_formula(spec)
aut.add_trap_state()
print(len(aut.g.nodes()))
print(len(aut.g.edges()))
print(aut)
print(aut.g.nodes())
aut.visualize(draw='pydot', save_path=os.getcwd(), dot_file_name='fsa', svg_file_name='fsa')
