# import travel.thailand
# trip_to = travel.thailand.ThailandPackgae() 
# trip_to.detail() 

from travel.thailand import ThailandPackgae
trip_to = ThailandPackgae() 
trip_to.detail() 

import inspect 
import random 
from travel import * 

print(inspect.getfile(random))
print(inspect.getfile(thailand)) # random 폴더에다 가져다 두면 똑같이 사용 가능  
#linting : 파일 int 비활성화 / setting -> linting enable 해제 