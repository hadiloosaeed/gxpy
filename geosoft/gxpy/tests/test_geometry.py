import unittest
import os
import numpy as np
import json

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxgm
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.coordinate_system as gxcs

from base import GXPYTest


class Test(GXPYTest):
    def test_version(self):
        self.start()
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_exception(self):
        self.start()

        self.assertRaises(ValueError, gxgm.Point, [1, 'yada', 2])

    def test_cs(self):
        self.start()

        p = gxgm.Point((5, 10))
        self.assertTrue(p == p)
        self.assertTrue(gxgm.Point((1,2), coordinate_system="huh") == gxgm.Point((1,2), coordinate_system="huh"))
        self.assertTrue(gxgm.Point((1, 2), coordinate_system="huh") == gxgm.Point((1, 2)))
        self.assertTrue(gxgm.Point((1, 2)) == gxgm.Point((1, 2)))
        self.assertFalse(gxgm.Point((1, 2), coordinate_system="huh") == gxgm.Point((1, 2), coordinate_system="huh?"))

        s = "WGS 84 / UTM zone 32N <0, 0, 0, 10, 15, 32>"
        p = gxgm.Point((5,10), coordinate_system=s)
        hcsd = p.coordinate_system.coordinate_dict()
        self.assertEqual(hcsd['name'], "WGS 84 / UTM zone 32N <0,0,0,10,15,32>")
        self.assertTrue(p == p)

        s = s + ' [geoid]'
        pp = gxgm.PPoint(((8, 12), (5, 10)), coordinate_system=s)
        hcsd = p.coordinate_system.coordinate_dict()
        self.assertEqual(hcsd['name'], "WGS 84 / UTM zone 32N <0,0,0,10,15,32>")
        self.assertEqual(pp.coordinate_system.vcs, "geoid")
        self.assertTrue(pp == pp)
        self.assertTrue(pp == gxgm.PPoint(((8, 12), (5, 10))))
        self.assertFalse(pp == gxgm.PPoint(((8, 12), (5, 10)), coordinate_system='WGS 84 [geoid]'))
        self.assertFalse(gxgm.PPoint(((8, 12), (5, 10)), coordinate_system='WGS 84 [geoid]') == pp)

    def test_point(self):
        self.start()

        p = gxgm.Point((5,10))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 0.0])
        self.assertEqual(p.xy, (5.0,10.0))
        self.assertEqual(p.xyz, (5.0, 10.0, 0.0))
        self.assertEqual(p.x, 5.0)
        self.assertEqual(p.y, 10.0)
        self.assertEqual(p.z, 0.0)

        p -= (0, 0, 15)
        self.assertEqual(p.xyz, (5.0, 10.0, -15.0))

        p = gxgm.Point((5,10,3.5))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 3.5])
        self.assertEqual(p.xyz, (5.0, 10.0, 3.5))
        self.assertEqual(p.x, 5.0)
        self.assertEqual(p.y, 10.0)
        self.assertEqual(p.z, 3.5)

        p = gxgm.Point(4)
        self.assertEqual(p.xyz, (4.0, 4.0, 4.0))

        p += (1, 2, 3)
        self.assertEqual(p.xyz, (5., 6., 7.))

        p *= 2
        self.assertEqual(p.xyz, (10., 12., 14.))

        p /= 2
        self.assertEqual(p.xyz, (5., 6., 7.))

        p = -p
        self.assertEqual(p.xyz, (-5., -6., -7.))

        p = p + 1
        self.assertEqual(p.xyz, (-4., -5., -6.))

        p = p + (1, 2)
        self.assertEqual(p.xyz, (-3., -3., -6.))

        p = p + (5, 2, 6)
        self.assertEqual(p.xyz, (2., -1., 0.))

        p.x = p.x + 2
        p.y -= 2
        p.z = 5
        self.assertEqual(p.xyz, (4., -3., 5.))

        p.xy = (99, '88')
        self.assertEqual(p.xyz, (99., 88., 5.))

        p.xyz = [0, 1, 45]
        self.assertEqual(p.xyz, (0., 1., 45.))

    def test_ppoint(self):
        self.start()

        points = [(5, 10), (6, 11), (7, 12)]
        pp = gxgm.PPoint(points)
        self.assertEqual(len(pp), 3)
        i = 0
        for p in pp:
            self.assertEqual(p.xy, points[i])
            i += 1
        i = 0
        for p in pp:
            self.assertEqual(p.xyz, (points[i][0], points[i][1], 0.0))
            i += 1

        p = pp[1]
        self.assertEqual(p.xy, points[1])

        pp -= (0, 0, 15)
        self.assertEqual(pp[0].xyz, (5.0, 10.0, -15.0))
        self.assertEqual(pp[2].xyz, (7.0, 12.0, -15.0))

        pp = gxgm.PPoint([(5, 10, 3.5)])
        self.assertEqual(pp[0].xyz, (5.0, 10.0, 3.5))

        pp = gxgm.PPoint(((1, 2, 3), (4, 5, 6), (7, 8, 9)))

        pp += (1, 2, 3)
        self.assertEqual(pp[0].xyz, (2., 4., 6.))
        self.assertEqual(pp[2].xyz, (8., 10., 12.))

        pp *= 2
        self.assertEqual(pp[1].xyz, (10., 14., 18.))

        pp /= 2
        self.assertEqual(pp[1].xyz, (5., 7., 9.))

        pp = -pp
        self.assertEqual(pp[1].xyz, (-5., -7., -9.))

        pp = pp + (1, 2)
        self.assertEqual(pp[1].xyz, (-4., -5., -9.))

        pp = pp + (5, 2, 6)
        self.assertEqual(pp[1].xyz, (1., -3., -3.))

        pp = pp + ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        self.assertEqual(pp[1].xyz, (5., 2., 3.))

        pp = pp * gxgm.PPoint(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
        self.assertEqual(pp[1].xyz, (20., 10., 18.))
        self.assertEqual(len(pp), 3)
        self.assertEqual(pp.x.tolist(), [5., 20., 35.])
        self.assertEqual(pp.y.tolist(), [4., 10., 16.])
        self.assertEqual(pp.z.tolist(), [9., 18., 27.])

        points = [(5, 10), (6, 11), (7, 12)]
        pp = gxgm.PPoint(points, z=3.5)
        self.assertEqual(pp.x.tolist(), [5., 6., 7.])
        self.assertEqual(pp.z.tolist(), [3.5, 3.5, 3.5])
        self.assertEqual(pp.xy.tolist(), np.array(points).tolist())

        pp.x = 4.8
        pp.y = (8., 5., 3.)
        pp.z = (1., 2., "-3")
        self.assertEqual(pp.x.tolist(), [4.8, 4.8, 4.8])
        self.assertEqual(pp.y.tolist(), [8., 5., 3.])
        self.assertEqual(pp.z.tolist(), [1., 2., -3.])

        pp.xy = [(1, 2), (3,4), (5,6)]
        self.assertEqual(pp.xy.tolist(), [[1., 2.], [3., 4.], [5., 6.]])

    def test_ppoint_constructors(self):
        self.start()

        def verify():
            self.assertEqual(pp.x.tolist(), [1., 4., 7., 10., 13.])
            self.assertEqual(pp.z.tolist(), [3., 6., 9., 12., 15.])
            self.assertEqual(pp.xy.tolist(), nppp[:, :2].tolist())

        lpp = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15))
        nppp = np.array(lpp)
        pp = gxgm.PPoint(lpp)
        verify()

        nppp = np.array(lpp)
        pp = gxgm.PPoint(nppp)
        verify()

        vvx = gxvv.GXvv(nppp[:, 0])
        vvy = gxvv.GXvv(nppp[:, 1])
        vvz = gxvv.GXvv(nppp[:, 2])
        pp = gxgm.PPoint((vvx, vvy, vvz))
        verify()

        p1, p2 = pp.extent()
        self.assertTrue(p1 == gxgm.Point((1, 2, 3)))
        self.assertTrue(p2 == gxgm.Point((13, 14, 15)))


    def test_copy(self):
        self.start()

        p1 = gxgm.Point((1,2))
        p2 = p1
        self.assertTrue(p1 is p2)
        p2 = p1.copy()
        self.assertFalse(p1 is p2)
        self.assertTrue(p1 == p2)

        p2.cs = "WGS 84"
        self.assertTrue(p1 == p2)
        p1.cs = "WGS 84"
        self.assertTrue(p1 == p2)
        p1.cs = gxcs.Coordinate_system("WGS 84 [geoid]")
        self.assertTrue(p1 == p2)

    def test_p2(self):
        self.start()

        b1 = gxgm.Point2((gxgm.Point((0, 1)), (10, 20, -1)))
        self.assertEqual('Point2[(0.0, 1.0, 0.0) (10.0, 20.0, -1.0)]', str(b1))
        self.assertEqual(b1.x2, (0., 10.))
        self.assertEqual(b1.y2, (1., 20.))
        self.assertEqual(b1.z2, (0, -1.))

        b2 = gxgm.Point2(((0, 1), (10, 20, -1)))
        self.assertTrue(b1 == b2)

        b1 = gxgm.Point2((gxgm.Point((0, 1, -20)),(10, 20, -1)))
        self.assertEqual('Point2[(0.0, 1.0, -20.0) (10.0, 20.0, -1.0)]', str(b1))
        self.assertEqual(b1.x2, (0., 10.))
        self.assertEqual(b1.y2, (1., 20.))
        self.assertEqual(b1.z2, (-20., -1.))
        b2 = gxgm.Point2((gxgm.Point((b1.x2[0], b1.y2[0], b1.z2[0])),
                         gxgm.Point((b1.x2[1], b1.y2[1], b1.z2[1]))))
        self.assertTrue(b1 == b2)
        b2 = gxgm.Point2((gxgm.Point((b1.x2[1], b1.y2[1], b1.z2[1])),
                         gxgm.Point((b1.x2[0], b1.y2[0], b1.z2[0]))), coordinate_system="WGS 84")
        self.assertTrue(b1 == b2)
        b2 = gxgm.Point2(((b1.x2[1], b1.y2[1], b1.z2[1]), (b1.x2[0], b1.y2[0], b1.z2[0])), coordinate_system="WGS 84")
        self.assertTrue(b1 == b2)
        b2 = gxgm.Point2((b1.x2[1], b1.y2[1], b1.z2[1], b1.x2[0], b1.y2[0], b1.z2[0]), coordinate_system="WGS 84")
        self.assertTrue(b1 == b2)

        c = gxgm.Point(((b2.p0.x + b2.p1.x) * 0.5,
                        (b2.p0.y + b2.p1.y) * 0.5,
                        (b2.p0.z + b2.p1.z) * 0.5))
        self.assertEqual(b2.centroid, c)
        self.assertEqual(b2.dimension, (abs(b2.p1.x - b2.p0.x), abs(b2.p1.y - b2.p0.y), abs(b2.p1.z - b2.p0.z)))

        self.assertEqual(b2.extent_xyz, (0.0, 1.0, -20.0, 10.0, 20.0, -1.0))
        self.assertEqual(b2.extent_xy, (0.0, 1.0, 10.0, 20.0))

if __name__ == '__main__':

    unittest.main()
