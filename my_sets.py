"""
learn about sets
an unordered collection of unique, immutable objects
define it using {}
you can use the set constructor to create one
"""


def main():
    """
    Test function
    :return: 
    """
    p = {6,75,21,45}
    print(p, type(p))
    data = [1,3,5,2,88,3,1]
    print(data, type(data))
    #eliminate duplicates
    sdata = set(data)
    print(sdata, type(sdata))
    for item in sdata:
        print(item)
    print(5 in sdata)
    #adding elements to sets
    sdata.add(45)
    print(sdata)
    sdata.update([2,99,44,33,1,2,88])
    print(sdata)
    sdata.remove(44)
    print(sdata)
    sdata.discard(77)
    print(sdata)
    # copying sets
    bk_data = sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)

    #define some sets
    blue_eyes = {'olivia','harry','lily','jack'}
    blonde_hair = {'harry','jack','amelia', 'mai','joshua'}
    smell_hcn = {'harry', 'amelia'}
    taste_ptc = {'harry','lily','amelia','lola'}
    o_blood = {'mia', 'joshua','lily','olivia'}
    b_blood = {'amelia','jack'}
    a_blood = {'harry'}
    ab_blood = {'joshua', 'lola'}
    print(blue_eyes.union(blonde_hair))
    print(blue_eyes.intersection(taste_ptc))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blonde_hair.difference(ab_blood))
    print(taste_ptc.issuperset(smell_hcn))




if __name__ == '__main__':
    main()
    exit(0)