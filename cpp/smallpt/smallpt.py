# Python port of Kevin Beason's Global Illumination renderer in 99 lines of c++
# http://kevinbeason.com/smallpt/
#
# TODO: 
# - Fix recursion limit exceeded crash (I believe the problem and solution
#   are discussed on the 2nd page of comments on Beason's smallpt page)
# - Cleanup pass (enforce python "best practices")
# - Performance pass

import math
import png
import random
import sys
import time

class Vec:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __repr__(self):
        return repr([self.x, self.y, self.z])
    
    def __add__(self, b):
        return Vec(self.x + b.x, self.y + b.y, self.z + b.z)
    
    def __sub__(self, b):
        return Vec(self.x - b.x, self.y - b.y, self.z - b.z)
    
    def __mul__(self, b):
        return Vec(self.x * b, self.y * b, self.z * b)
        
    def mult(self, b):
        return Vec(self.x * b.x, self.y * b.y, self.z * b.z)
    
    def norm(self):
        m = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return self * (1.0 / m)
    
    def dot(self, b):
        return self.x * b.x + self.y * b.y + self.z * b.z
    
    def cross(self, b):
        x = self.y * b.z - self.z * b.y
        y = self.z * b.x - self.x * b.z
        z = self.x * b.y - self.y * b.x
        return Vec(x, y, z)

class Ray:
    def __init__(self, o, d):
        self.o = o
        self.d = d
    def __str__(self):
        return "(Origin=" + str(self.o) + ", Dir=" + str(self.d) + ")"

DIFF = 0
SPEC = 1
REFR = 2

class Sphere:
    def __init__(self, rad, p, e, c, refl):
        self.rad = rad
        self.p = p
        self.e = e
        self.c = c
        self.refl = refl

    def intersect(self, r):
    # Ray intersection, returns distance, 0 if nohit
        # Solve t^2*d.d + 2*t*(o-p).d + (o-p).(o-p)-R^2 = 0
        op = self.p - r.o
        eps = 1e-4
        b = op.dot(r.d)
        det = (b * b) - op.dot(op) + (self.rad * self.rad)
        if det < 0.0:
            return None
        else:
            det = math.sqrt(det)
        t = b - det
        if t > eps:
            return t
        t = b + det
        if t > eps:
            return t
        else:
            return None

# Scene: radius, position, emission, color, material
spheres = [
  Sphere(1e5, Vec( 1e5+1.0,40.8,81.6), Vec(),Vec(.75,.25,.25),DIFF),#Left
  Sphere(1e5, Vec(-1e5+99.0,40.8,81.6),Vec(),Vec(.25,.25,.75),DIFF),#Rght
  Sphere(1e5, Vec(50.0,40.8, 1e5),     Vec(),Vec(.75,.75,.75),DIFF),#Back
  Sphere(1e5, Vec(50.0,40.8,-1e5+170.0), Vec(),Vec(),           DIFF),#Frnt
  Sphere(1e5, Vec(50.0, 1e5, 81.6),    Vec(),Vec(.75,.75,.75),DIFF),#Botm
  Sphere(1e5, Vec(50.0,-1e5+81.6,81.6),Vec(),Vec(.75,.75,.75),DIFF),#Top
  Sphere(16.5,Vec(27.0,16.5,47.0),       Vec(),Vec(1.0,1.0,1.0)*.999, SPEC),#Mirr
  Sphere(16.5,Vec(73.0,16.5,78.0),       Vec(),Vec(1.0,1.0,1.0)*.999, REFR),#Glas
  Sphere(600.0, Vec(50.0,681.6-.27,81.6),Vec(12.0,12.0,12.0),  Vec(), DIFF) #Lite
]

def clamp(x):
    if x < 0.0:
        return 0.0
    elif x > 1.0:
        return 1.0
    else:
        return x

def toInt(x):
    return int(math.pow(clamp(x), 1.0/2.0)*255.0 + .5)
#inline int toInt(double x){ return int(pow(clamp(x),1/2.2)*255+.5); }

def intersect(r, t, id):
    d = 0.0
    inf = 1e20
    t = 1e20
    for i in xrange(len(spheres)-1, -1, -1):
        d = spheres[i].intersect(r)
        if d and d < t:
            t = d
            id = i
    return t < inf, t, id

