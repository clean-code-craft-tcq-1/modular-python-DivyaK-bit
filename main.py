from ReferenceFile import *
from test_colorPair import *

def PrintData(refdata):
  for code in refdata:
    print(code)
    
if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  PrintData(createReferenceInfo())
  print('Done :)')
