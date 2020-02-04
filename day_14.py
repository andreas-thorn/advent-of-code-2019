from collections import defaultdict
from math import ceil, floor

data_input = """1 FVBHS, 29 HWPND => 4 CPXDX
5 TNWDG, 69 VZMS, 1 GXSD, 48 NCLZ, 3 RSRZ, 15 HWPND, 25 SGPK, 2 SVCQ => 1 FUEL
1 PQRLB, 1 TWPMQ => 4 QBXC
9 QBXC => 7 RNHQ
12 VZMS => 6 MGQRZ
6 QBVG, 10 XJWX => 6 BWLZ
4 MVGN => 6 BHZH
2 LKTWD => 7 FVBHS
2 BWFK => 7 TFPQ
15 VZBJ, 9 TSVN, 2 BWLZ => 2 TNWDG
10 KVFL, 2 BWLZ, 1 VGSBF => 4 KBFJV
12 TXCR, 2 JMBG => 4 DCFD
5 VMDT, 6 JKPFT, 3 RJKJD => 7 LGWM
1 LDFGW => 2 DHRBP
129 ORE => 8 LDFGW
9 DNVRJ => 8 BMNGX
7 NLPB => 6 NCLZ
1 VMDT, 6 DCFD => 9 SGRXC
1 LDFGW, 2 VRHFB => 8 QHGQC
10 VGSBF, 5 WVMG, 6 BWLZ => 3 BWFK
4 KVFL, 1 TSVN => 6 SVCQ
2 VZBJ, 3 SWJZ => 3 QZLC
5 JMBG, 1 PQRLB => 3 CJLH
13 LKTWD, 6 TFPQ => 3 WVRXR
20 QHGQC, 10 NSPVD => 5 VGSBF
5 TFPQ, 1 DHRBP, 2 KVFL => 8 NLPB
2 KBFJV, 1 CJLH, 20 RNHQ, 1 BWLZ, 13 MNBK, 1 BHZH, 1 PKRJF => 8 RSRZ
154 ORE => 2 VRHFB
2 NHRCK => 7 DNVRJ
2 VRHFB, 4 XJWX => 4 NHRCK
1 TFPQ, 12 JMBG => 5 MNBK
8 TMFS => 2 VZMS
175 ORE => 2 TMFS
1 LBZN, 2 SWJZ, 3 VGSBF => 8 BLDN
7 KFJD, 5 WVRXR, 5 RJKJD => 6 MVGN
3 RJKJD, 1 TXCR => 8 KVFL
3 QHGQC, 1 MGQRZ, 10 VGSBF => 8 LKTWD
178 ORE => 1 XJWX
1 QBXC, 1 BWFK => 6 TSVN
1 NHRCK, 2 DHRBP => 4 VZBJ
1 LDFGW, 2 NHRCK, 10 BWLZ => 8 TWPMQ
28 TWPMQ => 4 RJKJD
10 SVCQ, 1 KVFL => 6 CZNMG
3 VZMS, 3 MGQRZ => 3 WVMG
19 MGQRZ => 8 KFJD
3 WVMG => 6 PQRLB
31 SVCQ, 1 TXCR => 8 VMDT
20 KFJD, 5 CPXDX, 2 BLDN, 2 PQWJX, 12 TFPQ, 2 BHZH, 2 MVGN => 9 SGPK
7 QZLC => 8 JMBG
1 PQRLB => 1 HWPND
9 VMDT, 5 CZNMG, 3 CPXDX, 1 MVGN, 8 VSMTK, 2 SGRXC, 1 MNBK, 8 LGWM => 7 GXSD
2 NSPVD => 8 QBVG
20 CZNMG => 4 PQWJX
1 LDFGW => 4 NSPVD
16 KBFJV, 22 BLDN => 2 VSMTK
10 BWLZ => 9 LBZN
1 BWLZ => 3 SWJZ
1 HWPND => 9 TXCR
12 CJLH, 9 LGWM, 3 BHZH => 6 PKRJF
5 BMNGX => 7 JKPFT"""


def read_input():
    reactions = dict()
    for reaction in data_input.split('\n'):
        input, output = reaction.split(" => ")
        output_qnt, output_chemical = output.split(' ')
        inputs = []
        for chem in input.split(', '):
            input_qnt, input_chemical = chem.split(' ')
            inputs.append((int(input_qnt), input_chemical))

        reactions[output_chemical] = (int(output_qnt), inputs)

    return reactions


def ores_required(reactions, chemical, needed, leftovers):
    ores = 0
    if chemical == "ORE":
        return needed

    number_produced, reaction = reactions[chemical]  # The reaction and the amount produced for the requested chemical
    leftover = leftovers[chemical]  # Get leftovers if any

    repetitions = ceil((needed - leftover)/number_produced)  # How many times the reaction needs to be repeated

    for amt, chem in reaction:
        ores += ores_required(reactions, chem, amt * repetitions, leftovers)

    leftovers[chemical] += ((repetitions * number_produced) - needed)  # Store any leftovers

    return ores


def part_one(reactions):
    print(f"Part one: {ores_required(reactions, 'FUEL', 1, defaultdict(int))}")


def part_two(reactions):
    target = 1000000000000
    guess = target / 2
    high, low = target, 0
    answer = None

    while answer is None:
        nr_ores = ores_required(reactions, "FUEL", guess, defaultdict(int))

        if nr_ores < target:
            low = guess
        else:
            high = guess

        new_guess = floor((high + low) / 2)
        if new_guess == guess:
            answer = guess
        guess = new_guess

    print(f"Part two: {answer}")


if __name__ == '__main__':
    chemical_reactions = read_input()

    part_one(chemical_reactions)
    part_two(chemical_reactions)