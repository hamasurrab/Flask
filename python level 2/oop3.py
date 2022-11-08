#   special methods
class book():
    def __init__(self,author,tittle,pages):
        self.author=author
        self.tittle=tittle
        self.pages=pages
    def __repr__(self):
        return f"author:{self.author},tittle:{self.tittle}"

    def __len__(self):
        return self.pages    
x=book('Hamas','Python',212)        
print(x)
print(len(x))