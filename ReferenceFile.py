import PairDefination as pd

def createReferenceInfo():
    pair_number_start_index = 1
    pair_number_end_index = 26     
    reference_data = []
    for pair_number in range(pair_number_start_index, pair_number_end_index):
        major_color, minor_color = pd.get_color_from_pair_number(pair_number)
        colorCode = pd.color_pair_to_string(major_color, minor_color)
        reference_data.append({'Number': pair_number, 'Color Code pairs': colorCode})
    return reference_data

