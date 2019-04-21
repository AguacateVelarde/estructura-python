class Nodo:
  def __init__( self, data=None ):
    self.data = data
    self.next = None

class Pila:
  def __init__( self ):
    self.pila = None

  def printPila( self ):
    if self.pila is None:
      print( "Pila Vacía" )
    else:
      temp = self.pila
      while temp is not None:
        print( temp.data, end=" - ")
        temp = temp.next

  def addElement( self, data ):
    if self.pila is None:
      self.pila = Nodo( data=data )
    else:
      temp = self.pila
      self.pila = Nodo( data )
      self.pila.next = temp


  def getElement( self ):
    data = self.pila.data
    self.pila = self.pila.next
    return data


 def main():
     obj = Pila()
     obj.printPila()

     obj.addElement( 7 )
     obj.addElement( 12 )

     print( obj.getElement() )

     obj.printPila()
