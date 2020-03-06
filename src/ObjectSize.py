import cv2
import imutils
import numpy as np
from imutils import contours
from imutils import perspective
from scipy.spatial import distance as dist


class ObjectSize:
    def __init__(self,image,objReferencia):
        self.image = image
        self.objReferencia = objReferencia
        self.pixelPerMetric = None
        self.realWorldMeasure = None

    def midpoint(self,ptA, ptB):
        return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

    def getSize(self,file = None, outside = None):

        # imagem obtida atraves da webcam
        if file == None:
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)
            edged = cv2.Canny(gray, 50, 100)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)
        else: #file de modelo
            if outside != None:
                image = cv2.imread(file, cv2.IMREAD_COLOR)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (7, 7), 0)
                edged = cv2.Canny(gray, 50, 100)
                cv2.floodFill(edged, None, (0, 0), 255)
                cv2.floodFill(edged, None, (0, 0), 0)

            else:
                image = cv2.imread(file, cv2.IMREAD_COLOR)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (7, 7), 0)
                edged = cv2.Canny(gray, 50, 100)
                edged = cv2.dilate(edged, None, iterations=5)
                edged = cv2.erode(edged, None, iterations=5)
                cv2.floodFill(edged, None, (0, 0), 255)
                cv2.floodFill(edged, None, (0, 0), 0)
        # find contours in the edge map
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # sort the contours from left-to-right and initialize the
        # 'pixels per metric' calibration variable

        (cnts, _) = contours.sort_contours(cnts)
        pixelsPerMetric = None
        objList = []
        # loop over the contours individually
        for c in cnts:
            # if the contour is not sufficiently large, ignore it
            if cv2.contourArea(c) < 100:
                continue
            obj = []
            # compute the rotated bounding box of the contour
            orig = self.image.copy()
            box = cv2.minAreaRect(c)
            box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype="int")

            # order the points in the contour such that they appear
            # in top-left, top-right, bottom-right, and bottom-left
            # order, then draw the outline of the rotated bounding
            # box
            box = perspective.order_points(box)
            cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

            # loop over the original points and draw them
            '''for (x, y) in box:
                cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)'''

            # unpack the ordered bounding box, then compute the midpoint
            # between the top-left and top-right coordinates, followed by
            # the midpoint between bottom-left and bottom-right coordinates
            obj.append(box)
            (tl, tr, br, bl) = box
            (tltrX, tltrY) = self.midpoint(tl, tr)
            (blbrX, blbrY) = self.midpoint(bl, br)

            # compute the midpoint between the top-left and top-right points,
            # followed by the midpoint between the top-righ and bottom-right
            (tlblX, tlblY) = self.midpoint(tl, bl)
            (trbrX, trbrY) = self.midpoint(tr, br)

            #center
            mid = self.midpoint(tl, br)

            # compute the Euclidean distance between the midpoints
            dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

            # compute the size of the object
            #distancia em cruz do objeto
            dimA = dA / self.getPixelPerMetric()
            dimB = dB / self.getPixelPerMetric()

            obj.append(mid)
            dim = {
                    'pixel': { 'vertical' : dA, 'horizontal' : dB },
                    'real' : { 'vertical' : dimA , 'horizontal' : dimB }
                    }
            obj.append(dim)
            objList.append(obj)

        return objList, edged.shape

    def distanciaEuclidiana(self, pt1, pt2):
        return dist.euclidean(pt1, pt2)

    def getPixelPerMetric(self):
        return self.pixelPerMetric

    def setPixelPerMetric(self, objRef, realWorldMeasure):
        qtdPixel = self.distanciaEuclidiana((objRef[0][0][0], objRef[0][0][1]), (objRef[3][0][0], objRef[3][0][1]))
        self.realWorldMeasure = realWorldMeasure
        self.pixelPerMetric = qtdPixel / realWorldMeasure

    def getProporcao(self, qtdPixel):
        print(self.realWorldMeasure)
        print(self.pixelPerMetric)
        return (qtdPixel * self.realWorldMeasure) / self.pixelPerMetric