from dataclasses import dataclass
#pytest testing/test_homework_02 -s -vv
@dataclass()
class Engine():
    volume: int
    pistons: int

"""
create dataclass `Engine`

@dataclasses
class Engine:
    volume: None
    pistons: None
"""