from typing import Dict
from dataclasses import dataclass
from datetime import datetime
from typing import List 


@dataclass 
class BlogPost :
    slug : str 
    title : str 
    date : datetime 
    description : str 
    tags : List[str]
    content : str 
    
