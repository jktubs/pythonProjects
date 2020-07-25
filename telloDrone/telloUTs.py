import unittest
from utils import *
import os


class TestUtilsMethods(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def test_findFaces(self):
        dirname = os.path.dirname(__file__)
        img = cv2.imread(os.path.join(dirname, '../openCV/Resources/All-Faces-Down-750.jpg'))
        img, faces = findFaces(img)
        #print("\nlen Faces = " + str(len(faces)))
        #cv2.imshow("Result", img)
        #cv2.waitKey(0)
        self.assertEqual(len(faces), 5)


if __name__ == '__main__':
    unittest.main()
    print("Finished main")
    sys.exit(1)
