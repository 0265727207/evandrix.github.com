package gaerender;

import java.util.Random;

public class Sample {
	//Scene: radius, position, emission, color, material
	Sphere spheres[];
	int sphereCount;
	Random rand;
	double inf=1e20;
	
	void createScene()
	{
		rand = new Random();
		
		sphereCount = 9;
		spheres = new Sphere[sphereCount];
		
		//Left
		spheres[0] = new Sphere(1e5, new Vec( 1e5+1,40.8,81.6), new Vec(0,0,0), new Vec(.75,.25,.25), Refl_t.DIFF);
	
		// Right
		spheres[1] = new Sphere(1e5, new Vec(-1e5+99,40.8,81.6), new Vec(0,0,0), new Vec(.25,.25,.75), Refl_t.DIFF);
		
		// Back
		spheres[2] = new Sphere(1e5, new Vec(50,40.8, 1e5), new Vec(0,0,0), new Vec(.75,.75,.75), Refl_t.DIFF);
		
		// Front
		spheres[3] = new Sphere(1e5, new Vec(50,40.8,-1e5+170), new Vec(0,0,0), new Vec(0,0,0), Refl_t.DIFF);
		
		// Bottom
		spheres[4] = new Sphere(1e5, new Vec(50, 1e5, 81.6), new Vec(0,0,0), new Vec(.75,.75,.75), Refl_t.DIFF);
		
		// Top
		spheres[5] = new Sphere(1e5, new Vec(50,-1e5+81.6,81.6), new Vec(0,0,0), new Vec(.75,.75,.75), Refl_t.DIFF);
		
		// Mirror
		spheres[6] = new Sphere(16.5, new Vec(27,16.5,47), new Vec(0,0,0), new Vec(.999,.999,.999), Refl_t.SPEC);
		
		// Glass
		spheres[7] = new Sphere(16.5, new Vec(73,16.5,78), new Vec(0,0,0), new Vec(.999,.999,.999), Refl_t.REFR);
		
		// Light
		spheres[8] = new Sphere(600, new Vec(50,681.6-.27,81.6),new Vec(12,12,12), new Vec(0,0,0), Refl_t.DIFF);
	}
	
	double clamp(double x)
	{
		return x < 0.0 ? 0.0 : x > 1.0 ? 1.0 : x;
	}
	
	int toInt(double x)
	{
		return (int)(Math.pow(clamp(x),1.0/2.2)*255.0+.5);
	}
	
	class Intersection
	{
		Boolean b;
		double t; // distance to intersection
		int id; // id of intersected object
	}
	
	// intersect(const Ray &r, double &t, int &id)
	void intersect(Ray r, Intersection i)
	{
		double d;

		for(int j = sphereCount-1; j >= 0; --j)
		{
			d = spheres[j].intersect(r);
			if(d > 0.0 && d < i.t)
			{
				i.t = d;
				i.id = j;
			}
		}
		
		i.b = i.t < inf;
	}
	
