import PairDefination as cpg

def createReferenceInfo():
    pair_number_start_index = 1
    pair_number_end_index = 26     
    reference_data = []
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        major_color, minor_color = cpg.get_color_from_pair_number(pair_number)
        formatted_colorpair = cpg.color_pair_to_string(major_color, minor_color)
        reference_data.append({'Pair Number': pair_number, 'Color Code pairs': formatted_colorpair})
    return reference_data

def PairList(refInfo, colList=None):
    if not colList: colList = list(refInfo[0].keys() if refInfo else [])
    myList = [colList]
    for item in refInfo: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
    colSize = [max(map(len,col)) for col in zip(*myList)]
    formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
    myList.insert(1, ['-' * i for i in colSize])
    for item in myList: print(formatStr.format(*item))
