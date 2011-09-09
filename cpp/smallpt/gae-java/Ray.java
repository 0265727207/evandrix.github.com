package gaerender;

public class Ray {
	
	Vec o, d;
	
	public String toString()
	{
		return "(Origin=" + o + ", Dir=" + d + ")";
	}
	
	public Ray(Vec o_, Vec d_)
	{
		o = o_;
		d = d_;
	}
}