	// radiance(const Ray &r, int depth, unsigned short *Xi)
	Vec radiance(Ray r, int depth)
	{
		Intersection inter = new Intersection();
		inter.t = inf;
		inter.id = 0;
		inter.b = false;

		intersect(r, inter);
		if(!inter.b)
		{
			// if miss, return black
			return new Vec(0,0,0);
		}
		
		// the hit object
		Sphere obj = spheres[inter.id];
		
		Vec x = r.o.add(r.d.mult(inter.t));
		Vec n = x.sub(obj.p);
		n.norm();
		
		Vec nl = n.dot(r.d) < 0.0 ? n : n.mult(-1.0);
		Vec f = new Vec(obj.c.x, obj.c.y, obj.c.z);
		
		// max refl
		double p = f.x>f.y && f.x>f.z ? f.x : f.y>f.z ? f.y : f.z;
		
		if(++depth > 5)
		{
			// Added the depth limit to prevent stack overflow.
			if(rand.nextDouble() < p && depth < 200)
			{
				f = f.mult((1.0/p));
			}
			else
			{
				return obj.e; //R.R.
			}
		}
		
		// Ideal DIFFUSE reflection
		if(obj.refl == Refl_t.DIFF)
		{
			double r1 = 2.0 * Math.PI * rand.nextDouble();
			double r2 = rand.nextDouble();
			double r2s = Math.sqrt(r2);
			Vec w = nl;
			Vec u = ((Math.abs(w.x)>0.1? new Vec(0,1,0): new Vec(1,0,0)).cross(w));
			u.norm();
			Vec v = w.cross(u);
			Vec d = (u.mult(Math.cos(r1)*r2s)).add(v.mult(Math.sin(r1)*r2s)).add(w.mult(Math.sqrt(1.0-r2)));
			d.norm();
			return obj.e.add(f.mult(radiance(new Ray(x,d), depth)));
		}
		// Ideal SPECULAR reflection
		else if(obj.refl == Refl_t.SPEC)
		{
			return obj.e.add(f.mult(radiance(new Ray(x, r.d.sub(n.mult(2.0).mult(n.dot(r.d)))),depth)));
		}
		
		// Ideal dielectric REFRACTION
		Ray reflRay = new Ray(x, r.d.sub(n.mult(2.0).mult(n.dot(r.d))));
		
		// Ray from outside going in?
		Boolean into = n.dot(nl) > 0.0;
		
		double nc=1.0, nt=1.5, nnt=into?nc/nt:nt/nc, ddn=r.d.dot(nl);
		
		// Total internal reflection
		double cos2t=1-nnt*nnt*(1.0-ddn*ddn);
		if(cos2t < 0.0)
		{
			return obj.e.add(f.mult(radiance(reflRay,depth)));
		}
		
		Vec tdir = (r.d.mult(nnt)).sub((n.mult((into?1.0:-1.0)).mult(ddn*nnt+Math.sqrt(cos2t))));
		tdir.norm();
		
		double a=nt-nc, b=nt+nc, R0=a*a/(b*b), c = 1.0-(into?-ddn:tdir.dot(n));
		double Re=R0+(1.0-R0)*c*c*c*c*c,Tr=1.0-Re,P=.25+.5*Re,RP=Re/P,TP=Tr/(1.0-P);
		
		// Russian roulette
		Vec xx;
		if(depth > 2)
		{
			if(rand.nextDouble() < P)
			{
				xx = radiance(reflRay,depth).mult(RP);
			}
			else
			{
				xx = radiance(new Ray(x,tdir),depth).mult(TP);
			}
		}
		else
		{
			xx = (radiance(reflRay,depth).mult(Re)).add(radiance(new Ray(x,tdir),depth).mult(Tr));			
		}
		
		return obj.e.add(f.mult(xx));
	}
	
	Vec[] Get(int w, int h, int x, int y, int pixels, int samples)
	{
		createScene();
		
		samples = samples/4;
		
		Vec pos = new Vec(50,52,295.6);
		Vec dir = new Vec(0,-0.062612,-1);
		dir.norm();
		
		Ray cam = new Ray(pos, dir);
		Vec cx = new Vec(w*0.5135/h,0,0);
		Vec cy = (cx.cross(cam.d));
		cy.norm();
		cy = cy.mult(0.5135);
		
		Vec c[] = new Vec[pixels];
		
		for(int i = 0; i < pixels; i++)
		{			
			// 2x2 subpixel rows
			for(int sy = 0; sy < 2; sy++)
			{
				// 2x2 subpixel cols
				for(int sx = 0; sx < 2; sx++)
				{
					Vec r = new Vec(0,0,0);
					for(int s = 0; s < samples; s++)
					{
						double r1 = 2.0 * rand.nextDouble();
						double dx = r1 < 1.0 ? Math.sqrt(r1) - 1.0 : 1.0 - Math.sqrt(2.0 - r1);
						double r2 = 2.0 * rand.nextDouble();
						double dy = r2 < 1.0 ? Math.sqrt(r2) - 1.0 : 1.0 - Math.sqrt(2.0 - r2);
						
						Vec d = cx.mult( ( (sx+.5 + dx)/2.0 + x)/w - .5);
						d = d.add(cy.mult( ( (sy+.5 + dy)/2.0 + y)/h - .5));
						d = d.add(cam.d);
						Vec e = new Vec(d.x, d.y, d.z);
						e.norm();
						Ray ray = new Ray(cam.o.add(d.mult(140.0)), e);
						r = r.add(radiance(ray, 0).mult(1.0/samples));
					} // Camera rays are pushed ^^^^^ forward to start in interior
					
					Vec ff = new Vec(clamp(r.x),clamp(r.y),clamp(r.z));
					ff = ff.mult(0.25);
					if(c[i] == null)
						c[i] = new Vec(0,0,0);
					
					c[i] = c[i].add(ff);
				}
			}
			
			// When we reach the last column in the current row, go
			// to the first column in the next row.
			x += 1;
			if(x >= w)
			{
				x = 0;
				y += 1;
			}
		}
		
		return c;
	}
}
