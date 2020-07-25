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
        img, faces, myFaceListC, myFaceListArea = findFaces(img)
        #print("\n")
        #for a in myFaceListArea:
        #    print(a)
        #print("len Faces = " + str(len(faces)))
        #cv2.imshow("Result", img)
        #cv2.waitKey(0)
        myFaceListArea.sort()
        self.assertEqual(5041, myFaceListArea[0])
        self.assertEqual(5041, myFaceListArea[1])
        self.assertEqual(6561, myFaceListArea[2])
        self.assertEqual(6889, myFaceListArea[3])
        self.assertEqual(10404, myFaceListArea[4])
        self.assertEqual(len(faces), 5)


if __name__ == '__main__':
    unittest.main()
    print("Finished main")
    sys.exit(1)
