class Nodo:
  def __init__( self, data=None ):
    self.data = data
    self.next = None

class LL:
  def __init__( self ):
    self.first = None

  def push( self, data ):
    if self.first is None:
      self.first = Nodo( data=data )
    else:
      temp = self.first
      while temp.next is not None:
        temp = temp.next
      temp.next = Nodo( data=data )

  def printLL( self ):
    temp = self.first
    if temp is not None :
      while temp.next is not None :
        print( temp.data, end=" -> " )
        temp = temp.next
      print( temp.data )
    else:
      print( "Lista vacía" )

  def pop( self ):
    actual = self.first
    self.first = None
    if actual.next is None:
      return actual.data
    else:
      while actual.next is not None:
        self.push( actual.data )
        actual = actual.next
      return actual.data


def main():
    obj = LL()

    #Se insertan valores
    obj.push( 14 )
    obj.push( 43 )

    #Se imprimen valores
    obj.printLL()

    #Se eliminan e imprimen valores
    print( obj.pop() )

if __name__ == '__main__':
     main()
