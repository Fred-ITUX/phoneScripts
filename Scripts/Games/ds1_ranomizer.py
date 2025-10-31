import random

#### Starter class: Deprived
#### Level max 100
#### No boss soul weapons, boss weapon drops are permitted (moonlight, dragon...)

#################################################3

phase1 = ["Moonlight Butterfly", "Pinwheel", "Taurus Demon", "Quelaag", "Bell Gargoyles"]
phase2 = ["Iron Golem", "Ceaseless Discharge"]

phase_Locked_first = "Ornstein and Smough"

phase3 = ["Four Kings", "Seath", "Bed of Chaos", "Nito", "Kalameet", "Artorias" ]

phase_Locked_last = "Manus, Gwyn"

for i in range(0, 5):
    
    random.shuffle(phase1)
    random.shuffle(phase2)
    random.shuffle(phase3)

print(f'''• Phase 1:\n {", ".join(phase1)}
\n• Phase 2:\n {", ".join(phase2)}
\n• Phase locked: {phase_Locked_first}
\n• Phase 3:\n {", ".join(phase3)}
\n• Phase locked: {phase_Locked_last}
''')