def radiance(r, depth):
    (bHit, t, id) = intersect(r, 0.0, 0)
    if not bHit: # if miss, return black
        return Vec()
    obj = spheres[id] # the hit object
    x = r.o + r.d * t
    n = (x - obj.p).norm()
    n1 = n * -1
    if n.dot(r.d) < 0:
        n1 = n
    f = obj.c
    p = f.z # max refl
    if f.x > f.y and f.x > f.z:
        p = f.x
    elif f.y > f.z:
        p = f.y
    
    depth = depth + 1
    if depth > 5:
        if random.random() < p:
            f = f * (1.0/p)
        else:
            return obj.e
    if obj.refl is DIFF:
        r1 = 2.0 * math.pi * random.random()
        r2 = random.random()
        r2s = math.sqrt(r2)
        w = Vec(n1.x, n1.y, n1.z)
        u = Vec(1.0)
        if math.fabs(w.x) > 0.1:
            u = Vec(0.0, 1.0)
        u = (u.cross(w)).norm()
        v = w.cross(u)
        d = (u * math.cos(r1) * r2s + v * math.sin(r1) * r2s + w * math.sqrt(1.0 - r2)).norm()
        return obj.e + f.mult(radiance(Ray(x, d), depth))
    elif obj.refl is SPEC: # Ideal SPECULAR reflection
        return obj.e + f.mult(radiance(Ray(x, r.d-n*2.0*n.dot(r.d)), depth))
    
    reflRay = Ray(x, r.d - n * 2.0 * n.dot(r.d)) # Ideal dielectric REFRACTION
    into = n.dot(n1) > 0.0 # Ray from outside going in?
    
    nc = 1.0
    nt = 1.5
    nnt = nt / nc
    if into:
        nnt = nc / nt
    ddn = r.d.dot(n1)
    cos2t = 1.0 - nnt * nnt * (1.0 - ddn * ddn)
    if cos2t < 0.0: # Total internal reflection
        return obj.e + f.mult(radiance(reflRay, depth))
    
    mult = -1.0
    if into:
        mult = 1.0
    tdir = (r.d * nnt - n * (mult * (ddn * nnt + math.sqrt(cos2t)))).norm()
    a = nt - nc
    b = nt + nc
    R0 = (a * a) / (b * b)
    if into:
        c = 1.0 + ddn
    else:
        c = 1.0 - tdir.dot(n)
    Re = R0 + (1.0 - R0) * c * c * c * c * c
    Tr = 1.0 - Re
    P = 0.25 + 0.5 * Re
    RP = Re / P
    TP = Tr / (1.0 - P)
    
    if depth > 2:
        if random.random() < P:
            foo = radiance(reflRay, depth) * RP
        else:
            foo = radiance(Ray(x, tdir), depth) * TP
    else:
        foo = radiance(reflRay, depth) * Re + radiance(Ray(x, tdir), depth) * Tr
    return obj.e + f.mult(foo)

def main():
    w = 400
    h = 300
    samps = 2
    cam = Ray(Vec(50.0,52.0,295.6), Vec(0.0,-0.042612,-1.0).norm())
    cx = Vec(w * 0.5135/h)
    cy = (cx.cross(cam.d)).norm() * 0.5135
    c = []
    for y in xrange(0, h):
        for x in xrange(0, w):
            c.append(Vec())
    i = 0

    start = time.time()
    for y in xrange(0, h):
        percent = 100.0 * y / (h - 1)
        elapsed = (time.time() - start)/60.0
        remaining = 0.0
        if percent > 0.0:
            remaining = (100.0/percent) * elapsed - elapsed
        print "Rendering SPP: %d Completion: %5.2f%% Elapsed: %.2f min Remain: %.2f" % (samps*4, percent, elapsed, remaining)
        
        for x in xrange(0, w):
            i = (h-y-1)*w+x
            for sy in xrange(0, 2):
                for sx in xrange(0, 2):
                    r = Vec()
                    for s in xrange(0, samps):
                        r1 = 2.0 * random.random()
                        if r1 < 1.0:
                            dx = math.sqrt(r1) - 1.0
                        else:
                            dx = 1.0 - math.sqrt(2.0 - r1)
                        r2 = 2.0 * random.random()
                        if r2 < 1.0:
                            dy = math.sqrt(r2) - 1.0
                        else:
                            dy = 1.0 - math.sqrt(2.0 - r2)
                        d = cx*( ( (sx+0.5 + dx)/2.0 + x)/w - 0.5) + cy*( ( (sy+0.5 + dy)/2.0 + y)/h -0.5) + cam.d
                        r = r + radiance(Ray(cam.o + d * 140.0, d.norm()), 0) * (1.0/samps)
                    c[i] = c[i] + Vec(clamp(r.x), clamp(r.y), clamp(r.z)) * 0.25
            i = i + 1

    print "Done rendering, changing format"
    c2 = []
    i = 0
    for y in xrange(0, h):
        c3 = []
        for x in xrange(0, w):
            foo = c[i]
            i = i + 1
            c3.append(toInt(foo.x))
            c3.append(toInt(foo.y))
            c3.append(toInt(foo.z))
        c2.append(c3)

    print "Writing file"
    f = open('640x480x8spp.png', 'wb')
    writer = png.Writer(w, h)
    writer.write(f, c2)
    f.close()

sys.setrecursionlimit(2000)

if __name__ == "__main__":
    main()