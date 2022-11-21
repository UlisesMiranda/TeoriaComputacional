class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, middle = None):
        self.val = val
        self.left = left
        self.right = right
        self.middle = middle
        
class Solution(object):
    def automataCadenas(self, root:TreeNode, cadena):
        def dfs(root, cadena, aceptada):
            nextCadena = ''
            first = ''
            if (cadena):
                first, nextCadena = cadena[0], cadena[1:]

            if root.val == 2 and first == '':
                aceptada.append(1)
            if (root.left and first == '0'):
                dfs(root.left, nextCadena, aceptada)
            if (root.right and first == '1'):
                dfs(root.right, nextCadena, aceptada)
            if (root.middle and first == '0'):
                dfs(root.middle, nextCadena, aceptada)
                
            return aceptada
        
        esAceptada = dfs(root, cadena, [])
        
        if (1 in esAceptada):
            return True
        else:
            return False
        
cadena = input("Ingrese su cadena: ")
cadenaAux = cadena

root = TreeNode(0)
root.left = TreeNode(1)
root.middle = root
root.right = root
root.left.right = TreeNode(2)

print(Solution.automataCadenas(Solution, root, cadena))

