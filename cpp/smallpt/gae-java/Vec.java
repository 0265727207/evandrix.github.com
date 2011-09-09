package gaerender;

public class Vec {
	
	public double x, y, z;
	
	public String toString()
	{
		return "(" + x + ", " + y + ", " + z + ")";
	}
	
	public Vec(String s)
	{
		s = s.replace("(", "");
		s = s.replace(")", "");
		String[] split = s.split(",");
		x = Double.parseDouble(split[0]);
		y = Double.parseDouble(split[1]);
		z = Double.parseDouble(split[2]);
	}
	
	public Vec(double x_, double y_, double z_)
	{
		x=x_; y=y_; z=z_;
	}
	
	public Vec add(Vec b)
	{
		return new Vec(x+b.x,y+b.y,z+b.z);
	}
	
	Vec sub(Vec b)
	{
		return new Vec(x-b.x, y-b.y, z-b.z);
	}
	
	Vec mult(double b)
	{
		return new Vec(x*b,y*b,z*b);
	}
	
	Vec mult(Vec b) 
	{
		return new Vec(x*b.x,y*b.y,z*b.z);
	}
	
	void norm()
	{
		double f = 1.0 / Math.sqrt(x*x+y*y+z*z);
		x *= f;
		y *= f;
		z *= f;
	}
	
	double dot(Vec b)
	{
		return x*b.x+y*b.y+z*b.z;
	}
	
	Vec cross(Vec b)
	{
		return new Vec(y*b.z-z*b.y,z*b.x-x*b.z,x*b.y-y*b.x);
	}
}