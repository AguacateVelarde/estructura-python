# !pip install pptree -> instala la madre
from pptree import *


class ArbolBB:
  def __init__( self, data=None ):
    self.head = data
    self.derecha = None
    self.izquierda = None

  def printArbol( self, father=None ):
    if self.head is None:
      print( "Está vacía")
    else:
      if father is None:
        pointer = Node( str(self.head) )
      else:
        pointer = father

      if self.izquierda is not None:
        der = Node( str(self.izquierda.head), pointer )
        self.izquierda.printArbol( der )
      if self.derecha is not None:
        iz = Node( str(self.derecha.head), pointer )
        self.derecha.printArbol( iz )

      if father is None:
        print_tree(pointer)


  def addElement( self, data ):
    if self.head is None:
      self.head = data
    else:
      if self.head > data :
        if self.izquierda is None :
          self.izquierda = ArbolBB( data )
        else :
          self.izquierda.addElement( data )
      elif self.head < data :
        if self.derecha is None:
          self.derecha = ArbolBB( data )
        else :
          self.derecha.addElement( data )
      else :
        print( f"Dato ya existe, {data}" )
    
