package gaerender;

public class Sphere {
	double rad;
	Vec p, e, c;
	Refl_t refl;
	
	public Sphere(double rad_, Vec p_, Vec e_, Vec c_, Refl_t refl_)
	{
		rad = rad_;
		p = p_;
		e = e_;
		c = c_;
		refl = refl_;
	}
	
	// Solve t^2*d.d + 2*t*(o-p).d + (o-p).(o-p)-R^2 = 0
	// returns distance, 0 if nohit
	double intersect(Ray r)
	{
		Vec op = p.sub(r.o);
		double t = 0.0;
		double eps = 1e-4;
		double b = op.dot(r.d);
		double det = b*b-op.dot(op)+rad*rad;
		
		if(det < 0.0)
		{
			return 0.0;
		}
		else
		{
			det = Math.sqrt(det);
		}
		
		t = b - det;
		if(t > eps)
		{
			return t;
		}
		t = b + det;
		if(t > eps)
		{
			return t;
		}
		
    	return 0.0;
	}
}
