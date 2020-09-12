class css:

    def __init__(self, cssfile):
        print("in css class")
        file = open(cssfile, 'r')
        CSStext = file.read()
        List = []
        for i in file.readlines():
            List.append(i)
        file.close()

        self.ListContent = List
        self.cssContent = CSStext
        self.CSSFile =  cssfile
    def write(self,selector, elements):
        self.cssContent += self.container(selector, elements)
        file = open(self.CSSFile, 'w')
        file.write(self.cssContent)
        file.close()

    def container(self, selector, elements):
        cont = '\n'+selector+'{\n'
        for i in elements:
            if 'bg' in i :
                if i =='bg-co':
                    cont += 'background-color:'+elements[i]+';\n'
            if 'co' in i:
                if i == 'co':
                    cont += 'color:'+elements[i]+';\n'
        return cont+'}'
