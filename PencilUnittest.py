import unittest

class TestPencilDurability(unittest.TestCase):
    def setUp(self):
        # Pencil(pencil length, eraser durability, point durability)
        self.pencil = Pencil(pencilLength = 120,eraserDurability = 100, pointDurability = 25)

    def testWrite(self):
        self.pencil.write("Sample text")
        self.assertEqual(self.pencil.getSheet(), "Sample text", "Text does not match")
    
    def testWriteAppend(self):
        self.pencil.write("Sample text")
        self.pencil.write("plus some more")
        self.assertEqual(self.pencil.getSheet(), "Sample text plus some more","Text is not appending")
    
    def testPointDegradation(self):
        pointDurability = self.pencil.getPointDurability()
        # Lowercase letters should degrade the pencil point by a value of one.
        # capital letters should degrade the point by two.
        # Writing spaces and newlines expends no graphite
        self.pencil.write("Today is Friday ")
        self.assertEqual(self.pencil.getPointDurability(),(pointDurability - 15),"point durability does not match")
        self.pencil.write("and it is a good day")
        self.assertEqual(self.pencil.getSheet(), "Today is Friday and it is a go      ","Pencil does not follow point durability")