@Name: ubaid
@Rollno: 261031575
#Question 3
class SetOfKeys:
    pass
class RamModules:
    pass
class HardDisk:
    pass
class MultlipleProcessors:
    pass
class MagneticDrums:
    pass
class Student: #Aggregation
    def __init__(self):
        self.name = name
        self.Rollno = Rollno
        self.Major = Major
        self.gpa = gpa
class Laptop: #Composition
    def __init__(self):
        self.Students = [Student() "More....."]
        self.SetOfKeys = SetOfKeys()
        self.RamModules = RamModules()
        self.HardDisk = MagneticDrums(HardDisk)

#Question 4
class AuthorBooks:
    pass
class Title:
    pass
class PublishDate:
    pass
class ISBN:
    pass
class Author: #Aggregation
    def __init__(self):
        self.name = name
        self.DOB = DOB
        self.ListOfAuthorBooks = AuthorBooks()
class Book: 
    def __init__(self):
        self.title = Title(AuthorBooks)
        self.author = Author()
        self.ISBN = ISBN()
        self.PublishDate = PublishDate(AuthorBooks)
class Library: #Composition
        def __init__(self):
            self.ListOfBooks = [book(),book(),book(),book() 'More.......']

#Question 5
class SpaceStation: #Compoistion
    pass
class OxgyenSupply:
    pass
class PropulsionSystem:
    pass
class VitalSigns:
    pass
class EnviromentalData:
    pass
class Keyboard:
    pass
class NetworkPortConnecter:
    pass
class AreasOfStation: 
    pass
class air:
    pass
class WaterSupply:
    pass
class Lighting:
    pass
class Temperature:
    pass
class Visor:
    def __init__(self):
        self.VitalSigns= VitalSigns()
        self.EnviromentalData = EnviromentalData()
class SpaceSuit:
    def __init__(self):
        self.OxgyenSupplier = OxgyenSupply()
        self.PropulsionSystem = PropulsionSystem()
class Helment:
    def __init__(self):
        self.Visor = Visor()
        self.
class MissionDevice:
    def __init__(self):
        self.Keyboard = Keyboard()
        self.Port = NetworkPortConnecter()
class CrewMember: #Aggergation
    def __init__(self):
        self.IDcard = IDcard()
        self.SpaceSuit = SpaceSuit()
        self.Helment = Helment()
        self.PersonalDevice = MissionDevice()
        self.Interact = AiSystem()
class IDcard:
    def __init__(self):
        self.AccessOfAreas = AreasOfStation()
class AiSystem:
    def __init__(self):
        self.MonitorAndControl = MonitorAndControl()
class MonitorAndControl:
    def __init__(self):
        self.air = air()
        self.waterSupply = WaterSupply()
        self.lighting = Lighting()
        self.temperature = Temperature()

#Question 6

class PrehistoricEra:
    pass
class PrimitiveOrganisms:
    pass
class Earth: #Composition
    def __init__(self):
        self.Era = PrehistoricEra()
class Aliens: #Aggergration
    def __init__(self):
        self.Study = PrimitiveOrganisms()
        self.SuddenEvent = TragedyStruck()
class ship:
    def __init__(self):
        pass
    def shipMalfuncation(self):
        pass
class TragedyStruck:
    pass
class GiantSwampLeeches:
    pass
class TechnologyLay:
    pass
class IndigenousCreatures:
    pass
class Time:
    pass
class Danger:
    pass
class Space:
    pass


