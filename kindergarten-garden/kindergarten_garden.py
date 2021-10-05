class Garden:
    def __init__(self, diagram, students = ["Bob", "Alice", "Charlie", "David", "Eve", "Fred","Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = sorted(students)   
        self.diagram = diagram
        
    def plants(self, name):
            diagram = self.diagram.split("\n")

            ps = ""

            i = self.students.index(name)
            ps += diagram[0][i*2:i*2+2]
            ps += diagram[1][i*2:i*2+2]

            plants = ""
            for p in ps:
                plants += self.returnPlantName(p) + " "
            return plants.split()
    
    def returnPlantName(self,letter):
        if letter == "G":
            return "Grass"            
        if letter == "C":
            return "Clover"            
        if letter == "R":
            return "Radishes"            
        if letter == "V":
            return "Violets"            
        return ""